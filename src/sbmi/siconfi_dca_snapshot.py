"""Captura atômica e limitada da DCA oficial do SICONFI."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Protocol
from urllib.parse import urlparse

import pandas as pd

BASE_URL = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca"


class HttpResponse(Protocol):
    content: bytes
    headers: dict[str, str]
    url: str

    def raise_for_status(self) -> None: ...


class HttpSession(Protocol):
    def get(self, url: str, **kwargs) -> HttpResponse: ...


@dataclass(frozen=True)
class SiconfiSnapshotResult:
    snapshot_path: Path
    files: int
    rows: int
    bytes: int


def snapshot_siconfi_dca(
    session: HttpSession,
    snapshots_root: Path,
    *,
    snapshot_id: str,
    municipality_code: int = 4318002,
    years: tuple[int, ...] = tuple(range(2019, 2026)),
    timeout_seconds: int = 30,
    max_response_bytes: int = 5_000_000,
) -> SiconfiSnapshotResult:
    """Baixa uma página DCA por exercício e recusa respostas incompletas."""
    if not snapshot_id or Path(snapshot_id).name != snapshot_id:
        raise ValueError("Identificador de snapshot inválido")
    if not years or len(set(years)) != len(years):
        raise ValueError("Exercícios ausentes ou duplicados")
    root = snapshots_root.resolve()
    final = root / snapshot_id
    partial = root / f".{snapshot_id}.partial"
    if final.exists() or partial.exists():
        raise FileExistsError(final)

    partial.mkdir(parents=True)
    manifest_rows = []
    total_rows = 0
    total_bytes = 0
    try:
        for year in years:
            params = {"an_exercicio": year, "id_ente": municipality_code}
            response = session.get(
                BASE_URL,
                params=params,
                headers={"Accept": "application/json"},
                timeout=timeout_seconds,
            )
            response.raise_for_status()
            content = bytes(response.content)
            if not content or len(content) > max_response_bytes:
                raise ValueError(f"Resposta de {year} vazia ou acima do limite")
            content_type = str(response.headers.get("Content-Type", ""))
            if "json" not in content_type.lower():
                raise ValueError(f"Tipo de conteúdo inesperado para {year}: {content_type}")
            final_url = str(getattr(response, "url", BASE_URL))
            parsed_final = urlparse(final_url)
            parsed_base = urlparse(BASE_URL)
            if (
                parsed_final.scheme != "https"
                or parsed_final.hostname != parsed_base.hostname
                or parsed_final.path.rstrip("/") != parsed_base.path
            ):
                raise ValueError(f"URL final não autorizada para {year}: {final_url}")
            payload = json.loads(content)
            items = payload.get("items")
            if not isinstance(items, list) or payload.get("hasMore") is not False:
                raise ValueError(f"Resposta incompleta ou inválida para {year}")
            if any(
                row.get("exercicio") != year or row.get("cod_ibge") != municipality_code
                for row in items
            ):
                raise ValueError(f"Geografia ou exercício divergente em {year}")
            filename = f"dca_{municipality_code}_{year}.json"
            (partial / filename).write_bytes(content)
            digest = hashlib.sha256(content).hexdigest()
            manifest_rows.append(
                {
                    "source_id": f"siconfi_dca_{municipality_code}_{year}",
                    "institution": "Secretaria do Tesouro Nacional/SICONFI",
                    "source_url": f"{BASE_URL}?an_exercicio={year}&id_ente={municipality_code}",
                    "final_url": final_url,
                    "obtained_at_utc": datetime.now(UTC).isoformat(),
                    "reference_year": year,
                    "municipality_code": municipality_code,
                    "file": filename,
                    "bytes": len(content),
                    "content_type": content_type,
                    "sha256": digest,
                    "rows": len(items),
                    "has_more": False,
                    "nature": "observed",
                    "audit_status": "VERIFIED",
                }
            )
            total_rows += len(items)
            total_bytes += len(content)
        pd.DataFrame(manifest_rows).to_csv(partial / "manifest.csv", index=False)
        final.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(final)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return SiconfiSnapshotResult(final, len(years), total_rows, total_bytes)
