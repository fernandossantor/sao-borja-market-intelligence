"""Síntese de cobertura que preserva relações temáticas secundárias."""

from __future__ import annotations

import pandas as pd

from sbmi.base_territorial_coverage import (
    BLOCKS,
    BLOCK_LABELS,
    CoverageMapResult,
    build_summary,
)


def _matched_mask(files: pd.DataFrame, block: str) -> pd.Series:
    matched = files["matched_blocks"].fillna("").astype(str)
    return matched.map(
        lambda value: block in {part for part in value.split("|") if part}
    ) | files["primary_block"].eq(block)


def _coverage_status(
    *,
    curated_modules: int,
    validated_staging: int,
    derived_products: int,
    primary_candidates: int,
    primary_raw_files: int,
    all_candidates: int,
) -> str:
    if curated_modules:
        return "CURATED_VALIDATED_PRESENT"
    if validated_staging:
        return "STAGING_VALIDATED_PRESENT"
    if derived_products:
        return "DERIVED_PRODUCTS_AUDITED_PRESENT"
    if primary_raw_files:
        return "RAW_SOURCES_PRESENT"
    if primary_candidates:
        return "METADATA_CANDIDATES_PRESENT"
    if all_candidates:
        return "SECONDARY_TOPIC_CANDIDATES_PRESENT"
    return "NO_CANDIDATE_IDENTIFIED"


def _next_action(status: str) -> str:
    return {
        "CURATED_VALIDATED_PRESENT": (
            "Integrar o módulo à síntese comum e avaliar lacunas de cobertura."
        ),
        "STAGING_VALIDATED_PRESENT": (
            "Documentar conceitos, unidade, abrangência e construir camada curada."
        ),
        "DERIVED_PRODUCTS_AUDITED_PRESENT": (
            "Revisar metodologia, fonte, período e atualidade antes da reutilização."
        ),
        "RAW_SOURCES_PRESENT": (
            "Auditar conteúdo e estrutura; construir staging quando aplicável."
        ),
        "METADATA_CANDIDATES_PRESENT": (
            "Confirmar a classificação e a utilidade analítica dos candidatos."
        ),
        "SECONDARY_TOPIC_CANDIDATES_PRESENT": (
            "Avaliar a suficiência das menções secundárias e procurar fonte dedicada "
            "somente se a cobertura temática for insuficiente."
        ),
        "NO_CANDIDATE_IDENTIFIED": (
            "Revisar o acervo antes de buscar nova fonte externa."
        ),
    }[status]


def build_secondary_aware_block_summary(
    files: pd.DataFrame,
    evidence: pd.DataFrame,
) -> pd.DataFrame:
    """Conta relações primárias e secundárias sem tratá-las como equivalentes."""
    eligible = files.loc[files["analytical_candidate"]]
    records: list[dict[str, object]] = []
    for block in BLOCKS:
        matched_group = eligible.loc[_matched_mask(eligible, block)]
        primary_group = matched_group.loc[
            matched_group["primary_block"].eq(block)
        ]
        secondary_group = matched_group.loc[
            ~matched_group["primary_block"].eq(block)
        ]
        evidence_group = evidence.loc[evidence["block"].eq(block)]
        staging = evidence_group.loc[evidence_group["layer"].eq("staging")]
        validated_staging = int(
            staging["validation_status"].eq("STRUCTURAL_VALIDATION_OK").sum()
        )
        curated = int(
            evidence_group["layer"].eq("curated_local_module").sum()
        )
        derived = int(
            evidence_group["layer"].eq("historical_derived_product").sum()
        )
        primary_raw = int(primary_group["source_stage"].eq("raw").sum())
        status = _coverage_status(
            curated_modules=curated,
            validated_staging=validated_staging,
            derived_products=derived,
            primary_candidates=len(primary_group),
            primary_raw_files=primary_raw,
            all_candidates=len(matched_group),
        )
        records.append(
            {
                "block": block,
                "block_label": BLOCK_LABELS[block],
                "candidate_files": len(matched_group),
                "primary_candidate_files": len(primary_group),
                "secondary_candidate_files": len(secondary_group),
                "known_bytes": int(matched_group["size_bytes"].sum()),
                "source_families": int(
                    matched_group["source_family"].nunique()
                ),
                "raw_files": int(
                    matched_group["source_stage"].eq("raw").sum()
                ),
                "primary_raw_files": primary_raw,
                "secondary_raw_files": int(
                    secondary_group["source_stage"].eq("raw").sum()
                ),
                "processed_files": int(
                    matched_group["source_stage"].eq("processed").sum()
                ),
                "warehouse_files": int(
                    matched_group["source_stage"].eq("warehouse").sum()
                ),
                "export_files": int(
                    matched_group["source_stage"].eq("exports").sum()
                ),
                "staging_datasets": len(staging),
                "validated_staging_datasets": validated_staging,
                "curated_modules": curated,
                "audited_derived_families": derived,
                "coverage_status": status,
                "substantive_validation_status": (
                    "PARTIAL" if curated else "PENDING"
                ),
                "next_action": _next_action(status),
                "nature": "calculated_diagnostic",
            }
        )
    return pd.DataFrame(records)


def build_secondary_aware_gap_register(
    block_summary: pd.DataFrame,
) -> pd.DataFrame:
    """Distingue falta de fonte dedicada de ausência de qualquer candidato."""
    gap_by_status = {
        "CURATED_VALIDATED_PRESENT": (
            "INTEGRATION_AND_SYNTHESIS_PENDING",
            "A cobertura validada pode não ser exaustiva para o bloco.",
        ),
        "STAGING_VALIDATED_PRESENT": (
            "CURATED_LAYER_PENDING",
            "A validação é estrutural; conceitos e comparabilidade seguem pendentes.",
        ),
        "DERIVED_PRODUCTS_AUDITED_PRESENT": (
            "METHODOLOGICAL_REVIEW_PENDING",
            "A presença de produto não comprova atualidade ou validade metodológica.",
        ),
        "RAW_SOURCES_PRESENT": (
            "STRUCTURAL_AUDIT_OR_STAGING_PENDING",
            "A presença da fonte não comprova legibilidade ou utilidade analítica.",
        ),
        "METADATA_CANDIDATES_PRESENT": (
            "CLASSIFICATION_AND_VALIDATION_PENDING",
            "A classificação decorre de regras de caminho e palavras-chave.",
        ),
        "SECONDARY_TOPIC_CANDIDATES_PRESENT": (
            "DEDICATED_SOURCE_REVIEW_PENDING",
            "Há menções temáticas, mas nenhuma fonte primária dedicada foi identificada.",
        ),
        "NO_CANDIDATE_IDENTIFIED": (
            "NO_CANDIDATE_IDENTIFIED_BY_CURRENT_RULES",
            "Não é possível concluir ausência de dados apenas pelo mapa atual.",
        ),
    }
    records: list[dict[str, object]] = []
    for row in block_summary.itertuples(index=False):
        gap_class, limitation = gap_by_status[row.coverage_status]
        records.append(
            {
                "block": row.block,
                "block_label": row.block_label,
                "coverage_status": row.coverage_status,
                "gap_class": gap_class,
                "what_cannot_be_concluded": limitation,
                "required_next_evidence": row.next_action,
                "nature": "calculated_diagnostic",
            }
        )
    return pd.DataFrame(records)


def apply_secondary_topic_coverage(
    result: CoverageMapResult,
    inventory: pd.DataFrame,
) -> CoverageMapResult:
    """Atualiza a síntese final preservando a hierarquia entre relações."""
    block_summary = build_secondary_aware_block_summary(
        result.files,
        result.evidence_register,
    )
    gap_register = build_secondary_aware_gap_register(block_summary)
    summary = build_summary(
        inventory,
        result.files,
        result.source_families,
        result.evidence_register,
        block_summary,
    )
    return CoverageMapResult(
        files=result.files,
        source_families=result.source_families,
        evidence_register=result.evidence_register,
        block_summary=block_summary,
        gap_register=gap_register,
        summary=summary,
    )
