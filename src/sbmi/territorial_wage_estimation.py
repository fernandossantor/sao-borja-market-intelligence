"""Estimate territorial employment and wage exposure from RAIS workers and RFB cells."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from sbmi.territorial_employment_estimation import (
    EXTERNAL_BRANCH,
    LOCAL_BRANCH,
    MATCH_LEVELS,
    MATRIX_LOCAL,
    STATUSES,
    _code,
    _match_key,
    _prepare_rfb,
    _tables,
)

METRICS = ["active_links", "dec_mass", "avg_rem_sum"]


@dataclass(frozen=True)
class WageEstimationResult:
    cells: pd.DataFrame
    coverage: pd.DataFrame
    division: pd.DataFrame
    summary: pd.DataFrame
    validation: pd.DataFrame


def _numeric(series: pd.Series) -> pd.Series:
    """Parse RAIS nominal remuneration values while preserving empty fields as NA."""
    text = series.fillna("").astype(str).str.strip().replace("", pd.NA)
    filled = text.fillna("")
    both = filled.str.contains(",", regex=False) & filled.str.contains(".", regex=False)
    comma_decimal = both & (filled.str.rfind(",") > filled.str.rfind("."))
    dot_decimal = both & ~comma_decimal
    text.loc[comma_decimal] = (
        text.loc[comma_decimal]
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    text.loc[dot_decimal] = text.loc[dot_decimal].str.replace(",", "", regex=False)
    only_comma = filled.str.contains(",", regex=False) & ~filled.str.contains(".", regex=False)
    text.loc[only_comma] = text.loc[only_comma].str.replace(",", ".", regex=False)
    return pd.to_numeric(text, errors="coerce")


def _prepare_worker_rows(
    frame: pd.DataFrame,
    municipality_code: str,
    establishment_type: str,
    nature_prefix: str,
) -> pd.DataFrame:
    required = {
        "CNAE 2.0 Subclasse - Codigo",
        "Município - Código",
        "Natureza Jurídica - Código",
        "Ind Vínculo Ativo 31/12 - Código",
        "Ind Vínculo Abandonado - Código",
        "Tipo Estabelecimento - Código",
        "Vl Rem Dezembro Nom",
        "Vl Rem Média Nom",
    }
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"RAIS vínculos sem colunas obrigatórias: {missing}")

    work = frame.copy()
    work["municipality_code"] = _code(work["Município - Código"])
    work["establishment_type"] = _code(work["Tipo Estabelecimento - Código"])
    work["natureza_juridica"] = _code(work["Natureza Jurídica - Código"], 4)
    work["cnae_subclass"] = _code(work["CNAE 2.0 Subclasse - Codigo"], 7)
    work["active_indicator"] = _code(work["Ind Vínculo Ativo 31/12 - Código"])
    work["abandoned_indicator"] = _code(work["Ind Vínculo Abandonado - Código"])
    work["dec_rem"] = _numeric(work["Vl Rem Dezembro Nom"])
    work["avg_rem"] = _numeric(work["Vl Rem Média Nom"])

    return work[
        (work["municipality_code"] == str(municipality_code))
        & (work["active_indicator"] == "1")
        & (work["abandoned_indicator"] == "0")
        & (work["establishment_type"] == str(establishment_type))
        & work["natureza_juridica"].str.startswith(str(nature_prefix))
    ].copy()


def _aggregate_worker_cells(rows: pd.DataFrame) -> pd.DataFrame:
    cells = (
        rows.groupby(["cnae_subclass", "natureza_juridica"], as_index=False)
        .agg(
            active_links=("cnae_subclass", "size"),
            dec_valid=("dec_rem", "count"),
            dec_mass=("dec_rem", "sum"),
            avg_valid=("avg_rem", "count"),
            avg_rem_sum=("avg_rem", "sum"),
        )
        .sort_values(["cnae_subclass", "natureza_juridica"])
        .reset_index(drop=True)
    )
    cells["cnae_class"] = cells["cnae_subclass"].str[:5]
    cells["cnae_division"] = cells["cnae_subclass"].str[:2]
    return cells


def _assign_metrics(rais: pd.DataFrame, rfb: pd.DataFrame) -> pd.DataFrame:
    tables = _tables(rfb)
    rows: list[dict[str, object]] = []
    for _, row in rais.iterrows():
        level = "unmatched"
        counts = pd.Series({status: 0 for status in STATUSES})
        for candidate in MATCH_LEVELS:
            key = _match_key(row, candidate)
            if key in tables[candidate].index:
                level = candidate
                counts = tables[candidate].loc[key]
                break
        total = float(counts.sum())
        out = row.to_dict() | {
            "match_level": level,
            "rfb_matrix_local": int(counts[MATRIX_LOCAL]),
            "rfb_local_branch": int(counts[LOCAL_BRANCH]),
            "rfb_external_branch": int(counts[EXTERNAL_BRANCH]),
            "rfb_establishments_in_match": int(total),
            "result_nature": "estimated",
        }
        for metric in METRICS:
            value = float(row[metric])
            out[f"estimated_matrix_local_{metric}"] = (
                value * float(counts[MATRIX_LOCAL]) / total if total else 0.0
            )
            out[f"estimated_local_branch_{metric}"] = (
                value * float(counts[LOCAL_BRANCH]) / total if total else 0.0
            )
            out[f"estimated_external_{metric}"] = (
                value * float(counts[EXTERNAL_BRANCH]) / total if total else 0.0
            )
        rows.append(out)
    return pd.DataFrame(rows)


def _coverage(cells: pd.DataFrame) -> pd.DataFrame:
    totals = {metric: float(cells[metric].sum()) for metric in METRICS}
    rows = []
    for level in MATCH_LEVELS + ["unmatched"]:
        part = cells[cells["match_level"] == level]
        row: dict[str, object] = {"match_level": level, "rais_cells": len(part)}
        for metric in METRICS:
            value = float(part[metric].sum())
            total = totals[metric]
            row[metric] = value
            row[f"{metric}_share_pct"] = 100 * value / total if total else 0.0
        row["nature"] = "calculated"
        rows.append(row)
    return pd.DataFrame(rows)


def _division(cells: pd.DataFrame) -> pd.DataFrame:
    aggregations: dict[str, tuple[str, str]] = {}
    for metric in METRICS:
        aggregations[metric] = (metric, "sum")
        aggregations[f"estimated_matrix_local_{metric}"] = (
            f"estimated_matrix_local_{metric}",
            "sum",
        )
        aggregations[f"estimated_local_branch_{metric}"] = (
            f"estimated_local_branch_{metric}",
            "sum",
        )
        aggregations[f"estimated_external_{metric}"] = (
            f"estimated_external_{metric}",
            "sum",
        )
    out = cells.groupby("cnae_division", as_index=False).agg(**aggregations)
    for metric in METRICS:
        denominator = out[metric].astype(float).where(out[metric] != 0)
        total_external = float(out[f"estimated_external_{metric}"].sum())
        out[f"estimated_external_{metric}_share_within_division_pct"] = (
            100 * out[f"estimated_external_{metric}"] / denominator
        ).fillna(0.0)
        out[f"share_of_total_estimated_external_{metric}_pct"] = (
            100 * out[f"estimated_external_{metric}"] / total_external
            if total_external
            else 0.0
        )
    out["result_nature"] = "estimated"
    return out.sort_values("estimated_external_avg_rem_sum", ascending=False).reset_index(drop=True)


def _metric_summary(cells: pd.DataFrame, metric: str) -> tuple[float, float, float, float]:
    total = float(cells[metric].sum())
    external = float(cells[f"estimated_external_{metric}"].sum())
    share = 100 * external / total if total else 0.0
    exact = cells[cells["match_level"] == "subclass_nature"]
    exact_total = float(exact[metric].sum())
    exact_external = float(exact[f"estimated_external_{metric}"].sum())
    exact_share = 100 * exact_external / exact_total if exact_total else 0.0
    return total, external, share, exact_share


def estimate_territorial_wages(
    rais_workers_frame: pd.DataFrame,
    rfb_frame: pd.DataFrame,
    *,
    municipality_code: str = "431800",
    cnpj_establishment_type: str = "1",
    business_nature_prefix: str = "2",
    expected_business_active_links: int | None = None,
) -> WageEstimationResult:
    worker_rows = _prepare_worker_rows(
        rais_workers_frame,
        municipality_code,
        cnpj_establishment_type,
        business_nature_prefix,
    )
    rais = _aggregate_worker_cells(worker_rows)
    rfb = _prepare_rfb(rfb_frame, business_nature_prefix)
    cells = _assign_metrics(rais, rfb)
    coverage = _coverage(cells)
    division = _division(cells)

    employment = _metric_summary(cells, "active_links")
    december = _metric_summary(cells, "dec_mass")
    average = _metric_summary(cells, "avg_rem_sum")
    rfb_total = float(rfb["estabelecimentos"].sum())
    rfb_external = float(
        rfb.loc[rfb["territorial_control_status"] == EXTERNAL_BRANCH, "estabelecimentos"].sum()
    )
    establishment_share = 100 * rfb_external / rfb_total if rfb_total else 0.0
    avg_external_mean = average[1] / employment[1] if employment[1] else 0.0
    local_links = employment[0] - employment[1]
    local_avg_sum = average[0] - average[1]
    avg_local_mean = local_avg_sum / local_links if local_links else 0.0

    summary = pd.DataFrame(
        [
            ("rais_business_active_links", employment[0], "observed"),
            ("rais_dec_valid_links", float(worker_rows["dec_rem"].notna().sum()), "observed"),
            ("rais_dec_missing_links", float(worker_rows["dec_rem"].isna().sum()), "observed"),
            ("rais_dec_zero_links", float(worker_rows["dec_rem"].eq(0).sum()), "observed"),
            ("rais_dec_mass_informed", december[0], "observed"),
            ("rais_avg_valid_links", float(worker_rows["avg_rem"].notna().sum()), "observed"),
            ("rais_avg_zero_links", float(worker_rows["avg_rem"].eq(0).sum()), "observed"),
            ("rais_avg_rem_sum", average[0], "observed"),
            ("rais_avg_rem_mean", float(worker_rows["avg_rem"].mean()), "calculated"),
            ("rais_avg_rem_median", float(worker_rows["avg_rem"].median()), "calculated"),
            ("rfb_business_establishments", rfb_total, "calculated"),
            ("rfb_external_business_establishments", rfb_external, "calculated"),
            ("rfb_external_business_establishments_share_pct", establishment_share, "calculated"),
            ("estimated_external_active_links", employment[1], "estimated"),
            ("estimated_external_active_links_share_pct", employment[2], "estimated"),
            ("exact_only_estimated_external_active_links_share_pct", employment[3], "estimated"),
            ("estimated_external_dec_mass", december[1], "estimated"),
            ("estimated_external_dec_mass_share_pct", december[2], "estimated"),
            ("exact_only_estimated_external_dec_mass_share_pct", december[3], "estimated"),
            ("estimated_external_avg_rem_sum", average[1], "estimated"),
            ("estimated_external_avg_rem_sum_share_pct", average[2], "estimated"),
            ("exact_only_estimated_external_avg_rem_sum_share_pct", average[3], "estimated"),
            (
                "external_dec_weight_over_employment_weight",
                december[2] / employment[2] if employment[2] else 0.0,
                "estimated",
            ),
            (
                "external_avg_rem_weight_over_employment_weight",
                average[2] / employment[2] if employment[2] else 0.0,
                "estimated",
            ),
            ("estimated_external_avg_rem_per_link", avg_external_mean, "estimated"),
            ("estimated_local_tied_avg_rem_per_link", avg_local_mean, "estimated"),
        ],
        columns=["indicator", "value", "nature"],
    )

    validations: list[tuple[str, float, str]] = []
    if expected_business_active_links is not None:
        validations.append(
            (
                "rais_business_active_links",
                employment[0],
                "PASS" if employment[0] == expected_business_active_links else "REVIEW",
            )
        )
    for metric in METRICS:
        observed = float(cells[metric].sum())
        allocated = sum(
            float(cells[f"estimated_{status}_{metric}"].sum())
            for status in ["matrix_local", "local_branch", "external"]
        )
        diff = abs(allocated - observed)
        validations.append(
            (f"{metric}_allocation_reconcile", diff, "PASS" if diff < 0.01 else "FAIL")
        )
    unmatched_links = float(
        cells.loc[cells["match_level"] == "unmatched", "active_links"].sum()
    )
    validations.extend(
        [
            (
                "unmatched_active_links",
                unmatched_links,
                "PASS" if unmatched_links == 0 else "REVIEW",
            ),
            ("rfb_business_establishments", rfb_total, "PASS" if rfb_total == 6906 else "REVIEW"),
            (
                "rfb_external_business_establishments",
                rfb_external,
                "PASS" if rfb_external == 284 else "REVIEW",
            ),
        ]
    )
    validation = pd.DataFrame(validations, columns=["indicator", "value", "status"])
    if "FAIL" in set(validation["status"]):
        raise ValueError("Reconciliação da estimativa de remuneração falhou")
    return WageEstimationResult(cells, coverage, division, summary, validation)


def build_source_manifest(rais_workers_path: Path, rfb_path: Path) -> pd.DataFrame:
    rows = []
    for role, path in [("rais_workers_extract", rais_workers_path), ("rfb_cells", rfb_path)]:
        content = Path(path).read_bytes()
        rows.append(
            {
                "role": role,
                "source_file": Path(path).name,
                "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
                "nature": "observed_input",
            }
        )
    return pd.DataFrame(rows)


def write_wage_outputs(
    result: WageEstimationResult,
    output_dir: Path,
    *,
    source_manifest: pd.DataFrame | None = None,
    run_metadata: pd.DataFrame | None = None,
) -> None:
    output_dir = Path(output_dir)
    if output_dir.exists():
        raise FileExistsError(output_dir)
    output_dir.mkdir(parents=True)
    outputs = {
        "territorial_wage_cells.csv": result.cells,
        "territorial_wage_coverage.csv": result.coverage,
        "territorial_wage_by_division.csv": result.division,
        "territorial_wage_summary.csv": result.summary,
        "validation.csv": result.validation,
    }
    if source_manifest is not None:
        outputs["source_manifest.csv"] = source_manifest
    if run_metadata is not None:
        outputs["run_metadata.csv"] = run_metadata
    for name, frame in outputs.items():
        frame.to_csv(output_dir / name, index=False)
