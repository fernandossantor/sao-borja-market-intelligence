"""Captura reproduzível dos scorecards publicados do IPS Brasil."""

from __future__ import annotations

import hashlib
import html
import re
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Protocol

import pandas as pd
import requests

DEFAULT_YEARS = (2024, 2025, 2026)
DEFAULT_IBGE_CODE = "4318002"
DEFAULT_MUNICIPALITY = "São Borja"
BASE_URL = "https://ipsbrasil.org.br/explore/scorecard"
SUMMARY_LABELS = (
    "Necessidades Humanas Básicas",
    "Fundamentos do Bem-estar",
    "Oportunidades",
    "Nutrição e Cuidados Médicos Básicos",
    "Água e Saneamento",
    "Moradia",
    "Segurança Pessoal",
    "Acesso ao Conhecimento Básico",
    "Acesso à Informação e Comunicação",
    "Saúde e Bem-estar",
    "Qualidade do Meio Ambiente",
    "Direitos Individuais",
    "Liberdades Individuais e de Escolha",
    "Inclusão Social",
    "Acesso à Educação Superior",
)


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


def scorecard_url(year: int, *, ibge_code: str = DEFAULT_IBGE_CODE) -> str:
    """Monta a URL pública do scorecard municipal para uma edição."""
    if year < 2024:
        raise ValueError("O IPS Brasil municipal disponível nesta rotina começa em 2024.")
    if not ibge_code.isdigit():
        raise ValueError("O código IBGE deve conter apenas dígitos.")
    return f"{BASE_URL}/{ibge_code}?year={year}"


def visible_text(source: str) -> str:
    """Reduz HTML a texto visível para validações estruturais."""
    text = re.sub(
        r"<script\b[^>]*>.*?</script>",
        " ",
        source,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(
        r"<style\b[^>]*>.*?</style>",
        " ",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def validate_scorecard_html(
    source: str,
    *,
    year: int,
    ibge_code: str,
    municipality: str,
) -> int:
    """Valida município, edição e presença dos 15 agregados oficiais."""
    text = visible_text(source)
    if municipality.casefold() not in text.casefold():
        raise ValueError(f"Município ausente no scorecard de {year}: {municipality!r}.")
    if ibge_code not in source:
        raise ValueError(f"Código IBGE ausente no scorecard de {year}: {ibge_code}.")
    marker = re.compile(rf"IPS\s+BRASIL\s+{year}\b", flags=re.IGNORECASE)
    if marker.search(text) is None:
        raise ValueError(f"A edição {year} não foi confirmada no conteúdo do scorecard.")
    labels_found = sum(label.casefold() in text.casefold() for label in SUMMARY_LABELS)
    if labels_found != len(SUMMARY_LABELS):
        raise ValueError(
            "Estrutura agregada incompleta no scorecard: "
            f"ano={year}, observados={labels_found}, esperados={len(SUMMARY_LABELS)}"
        )
    return labels_found


def _new_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "SBMI/0.1 (territorial-market-intelligence; "
                "reproducible-public-scorecard-capture)"
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
    municipality: str = DEFAULT_MUNICIPALITY,
    session: SessionLike | None = None,
    timeout_seconds: int = 60,
    max_total_bytes: int = 10_000_000,
) -> IpsWebSnapshotResult:
    """Captura scorecards diretos e publica apenas após todas as validações."""
    if not snapshot_id or "/" in snapshot_id or ".." in snapshot_id:
        raise ValueError("Identificador de snapshot inválido.")
    if not years or len(set(years)) != len(years):
        raise ValueError("Os anos devem ser únicos e não vazios.")
    if not municipality.strip():
        raise ValueError("O município deve ser informado.")
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
            url = scorecard_url(year, ibge_code=ibge_code)
            response = client.get(url, timeout=timeout_seconds, allow_redirects=True)
            response.raise_for_status()
            content = response.content
            content_type = str(response.headers.get("content-type", ""))
            if "text/html" not in content_type.lower():
                raise ValueError(
                    f"Conteúdo inesperado para {year}: content_type={content_type!r}"
                )
            total_bytes += len(content)
            if total_bytes > max_total_bytes:
                raise ValueError(
                    "Captura bloqueada pelo limite: "
                    f"baixado={total_bytes}, limite={max_total_bytes}"
                )
            source = content.decode("utf-8")
            labels_found = validate_scorecard_html(
                source,
                year=year,
                ibge_code=ibge_code,
                municipality=municipality,
            )
            filename = f"ips_brasil_scorecard_{year}.html"
            (partial_path / filename).write_bytes(content)
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
                    "municipality": municipality,
                    "year_marker_confirmed": True,
                    "summary_labels_observed": labels_found,
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
        bytes=total_bytes,
        years=tuple(years),
        requests=len(manifest_rows),
        transferred_bytes=total_bytes,
    )
