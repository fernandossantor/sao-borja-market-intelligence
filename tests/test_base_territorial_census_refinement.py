import pandas as pd

from sbmi.base_territorial_census_refinement import refine_census_topic_files


def _files() -> pd.DataFrame:
    rows = [
        {
            "relative_path": (
                "raw/social/Censo 2022 - População por sexo - São Borja (RS).xlsx"
            ),
            "source_stage": "raw",
            "source_family": "raw/social",
            "primary_block": "saude_condicoes_sociais",
            "block_label": "Saúde e condições sociais",
            "matched_blocks": "saude_condicoes_sociais",
            "classification_method": "EXPLICIT_PATH_OVERRIDE",
            "classification_basis": "PATH_OVERRIDE_RAW_SOCIAL",
            "classification_confidence": "HIGH",
            "coverage_eligible": True,
            "analytical_extension": True,
            "analytical_candidate": True,
        },
        {
            "relative_path": (
                "processed/social/Censo 2022 - Alfabetização - "
                "São Borja (RS)_Sheet1.parquet"
            ),
            "source_stage": "processed",
            "source_family": "processed/social",
            "primary_block": "demografia",
            "block_label": "Demografia",
            "matched_blocks": "demografia",
            "classification_method": "KEYWORD_RULE",
            "classification_basis": "demografia:censo",
            "classification_confidence": "MEDIUM",
            "coverage_eligible": True,
            "analytical_extension": True,
            "analytical_candidate": True,
        },
        {
            "relative_path": "exports/census_profile.csv",
            "source_stage": "exports",
            "source_family": "exports/census_profile.csv",
            "primary_block": "demografia",
            "block_label": "Demografia",
            "matched_blocks": "demografia",
            "classification_method": "EXPLICIT_CALIBRATION_RULE",
            "classification_basis": "CALIBRATION_EXPORT_CENSUS",
            "classification_confidence": "HIGH",
            "coverage_eligible": True,
            "analytical_extension": True,
            "analytical_candidate": True,
        },
    ]
    return pd.DataFrame(rows)


def test_raw_census_source_overrides_generic_social_path() -> None:
    refined = refine_census_topic_files(_files()).set_index("relative_path")
    path = "raw/social/Censo 2022 - População por sexo - São Borja (RS).xlsx"

    assert refined.loc[path, "primary_block"] == "demografia"
    assert refined.loc[path, "matched_blocks"] == "demografia"
    assert (
        refined.loc[path, "classification_method"]
        == "EXPLICIT_CENSUS_TOPIC_REVIEW"
    )


def test_adjacent_census_topic_preserves_demography_as_secondary() -> None:
    refined = refine_census_topic_files(_files()).set_index("relative_path")
    path = (
        "processed/social/Censo 2022 - Alfabetização - "
        "São Borja (RS)_Sheet1.parquet"
    )

    assert refined.loc[path, "primary_block"] == "educacao"
    assert refined.loc[path, "matched_blocks"] == "educacao|demografia"


def test_census_profile_is_not_an_independent_analytical_candidate() -> None:
    refined = refine_census_topic_files(_files()).set_index("relative_path")
    row = refined.loc["exports/census_profile.csv"]

    assert row["primary_block"] == "governanca_documentacao"
    assert not bool(row["coverage_eligible"])
    assert not bool(row["analytical_candidate"])
    assert row["classification_basis"] == "CENSUS_PROFILE_IS_TECHNICAL_METADATA"
