from pathlib import Path

import pandas as pd
import pytest

from sbmi.demography_census_quality_review import (
    review_census_quality,
    write_census_quality_review,
)


def _datasets() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "dataset_identity": "dataset exato",
                "processed_relative_path": "processed/exato.parquet",
                "content_equivalence_status": "EXACT_AFTER_CANONICALIZATION",
            },
            {
                "dataset_identity": "dataset escala",
                "processed_relative_path": "processed/escala.parquet",
                "content_equivalence_status": "CELL_VALUE_MISMATCH",
            },
        ]
    )


def _differences() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "dataset_identity": "dataset escala",
                "column": "percentual",
                "raw_kind": "number",
                "raw_value": "23.18",
                "processed_kind": "number",
                "processed_value": "2318",
            },
            {
                "dataset_identity": "dataset escala",
                "column": "percentual",
                "raw_kind": "number",
                "raw_value": "0.31",
                "processed_kind": "number",
                "processed_value": "31",
            },
        ]
    )


def test_review_confirms_content_but_not_source_authority() -> None:
    result = review_census_quality(_datasets(), _differences())
    register = result.datasets.set_index("dataset_identity")

    exact = register.loc["dataset exato"]
    assert exact["quality_class"] == "NO_CONTENT_ANOMALY_DETECTED"
    assert (
        exact["processed_reuse_status"]
        == "CONTENT_EQUIVALENT_SOURCE_NOT_VALIDATED"
    )
    assert exact["conceptual_validation_status"] == "NOT_VALIDATED"


def test_review_detects_factor_100_decimal_scale_error() -> None:
    result = review_census_quality(_datasets(), _differences())
    anomaly = result.datasets.set_index("dataset_identity").loc["dataset escala"]

    assert anomaly["quality_class"] == "SYSTEMATIC_DECIMAL_SCALE_ERROR"
    assert anomaly["observed_scale_factors"] == "100"
    assert anomaly["processed_reuse_status"] == "QUARANTINE_PROCESSED_PRODUCT"
    assert (
        anomaly["recommended_action"]
        == "REBUILD_FROM_RAW_SOURCE_WITH_DECIMAL_PRESERVATION"
    )


def test_summary_preserves_observed_and_calculated_counts() -> None:
    result = review_census_quality(_datasets(), _differences())
    summary = result.summary.set_index("indicator")

    assert int(summary.loc["datasets_reviewed", "value"]) == 2
    assert int(summary.loc["content_equivalent_datasets", "value"]) == 1
    assert int(summary.loc["datasets_quarantined", "value"]) == 1
    assert int(summary.loc["systematic_decimal_scale_errors", "value"]) == 1
    assert int(summary.loc["affected_cells", "value"]) == 2
    assert int(summary.loc["conceptually_validated_datasets", "value"]) == 0


def test_heterogeneous_mismatch_is_not_silently_corrected() -> None:
    datasets = pd.DataFrame(
        [
            {
                "dataset_identity": "heterogeneo",
                "processed_relative_path": "processed/heterogeneo.parquet",
                "content_equivalence_status": "CELL_VALUE_MISMATCH",
            }
        ]
    )
    differences = pd.DataFrame(
        [
            {
                "dataset_identity": "heterogeneo",
                "column": "categoria",
                "raw_kind": "text",
                "raw_value": "A",
                "processed_kind": "text",
                "processed_value": "B",
            }
        ]
    )

    result = review_census_quality(datasets, differences)
    row = result.datasets.iloc[0]

    assert row["quality_class"] == "HETEROGENEOUS_CONTENT_MISMATCH"
    assert row["processed_reuse_status"] == "QUARANTINE_PROCESSED_PRODUCT"
    assert row["observed_scale_factors"] == ""


def test_write_quality_review_is_atomic_and_refuses_overwrite(
    tmp_path: Path,
) -> None:
    result = review_census_quality(_datasets(), _differences())
    target = tmp_path / "quality"

    written = write_census_quality_review(result, target)

    assert written == target.resolve()
    assert (target / "demography_census_quality_register.csv").is_file()
    assert (target / "demography_census_quarantine_register.csv").is_file()
    assert (target / "demography_census_quality_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_census_quality_review(result, target)
