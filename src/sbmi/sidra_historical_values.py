"""Captura rastreável de valores agropecuários históricos do SIDRA."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

EXPECTED_HOST = "apisidra.ibge.gov.br"
MUNICIPALITY_CODE = "4318002"
YEAR_MIN = 1996
YEAR_MAX = 2026
MISSING_MARKERS = {"", "-", "..", "...", "X"}


@dataclass(frozen=True)
class ValuesResult:
    manifest: pd.DataFrame
    curated: pd.DataFrame
    validation: pd.DataFrame
    snapshot_path: Path
    staging_path: Path
    curated_path: Path
    export_path: Path
    audit_path: Path


def _identifier(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip() or Path(value).name != value:
        raise ValueError(f"{field} deve ser um identificador simples")


def _paths(root: Path, identifier: str) -> tuple[Path, Path]:
    target = root.resolve() / identifier
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    return target, partial


def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if (
        parsed.scheme != "https"
        or parsed.hostname != EXPECTED_HOST
        or not parsed.path.startswith("/values/t/")
    ):
        raise ValueError(f"URL de valores fora do endpoint permitido: {url}")


def _fetch(session, row, timeout: float, limit: int) -> tuple[bytes, list[dict], dict]:
    url = str(row.url)
    _validate_url(url)
    response = session.get(
        url,
        timeout=timeout,
        headers={
            "Accept": "application/json",
            "User-Agent": "sbmi-sidra-historical-values/1.0",
        },
    )
    response.raise_for_status()
    content = bytes(response.content)
    if not content or len(content) > limit:
        raise ValueError(f"Resposta vazia ou acima do limite: {row.query_id}")
    content_type = str(response.headers.get("Content-Type", ""))
    if "json" not in content_type.lower():
        raise ValueError(f"Tipo de conteúdo inesperado: {content_type}")
    final_url = str(getattr(response, "url", url))
    _validate_url(final_url)
    payload = json.loads(content)
    if not isinstance(payload, list) or len(payload) < 1 or not isinstance(payload[0], dict):
        raise ValueError(f"Resposta SIDRA inválida: {row.query_id}")
    return content, payload, {
        "query_id": str(row.query_id),
        "table_id": str(row.table_id),
        "source_url": url,
        "final_url": final_url,
        "obtained_at": datetime.now(UTC).isoformat(),
        "status_code": int(response.status_code),
        "content_type": content_type,
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "raw_file": f"sidra_values_{row.table_id}.json",
        "source_institution": "IBGE/SIDRA",
        "nature": "observed",
    }


def _normalize(query, payload: list[dict]) -> list[dict]:
    header, records = payload[0], payload[1:]
    required = {"NC", "MC", "MN", "V", "D1C", "D2C", "D3C", "D4C"}
    if not required.issubset(header):
        raise ValueError(f"Esquema SIDRA incompleto: {query.query_id}")
    output = []
    for record in records:
        year_text = str(record.get("D2C", ""))
        if (
            str(record.get("NC")) != "6"
            or str(record.get("D1C")) != MUNICIPALITY_CODE
            or not year_text.isdigit()
            or not YEAR_MIN <= int(year_text) <= YEAR_MAX
        ):
            raise ValueError(f"Geografia ou período divergente: {query.query_id}")
        if str(record.get("D3C")) not in str(query.variable_ids).split(","):
            raise ValueError(f"Variável divergente: {query.query_id}")
        if str(record.get("D4C")) not in str(query.category_ids).split(","):
            raise ValueError(f"Categoria divergente: {query.query_id}")
        raw_value = str(record.get("V", ""))
        numeric_value = pd.to_numeric(raw_value.replace(",", "."), errors="coerce")
        output.append(
            {
                "query_id": str(query.query_id),
                "table_id": str(query.table_id),
                "municipality_code": str(record["D1C"]),
                "municipality_name": str(record.get("D1N", "")),
                "reference_year": int(year_text),
                "variable_id": str(record["D3C"]),
                "variable_name": str(record.get("D3N", "")),
                "classification_id": str(query.classification_id),
                "category_id": str(record["D4C"]),
                "category_name": str(record.get("D4N", "")),
                "unit_code": str(record.get("MC", "")),
                "unit_name": str(record.get("MN", "")),
                "raw_value": raw_value,
                "numeric_value": None if pd.isna(numeric_value) else float(numeric_value),
                "value_status": (
                    "MISSING_OR_SUPPRESSED"
                    if raw_value in MISSING_MARKERS
                    else "OBSERVED_NUMERIC"
                ),
                "source_url": str(query.url),
                "nature": "observed",
            }
        )
    return output


def collect_sidra_historical_values(
    session,
    *,
    query_plan_path: Path,
    snapshot_root: Path,
    staging_root: Path,
    curated_root: Path,
    export_root: Path,
    audit_root: Path,
    execution_id: str,
    timeout_seconds: float = 45.0,
    max_response_bytes: int = 5_000_000,
) -> ValuesResult:
    if timeout_seconds <= 0 or max_response_bytes <= 0:
        raise ValueError("Timeout e limite devem ser positivos")
    _identifier(execution_id, "execution_id")
    plan = pd.read_csv(query_plan_path, dtype=str)
    required = {
        "query_id",
        "table_id",
        "municipality_code",
        "variable_ids",
        "classification_id",
        "category_ids",
        "url",
        "execution_status",
    }
    if not required.issubset(plan.columns) or plan.empty:
        raise ValueError("Plano de consultas ausente ou inválido")
    if set(plan.execution_status) != {"PREPARED_NOT_EXECUTED"}:
        raise ValueError("Plano não está no estado autorizado")
    if set(plan.municipality_code) != {MUNICIPALITY_CODE}:
        raise ValueError("Plano contém município fora do escopo")

    roots = (snapshot_root, staging_root, curated_root, export_root, audit_root)
    targets = [_paths(root, execution_id) for root in roots]
    fetched = [
        _fetch(session, row, timeout_seconds, max_response_bytes)
        for row in plan.itertuples()
    ]
    records = [
        normalized
        for query, (_, payload, _) in zip(plan.itertuples(), fetched, strict=True)
        for normalized in _normalize(query, payload)
    ]
    curated = pd.DataFrame(records).sort_values(
        ["table_id", "reference_year", "variable_id", "category_id"]
    )
    key = ["table_id", "municipality_code", "reference_year", "variable_id", "category_id"]
    duplicate_count = int(curated.duplicated(key).sum())
    manifest = pd.DataFrame(item[2] for item in fetched).sort_values("table_id")
    validation = pd.DataFrame(
        [
            ("queries_executed", len(fetched), "observed", "PASS"),
            ("rows_received", len(curated), "calculated", "PASS"),
            (
                "duplicate_keys",
                duplicate_count,
                "calculated",
                "PASS" if not duplicate_count else "FAIL",
            ),
            ("minimum_year", int(curated.reference_year.min()), "calculated", "PASS"),
            ("maximum_year", int(curated.reference_year.max()), "calculated", "PASS"),
            (
                "missing_or_suppressed",
                int((curated.value_status == "MISSING_OR_SUPPRESSED").sum()),
                "calculated",
                "INFORMATIONAL",
            ),
        ],
        columns=["indicator", "value", "nature", "status"],
    )
    if duplicate_count:
        raise ValueError("Chaves duplicadas na resposta normalizada")

    for _, partial in targets:
        partial.mkdir(parents=True)
    try:
        snapshot_partial, staging_partial, curated_partial, export_partial, audit_partial = (
            item[1] for item in targets
        )
        for content, _, metadata in fetched:
            (snapshot_partial / metadata["raw_file"]).write_bytes(content)
        manifest.to_csv(snapshot_partial / "manifest.csv", index=False)
        curated.to_csv(staging_partial / "sidra_historical_values_staging.csv", index=False)
        curated.to_csv(curated_partial / "sidra_historical_values.csv", index=False)
        curated.to_csv(export_partial / "sidra_historical_values.csv", index=False)
        manifest.to_csv(audit_partial / "source_manifest.csv", index=False)
        validation.to_csv(audit_partial / "validation.csv", index=False)
        plan.assign(execution_status="EXECUTED").to_csv(
            audit_partial / "executed_query_plan.csv", index=False
        )
        for target, partial in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
            partial.replace(target)
    except Exception:
        for _, partial in targets:
            shutil.rmtree(partial, ignore_errors=True)
        raise
    return ValuesResult(manifest, curated, validation, *(item[0] for item in targets))
