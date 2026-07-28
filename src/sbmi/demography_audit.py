"""Auditoria dos candidatos demográficos existentes no acervo."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

DEMOGRAPHY_BLOCK = "demografia"
COVERAGE_REQUIRED_COLUMNS = {
    "relative_path",
    "file_name",
    "extension",
    "size_bytes",
    "source_stage",
    "source_family",
    "primary_block",
    "matched_blocks",
    "classification_method",
    "classification_basis",
    "classification_confidence",
    "analytical_candidate",
}
FILE_PROFILE_REQUIRED_COLUMNS = {
    "relative_path",
    "read_status",
    "tables_observed",
    "rows_observed",
}
TABLE_PROFILE_REQUIRED_COLUMNS = {
    "relative_path",
    "table_name",
    "source_format",
    "rows_observed",
    "columns_observed",
    "headers",
    "geography_signal_estimate",
    "time_signal_estimate",
    "measure_signal_estimate",
    "category_signal_estimate",
    "utility_estimate",
}


@dataclass(frozen=True)
class DemographyAuditResult:
    candidates: pd.DataFrame
    tables: pd.DataFrame
    families: pd.DataFrame
    decisions: pd.DataFrame
    summary: pd.DataFrame


def _truthy(value: object) -> bool:
    return value is True or str(value).strip().casefold() in {
        "true",
        "1",
        "yes",
    }


def _matched_blocks(value: object) -> set[str]:
    return {
        part.strip()
        for part in str(value or "").split("|")
        if part.strip()
    }


def _candidate_role(source_stage: object) -> str:
    return {
        "raw": "RAW_SOURCE_CANDIDATE",
        "processed": "DERIVED_PROCESSED_PRODUCT",
        "warehouse": "ANALYTICAL_CONTAINER",
        "exports": "DERIVED_EXPORT_PRODUCT",
    }.get(str(source_stage).strip().casefold(), "OTHER_CANDIDATE")


def _review_basis(method: object) -> str:
    normalized = str(method or "").strip()
    if normalized == "EXPLICIT_FILE_CONTENT_REVIEW":
        return "CONTENT_REVIEWED_CLASSIFICATION"
    if normalized in {
        "EXPLICIT_CALIBRATION_RULE",
        "EXPLICIT_PATH_OVERRIDE",
        "EXPLICIT_CONTENT_FAMILY_REVIEW",
    }:
        return "EXPLICIT_RULE_CLASSIFICATION"
    return "METADATA_OR_KEYWORD_CLASSIFICATION"


def select_demography_candidates(
    coverage_files: pd.DataFrame,
    *,
    include_secondary: bool = True,
) -> pd.DataFrame:
    """Seleciona candidatos demográficos sem equiparar relações secundárias."""
    missing = COVERAGE_REQUIRED_COLUMNS.difference(coverage_files.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no mapa de cobertura: "
            f"{sorted(missing)}"
        )

    frame = coverage_files.copy()
    eligible = frame["analytical_candidate"].map(_truthy)
    primary = frame["primary_block"].eq(DEMOGRAPHY_BLOCK)
    secondary = frame["matched_blocks"].map(
        lambda value: DEMOGRAPHY_BLOCK in _matched_blocks(value)
    ) & ~primary
    selected = frame.loc[eligible & (primary | (secondary if include_secondary else False))].copy()
    selected["demography_relation"] = "PRIMARY"
    selected.loc[~selected["primary_block"].eq(DEMOGRAPHY_BLOCK), "demography_relation"] = (
        "SECONDARY"
    )
    selected["candidate_role"] = selected["source_stage"].map(_candidate_role)
    selected["classification_review_basis"] = selected["classification_method"].map(
        _review_basis
    )
    selected["demography_priority"] = selected["demography_relation"].map(
        {"PRIMARY": 1, "SECONDARY": 2}
    )
    selected["nature"] = "observed_and_calculated"
    return selected.sort_values(
        ["demography_priority", "source_stage", "relative_path"]
    ).reset_index(drop=True)


def attach_file_profiles(
    candidates: pd.DataFrame,
    file_profiles: pd.DataFrame | None,
) -> pd.DataFrame:
    """Anexa o perfil estrutural existente sem reler ou alterar os arquivos."""
    profile_columns = [
        "relative_path",
        "read_status",
        "error_type",
        "error_message",
        "tables_observed",
        "rows_observed",
    ]
    if file_profiles is None or file_profiles.empty:
        result = candidates.copy()
        result["local_profile_available"] = False
        result["read_status"] = "PROFILE_NOT_AVAILABLE"
        result["error_type"] = ""
        result["error_message"] = ""
        result["tables_observed"] = 0
        result["rows_observed"] = 0
        result["structural_status"] = "PROFILE_NOT_AVAILABLE"
        return result

    missing = FILE_PROFILE_REQUIRED_COLUMNS.difference(file_profiles.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no perfil de arquivos derivados: "
            f"{sorted(missing)}"
        )
    profiles = file_profiles.copy()
    for column in ("error_type", "error_message"):
        if column not in profiles.columns:
            profiles[column] = ""
    profiles = profiles[profile_columns].drop_duplicates("relative_path", keep="last")
    result = candidates.merge(profiles, on="relative_path", how="left")
    result["local_profile_available"] = result["read_status"].notna()
    result["read_status"] = result["read_status"].fillna("PROFILE_NOT_AVAILABLE")
    result["error_type"] = result["error_type"].fillna("")
    result["error_message"] = result["error_message"].fillna("")
    result["tables_observed"] = pd.to_numeric(
        result["tables_observed"], errors="coerce"
    ).fillna(0).astype(int)
    result["rows_observed"] = pd.to_numeric(
        result["rows_observed"], errors="coerce"
    ).fillna(0).astype(int)
    result["structural_status"] = result["read_status"].map(
        {
            "OK": "STRUCTURAL_PROFILE_OK",
            "EMPTY": "STRUCTURAL_PROFILE_EMPTY",
            "ERROR": "STRUCTURAL_PROFILE_ERROR",
            "UNSUPPORTED": "STRUCTURAL_PROFILE_UNSUPPORTED",
            "AUXILIARY": "STRUCTURAL_PROFILE_AUXILIARY",
            "PROFILE_NOT_AVAILABLE": "PROFILE_NOT_AVAILABLE",
        }
    ).fillna("STRUCTURAL_PROFILE_REVIEW_REQUIRED")
    return result


def select_demography_tables(
    candidates: pd.DataFrame,
    table_profiles: pd.DataFrame | None,
) -> pd.DataFrame:
    """Seleciona tabelas dos candidatos e preserva sinais como estimativas."""
    output_columns = [
        "relative_path",
        "demography_relation",
        "source_stage",
        "source_family",
        "table_name",
        "source_format",
        "rows_observed",
        "columns_observed",
        "headers",
        "geography_signal_estimate",
        "time_signal_estimate",
        "measure_signal_estimate",
        "category_signal_estimate",
        "utility_estimate",
        "structural_signal_status",
        "nature",
    ]
    if table_profiles is None or table_profiles.empty:
        return pd.DataFrame(columns=output_columns)
    missing = TABLE_PROFILE_REQUIRED_COLUMNS.difference(table_profiles.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no perfil de tabelas derivadas: "
            f"{sorted(missing)}"
        )

    keys = candidates[
        ["relative_path", "demography_relation", "source_stage", "source_family"]
    ].drop_duplicates()
    tables = table_profiles.merge(keys, on="relative_path", how="inner")
    signals = [
        "geography_signal_estimate",
        "time_signal_estimate",
        "measure_signal_estimate",
    ]
    for column in signals + ["category_signal_estimate"]:
        tables[column] = tables[column].map(_truthy)
    complete = tables[signals].all(axis=1)
    partial = tables[signals].any(axis=1) & ~complete
    tables["structural_signal_status"] = "NO_CORE_SIGNAL_DETECTED"
    tables.loc[partial, "structural_signal_status"] = "PARTIAL_CORE_SIGNALS"
    tables.loc[complete, "structural_signal_status"] = "CORE_SIGNALS_PRESENT"
    tables["nature"] = "observed_and_estimated"
    return tables[output_columns].sort_values(
        ["demography_relation", "source_stage", "relative_path", "table_name"]
    ).reset_index(drop=True)


def build_family_summary(candidates: pd.DataFrame) -> pd.DataFrame:
    """Resume a disponibilidade estrutural por família e relação temática."""
    columns = [
        "demography_relation",
        "source_stage",
        "source_family",
        "candidate_files",
        "known_bytes",
        "profiled_files",
        "profile_error_files",
        "tables_observed",
        "rows_observed",
        "candidate_roles",
        "nature",
    ]
    if candidates.empty:
        return pd.DataFrame(columns=columns)
    records: list[dict[str, object]] = []
    group_columns = ["demography_relation", "source_stage", "source_family"]
    for key, group in candidates.groupby(group_columns, dropna=False, sort=True):
        relation, stage, family = key
        records.append(
            {
                "demography_relation": relation,
                "source_stage": stage,
                "source_family": family,
                "candidate_files": len(group),
                "known_bytes": int(
                    pd.to_numeric(group["size_bytes"], errors="coerce").fillna(0).sum()
                ),
                "profiled_files": int(group["local_profile_available"].sum()),
                "profile_error_files": int(group["read_status"].eq("ERROR").sum()),
                "tables_observed": int(group["tables_observed"].sum()),
                "rows_observed": int(group["rows_observed"].sum()),
                "candidate_roles": "|".join(sorted(set(group["candidate_role"]))),
                "nature": "calculated",
            }
        )
    return pd.DataFrame(records, columns=columns)


def _next_action(row: object) -> str:
    read_status = str(getattr(row, "read_status", ""))
    stage = str(getattr(row, "source_stage", ""))
    relation = str(getattr(row, "demography_relation", ""))
    if read_status == "ERROR":
        return "RESOLVE_STRUCTURAL_READ_ERROR"
    if read_status == "PROFILE_NOT_AVAILABLE":
        return "LOCATE_OR_SNAPSHOT_CANDIDATE"
    if relation == "SECONDARY":
        return "REVIEW_AS_CONTEXT_ONLY"
    if stage == "raw":
        return "DOCUMENT_SOURCE_PERIOD_UNIT_AND_GEOGRAPHY"
    return "TRACE_LINEAGE_AND_COMPARE_WITH_PRIMARY_SOURCE"


def build_decision_register(candidates: pd.DataFrame) -> pd.DataFrame:
    """Explicita o que ainda falta antes de construir a camada curada."""
    records: list[dict[str, object]] = []
    for row in candidates.itertuples(index=False):
        relation = str(row.demography_relation)
        records.append(
            {
                "relative_path": row.relative_path,
                "demography_relation": relation,
                "candidate_role": row.candidate_role,
                "structural_status": row.structural_status,
                "source_reference_status": "PENDING_CONTENT_REVIEW",
                "period_reference_status": "PENDING_CONTENT_REVIEW",
                "unit_status": "PENDING_CONTENT_REVIEW",
                "geographic_scope_status": "PENDING_CONTENT_REVIEW",
                "comparability_status": "NOT_ASSESSED",
                "curated_reuse_status": (
                    "CONTEXT_ONLY_UNTIL_CONFIRMED"
                    if relation == "SECONDARY"
                    else "PENDING_LINEAGE_AND_CONTENT_REVIEW"
                ),
                "next_action": _next_action(row),
                "what_cannot_be_concluded": (
                    "A presença do arquivo não comprova fonte original, período, "
                    "unidade, abrangência ou comparabilidade."
                ),
                "nature": "diagnostic_recommendation",
            }
        )
    return pd.DataFrame(records)


def build_summary(
    candidates: pd.DataFrame,
    tables: pd.DataFrame,
    families: pd.DataFrame,
) -> pd.DataFrame:
    """Preserva indicadores observados, calculados e estimados separadamente."""
    stage = candidates["source_stage"].fillna("").astype(str)
    indicators = [
        ("demography_candidates", len(candidates), "calculated"),
        (
            "primary_candidates",
            int(candidates["demography_relation"].eq("PRIMARY").sum()),
            "calculated",
        ),
        (
            "secondary_candidates",
            int(candidates["demography_relation"].eq("SECONDARY").sum()),
            "calculated",
        ),
        ("raw_candidates", int(stage.eq("raw").sum()), "calculated"),
        ("processed_candidates", int(stage.eq("processed").sum()), "calculated"),
        ("warehouse_candidates", int(stage.eq("warehouse").sum()), "calculated"),
        ("export_candidates", int(stage.eq("exports").sum()), "calculated"),
        (
            "profiled_candidates",
            int(candidates["local_profile_available"].sum()),
            "calculated",
        ),
        (
            "profile_error_candidates",
            int(candidates["read_status"].eq("ERROR").sum()),
            "calculated",
        ),
        ("tables_observed", len(tables), "observed"),
        (
            "rows_observed",
            int(pd.to_numeric(tables["rows_observed"], errors="coerce").fillna(0).sum())
            if not tables.empty
            else 0,
            "observed",
        ),
        (
            "tables_with_core_signals",
            int(tables["structural_signal_status"].eq("CORE_SIGNALS_PRESENT").sum())
            if not tables.empty
            else 0,
            "estimated",
        ),
        ("source_families", len(families), "calculated"),
        (
            "conceptually_validated_candidates",
            0,
            "observed",
        ),
    ]
    return pd.DataFrame(indicators, columns=["indicator", "value", "nature"])


def audit_demography_candidates(
    coverage_files: pd.DataFrame,
    *,
    file_profiles: pd.DataFrame | None = None,
    table_profiles: pd.DataFrame | None = None,
    include_secondary: bool = True,
) -> DemographyAuditResult:
    """Audita a disponibilidade antes de escolher séries demográficas."""
    selected = select_demography_candidates(
        coverage_files,
        include_secondary=include_secondary,
    )
    candidates = attach_file_profiles(selected, file_profiles)
    tables = select_demography_tables(candidates, table_profiles)
    families = build_family_summary(candidates)
    decisions = build_decision_register(candidates)
    summary = build_summary(candidates, tables, families)
    return DemographyAuditResult(
        candidates=candidates,
        tables=tables,
        families=families,
        decisions=decisions,
        summary=summary,
    )


def write_demography_audit(
    result: DemographyAuditResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica relatórios locais de modo atômico."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino da auditoria já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    outputs = {
        "demography_candidate_inventory.csv": result.candidates,
        "demography_table_profile.csv": result.tables,
        "demography_family_summary.csv": result.families,
        "demography_decision_register.csv": result.decisions,
        "demography_audit_summary.csv": result.summary,
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
