"""Calibração explícita do mapa de cobertura territorial."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

from sbmi.base_territorial_coverage import (
    BLOCK_LABELS,
    CoverageMapResult,
    build_block_summary,
    build_gap_register,
    build_source_family_summary,
    build_summary,
)

TECHNICAL_ARTIFACT_PREFIXES = (
    "exports/domain_",
    "exports/inventory.",
    "exports/institutional_csv_profile",
    "exports/missing_domain_profile",
    "exports/model_assumptions_registry",
    "exports/public_dataset_profile",
    "exports/public_dataset_summary",
    "exports/semantic_",
    "exports/social_catalog",
    "exports/social_domain_map",
    "exports/social_inventory",
)

CALIBRATION_RULES = (
    (
        "demografia",
        ("demografia",),
        (
            "exports/census_",
        ),
        "CALIBRATION_EXPORT_CENSUS",
    ),
    (
        "renda_emprego_trabalho",
        ("renda_emprego_trabalho", "economia_estrutura_produtiva"),
        (
            "exports/labor_market_",
            "exports/private_employment_",
            "processed/202601_aposentados_",
            "processed/202601_militares/",
            "processed/202601_pensionistas_",
            "processed/202601_reserva_reforma_militares/",
            "processed/202601_servidores_",
        ),
        "CALIBRATION_LABOR_AND_PUBLIC_PERSONNEL",
    ),
    (
        "economia_estrutura_produtiva",
        ("economia_estrutura_produtiva",),
        (
            "exports/economic_",
            "exports/private_sector_",
            "exports/private_vab_",
            "exports/public_sector_",
            "exports/public_structural_",
            "exports/public_vab_",
            "exports/sector_",
            "exports/structural_analysis",
        ),
        "CALIBRATION_ECONOMIC_DERIVED_PRODUCTS",
    ),
)


def _matches_any(path: str, prefixes: Iterable[str]) -> bool:
    normalized = path.strip().casefold()
    return any(normalized.startswith(prefix.casefold()) for prefix in prefixes)


def _apply_classification(
    files: pd.DataFrame,
    mask: pd.Series,
    *,
    primary_block: str,
    matched_blocks: tuple[str, ...],
    method: str,
    basis: str,
    eligible: bool,
) -> None:
    files.loc[mask, "primary_block"] = primary_block
    files.loc[mask, "block_label"] = BLOCK_LABELS[primary_block]
    files.loc[mask, "matched_blocks"] = "|".join(matched_blocks)
    files.loc[mask, "classification_method"] = method
    files.loc[mask, "classification_basis"] = basis
    files.loc[mask, "classification_confidence"] = "HIGH"
    files.loc[mask, "coverage_eligible"] = eligible
    files.loc[mask, "analytical_candidate"] = (
        files.loc[mask, "analytical_extension"] & eligible
    )


def refine_files(files: pd.DataFrame) -> pd.DataFrame:
    """Aplica somente regras explicitamente justificadas pela revisão manual."""
    refined = files.copy()
    paths = refined["relative_path"].fillna("").astype(str)

    technical_mask = paths.map(
        lambda path: _matches_any(path, TECHNICAL_ARTIFACT_PREFIXES)
    )
    _apply_classification(
        refined,
        technical_mask,
        primary_block="governanca_documentacao",
        matched_blocks=("governanca_documentacao",),
        method="EXPLICIT_NON_ANALYTICAL_ARTIFACT",
        basis="CALIBRATION_TECHNICAL_EXPORTS",
        eligible=False,
    )

    for primary, matched, prefixes, basis in CALIBRATION_RULES:
        rule_mask = paths.map(lambda path: _matches_any(path, prefixes))
        _apply_classification(
            refined,
            rule_mask,
            primary_block=primary,
            matched_blocks=matched,
            method="EXPLICIT_CALIBRATION_RULE",
            basis=basis,
            eligible=True,
        )

    return refined.sort_values(
        ["source_stage", "source_family", "relative_path"]
    ).reset_index(drop=True)


def refine_coverage_map(
    result: CoverageMapResult,
    inventory: pd.DataFrame,
) -> CoverageMapResult:
    """Recalcula o diagnóstico depois da calibração explícita."""
    files = refine_files(result.files)
    source_families = build_source_family_summary(files)
    block_summary = build_block_summary(files, result.evidence_register)
    gap_register = build_gap_register(block_summary)
    summary = build_summary(
        inventory,
        files,
        source_families,
        result.evidence_register,
        block_summary,
    )
    return CoverageMapResult(
        files=files,
        source_families=source_families,
        evidence_register=result.evidence_register,
        block_summary=block_summary,
        gap_register=gap_register,
        summary=summary,
    )
