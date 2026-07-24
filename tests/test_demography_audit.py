from pathlib import Path

import pandas as pd
import pytest

from sbmi.demography_audit import (
    attach_file_profiles,
    audit_demography_candidates,
    select_demography_candidates,
    write_demography_audit,
)


def _coverage() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": "exports/census_population.csv",
                "file_name": "census_population.csv",
                "extension": "csv",
                "size_bytes": 100,
                "source_stage": "exports",
                "source_family": "exports/census_population.csv",
                "primary_block": "demografia",
                "matched_blocks": "demografia",
                "classification_method": "EXPLICIT_CALIBRATION_RULE",
                "classification_basis": "CALIBRATION_EXPORT_CENSUS",
                "classification_confidence": "HIGH",
                "analytical_candidate": True,
            },
            {
                "relative_path": "raw/pdfs/relatorio_multitematico.pdf",
                "file_name": "relatorio_multitematico.pdf",
                "extension": "pdf",
                "size_bytes": 200,
                "source_stage": "raw",
                "source_family": "raw/pdfs",
                "primary_block": "transversal_multitematico",
                "matched_blocks": "transversal_multitematico|demografia|educacao",
                "classification_method": "EXPLICIT_FILE_CONTENT_REVIEW",
                "classification_basis": "REVIEWED_REPORT",
                "classification_confidence": "HIGH",
                "analytical_candidate": True,
            },
            {
                "relative_path": "exports/economic_factsheet.csv",
                "file_name": "economic_factsheet.csv",
                "extension": "csv",
                "size_bytes": 300,
                "source_stage": "exports",
                "source_family": "exports/economic_factsheet.csv",
                "primary_block": "economia_estrutura_produtiva",
                "matched_blocks": "economia_estrutura_produtiva",
                "classification_method": "EXPLICIT_CALIBRATION_RULE",
                "classification_basis": "CALIBRATION_ECONOMIC",
                "classification_confidence": "HIGH",
                "analytical_candidate": True,
            },
        ]
    )


def _file_profiles() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": "exports/census_population.csv",
                "read_status": "OK",
                "error_type": "",
                "error_message": "",
                "tables_observed": 1,
                "rows_observed": 10,
            }
        ]
    )


def _table_profiles() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": "exports/census_population.csv",
                "table_name": "census_population",
                "source_format": "csv",
                "rows_observed": 10,
                "columns_observed": 4,
                "headers": "municipio|ano|populacao|sexo",
                "geography_signal_estimate": True,
                "time_signal_estimate": True,
                "measure_signal_estimate": True,
                "category_signal_estimate": True,
                "utility_estimate": "ANALYTICAL_SIGNAL_PRESENT",
            }
        ]
    )


def test_select_demography_candidates_preserves_primary_and_secondary() -> None:
    selected = select_demography_candidates(_coverage())

    assert len(selected) == 2
    assert selected["demography_relation"].tolist() == ["PRIMARY", "SECONDARY"]
    assert selected.iloc[0]["candidate_role"] == "DERIVED_EXPORT_PRODUCT"
    assert selected.iloc[1]["candidate_role"] == "RAW_SOURCE_CANDIDATE"


def test_primary_only_excludes_contextual_sources() -> None:
    selected = select_demography_candidates(
        _coverage(),
        include_secondary=False,
    )

    assert len(selected) == 1
    assert selected.iloc[0]["relative_path"] == "exports/census_population.csv"


def test_attach_profiles_keeps_missing_profile_explicit() -> None:
    candidates = select_demography_candidates(_coverage())
    profiled = attach_file_profiles(candidates, _file_profiles()).set_index(
        "relative_path"
    )

    assert bool(
        profiled.loc[
            "exports/census_population.csv",
            "local_profile_available",
        ]
    )
    assert (
        profiled.loc[
            "raw/pdfs/relatorio_multitematico.pdf",
            "read_status",
        ]
        == "PROFILE_NOT_AVAILABLE"
    )


def test_audit_does_not_claim_conceptual_validation() -> None:
    result = audit_demography_candidates(
        _coverage(),
        file_profiles=_file_profiles(),
        table_profiles=_table_profiles(),
    )
    summary = result.summary.set_index("indicator")
    decisions = result.decisions.set_index("relative_path")

    assert int(summary.loc["demography_candidates", "value"]) == 2
    assert int(summary.loc["tables_with_core_signals", "value"]) == 1
    assert int(summary.loc["conceptually_validated_candidates", "value"]) == 0
    assert (
        decisions.loc[
            "exports/census_population.csv",
            "next_action",
        ]
        == "TRACE_LINEAGE_AND_COMPARE_WITH_PRIMARY_SOURCE"
    )
    assert (
        decisions.loc[
            "raw/pdfs/relatorio_multitematico.pdf",
            "curated_reuse_status",
        ]
        == "CONTEXT_ONLY_UNTIL_CONFIRMED"
    )


def test_write_demography_audit_is_atomic_and_refuses_overwrite(
    tmp_path: Path,
) -> None:
    result = audit_demography_candidates(
        _coverage(),
        file_profiles=_file_profiles(),
        table_profiles=_table_profiles(),
    )
    target = tmp_path / "demography"

    written = write_demography_audit(result, target)

    assert written == target.resolve()
    assert (target / "demography_candidate_inventory.csv").is_file()
    assert (target / "demography_table_profile.csv").is_file()
    assert (target / "demography_family_summary.csv").is_file()
    assert (target / "demography_decision_register.csv").is_file()
    assert (target / "demography_audit_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_demography_audit(result, target)
