"""Descoberta histórica, limitada a metadados oficiais do SIDRA."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

MUNICIPALITY_CODE = "4318002"
TARGET_START_YEAR = 1996
TARGET_END_YEAR = 2026
ALLOWED_HOSTS = {"sidra.ibge.gov.br"}
ALLOWED_DIMENSIONS = {
    "demografia",
    "economia_estrutura_produtiva",
    "renda_emprego_trabalho",
    "educacao",
    "infraestrutura_conectividade",
    "financas_publicas_transferencias",
    "saude_condicoes_sociais",
    "ambiente_politico_regulatorio",
    "ambiente_sociocultural_territorial",
    "transversal_multitematico",
}
TABLE_SPECS = {
    "156": ("demografia|ambiente_sociocultural_territorial", "Censo Demográfico"),
    "289": ("economia_estrutura_produtiva", "PEVS"),
    "3939": ("economia_estrutura_produtiva", "PPM"),
    "5457": ("economia_estrutura_produtiva", "PAM"),
    "5938": ("economia_estrutura_produtiva", "PIB dos Municípios"),
    "6449": ("economia_estrutura_produtiva|renda_emprego_trabalho", "CEMPRE"),
    "6450": ("economia_estrutura_produtiva|renda_emprego_trabalho", "CEMPRE"),
    "6579": ("demografia", "Estimativas de População"),
    "9514": ("demografia|ambiente_sociocultural_territorial", "Censo Demográfico"),
}


@dataclass(frozen=True)
class Result:
    manifest: pd.DataFrame
    tables: pd.DataFrame
    periods: pd.DataFrame
    variables: pd.DataFrame
    classifications: pd.DataFrame
    categories: pd.DataFrame
    limitations: pd.DataFrame
    summary: pd.DataFrame
    snapshot_path: Path
    output_path: Path


def _validate_identifier(identifier: str, field: str) -> None:
    if not isinstance(identifier, str) or not identifier.strip():
        raise ValueError(f"{field} deve ser um identificador não vazio")
    if Path(identifier).name != identifier or identifier in {".", ".."}:
        raise ValueError(f"{field} deve ser um nome simples")


def _target(root: Path, identifier: str) -> tuple[Path, Path]:
    target = root.expanduser().resolve() / identifier
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    return target, partial


def _descriptor_url(table_id: str) -> str:
    return f"https://sidra.ibge.gov.br/ajax/tabela/descricao/1/{table_id}"


def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError(f"URL fora da lista oficial SIDRA: {url}")
    if "/values" in parsed.path.lower():
        raise ValueError("A descoberta histórica não pode consultar valores")


def _availability_years(value: str) -> list[int]:
    years: set[int] = set()
    for start, end in re.findall(r"(\d{4})(?:\s+a\s+(\d{4}))?", value or ""):
        first = int(start)
        last = int(end or start)
        if last < first:
            raise ValueError(f"Disponibilidade inválida: {value}")
        years.update(range(first, last + 1))
    return sorted(year for year in years if TARGET_START_YEAR <= year <= TARGET_END_YEAR)


def _fetch(session, table_id: str, timeout: float, limit: int) -> tuple[dict, dict]:
    url = _descriptor_url(table_id)
    _validate_url(url)
    response = session.get(
        url,
        timeout=timeout,
        headers={"User-Agent": "sbmi-sidra-historical-metadata-discovery/1.0"},
    )
    response.raise_for_status()
    content = bytes(response.content)
    if not content or len(content) > limit:
        raise ValueError(f"Conteúdo vazio ou acima do limite: {url}")
    content_type = str(response.headers.get("Content-Type", ""))
    if "json" not in content_type.lower():
        raise ValueError(f"Tipo inesperado em {url}: {content_type}")
    final_url = str(getattr(response, "url", url))
    _validate_url(final_url)
    document = json.loads(content)
    if str(document.get("Id")) != table_id:
        raise ValueError(f"ID divergente no descritor {table_id}")
    return document, {
        "table_id": table_id,
        "requested_url": url,
        "final_url": final_url,
        "status_code": int(response.status_code),
        "content_type": content_type,
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "local_file": f"descriptor_{table_id}.json",
        "content": content,
        "nature": "observed",
    }


def _records(documents: dict[str, dict]):
    tables = []
    periods = []
    variables = []
    classifications = []
    categories = []
    limitations = []
    for table_id, document in sorted(documents.items()):
        dimensions, expected_research = TABLE_SPECS[table_id]
        mapped = dimensions.split("|")
        if not set(mapped).issubset(ALLOWED_DIMENSIONS):
            raise ValueError(f"Dimensão nova ou não autorizada na tabela {table_id}")
        territories = [str(item.get("Nome", "")) for item in document.get("NiveisTerritoriais", [])]
        municipal = "Município" in territories
        if not municipal:
            raise ValueError(f"Tabela {table_id} sem nível municipal")
        availability = str(document.get("Disponibilidade", ""))
        years = _availability_years(availability)
        tables.append(
            {
                "table_id": table_id,
                "table_name": document.get("Nome", ""),
                "research": document.get("Pesquisa", expected_research),
                "expected_research": expected_research,
                "availability": availability,
                "period_type": document.get("TipoPeriodo", ""),
                "municipal_level": municipal,
                "municipality_code": MUNICIPALITY_CODE,
                "mapped_dimensions": dimensions,
                "metadata_status": "CONFIRMED",
                "conceptual_equivalence_status": "NOT_ASSESSED",
                "nature": "observed",
            }
        )
        periods.extend(
            {
                "table_id": table_id,
                "reference_year": year,
                "inside_target_interval": True,
                "availability_source": availability,
                "nature": "calculated_from_observed_metadata",
            }
            for year in years
        )
        if TARGET_END_YEAR not in years:
            limitations.append(
                {
                    "table_id": table_id,
                    "limitation_code": "TARGET_END_YEAR_UNAVAILABLE",
                    "statement": f"Descritor não informa disponibilidade para {TARGET_END_YEAR}.",
                    "nature": "observed_limitation",
                }
            )
        limitations.append(
            {
                "table_id": table_id,
                "limitation_code": "MUNICIPAL_VALUES_NOT_CHECKED",
                "statement": "A presença de nível municipal não comprova valores para São Borja.",
                "nature": "observed_limitation",
            }
        )
        for variable in document.get("Variaveis", []):
            units = variable.get("UnidadeDeMedida") or [{}]
            variables.append(
                {
                    "table_id": table_id,
                    "variable_id": str(variable.get("Id", "")),
                    "variable_name": variable.get("Nome", ""),
                    "unit": units[0].get("Unidade", ""),
                    "availability": units[0].get("Periodo", availability),
                    "is_derived": False,
                    "nature": "observed",
                }
            )
            for derived in variable.get("VariaveisDerivadas", []):
                variables.append(
                    {
                        "table_id": table_id,
                        "variable_id": str(derived.get("Id", "")),
                        "variable_name": derived.get("Nome", ""),
                        "unit": derived.get("UnidadeDeMedida", ""),
                        "availability": derived.get("Periodo", availability),
                        "is_derived": True,
                        "nature": "observed",
                    }
                )
        for classification in document.get("Classificacoes", []):
            classification_id = str(classification.get("Id", ""))
            total_id = str(classification.get("IndiceTotal", ""))
            classifications.append(
                {
                    "table_id": table_id,
                    "classification_id": classification_id,
                    "classification_name": classification.get("Nome", ""),
                    "total_category_id": total_id,
                    "allows_total": bool(classification.get("AdmiteTotal")),
                    "nature": "observed",
                }
            )
            for category in classification.get("Categorias", []):
                category_id = str(category.get("Id", ""))
                categories.append(
                    {
                        "table_id": table_id,
                        "classification_id": classification_id,
                        "category_id": category_id,
                        "category_name": category.get("Nome", ""),
                        "is_total": category_id == total_id,
                        "availability": category.get("Disponibilidade", ""),
                        "nature": "observed",
                    }
                )
    return tuple(
        pd.DataFrame(frame)
        for frame in (tables, periods, variables, classifications, categories, limitations)
    )


def discover_sidra_historical_metadata(
    session,
    *,
    snapshots_root: Path,
    audit_root: Path,
    snapshot_id: str,
    run_id: str,
    timeout_seconds: float = 45.0,
    max_descriptor_bytes: int = 5_000_000,
) -> Result:
    if timeout_seconds <= 0 or max_descriptor_bytes <= 0:
        raise ValueError("Timeout e limite devem ser positivos")
    _validate_identifier(snapshot_id, "snapshot_id")
    _validate_identifier(run_id, "run_id")
    snapshot_path, snapshot_partial = _target(snapshots_root, snapshot_id)
    output_path, output_partial = _target(audit_root, run_id)
    fetched = {
        table_id: _fetch(session, table_id, timeout_seconds, max_descriptor_bytes)
        for table_id in TABLE_SPECS
    }
    documents = {table_id: item[0] for table_id, item in fetched.items()}
    manifests = [item[1] for item in fetched.values()]
    tables, periods, variables, classifications, categories, limitations = _records(documents)
    obtained_at = datetime.now(UTC).isoformat()
    manifest = pd.DataFrame(
        [
            {k: v for k, v in row.items() if k != "content"} | {"obtained_at": obtained_at}
            for row in manifests
        ]
    ).sort_values("table_id")
    summary = pd.DataFrame(
        [
            ("descriptors_captured", len(manifest), "observed"),
            ("tables_confirmed", len(tables), "calculated"),
            ("target_period_rows", len(periods), "calculated"),
            ("variables_identified", len(variables), "calculated"),
            ("classifications_identified", len(classifications), "calculated"),
            ("categories_identified", len(categories), "calculated"),
            (
                "dimensions_used",
                len({d for value in tables.mapped_dimensions for d in value.split("|")}),
                "calculated",
            ),
            ("values_requests", 0, "observed"),
            ("conceptually_validated_tables", 0, "observed"),
        ],
        columns=["indicator", "value", "nature"],
    )
    snapshot_partial.mkdir(parents=True)
    output_partial.mkdir(parents=True)
    try:
        for row in manifests:
            (snapshot_partial / row["local_file"]).write_bytes(row["content"])
        manifest.to_csv(snapshot_partial / "sidra_historical_manifest.csv", index=False)
        for name, frame in (
            ("sidra_historical_table_register", tables),
            ("sidra_historical_period_register", periods),
            ("sidra_historical_variable_register", variables),
            ("sidra_historical_classification_register", classifications),
            ("sidra_historical_category_register", categories),
            ("sidra_historical_limitation_register", limitations),
            ("sidra_historical_summary", summary),
        ):
            frame.to_csv(output_partial / f"{name}.csv", index=False)
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        snapshot_partial.replace(snapshot_path)
        output_partial.replace(output_path)
    except Exception:
        shutil.rmtree(snapshot_partial, ignore_errors=True)
        shutil.rmtree(output_partial, ignore_errors=True)
        raise
    return Result(
        manifest,
        tables,
        periods,
        variables,
        classifications,
        categories,
        limitations,
        summary,
        snapshot_path,
        output_path,
    )
