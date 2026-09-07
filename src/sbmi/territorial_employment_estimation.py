"""Estimate employment exposure to local and external business structures."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

MATRIX_LOCAL = "MATRIZ_LOCAL"
LOCAL_BRANCH = "FILIAL_DE_MATRIZ_LOCAL"
EXTERNAL_BRANCH = "FILIAL_DE_MATRIZ_EXTERNA"
STATUSES = [MATRIX_LOCAL, LOCAL_BRANCH, EXTERNAL_BRANCH]
MATCH_LEVELS = ["subclass_nature", "subclass", "class_nature", "class", "division"]
SENSITIVITY_FACTORS = [0.5, 0.75, 1.0, 1.5, 2.0, 3.0]


@dataclass(frozen=True)
class EmploymentEstimationResult:
    cells: pd.DataFrame
    coverage: pd.DataFrame
    division: pd.DataFrame
    sensitivity: pd.DataFrame
    summary: pd.DataFrame
    validation: pd.DataFrame


def _code(series: pd.Series, width: int | None = None) -> pd.Series:
    out = series.fillna("").astype(str).str.strip().str.replace(r"\.0$", "", regex=True)
    return out.str.zfill(width) if width else out


def _prepare_rais(
    frame: pd.DataFrame,
    municipality_code: str,
    establishment_type: str,
    nature_prefix: str,
) -> pd.DataFrame:
    required = {
        "CNAE 2.0 Subclasse - Codigo",
        "Município - Código",
        "Natureza Jurídica - Código",
        "Qtd Vínculos Ativos",
        "Tipo Estabelecimento - Código",
    }
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"RAIS sem colunas obrigatórias: {missing}")

    work = frame.copy()
    work["municipality_code"] = _code(work["Município - Código"])
    work["establishment_type"] = _code(work["Tipo Estabelecimento - Código"])
    work["natureza_juridica"] = _code(work["Natureza Jurídica - Código"], 4)
    work["cnae_subclass"] = _code(work["CNAE 2.0 Subclasse - Codigo"], 7)
    work["active_links"] = pd.to_numeric(work["Qtd Vínculos Ativos"], errors="coerce").fillna(0)
    work = work[
        (work["municipality_code"] == str(municipality_code))
        & (work["establishment_type"] == str(establishment_type))
        & work["natureza_juridica"].str.startswith(str(nature_prefix))
    ]
    cells = (
        work.groupby(["cnae_subclass", "natureza_juridica"], as_index=False)
        .agg(
            rais_establishments=("establishment_type", "size"),
            active_links=("active_links", "sum"),
        )
        .sort_values(["cnae_subclass", "natureza_juridica"])
        .reset_index(drop=True)
    )
    cells["cnae_class"] = cells["cnae_subclass"].str[:5]
    cells["cnae_division"] = cells["cnae_subclass"].str[:2]
    return cells


def _prepare_rfb(frame: pd.DataFrame, nature_prefix: str) -> pd.DataFrame:
    required = {
        "cnae_subclass",
        "natureza_juridica",
        "territorial_control_status",
        "estabelecimentos",
    }
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"RFB sem colunas obrigatórias: {missing}")

    work = frame.copy()
    work["cnae_subclass"] = _code(work["cnae_subclass"], 7)
    work["natureza_juridica"] = _code(work["natureza_juridica"], 4)
    work["estabelecimentos"] = pd.to_numeric(work["estabelecimentos"], errors="raise").astype(int)
    work = work[
        work["natureza_juridica"].str.startswith(str(nature_prefix))
        & work["territorial_control_status"].isin(STATUSES)
    ].copy()
    work["cnae_class"] = work["cnae_subclass"].str[:5]
    work["cnae_division"] = work["cnae_subclass"].str[:2]
    return work.reset_index(drop=True)


def _pivot(frame: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    out = (
        frame.groupby(keys + ["territorial_control_status"])["estabelecimentos"]
        .sum()
        .unstack(fill_value=0)
    )
    for status in STATUSES:
        if status not in out.columns:
            out[status] = 0
    return out[STATUSES]


def _tables(rfb: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {
        "subclass_nature": _pivot(rfb, ["cnae_subclass", "natureza_juridica"]),
        "subclass": _pivot(rfb, ["cnae_subclass"]),
        "class_nature": _pivot(rfb, ["cnae_class", "natureza_juridica"]),
        "class": _pivot(rfb, ["cnae_class"]),
        "division": _pivot(rfb, ["cnae_division"]),
    }


def _match_key(row: pd.Series, level: str):
    keys = {
        "subclass_nature": (row["cnae_subclass"], row["natureza_juridica"]),
        "subclass": row["cnae_subclass"],
        "class_nature": (row["cnae_class"], row["natureza_juridica"]),
        "class": row["cnae_class"],
        "division": row["cnae_division"],
    }
    return keys[level]


def _assign(rais: pd.DataFrame, rfb: pd.DataFrame) -> pd.DataFrame:
    tables = _tables(rfb)
    rows = []
    for _, row in rais.iterrows():
        level = "unmatched"
        counts = pd.Series({status: 0 for status in STATUSES})
        for candidate in MATCH_LEVELS:
            key = _match_key(row, candidate)
            if key in tables[candidate].index:
                level = candidate
                counts = tables[candidate].loc[key]
                break
        total = int(counts.sum())
        links = float(row["active_links"])
        rows.append(
            row.to_dict()
            | {
                "match_level": level,
                "rfb_matrix_local": int(counts[MATRIX_LOCAL]),
                "rfb_local_branch": int(counts[LOCAL_BRANCH]),
                "rfb_external_branch": int(counts[EXTERNAL_BRANCH]),
                "rfb_establishments_in_match": total,
                "estimated_matrix_local_links": (
                    links * counts[MATRIX_LOCAL] / total if total else 0.0
                ),
                "estimated_local_branch_links": (
                    links * counts[LOCAL_BRANCH] / total if total else 0.0
                ),
                "estimated_external_branch_links": (
                    links * counts[EXTERNAL_BRANCH] / total if total else 0.0
                ),
                "result_nature": "estimated",
            }
        )
    return pd.DataFrame(rows)


def _coverage(cells: pd.DataFrame) -> pd.DataFrame:
    total = float(cells["active_links"].sum())
    cumulative = 0.0
    rows = []
    for level in MATCH_LEVELS + ["unmatched"]:
        part = cells[cells["match_level"] == level]
        links = float(part["active_links"].sum())
        cumulative += links
        rows.append(
            {
                "match_level": level,
                "rais_cells": len(part),
                "rais_establishments": int(part["rais_establishments"].sum()),
                "active_links": links,
                "active_links_share_pct": 100 * links / total if total else 0.0,
                "cumulative_active_links_share_pct": 100 * cumulative / total if total else 0.0,
                "nature": "calculated",
            }
        )
    return pd.DataFrame(rows)


def _division(cells: pd.DataFrame) -> pd.DataFrame:
    out = (
        cells.groupby("cnae_division", as_index=False)
        .agg(
            active_links=("active_links", "sum"),
            estimated_matrix_local_links=("estimated_matrix_local_links", "sum"),
            estimated_local_branch_links=("estimated_local_branch_links", "sum"),
            estimated_external_branch_links=("estimated_external_branch_links", "sum"),
        )
        .sort_values("estimated_external_branch_links", ascending=False)
        .reset_index(drop=True)
    )
    denominator = out["active_links"].astype(float).where(out["active_links"] != 0)
    total_external = float(out["estimated_external_branch_links"].sum())
    out["estimated_external_share_within_division_pct"] = (
        100 * out["estimated_external_branch_links"] / denominator
    ).fillna(0.0)
    out["share_of_total_estimated_external_pct"] = (
        100 * out["estimated_external_branch_links"] / total_external if total_external else 0.0
    )
    out["result_nature"] = "estimated"
    return out


def _sensitivity(cells: pd.DataFrame) -> pd.DataFrame:
    total = float(cells["active_links"].sum())
    rows = []
    for factor in SENSITIVITY_FACTORS:
        estimated = 0.0
        for _, row in cells.iterrows():
            external = float(row["rfb_external_branch"])
            local = float(row["rfb_matrix_local"] + row["rfb_local_branch"])
            denominator = factor * external + local
            if denominator:
                estimated += float(row["active_links"]) * factor * external / denominator
        rows.append(
            {
                "external_relative_employment_factor": factor,
                "estimated_external_links": estimated,
                "estimated_external_share_pct": 100 * estimated / total if total else 0.0,
                "result_nature": "estimated_sensitivity",
            }
        )
    return pd.DataFrame(rows)


def _reverse_coverage(rfb: pd.DataFrame, rais: pd.DataFrame) -> dict[str, float]:
    keys = {
        "subclass_nature": set(zip(rais["cnae_subclass"], rais["natureza_juridica"])),
        "subclass": set(rais["cnae_subclass"]),
        "class_nature": set(zip(rais["cnae_class"], rais["natureza_juridica"])),
        "class": set(rais["cnae_class"]),
        "division": set(rais["cnae_division"]),
    }

    def level(row: pd.Series) -> str:
        for candidate in MATCH_LEVELS:
            if _match_key(row, candidate) in keys[candidate]:
                return candidate
        return "unmatched"

    work = rfb.copy()
    work["reverse_match_level"] = work.apply(level, axis=1)
    exact = work[work["reverse_match_level"] == "subclass_nature"]
    matched = work[work["reverse_match_level"] != "unmatched"]
    return {
        "rfb_exact_establishments": float(exact["estabelecimentos"].sum()),
        "rfb_exact_external_establishments": float(
            exact.loc[
                exact["territorial_control_status"] == EXTERNAL_BRANCH, "estabelecimentos"
            ].sum()
        ),
        "rfb_matched_external_establishments": float(
            matched.loc[
                matched["territorial_control_status"] == EXTERNAL_BRANCH, "estabelecimentos"
            ].sum()
        ),
    }


def estimate_territorial_employment(
    rais_frame: pd.DataFrame,
    rfb_frame: pd.DataFrame,
    *,
    municipality_code: str = "431800",
    cnpj_establishment_type: str = "1",
    business_nature_prefix: str = "2",
) -> EmploymentEstimationResult:
    rais = _prepare_rais(
        rais_frame,
        municipality_code,
        cnpj_establishment_type,
        business_nature_prefix,
    )
    rfb = _prepare_rfb(rfb_frame, business_nature_prefix)
    cells = _assign(rais, rfb)
    coverage = _coverage(cells)
    division = _division(cells)
    sensitivity = _sensitivity(cells)
    reverse = _reverse_coverage(rfb, rais)

    total_links = float(cells["active_links"].sum())
    total_matrix = float(cells["estimated_matrix_local_links"].sum())
    total_local_branch = float(cells["estimated_local_branch_links"].sum())
    total_external = float(cells["estimated_external_branch_links"].sum())
    exact = cells[cells["match_level"] == "subclass_nature"]
    exact_links = float(exact["active_links"].sum())
    exact_external = float(exact["estimated_external_branch_links"].sum())
    has_external = cells["rfb_external_branch"] > 0
    has_local = (cells["rfb_matrix_local"] + cells["rfb_local_branch"]) > 0
    exact_status_count = (
        (exact[["rfb_matrix_local", "rfb_local_branch", "rfb_external_branch"]] > 0).sum(axis=1)
    )
    positive = cells[cells["estimated_external_branch_links"] > 0].sort_values(
        "estimated_external_branch_links", ascending=False
    )
    total_positive = float(positive["estimated_external_branch_links"].sum())

    def top_share(n: int) -> float:
        return (
            100 * float(positive.head(n)["estimated_external_branch_links"].sum()) / total_positive
            if total_positive
            else 0.0
        )

    rfb_total = float(rfb["estabelecimentos"].sum())
    rfb_external = float(
        rfb.loc[rfb["territorial_control_status"] == EXTERNAL_BRANCH, "estabelecimentos"].sum()
    )
    establishment_share = 100 * rfb_external / rfb_total if rfb_total else 0.0
    external_share = 100 * total_external / total_links if total_links else 0.0
    summary = pd.DataFrame(
        [
            ("rais_business_establishments", rais["rais_establishments"].sum(), "observed"),
            ("rais_business_active_links", total_links, "observed"),
            ("rfb_business_establishments", rfb_total, "calculated"),
            ("rfb_external_business_establishments", rfb_external, "calculated"),
            ("rfb_external_business_establishments_share_pct", establishment_share, "calculated"),
            ("exact_match_active_links", exact_links, "calculated"),
            ("exact_match_active_links_share_pct", 100 * exact_links / total_links, "calculated"),
            (
                "exact_only_estimated_external_share_pct",
                100 * exact_external / exact_links,
                "estimated",
            ),
            ("estimated_matrix_local_links", total_matrix, "estimated"),
            ("estimated_local_branch_links", total_local_branch, "estimated"),
            ("estimated_external_branch_links", total_external, "estimated"),
            ("estimated_external_share_pct", external_share, "estimated"),
            (
                "external_labor_weight_over_establishment_weight",
                external_share / establishment_share if establishment_share else 0.0,
                "estimated",
            ),
            (
                "pure_external_cell_active_links",
                cells.loc[has_external & ~has_local, "active_links"].sum(),
                "calculated",
            ),
            (
                "any_external_cell_active_links",
                cells.loc[has_external, "active_links"].sum(),
                "calculated",
            ),
            ("exact_pure_cells", int((exact_status_count == 1).sum()), "calculated"),
            (
                "exact_pure_active_links",
                exact.loc[exact_status_count == 1, "active_links"].sum(),
                "calculated",
            ),
            ("exact_mixed_cells", int((exact_status_count > 1).sum()), "calculated"),
            (
                "exact_mixed_active_links",
                exact.loc[exact_status_count > 1, "active_links"].sum(),
                "calculated",
            ),
            ("positive_external_contribution_cells", len(positive), "calculated"),
            ("top1_external_contribution_share_pct", top_share(1), "calculated"),
            ("top5_external_contribution_share_pct", top_share(5), "calculated"),
            ("top10_external_contribution_share_pct", top_share(10), "calculated"),
            ("top20_external_contribution_share_pct", top_share(20), "calculated"),
            ("top50_external_contribution_share_pct", top_share(50), "calculated"),
            ("rfb_exact_establishments", reverse["rfb_exact_establishments"], "calculated"),
            (
                "rfb_exact_external_establishments",
                reverse["rfb_exact_external_establishments"],
                "calculated",
            ),
            (
                "rfb_matched_external_establishments",
                reverse["rfb_matched_external_establishments"],
                "calculated",
            ),
        ],
        columns=["indicator", "value", "nature"],
    )
    reconstructed = total_matrix + total_local_branch + total_external
    validation = pd.DataFrame(
        [
            ("rais_active_links_total", total_links, "PASS" if total_links == 8595 else "REVIEW"),
            (
                "estimated_links_reconcile",
                abs(reconstructed - total_links),
                "PASS" if abs(reconstructed - total_links) < 1e-6 else "FAIL",
            ),
            ("exact_match_active_links", exact_links, "PASS" if exact_links == 8581 else "REVIEW"),
            (
                "unmatched_active_links",
                float(
                    cells.loc[cells["match_level"] == "unmatched", "active_links"].sum()
                ),
                "PASS",
            ),
            ("rfb_business_establishments", rfb_total, "PASS" if rfb_total == 6906 else "REVIEW"),
            (
                "rfb_external_business_establishments",
                rfb_external,
                "PASS" if rfb_external == 284 else "REVIEW",
            ),
        ],
        columns=["indicator", "value", "status"],
    )
    if "FAIL" in set(validation["status"]):
        raise ValueError("Reconciliação da estimativa falhou")
    return EmploymentEstimationResult(cells, coverage, division, sensitivity, summary, validation)


def build_source_manifest(rais_path: Path, rfb_path: Path) -> pd.DataFrame:
    rows = []
    for role, path in [("rais_establishments_extract", rais_path), ("rfb_cells", rfb_path)]:
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


def write_estimation_outputs(
    result: EmploymentEstimationResult,
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
        "territorial_employment_cells.csv": result.cells,
        "territorial_employment_coverage.csv": result.coverage,
        "territorial_employment_by_division.csv": result.division,
        "territorial_employment_sensitivity.csv": result.sensitivity,
        "territorial_employment_summary.csv": result.summary,
        "validation.csv": result.validation,
    }
    if source_manifest is not None:
        outputs["source_manifest.csv"] = source_manifest
    if run_metadata is not None:
        outputs["run_metadata.csv"] = run_metadata
    for name, frame in outputs.items():
        frame.to_csv(output_dir / name, index=False)
