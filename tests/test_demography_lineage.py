from pathlib import Path

import pandas as pd
import pytest

from sbmi.demography_lineage import (
    audit_demography_lineage,
    select_lineage_candidates,
    write_demography_lineage,
)


def _coverage() -> pd.DataFrame:
    base = {
        "extension": "xlsx",
        "source_family": "raw/social",
        "primary_block": "saude_condicoes_sociais",
        "matched_blocks": "saude_condicoes_sociais",
        "classification_method": "EXPLICIT_PATH_OVERRIDE",
        "classification_basis": "PATH_OVERRIDE_RAW_SOCIAL",
        "analytical_candidate": True,
    }
    return pd.DataFrame(
        [
            {
                **base,
                "relative_path": (
                    "raw/social/Censo 2022 - Crescimento Populacional - "
                    "São Borja (RS).xlsx"
                ),
                "file_name": (
                    "Censo 2022 - Crescimento Populacional - São Borja (RS).xlsx"
                ),
                "source_stage": "raw",
            },
            {
                **base,
                "relative_path": (
                    "processed/social/Censo 2022 - Crescimento Populacional - "
                    "São Borja (RS)_Sheet1.parquet"
                ),
                "file_name": (
                    "Censo 2022 - Crescimento Populacional - "
                    "São Borja (RS)_Sheet1.parquet"
                ),
                "extension": "parquet",
                "source_stage": "processed",
                "source_family": "processed/social",
                "primary_block": "demografia",
                "matched_blocks": "demografia",
                "classification_method": "KEYWORD_RULE",
                "classification_basis": "demografia:censo",
            },
            {
                **base,
                "relative_path": "exports/census_profile.csv",
                "file_name": "census_profile.csv",
                "extension": "csv",
                "source_stage": "exports",
                "source_family": "exports/census_profile.csv",
                "primary_block": "demografia",
                "matched_blocks": "demografia",
                "classification_method": "EXPLICIT_CALIBRATION_RULE",
                "classification_basis": "CALIBRATION_EXPORT_CENSUS",
            },
            {
                **base,
                "relative_path": "exports/economic_factsheet.csv",
                "file_name": "economic_factsheet.csv",
                "extension": "csv",
                "source_stage": "exports",
                "source_family": "exports/economic_factsheet.csv",
                "primary_block": "economia_estrutura_produtiva",
                "matched_blocks": "economia_estrutura_produtiva",
            },
        ]
    )


def test_selects_raw_processed_and_technical_profile() -> None:
    selected = select_lineage_candidates(_coverage())

    assert len(selected) == 3
    assert set(selected["candidate_kind"]) == {
        "RAW_CENSUS_SOURCE",
        "PROCESSED_CENSUS_PRODUCT",
        "TECHNICAL_CENSUS_PROFILE",
    }


def test_matches_raw_and_processed_by_normalized_identity() -> None:
    result = audit_demography_lineage(_coverage())
    lineage = result.lineage_register.iloc[0]
    summary = result.summary.set_index("indicator")

    assert lineage["lineage_match_status"] == "MATCHED_ONE_TO_ONE_BY_NAME"
    assert lineage["content_equivalence_status"] == "NOT_TESTED"
    assert int(summary.loc["matched_one_to_one_by_name", "value"]) == 1
    assert int(summary.loc["content_equivalence_tests_completed", "value"]) == 0
    assert int(summary.loc["conceptually_validated_datasets", "value"]) == 0


def test_proposes_raw_demography_and_excludes_profile() -> None:
    result = audit_demography_lineage(_coverage())
    corrections = result.classification_corrections.set_index("relative_path")
    raw_path = (
        "raw/social/Censo 2022 - Crescimento Populacional - São Borja (RS).xlsx"
    )

    assert corrections.loc[raw_path, "proposed_primary_block"] == "demografia"
    assert bool(corrections.loc[raw_path, "proposed_analytical_candidate"])
    assert (
        corrections.loc[
            "exports/census_profile.csv",
            "proposed_primary_block",
        ]
        == "governanca_documentacao"
    )
    assert not bool(
        corrections.loc[
            "exports/census_profile.csv",
            "proposed_analytical_candidate",
        ]
    )


def test_unmatched_processed_remains_explicit() -> None:
    coverage = _coverage().loc[
        ~_coverage()["relative_path"].str.startswith("raw/social/")
    ]
    result = audit_demography_lineage(coverage)

    assert result.lineage_register.iloc[0]["lineage_match_status"] == "PROCESSED_ONLY"


def test_write_lineage_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = audit_demography_lineage(_coverage())
    target = tmp_path / "lineage"

    written = write_demography_lineage(result, target)

    assert written == target.resolve()
    assert (target / "demography_lineage_candidates.csv").is_file()
    assert (target / "demography_lineage_register.csv").is_file()
    assert (target / "demography_classification_corrections.csv").is_file()
    assert (target / "demography_lineage_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_demography_lineage(result, target)
