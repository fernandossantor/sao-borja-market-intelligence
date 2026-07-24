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
    normalize_text,
)

REFINEMENT_LABELS = {
    **BLOCK_LABELS,
    "fora_do_escopo_territorial": "Fora do escopo territorial",
}

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
    "exports/dashboard_dataset.csv",
    "warehouse/sao_borja.duckdb",
)

CALIBRATION_RULES = (
    (
        "demografia",
        ("demografia",),
        ("exports/census_",),
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

REVIEWED_FILE_RULES = {
    normalize_text("raw/pdfs/05154620-fronteira-oeste.pdf"): (
        "ambiente_politico_regulatorio",
        (
            "ambiente_politico_regulatorio",
            "transversal_multitematico",
            "economia_estrutura_produtiva",
            "infraestrutura_conectividade",
        ),
        "REVIEWED_COREDES_PED_2022_2030",
        True,
    ),
    normalize_text("raw/pdfs/25155756-mapa-corede-fronteiraoeste-2010.pdf"): (
        "ambiente_sociocultural_territorial",
        (
            "ambiente_sociocultural_territorial",
            "ambiente_politico_regulatorio",
        ),
        "REVIEWED_COREDES_TERRITORIAL_MAP",
        True,
    ),
    normalize_text("raw/pdfs/431084.pdf"): (
        "ambiente_sociocultural_territorial",
        ("ambiente_sociocultural_territorial",),
        "REVIEWED_ARCHAEOLOGICAL_HERITAGE_DISSERTATION",
        True,
    ),
    normalize_text("raw/pdfs/Apresentao_Encontro_de_secretarios.pdf"): (
        "economia_estrutura_produtiva",
        (
            "economia_estrutura_produtiva",
            "demografia",
            "ambiente_sociocultural_territorial",
        ),
        "REVIEWED_MUNICIPAL_AGRICULTURAL_PROFILE",
        True,
    ),
    normalize_text("raw/pdfs/DIS_PPGPC_2019_RODRIGUES_JOSE.pdf"): (
        "ambiente_sociocultural_territorial",
        ("ambiente_sociocultural_territorial",),
        "REVIEWED_MISSION_HERITAGE_DISSERTATION",
        True,
    ),
    normalize_text("raw/pdfs/FGVSOCIAL_Classes76a24Jan.pdf"): (
        "renda_emprego_trabalho",
        (
            "renda_emprego_trabalho",
            "economia_estrutura_produtiva",
        ),
        "REVIEWED_NATIONAL_INCOME_CLASS_REFERENCE",
        True,
    ),
    normalize_text("raw/pdfs/Perfil_Cidades_Gauchas-Sao_Borja.pdf"): (
        "transversal_multitematico",
        (
            "transversal_multitematico",
            "economia_estrutura_produtiva",
            "demografia",
            "financas_publicas_transferencias",
        ),
        "REVIEWED_SEBRAE_MUNICIPAL_PROFILE",
        True,
    ),
    normalize_text("raw/pdfs/PlanoDiretorMAPA.pdf"): (
        "ambiente_politico_regulatorio",
        (
            "ambiente_politico_regulatorio",
            "infraestrutura_conectividade",
            "ambiente_sociocultural_territorial",
        ),
        "REVIEWED_MUNICIPAL_MASTER_PLAN_MAP",
        True,
    ),
    normalize_text("raw/pdfs/Plano_Municipal_de_Sade_2014_2017.pdf"): (
        "saude_condicoes_sociais",
        (
            "saude_condicoes_sociais",
            "ambiente_politico_regulatorio",
        ),
        "REVIEWED_MUNICIPAL_HEALTH_PLAN",
        True,
    ),
    normalize_text("raw/pdfs/São_Borja-Relatorio_Versão_Final.pdf"): (
        "transversal_multitematico",
        (
            "transversal_multitematico",
            "demografia",
            "economia_estrutura_produtiva",
            "renda_emprego_trabalho",
            "educacao",
            "infraestrutura_conectividade",
            "saude_condicoes_sociais",
            "ambiente_sociocultural_territorial",
        ),
        "REVIEWED_MULTITHEMATIC_MUNICIPAL_REPORT",
        True,
    ),
    normalize_text("raw/pdfs/Sistema_motorizado.pdf"): (
        "infraestrutura_conectividade",
        (
            "infraestrutura_conectividade",
            "ambiente_politico_regulatorio",
            "ambiente_sociocultural_territorial",
        ),
        "REVIEWED_URBAN_ROAD_SYSTEM_MAP",
        True,
    ),
    normalize_text("raw/pdfs/admin,+1.pdf"): (
        "fora_do_escopo_territorial",
        ("fora_do_escopo_territorial",),
        "REVIEWED_OUT_OF_SCOPE_SANTA_CATARINA_HISTORIOGRAPHY",
        False,
    ),
    normalize_text("raw/pdfs/admin,+4659-26847-1-SM.pdf"): (
        "transversal_multitematico",
        (
            "transversal_multitematico",
            "demografia",
            "economia_estrutura_produtiva",
            "renda_emprego_trabalho",
            "educacao",
            "infraestrutura_conectividade",
            "saude_condicoes_sociais",
            "ambiente_politico_regulatorio",
            "ambiente_sociocultural_territorial",
        ),
        "REVIEWED_COREDES_SOCIOECONOMIC_PROFILE_2025",
        True,
    ),
    normalize_text("raw/pdfs/dossie-missoes-volume-1_o-temporal.pdf"): (
        "ambiente_sociocultural_territorial",
        ("ambiente_sociocultural_territorial",),
        "REVIEWED_MISSION_CULTURAL_DOSSIER",
        True,
    ),
    normalize_text(
        "raw/pdfs/lhilgemberg,+11+-+REDUÇÕES+JESUÍTICAS+NO+RIO+GRANDE+DO+SUL.pdf"
    ): (
        "ambiente_sociocultural_territorial",
        ("ambiente_sociocultural_territorial",),
        "REVIEWED_JESUIT_REDUCTIONS_REFERENCE",
        True,
    ),
}


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
    files.loc[mask, "block_label"] = REFINEMENT_LABELS[primary_block]
    files.loc[mask, "matched_blocks"] = "|".join(matched_blocks)
    files.loc[mask, "classification_method"] = method
    files.loc[mask, "classification_basis"] = basis
    files.loc[mask, "classification_confidence"] = "HIGH"
    files.loc[mask, "coverage_eligible"] = eligible
    files.loc[mask, "analytical_candidate"] = (
        files.loc[mask, "analytical_extension"] & eligible
    )


def _apply_institutional_review(
    refined: pd.DataFrame,
    normalized_paths: pd.Series,
) -> None:
    institutional_scope = normalized_paths.str.startswith(
        (
            "raw institucional ",
            "processed institucional ",
            "processed 202601 ",
        )
    )
    documentation = institutional_scope & (
        normalized_paths.str.contains(" observacoes ", regex=False)
        | normalized_paths.str.contains("tabela5881 notas", regex=False)
    )
    analytical = institutional_scope & ~documentation & (
        normalized_paths.str.contains(" cadastro ", regex=False)
        | normalized_paths.str.contains(" afastamentos ", regex=False)
        | normalized_paths.str.contains("serv por mun exerc", regex=False)
        | normalized_paths.str.contains("tabela5881", regex=False)
    )
    _apply_classification(
        refined,
        analytical,
        primary_block="renda_emprego_trabalho",
        matched_blocks=(
            "renda_emprego_trabalho",
            "economia_estrutura_produtiva",
        ),
        method="EXPLICIT_CONTENT_FAMILY_REVIEW",
        basis="REVIEWED_PUBLIC_PERSONNEL_AND_EMPLOYMENT_DATA",
        eligible=True,
    )
    _apply_classification(
        refined,
        documentation,
        primary_block="governanca_documentacao",
        matched_blocks=("governanca_documentacao",),
        method="EXPLICIT_NON_ANALYTICAL_ARTIFACT",
        basis="REVIEWED_DATASET_NOTES_AND_OBSERVATIONS",
        eligible=False,
    )


def _apply_reviewed_files(
    refined: pd.DataFrame,
    normalized_paths: pd.Series,
) -> None:
    for normalized_path, rule in REVIEWED_FILE_RULES.items():
        primary, matched, basis, eligible = rule
        _apply_classification(
            refined,
            normalized_paths.eq(normalized_path),
            primary_block=primary,
            matched_blocks=matched,
            method="EXPLICIT_FILE_CONTENT_REVIEW",
            basis=basis,
            eligible=eligible,
        )


def refine_files(files: pd.DataFrame) -> pd.DataFrame:
    """Aplica somente regras explicitamente justificadas pela revisão manual."""
    refined = files.copy()
    paths = refined["relative_path"].fillna("").astype(str)
    normalized_paths = paths.map(normalize_text)

    technical_mask = paths.map(
        lambda path: _matches_any(path, TECHNICAL_ARTIFACT_PREFIXES)
    )
    _apply_classification(
        refined,
        technical_mask,
        primary_block="governanca_documentacao",
        matched_blocks=("governanca_documentacao",),
        method="EXPLICIT_NON_ANALYTICAL_ARTIFACT",
        basis="CALIBRATION_TECHNICAL_EXPORTS_AND_WAREHOUSE",
        eligible=False,
    )

    for primary, matched, prefixes, basis in CALIBRATION_RULES:
        rule_mask = paths.map(
            lambda path, rule_prefixes=prefixes: _matches_any(
                path,
                rule_prefixes,
            )
        )
        _apply_classification(
            refined,
            rule_mask,
            primary_block=primary,
            matched_blocks=matched,
            method="EXPLICIT_CALIBRATION_RULE",
            basis=basis,
            eligible=True,
        )

    _apply_institutional_review(refined, normalized_paths)
    _apply_reviewed_files(refined, normalized_paths)

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
