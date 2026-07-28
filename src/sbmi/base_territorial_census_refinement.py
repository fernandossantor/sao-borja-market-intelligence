"""Refinamento temático dos arquivos do Censo 2022 de São Borja."""

from __future__ import annotations

import pandas as pd

from sbmi.base_territorial_coverage import (
    BLOCK_LABELS,
    CoverageMapResult,
    build_source_family_summary,
    normalize_text,
)

CENSUS_PROFILE_PATH = normalize_text("exports/census_profile.csv")
CENSUS_SCOPE_TOKENS = ("censo 2022", "sao borja rs")
CENSUS_TOPIC_RULES = (
    (
        "alfabetizacao",
        "educacao",
        ("educacao", "demografia"),
        "CENSUS_2022_LITERACY",
    ),
    (
        "caracteristicas do entorno",
        "infraestrutura_conectividade",
        ("infraestrutura_conectividade", "demografia"),
        "CENSUS_2022_SURROUNDINGS",
    ),
    (
        "caracteristicas dos domicilios",
        "infraestrutura_conectividade",
        ("infraestrutura_conectividade", "demografia"),
        "CENSUS_2022_HOUSEHOLD_CHARACTERISTICS",
    ),
    (
        "composicao domiciliar",
        "demografia",
        ("demografia",),
        "CENSUS_2022_HOUSEHOLD_COMPOSITION",
    ),
    (
        "crescimento populacional",
        "demografia",
        ("demografia",),
        "CENSUS_2022_POPULATION_GROWTH",
    ),
    (
        "deficiencia e autismo",
        "saude_condicoes_sociais",
        ("saude_condicoes_sociais", "demografia"),
        "CENSUS_2022_DISABILITY_AUTISM",
    ),
    (
        "meios de transporte mais usados",
        "infraestrutura_conectividade",
        ("infraestrutura_conectividade", "demografia"),
        "CENSUS_2022_TRANSPORT_MODES",
    ),
    (
        "nivel de instrucao",
        "educacao",
        ("educacao", "demografia"),
        "CENSUS_2022_EDUCATIONAL_ATTAINMENT",
    ),
    (
        "piramide etaria",
        "demografia",
        ("demografia",),
        "CENSUS_2022_AGE_PYRAMID",
    ),
    (
        "populacao indigena",
        "demografia",
        ("demografia", "ambiente_sociocultural_territorial"),
        "CENSUS_2022_INDIGENOUS_POPULATION",
    ),
    (
        "populacao por cor ou raca",
        "demografia",
        ("demografia", "ambiente_sociocultural_territorial"),
        "CENSUS_2022_RACE_COLOR",
    ),
    (
        "populacao por religiao",
        "ambiente_sociocultural_territorial",
        ("ambiente_sociocultural_territorial", "demografia"),
        "CENSUS_2022_RELIGION",
    ),
    (
        "populacao por sexo",
        "demografia",
        ("demografia",),
        "CENSUS_2022_SEX",
    ),
    (
        "populacao por situacao do domicilio",
        "demografia",
        ("demografia", "ambiente_sociocultural_territorial"),
        "CENSUS_2022_URBAN_RURAL",
    ),
    (
        "populacao quilombola",
        "demografia",
        ("demografia", "ambiente_sociocultural_territorial"),
        "CENSUS_2022_QUILOMBOLA_POPULATION",
    ),
    (
        "populacao residente em favelas",
        "demografia",
        (
            "demografia",
            "saude_condicoes_sociais",
            "ambiente_sociocultural_territorial",
        ),
        "CENSUS_2022_FAVELA_POPULATION",
    ),
    (
        "territorio",
        "demografia",
        (
            "demografia",
            "ambiente_sociocultural_territorial",
            "infraestrutura_conectividade",
        ),
        "CENSUS_2022_TERRITORY",
    ),
)


def _is_census_source(normalized_path: str) -> bool:
    return all(token in normalized_path for token in CENSUS_SCOPE_TOKENS)


def _apply(
    files: pd.DataFrame,
    mask: pd.Series,
    *,
    primary_block: str,
    matched_blocks: tuple[str, ...],
    basis: str,
    eligible: bool = True,
) -> None:
    files.loc[mask, "primary_block"] = primary_block
    files.loc[mask, "block_label"] = BLOCK_LABELS[primary_block]
    files.loc[mask, "matched_blocks"] = "|".join(matched_blocks)
    files.loc[mask, "classification_method"] = "EXPLICIT_CENSUS_TOPIC_REVIEW"
    files.loc[mask, "classification_basis"] = basis
    files.loc[mask, "classification_confidence"] = "HIGH"
    files.loc[mask, "coverage_eligible"] = eligible
    files.loc[mask, "analytical_candidate"] = (
        files.loc[mask, "analytical_extension"] & eligible
    )


def refine_census_topic_files(files: pd.DataFrame) -> pd.DataFrame:
    """Corrige a classificação de fontes e produtos censitários já conhecidos."""
    refined = files.copy()
    normalized_paths = refined["relative_path"].fillna("").astype(str).map(
        normalize_text
    )

    profile_mask = normalized_paths.eq(CENSUS_PROFILE_PATH)
    _apply(
        refined,
        profile_mask,
        primary_block="governanca_documentacao",
        matched_blocks=("governanca_documentacao",),
        basis="CENSUS_PROFILE_IS_TECHNICAL_METADATA",
        eligible=False,
    )

    census_scope = normalized_paths.map(_is_census_source)
    matched_any = pd.Series(False, index=refined.index)
    for token, primary, matched, basis in CENSUS_TOPIC_RULES:
        rule_mask = census_scope & normalized_paths.str.contains(
            token,
            regex=False,
        )
        matched_any |= rule_mask
        _apply(
            refined,
            rule_mask,
            primary_block=primary,
            matched_blocks=matched,
            basis=basis,
        )

    unmatched = census_scope & ~matched_any
    if unmatched.any():
        _apply(
            refined,
            unmatched,
            primary_block="transversal_multitematico",
            matched_blocks=("transversal_multitematico", "demografia"),
            basis="CENSUS_2022_TOPIC_REVIEW_REQUIRED",
        )
        refined.loc[unmatched, "classification_confidence"] = "MEDIUM"

    return refined.sort_values(
        ["source_stage", "source_family", "relative_path"]
    ).reset_index(drop=True)


def apply_census_topic_refinement(
    result: CoverageMapResult,
) -> CoverageMapResult:
    """Atualiza arquivos e famílias antes da síntese com temas secundários."""
    files = refine_census_topic_files(result.files)
    source_families = build_source_family_summary(files)
    return CoverageMapResult(
        files=files,
        source_families=source_families,
        evidence_register=result.evidence_register,
        block_summary=result.block_summary,
        gap_register=result.gap_register,
        summary=result.summary,
    )
