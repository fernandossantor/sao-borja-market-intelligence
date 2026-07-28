import pandas as pd

from sbmi.demography_lineage import audit_demography_lineage


def _processed_literacy(primary_block: str, matched_blocks: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": (
                    "processed/social/Censo 2022 - Alfabetização - "
                    "São Borja (RS)_Sheet1.parquet"
                ),
                "file_name": (
                    "Censo 2022 - Alfabetização - "
                    "São Borja (RS)_Sheet1.parquet"
                ),
                "extension": "parquet",
                "source_stage": "processed",
                "source_family": "processed/social",
                "primary_block": primary_block,
                "matched_blocks": matched_blocks,
                "classification_method": "KEYWORD_RULE",
                "classification_basis": "demografia:censo",
                "analytical_candidate": True,
            }
        ]
    )


def test_lineage_proposes_education_for_literacy() -> None:
    result = audit_demography_lineage(
        _processed_literacy("demografia", "demografia")
    )
    correction = result.classification_corrections.iloc[0]

    assert correction["proposed_primary_block"] == "educacao"
    assert correction["proposed_matched_blocks"] == "educacao|demografia"
    assert correction["application_status"] == "PROPOSED_NOT_APPLIED"


def test_lineage_recognizes_topic_review_already_applied() -> None:
    result = audit_demography_lineage(
        _processed_literacy("educacao", "educacao|demografia")
    )
    correction = result.classification_corrections.iloc[0]
    summary = result.summary.set_index("indicator")

    assert correction["application_status"] == "ALREADY_APPLIED"
    assert int(summary.loc["proposed_classification_corrections", "value"]) == 0
    assert int(summary.loc["classification_reviews_already_applied", "value"]) == 1
