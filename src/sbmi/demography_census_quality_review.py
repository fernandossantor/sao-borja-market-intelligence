"""Diagnóstico de qualidade dos produtos processados do Censo 2022."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

import pandas as pd

DATASET_REQUIRED_COLUMNS = {
    "dataset_identity",
    "processed_relative_path",
    "content_equivalence_status",
}
DIFFERENCE_REQUIRED_COLUMNS = {
    "dataset_identity",
    "column",
    "raw_kind",
    "raw_value",
    "processed_kind",
    "processed_value",
}
EXACT_STATUS = "EXACT_AFTER_CANONICALIZATION"
MISMATCH_STATUSES = {
    "SCHEMA_MISMATCH",
    "ROW_COUNT_MISMATCH",
    "CELL_VALUE_MISMATCH",
    "READ_ERROR",
}


@dataclass(frozen=True)
class CensusQualityReviewResult:
    datasets: pd.DataFrame
    anomalies: pd.DataFrame
    summary: pd.DataFrame


def _decimal(value: object) -> Decimal | None:
    text = str(value or "").strip().replace(",", ".")
    if not text:
        return None
    try:
        return Decimal(text)
    except InvalidOperation:
        return None


def _scale_factor(raw_value: object, processed_value: object) -> Decimal | None:
    raw = _decimal(raw_value)
    processed = _decimal(processed_value)
    if raw is None or processed is None or raw == 0:
        return None
    return processed / raw


def _format_decimal(value: Decimal) -> str:
    normalized = value.normalize()
    text = format(normalized, "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def _classify_mismatch(group: pd.DataFrame) -> tuple[str, str, str, str]:
    if group.empty:
        return (
            "MISMATCH_WITHOUT_CELL_DETAIL",
            "QUARANTINE_PROCESSED_PRODUCT",
            "REVIEW_SCHEMA_ROWS_AND_READING_ERRORS",
            "",
        )
    numeric = group["raw_kind"].eq("number") & group["processed_kind"].eq(
        "number"
    )
    factors = [
        factor
        for factor in (
            _scale_factor(raw, processed)
            for raw, processed in zip(
                group["raw_value"],
                group["processed_value"],
                strict=True,
            )
        )
        if factor is not None
    ]
    unique_factors = sorted(set(factors))
    factor_text = "|".join(_format_decimal(value) for value in unique_factors)
    if bool(numeric.all()) and len(factors) == len(group) and len(unique_factors) == 1:
        factor = unique_factors[0]
        if factor in {Decimal("100"), Decimal("0.01")}:
            return (
                "SYSTEMATIC_DECIMAL_SCALE_ERROR",
                "QUARANTINE_PROCESSED_PRODUCT",
                "REBUILD_FROM_RAW_SOURCE_WITH_DECIMAL_PRESERVATION",
                factor_text,
            )
        return (
            "SYSTEMATIC_NUMERIC_SCALE_DIFFERENCE",
            "QUARANTINE_PROCESSED_PRODUCT",
            "REVIEW_NUMERIC_TRANSFORMATION_AND_REBUILD_FROM_RAW",
            factor_text,
        )
    return (
        "HETEROGENEOUS_CONTENT_MISMATCH",
        "QUARANTINE_PROCESSED_PRODUCT",
        "REVIEW_CELL_DIFFERENCES_AND_REBUILD_FROM_RAW",
        factor_text,
    )


def review_census_quality(
    dataset_comparison: pd.DataFrame,
    cell_differences: pd.DataFrame,
) -> CensusQualityReviewResult:
    """Classifica equivalências e anomalias sem validar a autoridade da fonte."""
    missing = DATASET_REQUIRED_COLUMNS.difference(dataset_comparison.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes na comparação por dataset: "
            f"{sorted(missing)}"
        )
    if cell_differences.empty:
        differences = pd.DataFrame(columns=sorted(DIFFERENCE_REQUIRED_COLUMNS))
    else:
        missing = DIFFERENCE_REQUIRED_COLUMNS.difference(cell_differences.columns)
        if missing:
            raise ValueError(
                "Colunas obrigatórias ausentes nas diferenças de células: "
                f"{sorted(missing)}"
            )
        differences = cell_differences.copy()

    records: list[dict[str, object]] = []
    anomaly_records: list[dict[str, object]] = []
    grouped = {
        str(identity): group.copy()
        for identity, group in differences.groupby("dataset_identity", sort=True)
    }
    for row in dataset_comparison.itertuples(index=False):
        identity = str(row.dataset_identity)
        status = str(row.content_equivalence_status)
        group = grouped.get(identity, pd.DataFrame(columns=differences.columns))
        if status == EXACT_STATUS:
            anomaly_class = "NO_CONTENT_ANOMALY_DETECTED"
            reuse_status = "CONTENT_EQUIVALENT_SOURCE_NOT_VALIDATED"
            action = "RETAIN_WITH_PROVENANCE_REVIEW_PENDING"
            factors = ""
        elif status in MISMATCH_STATUSES:
            anomaly_class, reuse_status, action, factors = _classify_mismatch(group)
        else:
            anomaly_class = "UNRECOGNIZED_COMPARISON_STATUS"
            reuse_status = "QUARANTINE_PROCESSED_PRODUCT"
            action = "REVIEW_COMPARISON_STATUS"
            factors = ""

        affected_columns = (
            "|".join(sorted(set(group["column"].astype(str))))
            if not group.empty
            else ""
        )
        records.append(
            {
                "dataset_identity": identity,
                "processed_relative_path": str(row.processed_relative_path),
                "content_equivalence_status": status,
                "affected_cells": len(group),
                "affected_columns": affected_columns,
                "observed_scale_factors": factors,
                "quality_class": anomaly_class,
                "processed_reuse_status": reuse_status,
                "recommended_action": action,
                "source_authority_status": "PENDING_SOURCE_METADATA_REVIEW",
                "conceptual_validation_status": "NOT_VALIDATED",
                "nature": "observed_and_calculated",
            }
        )
        if anomaly_class != "NO_CONTENT_ANOMALY_DETECTED":
            anomaly_records.append(records[-1].copy())

    datasets = pd.DataFrame(records).sort_values("dataset_identity").reset_index(
        drop=True
    )
    anomalies = pd.DataFrame(anomaly_records, columns=datasets.columns)
    summary = pd.DataFrame(
        [
            ("datasets_reviewed", len(datasets), "calculated"),
            (
                "content_equivalent_datasets",
                int(datasets["quality_class"].eq("NO_CONTENT_ANOMALY_DETECTED").sum()),
                "calculated",
            ),
            (
                "datasets_quarantined",
                int(
                    datasets["processed_reuse_status"]
                    .eq("QUARANTINE_PROCESSED_PRODUCT")
                    .sum()
                ),
                "calculated",
            ),
            (
                "systematic_decimal_scale_errors",
                int(
                    datasets["quality_class"]
                    .eq("SYSTEMATIC_DECIMAL_SCALE_ERROR")
                    .sum()
                ),
                "calculated",
            ),
            (
                "affected_cells",
                int(datasets["affected_cells"].sum()),
                "observed",
            ),
            ("source_authority_reviews_completed", 0, "observed"),
            ("conceptually_validated_datasets", 0, "observed"),
        ],
        columns=["indicator", "value", "nature"],
    )
    return CensusQualityReviewResult(
        datasets=datasets,
        anomalies=anomalies,
        summary=summary,
    )


def write_census_quality_review(
    result: CensusQualityReviewResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica o diagnóstico local de forma atômica."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino da revisão já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    outputs = {
        "demography_census_quality_register.csv": result.datasets,
        "demography_census_quarantine_register.csv": result.anomalies,
        "demography_census_quality_summary.csv": result.summary,
    }
    try:
        for file_name, frame in outputs.items():
            frame.to_csv(partial / file_name, index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
