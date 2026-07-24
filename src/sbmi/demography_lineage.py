"""Revisão de linhagem entre fontes brutas e produtos demográficos derivados."""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "relative_path",
    "file_name",
    "extension",
    "source_stage",
    "source_family",
    "primary_block",
    "matched_blocks",
    "classification_method",
    "classification_basis",
    "analytical_candidate",
}
RAW_CENSUS_PREFIX = "raw/social/censo 2022 - "
PROCESSED_CENSUS_PREFIX = "processed/social/censo 2022 - "
TECHNICAL_PROFILE_PATHS = {"exports/census_profile.csv"}


@dataclass(frozen=True)
class DemographyLineageResult:
    source_candidates: pd.DataFrame
    lineage_register: pd.DataFrame
    classification_corrections: pd.DataFrame
    summary: pd.DataFrame


def normalize_text(value: object) -> str:
    decomposed = unicodedata.normalize("NFKD", str(value or ""))
    ascii_text = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    normalized = re.sub(r"[^a-z0-9]+", " ", ascii_text.casefold()).strip()
    return re.sub(r"\s+", " ", normalized)


def _truthy(value: object) -> bool:
    return value is True or str(value).strip().casefold() in {
        "true",
        "1",
        "yes",
    }


def _dataset_identity(path: object) -> str:
    file_name = Path(str(path or "")).name
    stem = Path(file_name).stem
    stem = re.sub(r"_Sheet\d+$", "", stem, flags=re.IGNORECASE)
    return normalize_text(stem)


def _candidate_kind(path: object) -> str:
    normalized = str(path or "").strip().casefold()
    if normalized.startswith(RAW_CENSUS_PREFIX):
        return "RAW_CENSUS_SOURCE"
    if normalized.startswith(PROCESSED_CENSUS_PREFIX):
        return "PROCESSED_CENSUS_PRODUCT"
    if normalized in TECHNICAL_PROFILE_PATHS:
        return "TECHNICAL_CENSUS_PROFILE"
    return "OTHER"


def select_lineage_candidates(coverage_files: pd.DataFrame) -> pd.DataFrame:
    """Seleciona fontes e produtos do Censo sem depender da classe temática atual."""
    missing = REQUIRED_COLUMNS.difference(coverage_files.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no mapa de cobertura: "
            f"{sorted(missing)}"
        )

    frame = coverage_files.copy()
    frame["candidate_kind"] = frame["relative_path"].map(_candidate_kind)
    selected = frame.loc[frame["candidate_kind"].ne("OTHER")].copy()
    selected["dataset_identity"] = selected["relative_path"].map(_dataset_identity)
    selected["currently_analytical_candidate"] = selected[
        "analytical_candidate"
    ].map(_truthy)
    selected["lineage_evidence_basis"] = "NORMALIZED_FILENAME_AND_STAGE"
    selected["lineage_evidence_strength"] = "STRUCTURAL_ONLY"
    selected["nature"] = "observed_and_calculated"
    return selected.sort_values(
        ["dataset_identity", "candidate_kind", "relative_path"]
    ).reset_index(drop=True)


def build_lineage_register(source_candidates: pd.DataFrame) -> pd.DataFrame:
    """Relaciona fontes e derivados sem afirmar igualdade de conteúdo."""
    data_candidates = source_candidates.loc[
        source_candidates["candidate_kind"].isin(
            {"RAW_CENSUS_SOURCE", "PROCESSED_CENSUS_PRODUCT"}
        )
    ]
    records: list[dict[str, object]] = []
    for identity, group in data_candidates.groupby("dataset_identity", sort=True):
        raw_paths = sorted(
            group.loc[
                group["candidate_kind"].eq("RAW_CENSUS_SOURCE"),
                "relative_path",
            ].astype(str)
        )
        processed_paths = sorted(
            group.loc[
                group["candidate_kind"].eq("PROCESSED_CENSUS_PRODUCT"),
                "relative_path",
            ].astype(str)
        )
        if len(raw_paths) == 1 and len(processed_paths) == 1:
            status = "MATCHED_ONE_TO_ONE_BY_NAME"
        elif raw_paths and not processed_paths:
            status = "RAW_ONLY"
        elif processed_paths and not raw_paths:
            status = "PROCESSED_ONLY"
        else:
            status = "AMBIGUOUS_MULTIPLE_CANDIDATES"
        records.append(
            {
                "dataset_identity": identity,
                "raw_source_count": len(raw_paths),
                "processed_product_count": len(processed_paths),
                "raw_source_paths": "|".join(raw_paths),
                "processed_product_paths": "|".join(processed_paths),
                "lineage_match_status": status,
                "lineage_evidence_basis": "NORMALIZED_FILENAME_AND_STAGE",
                "content_equivalence_status": "NOT_TESTED",
                "source_authority_status": "PENDING_SOURCE_METADATA_REVIEW",
                "period_status": "PENDING_SOURCE_METADATA_REVIEW",
                "unit_status": "PENDING_SOURCE_METADATA_REVIEW",
                "geographic_scope_status": "PENDING_SOURCE_METADATA_REVIEW",
                "comparability_status": "NOT_ASSESSED",
                "next_action": (
                    "SNAPSHOT_RAW_AND_COMPARE_CONTENT"
                    if status == "MATCHED_ONE_TO_ONE_BY_NAME"
                    else "RESOLVE_LINEAGE_CANDIDATES"
                ),
                "what_cannot_be_concluded": (
                    "A correspondência nominal não comprova identidade de conteúdo, "
                    "fonte oficial, período, unidade ou comparabilidade."
                ),
                "nature": "calculated_diagnostic",
            }
        )
    return pd.DataFrame(records).sort_values("dataset_identity").reset_index(drop=True)


def build_classification_corrections(
    source_candidates: pd.DataFrame,
) -> pd.DataFrame:
    """Propõe correções explícitas ao mapa, sem aplicá-las silenciosamente."""
    records: list[dict[str, object]] = []
    for row in source_candidates.itertuples(index=False):
        if row.candidate_kind == "RAW_CENSUS_SOURCE":
            proposed_primary = "demografia"
            proposed_matched = "demografia"
            proposed_eligible = True
            reason = "RAW_CENSUS_SOURCE_EXACT_TITLE_FAMILY"
        elif row.candidate_kind == "TECHNICAL_CENSUS_PROFILE":
            proposed_primary = "governanca_documentacao"
            proposed_matched = "governanca_documentacao"
            proposed_eligible = False
            reason = "TECHNICAL_PROFILE_NOT_SUBSTANTIVE_DATA"
        else:
            proposed_primary = row.primary_block
            proposed_matched = row.matched_blocks
            proposed_eligible = bool(row.currently_analytical_candidate)
            reason = "KEEP_PROCESSED_DERIVED_CLASSIFICATION"
        records.append(
            {
                "relative_path": row.relative_path,
                "candidate_kind": row.candidate_kind,
                "current_primary_block": row.primary_block,
                "current_matched_blocks": row.matched_blocks,
                "current_analytical_candidate": row.currently_analytical_candidate,
                "proposed_primary_block": proposed_primary,
                "proposed_matched_blocks": proposed_matched,
                "proposed_analytical_candidate": proposed_eligible,
                "correction_reason": reason,
                "application_status": "PROPOSED_NOT_APPLIED",
                "nature": "diagnostic_recommendation",
            }
        )
    return pd.DataFrame(records).sort_values(
        ["candidate_kind", "relative_path"]
    ).reset_index(drop=True)


def build_summary(
    source_candidates: pd.DataFrame,
    lineage_register: pd.DataFrame,
    corrections: pd.DataFrame,
) -> pd.DataFrame:
    kinds = source_candidates["candidate_kind"]
    status = lineage_register["lineage_match_status"]
    indicators = [
        ("lineage_candidates", len(source_candidates), "calculated"),
        (
            "raw_census_sources",
            int(kinds.eq("RAW_CENSUS_SOURCE").sum()),
            "calculated",
        ),
        (
            "processed_census_products",
            int(kinds.eq("PROCESSED_CENSUS_PRODUCT").sum()),
            "calculated",
        ),
        (
            "technical_census_profiles",
            int(kinds.eq("TECHNICAL_CENSUS_PROFILE").sum()),
            "calculated",
        ),
        ("dataset_identities", len(lineage_register), "calculated"),
        (
            "matched_one_to_one_by_name",
            int(status.eq("MATCHED_ONE_TO_ONE_BY_NAME").sum()),
            "calculated",
        ),
        ("raw_only", int(status.eq("RAW_ONLY").sum()), "calculated"),
        ("processed_only", int(status.eq("PROCESSED_ONLY").sum()), "calculated"),
        (
            "ambiguous_lineage",
            int(status.eq("AMBIGUOUS_MULTIPLE_CANDIDATES").sum()),
            "calculated",
        ),
        (
            "proposed_classification_corrections",
            int(
                (
                    corrections["current_primary_block"]
                    != corrections["proposed_primary_block"]
                ).sum()
                + (
                    corrections["current_analytical_candidate"]
                    != corrections["proposed_analytical_candidate"]
                ).sum()
            ),
            "calculated",
        ),
        ("content_equivalence_tests_completed", 0, "observed"),
        ("conceptually_validated_datasets", 0, "observed"),
    ]
    return pd.DataFrame(indicators, columns=["indicator", "value", "nature"])


def audit_demography_lineage(
    coverage_files: pd.DataFrame,
) -> DemographyLineageResult:
    source_candidates = select_lineage_candidates(coverage_files)
    lineage_register = build_lineage_register(source_candidates)
    corrections = build_classification_corrections(source_candidates)
    summary = build_summary(source_candidates, lineage_register, corrections)
    return DemographyLineageResult(
        source_candidates=source_candidates,
        lineage_register=lineage_register,
        classification_corrections=corrections,
        summary=summary,
    )


def write_demography_lineage(
    result: DemographyLineageResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino da revisão de linhagem já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    outputs = {
        "demography_lineage_candidates.csv": result.source_candidates,
        "demography_lineage_register.csv": result.lineage_register,
        "demography_classification_corrections.csv": (
            result.classification_corrections
        ),
        "demography_lineage_summary.csv": result.summary,
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
