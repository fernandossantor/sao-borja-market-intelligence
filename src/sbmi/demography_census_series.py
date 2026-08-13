"""Captura oficial de recortes demográficos multidimensionais do SIDRA."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

HOST = "apisidra.ibge.gov.br"
MUNICIPALITY = "4318002"
MISSING = {"", "-", "..", "...", "X"}


@dataclass(frozen=True)
class CensusSeriesResult:
    values: pd.DataFrame
    manifest: pd.DataFrame
    validation: pd.DataFrame
    paths: dict[str, Path]


def _target(root: Path, execution_id: str) -> tuple[Path, Path]:
    target = root.resolve() / execution_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    return target, partial


def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if (
        parsed.scheme != "https"
        or parsed.hostname != HOST
        or not parsed.path.startswith("/values/t/")
    ):
        raise ValueError(f"URL fora do endpoint SIDRA permitido: {url}")


def _fetch(session, query: dict, timeout: float, limit: int):
    url = query["url"]
    _validate_url(url)
    response = session.get(
        url,
        timeout=timeout,
        headers={"Accept": "application/json", "User-Agent": "sbmi-demography-census-series/1.0"},
    )
    response.raise_for_status()
    content = bytes(response.content)
    if not content or len(content) > limit:
        raise ValueError(f"Resposta vazia ou acima do limite: {query['query_id']}")
    if "json" not in str(response.headers.get("Content-Type", "")).lower():
        raise ValueError(f"Tipo de conteúdo inesperado: {query['query_id']}")
    final_url = str(getattr(response, "url", url))
    _validate_url(final_url)
    payload = json.loads(content)
    if not isinstance(payload, list) or not payload or not isinstance(payload[0], dict):
        raise ValueError(f"Resposta SIDRA inválida: {query['query_id']}")
    return content, payload, final_url, response


def _normalize(query: dict, payload: list[dict]) -> list[dict]:
    header = payload[0]
    if not {"NC", "MC", "MN", "V", "D1C", "D2C", "D3C"}.issubset(header):
        raise ValueError(f"Esquema incompleto: {query['query_id']}")
    dimensions = []
    index = 4
    while f"D{index}C" in header:
        dimensions.append(
            (f"D{index}C", f"D{index}N", header[f"D{index}C"].removesuffix(" (Código)"))
        )
        index += 1
    output = []
    for row in payload[1:]:
        year = str(row.get("D2C", ""))
        if (
            str(row.get("NC")) != "6"
            or str(row.get("D1C")) != MUNICIPALITY
            or year not in query["years"]
        ):
            raise ValueError(f"Geografia ou período divergente: {query['query_id']}")
        if str(row.get("D3C")) not in query["variable_ids"]:
            raise ValueError(f"Variável divergente: {query['query_id']}")
        categories = [
            {
                "dimension": name,
                "category_id": str(row.get(code, "")),
                "category": str(row.get(label, "")),
            }
            for code, label, name in dimensions
        ]
        category_key = " | ".join(f"{item['dimension']}={item['category']}" for item in categories)
        raw = str(row.get("V", ""))
        number = pd.to_numeric(raw.replace(",", "."), errors="coerce")
        output.append(
            {
                "query_id": query["query_id"],
                "table_id": query["table_id"],
                "municipality_code": MUNICIPALITY,
                "municipality_name": str(row.get("D1N", "")),
                "reference_year": int(year),
                "variable_id": str(row["D3C"]),
                "variable_name": str(row.get("D3N", "")),
                "category_key": category_key,
                "category_dimensions_json": json.dumps(
                    categories, ensure_ascii=False, sort_keys=True
                ),
                "unit_code": str(row.get("MC", "")),
                "unit_name": str(row.get("MN", "")),
                "raw_value": raw,
                "numeric_value": None if pd.isna(number) else float(number),
                "value_status": "MISSING_OR_SUPPRESSED" if raw in MISSING else "OBSERVED_NUMERIC",
                "source_url": query["url"],
                "source_institution": "IBGE/SIDRA",
                "comparability_note": query["comparability_note"],
                "nature": "observed",
            }
        )
    if len(output) != query["expected_rows"]:
        raise ValueError(f"Quantidade inesperada de linhas: {query['query_id']}")
    return output


def collect_demography_census_series(
    session,
    *,
    queries: tuple[dict, ...],
    roots: dict[str, Path],
    execution_id: str,
    timeout_seconds: float = 30,
    max_response_bytes: int = 2_000_000,
) -> CensusSeriesResult:
    if not execution_id or Path(execution_id).name != execution_id:
        raise ValueError("execution_id deve ser um identificador simples")
    if set(roots) != {"raw", "staging", "curated", "exports", "audit"}:
        raise ValueError("Raízes das camadas incompletas")
    targets = {name: _target(root, execution_id) for name, root in roots.items()}
    fetched = [
        (query, *_fetch(session, query, timeout_seconds, max_response_bytes)) for query in queries
    ]
    records = [
        record for query, _, payload, _, _ in fetched for record in _normalize(query, payload)
    ]
    values = pd.DataFrame(records).sort_values(
        ["table_id", "reference_year", "variable_id", "category_key"]
    )
    duplicates = int(
        values.duplicated(["table_id", "reference_year", "variable_id", "category_key"]).sum()
    )
    if duplicates:
        raise ValueError("Chaves duplicadas na série censitária")
    manifest = pd.DataFrame(
        [
            {
                "query_id": query["query_id"],
                "table_id": query["table_id"],
                "source_url": query["url"],
                "final_url": final_url,
                "obtained_at": datetime.now(UTC).isoformat(),
                "status_code": int(response.status_code),
                "content_type": str(response.headers.get("Content-Type", "")),
                "rows": len(payload) - 1,
                "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
                "raw_file": f"sidra_values_{query['table_id']}.json",
                "nature": "observed",
            }
            for query, content, payload, final_url, response in fetched
        ]
    )
    validation = pd.DataFrame(
        [
            ("queries", len(queries), "observed", "PASS"),
            ("rows", len(values), "calculated", "PASS"),
            ("duplicate_keys", duplicates, "calculated", "PASS"),
            ("minimum_year", int(values.reference_year.min()), "calculated", "PASS"),
            ("maximum_year", int(values.reference_year.max()), "calculated", "PASS"),
            (
                "missing_or_suppressed",
                int(values.value_status.eq("MISSING_OR_SUPPRESSED").sum()),
                "calculated",
                "INFORMATIONAL",
            ),
        ],
        columns=["indicator", "value", "nature", "status"],
    )
    for _, partial in targets.values():
        partial.mkdir(parents=True)
    try:
        for query, content, _, _, _ in fetched:
            (targets["raw"][1] / f"sidra_values_{query['table_id']}.json").write_bytes(content)
        manifest.to_csv(targets["raw"][1] / "manifest.csv", index=False)
        values.to_csv(targets["staging"][1] / "demography_census_series_staging.csv", index=False)
        values.to_csv(targets["curated"][1] / "demography_census_series.csv", index=False)
        values.to_csv(targets["exports"][1] / "demography_census_series.csv", index=False)
        manifest.to_csv(targets["audit"][1] / "source_manifest.csv", index=False)
        validation.to_csv(targets["audit"][1] / "validation.csv", index=False)
        promoted: list[Path] = []
        for target, partial in targets.values():
            target.parent.mkdir(parents=True, exist_ok=True)
            partial.replace(target)
            promoted.append(target)
    except Exception:
        for _, partial in targets.values():
            shutil.rmtree(partial, ignore_errors=True)
        for target in reversed(locals().get("promoted", [])):
            shutil.rmtree(target, ignore_errors=True)
        raise
    return CensusSeriesResult(
        values, manifest, validation, {key: value[0] for key, value in targets.items()}
    )
