from datetime import date
from decimal import Decimal
from pathlib import Path

import pandas as pd
import pytest

from sbmi.inbox_staging import NUMERIC_HEADERS
from sbmi.inbox_staging_validation import (
    BASE_COLUMNS_BY_DATASET,
    EXPECTED_DATASETS,
    PROVENANCE_COLUMNS,
    validate_staging_directory,
    write_validation_output,
)

SNAPSHOT_ID = "new-files-20260723"


def _source_level(dataset: str) -> str:
    if dataset.startswith("federal_"):
        return "Federal"
    if dataset.startswith("estadual_"):
        return "Estadual"
    return "Municipal"


def _base_value(column: str) -> object:
    if column in {"mes_ano", "data"}:
        return date(2026, 1, 1)
    if column in NUMERIC_HEADERS:
        return Decimal("1.00")
    return "valor"


def _frame(dataset: str, *, rows: int = 1) -> pd.DataFrame:
    source_level = _source_level(dataset)
    source_path = f"raw/new_files/{source_level}/{dataset}.xlsx"
    records = []
    for index in range(rows):
        record = {
            column: _base_value(column)
            for column in BASE_COLUMNS_BY_DATASET[dataset]
        }
        record.update(
            {
                "_source_level": source_level,
                "_source_path": source_path,
                "_source_file": f"{dataset}.xlsx",
                "_source_sheet": "Dados",
                "_source_row": index + 2,
                "_snapshot_id": SNAPSHOT_ID,
                "_reference_year_filename": None,
                "_row_sha256": f"{index + 1:064x}",
                "_duplicate_group_id": None,
                "_duplicate_occurrence_count": 0,
                "_duplicate_class": None,
                "_duplicate_review_status": None,
                "_duplicate_row_hash": None,
            }
        )
        records.append(record)
    columns = [*BASE_COLUMNS_BY_DATASET[dataset], *PROVENANCE_COLUMNS]
    return pd.DataFrame(records, columns=columns)


def _write_staging(root: Path, frames: dict[str, pd.DataFrame]) -> Path:
    staging = root / SNAPSHOT_ID
    staging.mkdir(parents=True)
    manifest_records = []
    published: dict[str, pd.DataFrame] = {}
    for dataset in EXPECTED_DATASETS:
        frame = frames.get(dataset, _frame(dataset))
        published[dataset] = frame
        frame.to_parquet(staging / f"{dataset}.parquet", index=False)
        for source_path, group in frame.groupby("_source_path", dropna=False):
            manifest_records.append(
                {
                    "relative_path": source_path,
                    "source_declared": _source_level(dataset),
                    "dataset": dataset,
                    "input_rows": len(group),
                    "output_rows": len(group),
                    "disposition": "INCLUDED_IN_STAGING",
                    "basis": "EXPLICIT_DATA_CONTRACT",
                }
            )
    manifest = pd.DataFrame(manifest_records)
    manifest.to_csv(staging / "source_manifest.csv", index=False)
    icms = published["estadual_icms"]
    flagged = int(icms["_duplicate_group_id"].notna().sum())
    quality = pd.DataFrame(
        [
            ("source_tables_observed", len(manifest), "observed"),
            ("source_rows_observed", int(manifest["input_rows"].sum()), "observed"),
            ("source_files_excluded_from_staging", 0, "calculated"),
            ("source_rows_excluded_from_staging", 0, "calculated"),
            ("staging_datasets", len(published), "observed"),
            (
                "staging_rows",
                sum(len(frame) for frame in published.values()),
                "calculated",
            ),
            ("federal_source_files_included", 1, "calculated"),
            (
                "federal_rows",
                len(published["federal_transferencias"]),
                "calculated",
            ),
            ("icms_rows_retained", len(icms), "calculated"),
            ("icms_duplicate_rows_flagged", flagged, "calculated"),
        ],
        columns=["indicator", "value", "nature"],
    )
    quality.to_csv(staging / "staging_quality_summary.csv", index=False)
    return staging


def _indicator(result: object, name: str) -> int:
    summary = result.validation_summary.set_index("indicator")
    return int(summary.loc[name, "value"])


def test_validate_staging_reconciles_valid_contracts(tmp_path: Path) -> None:
    staging = _write_staging(tmp_path, {})
    result = validate_staging_directory(staging)

    assert _indicator(result, "datasets_loaded") == 6
    assert _indicator(result, "rows_validated") == 6
    assert _indicator(result, "row_reconciliation_failures") == 0
    assert _indicator(result, "quality_indicator_failures") == 0
    assert _indicator(result, "validation_errors") == 0
    assert set(result.dataset_summary["status"]) == {"OK"}


def test_validate_staging_detects_contract_and_provenance_failures(tmp_path: Path) -> None:
    federal = _frame("federal_transferencias")
    federal = federal.drop(columns=["valor_transferido"])
    federal.loc[0, "mes_ano"] = date(2027, 1, 1)
    federal.loc[0, "_source_file"] = "arquivo-incorreto.xlsx"
    federal.loc[0, "_row_sha256"] = "invalido"
    staging = _write_staging(tmp_path, {"federal_transferencias": federal})

    result = validate_staging_directory(staging)
    classes = set(result.validation_issues["issue_class"])

    assert "MISSING_REQUIRED_COLUMNS" in classes
    assert "FUTURE_DATE_VALUE" in classes
    assert "SOURCE_FILE_PATH_MISMATCH" in classes
    assert "INVALID_ROW_SHA256" in classes
    assert _indicator(result, "validation_errors") >= 4


def test_validate_staging_counts_consistent_duplicate_groups(tmp_path: Path) -> None:
    icms = _frame("estadual_icms", rows=3)
    icms["_duplicate_group_id"] = "duplicate-group-0001"
    icms["_duplicate_occurrence_count"] = 3
    icms["_duplicate_class"] = "STRICT_EXACT_ROW"
    icms["_duplicate_review_status"] = "PENDING_SOURCE_VALIDATION"
    icms["_duplicate_row_hash"] = "b" * 64
    staging = _write_staging(tmp_path, {"estadual_icms": icms})

    result = validate_staging_directory(staging)

    assert _indicator(result, "duplicate_flagged_rows") == 3
    assert _indicator(result, "duplicate_groups") == 1
    assert _indicator(result, "duplicate_excess") == 2
    assert _indicator(result, "duplicate_flag_inconsistencies") == 0
    assert _indicator(result, "quality_indicator_failures") == 0


def test_write_validation_output_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    staging = _write_staging(tmp_path / "input", {})
    result = validate_staging_directory(staging)
    target = tmp_path / "validation"

    written = write_validation_output(result, target)

    assert written == target.resolve()
    assert (target / "dataset_validation_summary.csv").is_file()
    assert (target / "manifest_reconciliation.csv").is_file()
    assert (target / "quality_reconciliation.csv").is_file()
    assert (target / "validation_issues.csv").is_file()
    assert (target / "staging_validation_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_validation_output(result, target)
