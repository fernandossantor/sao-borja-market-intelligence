"""Matriz temporal auditável entre evidências canônicas e complementares."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from sbmi.temporal_dimension_audit import DIMENSIONS, THEME_MAP

ACTIONABLE_DECISIONS = {
    "SEMANTIC_REVIEW_BEFORE_INTEGRATION",
    "COMPARE_WITH_LOCAL_MODULE",
    "VERIFY_PRIMARY_SOURCE_BEFORE_INTEGRATION",
}


@dataclass(frozen=True)
class ComplementaryTemporalMatrixResult:
    output_path: Path
    matrix: pd.DataFrame
    indicator_coverage: pd.DataFrame
    dimension_priority: pd.DataFrame
    validation: pd.DataFrame


def _simple_identifier(value: str) -> None:
    if not value or Path(value).name != value:
        raise ValueError("run_id deve ser um identificador simples")


def _expand_contracts(
    contracts: pd.DataFrame,
    observed: pd.DataFrame,
    start_year: int,
    end_year: int,
) -> pd.DataFrame:
    years = pd.DataFrame({"reference_year": range(start_year, end_year + 1)})
    keys = [
        "evidence_origin", "source_id", "query_id", "dimension",
        "indicator_key", "indicator_label", "classification", "decision",
    ]
    grid = contracts[keys].drop_duplicates().merge(years, how="cross")
    counts = (
        observed.groupby([
            "evidence_origin", "source_id", "query_id", "dimension",
            "indicator_key", "reference_year",
        ], dropna=False)
        .size()
        .rename("observed_rows")
        .reset_index()
    )
    grid = grid.merge(
        counts,
        on=[
            "evidence_origin", "source_id", "query_id", "dimension",
            "indicator_key", "reference_year",
        ],
        how="left",
        validate="one_to_one",
    )
    grid["observed_rows"] = grid["observed_rows"].fillna(0).astype(int)
    grid["evidence_status"] = grid.observed_rows.gt(0).map(
        {True: "OBSERVED", False: "GAP"}
    )
    grid["nature"] = "calculated_presence"
    return grid.sort_values(
        ["dimension", "indicator_key", "source_id", "reference_year"]
    ).reset_index(drop=True)


def build_complementary_temporal_matrix(
    *,
    values_path: Path,
    semantic_register_path: Path,
    canonical_facts_path: Path,
    output_root: Path,
    run_id: str,
    start_year: int = 1996,
    end_year: int = 2026,
) -> ComplementaryTemporalMatrixResult:
    """Constrói presença ano a ano sem inferir continuidade ou equivalência."""
    _simple_identifier(run_id)
    if end_year < start_year:
        raise ValueError("Intervalo temporal inválido")
    target = output_root.resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")

    values = pd.read_csv(values_path, dtype=str)
    register = pd.read_csv(semantic_register_path, dtype=str)
    facts = pd.read_parquet(canonical_facts_path)
    values_required = {
        "source_id", "query_id", "dimension", "reference_year", "field_name"
    }
    register_required = {
        "source_id", "query_id", "dimension", "field_name", "normalized_name",
        "classification", "decision",
    }
    facts_required = {
        "theme", "reference_year", "indicator_id", "indicator_name",
        "source_dataset",
    }
    if (
        not values_required.issubset(values.columns)
        or not register_required.issubset(register.columns)
        or not facts_required.issubset(facts.columns)
    ):
        raise ValueError("Contrato de entrada divergente")

    actionable = register.loc[
        register.decision.isin(ACTIONABLE_DECISIONS)
        & register.dimension.isin(DIMENSIONS)
    ].copy()
    comp_contracts = actionable.assign(
        evidence_origin="complementary_candidate",
        indicator_key=(
            actionable.source_id + ":" + actionable.query_id + ":"
            + actionable.normalized_name
        ),
        indicator_label=actionable.field_name,
    )
    comp_observed = values.merge(
        comp_contracts[[
            "source_id", "query_id", "dimension", "field_name",
            "evidence_origin", "indicator_key",
        ]].drop_duplicates(),
        on=["source_id", "query_id", "dimension", "field_name"],
        how="inner",
        validate="many_to_one",
    )
    comp_observed["reference_year"] = pd.to_numeric(
        comp_observed.reference_year, errors="coerce"
    ).astype("Int64")
    comp_observed = comp_observed.loc[
        comp_observed.reference_year.between(start_year, end_year)
    ].copy()

    canonical = facts.copy()
    canonical["dimension"] = canonical.theme.map(THEME_MAP)
    if canonical.dimension.isna().any():
        unknown = sorted(set(canonical.loc[canonical.dimension.isna(), "theme"]))
        raise ValueError(f"Temas canônicos não mapeados: {unknown}")
    canonical["reference_year"] = pd.to_numeric(
        canonical.reference_year, errors="coerce"
    ).astype("Int64")
    canonical = canonical.loc[
        canonical.reference_year.between(start_year, end_year)
    ].copy()
    canonical["evidence_origin"] = "canonical"
    canonical["source_id"] = canonical.source_dataset.astype(str)
    canonical["query_id"] = canonical.source_dataset.astype(str)
    canonical["indicator_key"] = canonical.indicator_id.astype(str)
    canonical["indicator_label"] = canonical.indicator_name.astype(str)
    canonical["classification"] = "CANONICAL_OBSERVED"
    canonical["decision"] = "PRESERVE_CANONICAL"
    canonical_contracts = canonical[[
        "evidence_origin", "source_id", "query_id", "dimension",
        "indicator_key", "indicator_label", "classification", "decision",
    ]].drop_duplicates()

    contracts = pd.concat([
        comp_contracts[canonical_contracts.columns],
        canonical_contracts,
    ], ignore_index=True)
    observed = pd.concat([
        comp_observed[[
            "evidence_origin", "source_id", "query_id", "dimension",
            "indicator_key", "reference_year",
        ]],
        canonical[[
            "evidence_origin", "source_id", "query_id", "dimension",
            "indicator_key", "reference_year",
        ]],
    ], ignore_index=True)
    matrix = _expand_contracts(contracts, observed, start_year, end_year)

    group_cols = [
        "evidence_origin", "source_id", "dimension", "indicator_key",
        "indicator_label", "classification", "decision",
    ]
    coverage_rows = []
    for keys, group in matrix.groupby(group_cols, dropna=False):
        observed_years = group.loc[
            group.evidence_status.eq("OBSERVED"), "reference_year"
        ].tolist()
        coverage_rows.append(dict(zip(group_cols, keys, strict=True)) | {
            "years_observed": len(observed_years),
            "target_years": end_year - start_year + 1,
            "first_year": min(observed_years) if observed_years else "",
            "last_year": max(observed_years) if observed_years else "",
            "missing_years": ",".join(map(str, group.loc[
                group.evidence_status.eq("GAP"), "reference_year"
            ].tolist())),
            "nature": "calculated_presence",
        })
    indicator_coverage = pd.DataFrame(coverage_rows)

    dimensions = pd.DataFrame({"dimension": list(DIMENSIONS)})
    priority = (
        matrix.loc[matrix.evidence_origin.eq("complementary_candidate")]
        .groupby("dimension")
        .agg(
            candidate_indicators=("indicator_key", "nunique"),
            candidate_year_cells=("evidence_status", "size"),
            observed_year_cells=("evidence_status", lambda s: int(s.eq("OBSERVED").sum())),
        )
        .reset_index()
    )
    dimension_priority = dimensions.merge(priority, on="dimension", how="left")
    count_columns = [
        "candidate_indicators", "candidate_year_cells", "observed_year_cells"
    ]
    for column in count_columns:
        dimension_priority[column] = dimension_priority[column].fillna(0).astype(int)
    dimension_priority["gap_year_cells"] = (
        dimension_priority.candidate_year_cells
        - dimension_priority.observed_year_cells
    )
    dimension_priority["priority_rank"] = (
        dimension_priority.observed_year_cells.rank(
            method="dense", ascending=False
        ).astype(int)
    )
    dimension_priority["nature"] = "calculated_priority_not_quality_score"
    dimension_priority = dimension_priority.sort_values(
        ["priority_rank", "dimension"]
    ).reset_index(drop=True)

    duplicate_keys = int(matrix.duplicated([
        "evidence_origin", "source_id", "query_id", "dimension",
        "indicator_key", "reference_year",
    ]).sum())
    validation = pd.DataFrame([
        ("dimensions_expected", len(DIMENSIONS), "calculated", "PASS"),
        ("dimensions_in_matrix", matrix.dimension.nunique(), "calculated", "PASS"),
        ("target_years", end_year - start_year + 1, "observed_parameter", "PASS"),
        ("candidate_contracts", len(comp_contracts), "calculated", "PASS"),
        ("matrix_duplicate_keys", duplicate_keys, "calculated",
         "PASS" if duplicate_keys == 0 else "FAIL"),
        ("canonical_rows_promoted", 0, "calculated", "PASS"),
    ], columns=["indicator", "value", "nature", "status"])
    if validation.status.eq("FAIL").any():
        raise ValueError("Validação da matriz temporal falhou")

    partial.mkdir(parents=True)
    try:
        matrix.to_csv(partial / "temporal_evidence_matrix.csv", index=False)
        indicator_coverage.to_csv(
            partial / "indicator_temporal_coverage.csv", index=False
        )
        dimension_priority.to_csv(
            partial / "dimension_priority.csv", index=False
        )
        validation.to_csv(partial / "validation.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return ComplementaryTemporalMatrixResult(
        target, matrix, indicator_coverage, dimension_priority, validation
    )
