"""Captura reproduzível das páginas publicadas do IPS Brasil."""

from __future__ import annotations

import hashlib
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol

import pandas as pd
import requests

DEFAULT_YEARS = (2024, 2025, 2026)
DEFAULT_IBGE_CODE = "4318002"
DEFAULT_PAGE = 499
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


def published_data_url(
    year: int,
    *,
    page: int = DEFAULT_PAGE,
    per_page: int = DEFAULT_PER_PAGE,
) -> str:
    """Monta a URL estável da tabela publicada, ordenada por código IBGE."""
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


def snapshot_published_ips_pages(
    snapshots_root: Path,
    *,
    snapshot_id: str = "ips-brasil-published-2024-2026",
    years: tuple[int, ...] = DEFAULT_YEARS,
    ibge_code: str = DEFAULT_IBGE_CODE,
    page: int = DEFAULT_PAGE,
    per_page: int = DEFAULT_PER_PAGE,
    session: SessionLike | None = None,
    timeout_seconds: int = 60,
    max_total_bytes: int = 10_000_000,
) -> IpsWebSnapshotResult:
    """Captura as páginas HTML e publica somente após todas as validações."""
    if not snapshot_id or "/" in snapshot_id or ".." in snapshot_id:
        raise ValueError("Identificador de snapshot inválido.")
    if not years or len(set(years)) != len(years):
        raise ValueError("Os anos devem ser únicos e não vazios.")
    if not ibge_code.isdigit():
        raise ValueError("O código IBGE deve conter apenas dígitos.")
    if timeout_seconds <= 0 or max_total_bytes <= 0:
        raise ValueError("Timeout e limite de bytes devem ser maiores que zero.")

    root = snapshots_root.expanduser().resolve()
    final_path = root / snapshot_id
    partial_path = root / f".{snapshot_id}.partial"
    if final_path.exists() or partial_path.exists():
        raise FileExistsError(f"A captura já existe ou está incompleta: {snapshot_id}")

    client = session or _new_session()
    partial_path.mkdir(parents=True, exist_ok=False)
    manifest_rows: list[dict[str, object]] = []
    total_bytes = 0

    try:
        for year in years:
            url = published_data_url(year, page=page, per_page=per_page)
            response = client.get(url, timeout=timeout_seconds, allow_redirects=True)
            response.raise_for_status()
            content = response.content
            content_type = str(response.headers.get("content-type", ""))
            if "text/html" not in content_type.lower():
                raise ValueError(
                    f"Conteúdo inesperado para {year}: content_type={content_type!r}"
                )
            if ibge_code.encode("utf-8") not in content:
                raise ValueError(
                    f"O código IBGE {ibge_code} não foi encontrado na página de {year}. "
                    "Revise a paginação publicada pelo site."
                )
            total_bytes += len(content)
            if total_bytes > max_total_bytes:
                raise ValueError(
                    "Captura bloqueada pelo limite: "
                    f"baixado={total_bytes}, limite={max_total_bytes}"
                )

            filename = f"ips_brasil_published_{year}.html"
            target = partial_path / filename
            target.write_bytes(content)
            digest = hashlib.sha256(content).hexdigest()
            manifest_rows.append(
                {
                    "reference_year": year,
                    "requested_url": url,
                    "final_url": str(response.url),
                    "status_code": int(response.status_code),
                    "content_type": content_type,
                    "bytes": len(content),
                    "sha256": digest,
                    "ibge_code": ibge_code,
                    "ibge_code_present": True,
                    "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
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
        bytes=total_bytes,
        years=tuple(years),
    )
