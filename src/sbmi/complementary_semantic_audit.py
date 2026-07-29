"""Auditoria semântica das quatro fontes complementares coletadas."""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pandas as pd

CLASSES = {
    "CONTENT_DUPLICATE",
    "PARTIAL_OVERLAP",
    "COMPLEMENTARY",
    "CONFLICT",
    "UNIQUE",
}
IPS_TECHNICAL_FIELDS = {"municipio", "uf"}


@dataclass(frozen=True)
class SemanticAuditResult:
    register: pd.DataFrame
    classification_summary: pd.DataFrame
    dimension_summary: pd.DataFrame
    ips_reconciliation: pd.DataFrame
    validation: pd.DataFrame
    output_path: Path


def normalize_name(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value))
    ascii_text = text.encode("ascii", "ignore").decode().casefold()
    return re.sub(r"[^a-z0-9]+", "_", ascii_text).strip("_")


def _simple_identifier(value: str) -> None:
    if not value or Path(value).name != value:
        raise ValueError("audit_id deve ser um identificador simples")


def _measure_names(url: str) -> set[str]:
    measures = parse_qs(urlparse(url).query).get("measures", [])
    return {
        normalize_name(item)
        for value in measures
        for item in value.split(",")
        if item.strip()
    }


def _ips_reconcile(values: pd.DataFrame, baseline: pd.DataFrame) -> pd.DataFrame:
    ips = values.loc[
        values.source_id.eq("ips_brasil_explorer"),
        ["query_id", "reference_year", "field_name", "numeric_value", "raw_value"],
    ].copy()
    ips["reference_year"] = pd.to_numeric(
        ips["reference_year"], errors="coerce"
    ).astype("Int64")
    ips["normalized_name"] = ips.field_name.map(normalize_name)
    ips["observed_value"] = pd.to_numeric(ips.numeric_value, errors="coerce")

    existing = baseline[[
        "reference_year", "indicator_label", "indicator_key", "value_numeric"
    ]].copy()
    existing["reference_year"] = pd.to_numeric(
        existing["reference_year"], errors="coerce"
    ).astype("Int64")
    existing["normalized_name"] = existing.indicator_label.map(normalize_name)
    existing["baseline_value"] = pd.to_numeric(existing.value_numeric, errors="coerce")
    joined = ips.merge(
        existing[[
            "reference_year", "normalized_name", "indicator_key", "baseline_value"
        ]],
        on=["reference_year", "normalized_name"],
        how="inner",
        validate="many_to_one",
    )
    joined["difference"] = joined.observed_value - joined.baseline_value
    joined["values_equal"] = joined.difference.abs().le(1e-9)
    joined["classification"] = joined.values_equal.map(
        {True: "CONTENT_DUPLICATE", False: "CONFLICT"}
    )
    return joined.sort_values(["reference_year", "indicator_key"]).reset_index(drop=True)


def _ibge_cross_source_status(values: pd.DataFrame) -> dict[str, tuple[str, str]]:
    censo = values.loc[
        values.source_id.eq("ibge_censo_2022_panorama")
        & values.indicator_id.notna()
        & values.reference_year.notna(),
        ["indicator_id", "reference_year", "raw_value"],
    ].drop_duplicates()
    cidades = values.loc[
        values.source_id.eq("ibge_cidades_panorama")
        & values.indicator_id.notna()
        & values.reference_year.notna(),
        ["indicator_id", "reference_year", "raw_value"],
    ].drop_duplicates()
    output: dict[str, tuple[str, str]] = {}
    for indicator, group in cidades.groupby("indicator_id"):
        other = censo.loc[censo.indicator_id.eq(indicator)]
        if other.empty:
            output[str(indicator)] = (
                "PARTIAL_OVERLAP",
                "Indicador do panorama municipal sem equivalência de conteúdo comprovada.",
            )
            continue
        common = group.merge(
            other,
            on=["indicator_id", "reference_year"],
            suffixes=("_cidades", "_censo"),
        )
        equal = (
            not common.empty
            and common.raw_value_cidades.astype(str).eq(
                common.raw_value_censo.astype(str)
            ).all()
        )
        complete = len(common) == len(group) == len(other)
        output[str(indicator)] = (
            (
                "CONTENT_DUPLICATE"
                if equal and complete
                else "PARTIAL_OVERLAP"
                if equal
                else "CONFLICT"
            ),
            (
                "Mesmo indicador, períodos e valores nas duas páginas oficiais."
                if equal and complete
                else "Há períodos ou escopo adicionais entre as páginas oficiais."
                if equal
                else "Mesmo indicador e período com valor divergente."
            ),
        )
    return output


def audit_complementary_semantics(
    *,
    values_path: Path,
    sebrae_inventory_path: Path,
    ips_baseline_path: Path,
    output_root: Path,
    audit_id: str,
) -> SemanticAuditResult:
    """Classifica contratos sem promover valores ao modelo canônico."""
    _simple_identifier(audit_id)
    target = output_root.resolve() / audit_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")

    values = pd.read_csv(values_path, dtype=str)
    required = {
        "source_id", "query_id", "dimension", "reference_year",
        "indicator_id", "field_name", "raw_value", "numeric_value",
    }
    if not required.issubset(values.columns) or values.empty:
        raise ValueError("Produto complementar ausente ou inválido")
    inventory = pd.read_csv(sebrae_inventory_path, dtype=str)
    baseline = pd.read_csv(ips_baseline_path, dtype=str)
    ips_reconciliation = _ips_reconcile(values, baseline)
    ips_status = (
        ips_reconciliation.groupby("normalized_name").classification
        .agg(lambda s: "CONFLICT" if "CONFLICT" in set(s) else "CONTENT_DUPLICATE")
        .to_dict()
    )
    ibge_status = _ibge_cross_source_status(values)

    sebrae = inventory.set_index("query_id")
    records = []
    group_columns = ["source_id", "query_id", "dimension", "field_name"]
    for keys, group in values.groupby(group_columns, dropna=False):
        source_id, query_id, dimension, field_name = (str(item) for item in keys)
        normalized = normalize_name(field_name)
        years = pd.to_numeric(group.reference_year, errors="coerce").dropna()
        base = {
            "source_id": source_id,
            "query_id": query_id,
            "dimension": dimension,
            "field_name": field_name,
            "normalized_name": normalized,
            "rows": len(group),
            "nonmissing_values": int(group.raw_value.notna().sum()),
            "minimum_year": int(years.min()) if not years.empty else "",
            "maximum_year": int(years.max()) if not years.empty else "",
            "nature": "calculated_classification",
        }
        if source_id == "ips_brasil_explorer":
            if normalized in IPS_TECHNICAL_FIELDS:
                classification = "UNIQUE"
                rationale = "Chave territorial, não indicador analítico."
                decision = "EXCLUDE_TECHNICAL_KEY"
            elif normalized in ips_status:
                classification = ips_status[normalized]
                rationale = (
                    "Nome, ano e valor reconciliados com o módulo IPS existente."
                    if classification == "CONTENT_DUPLICATE"
                    else "Valor diverge do módulo IPS existente no mesmo ano."
                )
                decision = (
                    "PRESERVE_RAW_DO_NOT_INTEGRATE"
                    if classification == "CONTENT_DUPLICATE"
                    else "QUARANTINE_CONFLICT"
                )
            else:
                classification = "COMPLEMENTARY"
                rationale = "Indicador individual não presente no módulo IPS canônico."
                decision = "SEMANTIC_REVIEW_BEFORE_INTEGRATION"
        elif source_id == "sebrae_observatorio_profile":
            plan = sebrae.loc[query_id]
            measures = _measure_names(str(plan.query_url))
            if normalized not in measures:
                classification = "UNIQUE"
                rationale = "Chave ou categoria de desagregação, não medida solicitada."
                decision = "EXCLUDE_TECHNICAL_KEY"
            else:
                declared = str(plan.overlap_classification)
                classification = (
                    "PARTIAL_OVERLAP"
                    if declared == "PARTIAL_OVERLAP"
                    else "COMPLEMENTARY"
                )
                rationale = str(plan.recommended_decision)
                decision = (
                    "COMPARE_WITH_LOCAL_MODULE"
                    if classification == "PARTIAL_OVERLAP"
                    else "VERIFY_PRIMARY_SOURCE_BEFORE_INTEGRATION"
                )
        elif source_id == "ibge_cidades_panorama":
            classification, rationale = ibge_status.get(
                str(group.indicator_id.dropna().iloc[0]),
                (
                    "PARTIAL_OVERLAP",
                    "Panorama municipal sobrepõe parcialmente módulos IBGE existentes.",
                ),
            )
            decision = (
                "PRESERVE_RAW_DO_NOT_INTEGRATE"
                if classification == "CONTENT_DUPLICATE"
                else "QUARANTINE_CONFLICT"
                if classification == "CONFLICT"
                else "SEMANTIC_REVIEW_BEFORE_INTEGRATION"
            )
        else:
            classification = "PARTIAL_OVERLAP"
            rationale = "Panorama Censo 2022 sobrepõe parcialmente o módulo censitário."
            decision = "SEMANTIC_REVIEW_BEFORE_INTEGRATION"
        records.append(base | {
            "classification": classification,
            "rationale": rationale,
            "decision": decision,
        })

    register = pd.DataFrame(records).sort_values(group_columns).reset_index(drop=True)
    if not set(register.classification).issubset(CLASSES):
        raise ValueError("Classificação fora do contrato")
    classification_summary = (
        register.groupby(["classification", "decision"])
        .agg(contracts=("query_id", "size"), rows=("rows", "sum"))
        .reset_index()
        .sort_values(["classification", "decision"])
    )
    dimension_summary = (
        register.groupby(["dimension", "classification"])
        .agg(contracts=("query_id", "size"), rows=("rows", "sum"))
        .reset_index()
        .sort_values(["dimension", "classification"])
    )
    conflicts = int(register.classification.eq("CONFLICT").sum())
    validation = pd.DataFrame([
        ("input_rows", len(values), "observed", "PASS"),
        ("contracts_classified", len(register), "calculated", "PASS"),
        ("unclassified_contracts", 0, "calculated", "PASS"),
        ("ips_reconciled_values", len(ips_reconciliation), "calculated", "PASS"),
        ("content_duplicates", int(register.classification.eq(
            "CONTENT_DUPLICATE").sum()), "calculated", "INFORMATIONAL"),
        ("conflicts", conflicts, "calculated",
         "REVIEW_REQUIRED" if conflicts else "PASS"),
        ("canonical_rows_promoted", 0, "observed", "PASS"),
        ("drive_operations", 0, "observed", "PASS"),
    ], columns=["indicator", "value", "nature", "status"])
    if len(ips_reconciliation) != 48:
        raise ValueError(
            "Reconciliação IPS incompleta: "
            f"observado={len(ips_reconciliation)}, esperado=48"
        )

    partial.mkdir(parents=True)
    try:
        register.to_csv(partial / "indicator_semantic_register.csv", index=False)
        classification_summary.to_csv(
            partial / "classification_summary.csv", index=False
        )
        dimension_summary.to_csv(partial / "dimension_summary.csv", index=False)
        ips_reconciliation.to_csv(partial / "ips_reconciliation.csv", index=False)
        validation.to_csv(partial / "validation.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return SemanticAuditResult(
        register,
        classification_summary,
        dimension_summary,
        ips_reconciliation,
        validation,
        target,
    )
