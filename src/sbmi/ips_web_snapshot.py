"""Captura reproduzível das páginas publicadas do IPS Brasil."""

from __future__ import annotations

import hashlib
import re
import shutil
import unicodedata
from dataclasses import dataclass
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Protocol

import pandas as pd
import requests

DEFAULT_YEARS = (2024, 2025, 2026)
DEFAULT_IBGE_CODE = "4318002"
DEFAULT_INITIAL_PAGE = 499
DEFAULT_MAX_PAGE = 700
DEFAULT_PER_PAGE = 10
BASE_URL = "https://ipsbrasil.org.br/explore/data"


class ResponseLike(Protocol):
    status_code: int
    content: bytes
    url: str
    headers: dict[str, str]

    def raise_for_status(self) -> None: ...


class SessionLike(Protocol):
    def get(self, url: str, **kwargs: object) -> ResponseLike: ...


@dataclass(frozen=True)
class IpsWebSnapshotResult:
    """Resumo da captura web concluída."""

    snapshot_path: Path
    pages: int
    bytes: int
    years: tuple[int, ...]
    requests: int
    transferred_bytes: int


class _TableParser(HTMLParser):
    """Extrai linhas de tabelas HTML sem dependências adicionais."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[str]]] = []
        self._table: list[list[str]] | None = None
        self._row: list[str] | None = None
        self._cell_parts: list[str] | None = None
        self._table_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        if tag == "table":
            self._table_depth += 1
            if self._table_depth == 1:
                self._table = []
        elif self._table_depth == 1 and tag == "tr":
            self._row = []
        elif self._table_depth == 1 and tag in {"th", "td"}:
            self._cell_parts = []

    def handle_data(self, data: str) -> None:
        if self._cell_parts is not None:
            self._cell_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._table_depth == 1 and tag in {"th", "td"}:
            if self._row is not None and self._cell_parts is not None:
                value = re.sub(r"\s+", " ", " ".join(self._cell_parts)).strip()
                self._row.append(value)
            self._cell_parts = None
        elif self._table_depth == 1 and tag == "tr":
            if self._table is not None and self._row:
                self._table.append(self._row)
            self._row = None
        elif tag == "table" and self._table_depth:
            if self._table_depth == 1 and self._table is not None:
                self.tables.append(self._table)
                self._table = None
            self._table_depth -= 1


def _normalize_label(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value))
    text = "".join(character for character in text if not unicodedata.combining(character))
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text).lower()
    return re.sub(r"\s+", " ", text).strip()


def extract_table_ibge_codes(html_text: str) -> tuple[int, ...]:
    """Extrai os códigos IBGE da tabela municipal publicada."""
    parser = _TableParser()
    parser.feed(html_text)
    codes: list[int] = []

    for table in parser.tables:
        code_index: int | None = None
        header_index: int | None = None
        for index, row in enumerate(table):
            normalized = [_normalize_label(cell) for cell in row]
            if "codigo ibge" in normalized and "municipio" in normalized:
                code_index = normalized.index("codigo ibge")
                header_index = index
                break
        if code_index is None or header_index is None:
            continue
        for row in table[header_index + 1 :]:
            if code_index >= len(row):
                continue
            value = row[code_index].strip()
            if re.fullmatch(r"\d{7}", value):
                codes.append(int(value))

    return tuple(codes)


def published_data_url(
    year: int,
    *,
    page: int,
    per_page: int = DEFAULT_PER_PAGE,
) -> str:
    """Monta a URL da tabela publicada, ordenada por código IBGE."""
    if year < 2024:
        raise ValueError("O IPS Brasil municipal disponível nesta rotina começa em 2024.")
    if page <= 0 or per_page <= 0:
        raise ValueError("page e per_page devem ser maiores que zero.")
    return (
        f"{BASE_URL}?page={page}&per_page={per_page}"
        f"&sort_by=code&sort_order=asc&year={year}"
    )


def _new_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "SBMI/0.1 (territorial-market-intelligence; "
                "reproducible-public-data-capture)"
            )
        }
    )
    return session


def _fetch_page(
    *,
    client: SessionLike,
    year: int,
    page: int,
    per_page: int,
    timeout_seconds: int,
) -> tuple[ResponseLike, tuple[int, ...]]:
    url = published_data_url(year, page=page, per_page=per_page)
    response = client.get(url, timeout=timeout_seconds, allow_redirects=True)
    response.raise_for_status()
    content_type = str(response.headers.get("content-type", ""))
    if "text/html" not in content_type.lower():
        raise ValueError(
            f"Conteúdo inesperado para {year}, página {page}: "
            f"content_type={content_type!r}"
        )
    codes = extract_table_ibge_codes(response.content.decode("utf-8"))
    if codes and tuple(sorted(codes)) != codes:
        raise ValueError(
            f"A tabela de {year}, página {page}, não está ordenada por código IBGE."
        )
    return response, codes


def _find_municipality_page(
    *,
    client: SessionLike,
    year: int,
    ibge_code: str,
    initial_page: int,
    max_page: int,
    per_page: int,
    timeout_seconds: int,
    max_total_bytes: int,
) -> tuple[ResponseLike, int, tuple[int, ...], int, int]:
    """Localiza a página por tentativa inicial e busca binária auditável."""
    target = int(ibge_code)
    cache: dict[int, tuple[ResponseLike, tuple[int, ...]]] = {}
    transferred = 0

    def fetch(page: int) -> tuple[ResponseLike, tuple[int, ...]]:
        nonlocal transferred
        if page not in cache:
            response, codes = _fetch_page(
                client=client,
                year=year,
                page=page,
                per_page=per_page,
                timeout_seconds=timeout_seconds,
            )
            transferred += len(response.content)
            if transferred > max_total_bytes:
                raise ValueError(
                    "Busca bloqueada pelo limite de bytes: "
                    f"ano={year}, transferido={transferred}, limite={max_total_bytes}"
                )
            cache[page] = (response, codes)
        return cache[page]

    if 1 <= initial_page <= max_page:
        response, codes = fetch(initial_page)
        if target in codes:
            return response, initial_page, codes, len(cache), transferred

    low = 1
    high = max_page
    while low <= high:
        page = (low + high) // 2
        response, codes = fetch(page)
        if target in codes:
            return response, page, codes, len(cache), transferred
        if not codes:
            high = page - 1
            continue
        minimum = min(codes)
        maximum = max(codes)
        if target < minimum:
            high = page - 1
        elif target > maximum:
            low = page + 1
        else:
            raise ValueError(
                f"O código {ibge_code} está entre os limites da página {page} "
                f"de {year}, mas não foi encontrado na tabela."
            )

    raise ValueError(
        f"O código IBGE {ibge_code} não foi encontrado em {year} "
        f"entre as páginas 1 e {max_page}."
    )


def snapshot_published_ips_pages(
    snapshots_root: Path,
    *,
    snapshot_id: str = "ips-brasil-published-2024-2026",
    years: tuple[int, ...] = DEFAULT_YEARS,
    ibge_code: str = DEFAULT_IBGE_CODE,
    initial_page: int = DEFAULT_INITIAL_PAGE,
    max_page: int = DEFAULT_MAX_PAGE,
    per_page: int = DEFAULT_PER_PAGE,
    session: SessionLike | None = None,
    timeout_seconds: int = 60,
    max_total_bytes: int = 25_000_000,
) -> IpsWebSnapshotResult:
    """Localiza e captura as páginas municipais, publicando após as validações."""
    if not snapshot_id or "/" in snapshot_id or ".." in snapshot_id:
        raise ValueError("Identificador de snapshot inválido.")
    if not years or len(set(years)) != len(years):
        raise ValueError("Os anos devem ser únicos e não vazios.")
    if not ibge_code.isdigit():
        raise ValueError("O código IBGE deve conter apenas dígitos.")
    if initial_page <= 0 or max_page <= 0 or initial_page > max_page:
        raise ValueError("As páginas inicial e máxima são inválidas.")
    if per_page <= 0 or timeout_seconds <= 0 or max_total_bytes <= 0:
        raise ValueError("Paginação, timeout e limite de bytes devem ser maiores que zero.")

    root = snapshots_root.expanduser().resolve()
    final_path = root / snapshot_id
    partial_path = root / f".{snapshot_id}.partial"
    if final_path.exists() or partial_path.exists():
        raise FileExistsError(f"A captura já existe ou está incompleta: {snapshot_id}")

    client = session or _new_session()
    partial_path.mkdir(parents=True, exist_ok=False)
    manifest_rows: list[dict[str, object]] = []
    stored_bytes = 0
    transferred_bytes = 0
    total_requests = 0

    try:
        for year in years:
            response, page_found, codes, requests_made, bytes_for_year = (
                _find_municipality_page(
                    client=client,
                    year=year,
                    ibge_code=ibge_code,
                    initial_page=initial_page,
                    max_page=max_page,
                    per_page=per_page,
                    timeout_seconds=timeout_seconds,
                    max_total_bytes=max_total_bytes - transferred_bytes,
                )
            )
            content = response.content
            stored_bytes += len(content)
            transferred_bytes += bytes_for_year
            total_requests += requests_made
            if transferred_bytes > max_total_bytes:
                raise ValueError(
                    "Captura bloqueada pelo limite total: "
                    f"transferido={transferred_bytes}, limite={max_total_bytes}"
                )

            filename = f"ips_brasil_published_{year}.html"
            target = partial_path / filename
            target.write_bytes(content)
            digest = hashlib.sha256(content).hexdigest()
            manifest_rows.append(
                {
                    "reference_year": year,
                    "requested_url": published_data_url(
                        year,
                        page=page_found,
                        per_page=per_page,
                    ),
                    "final_url": str(response.url),
                    "page_found": page_found,
                    "search_requests": requests_made,
                    "search_strategy": "INITIAL_PAGE_THEN_BINARY_SEARCH_BY_IBGE_CODE",
                    "table_min_ibge_code": min(codes),
                    "table_max_ibge_code": max(codes),
                    "status_code": int(response.status_code),
                    "content_type": str(response.headers.get("content-type", "")),
                    "stored_bytes": len(content),
                    "transferred_bytes": bytes_for_year,
                    "sha256": digest,
                    "ibge_code": ibge_code,
                    "ibge_code_present": True,
                    "retrieved_at_utc": datetime.now(UTC).isoformat(),
                    "local_file": filename,
                }
            )

        pd.DataFrame(manifest_rows).to_csv(
            partial_path / "web_manifest.csv",
            index=False,
        )
        final_path.parent.mkdir(parents=True, exist_ok=True)
        partial_path.replace(final_path)
    except Exception:
        shutil.rmtree(partial_path, ignore_errors=True)
        raise

    return IpsWebSnapshotResult(
        snapshot_path=final_path,
        pages=len(manifest_rows),
        bytes=stored_bytes,
        years=tuple(years),
        requests=total_requests,
        transferred_bytes=transferred_bytes,
    )
