import pandas as pd

from sbmi.drive_audit import (
    exact_duplicate_candidates,
    extension_summary,
    inventory_summary,
    top_level_summary,
)


def sample_inventory() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": "raw",
                "extension": "",
                "is_folder": True,
                "size_bytes": None,
                "sha256_checksum": None,
            },
            {
                "relative_path": "raw/a.csv",
                "extension": "csv",
                "is_folder": False,
                "size_bytes": 10,
                "sha256_checksum": "same",
            },
            {
                "relative_path": "raw/nested/b.csv",
                "extension": ".CSV",
                "is_folder": False,
                "size_bytes": 10,
                "sha256_checksum": "same",
            },
            {
                "relative_path": "exports/c.xlsx",
                "extension": "xlsx",
                "is_folder": False,
                "size_bytes": 25,
                "sha256_checksum": "unique",
            },
            {
                "relative_path": "exports/google-sheet",
                "extension": "",
                "is_folder": False,
                "size_bytes": None,
                "sha256_checksum": None,
            },
        ]
    )


def test_inventory_summary_distinguishes_observed_and_calculated_metrics() -> None:
    summary = inventory_summary(sample_inventory()).set_index("indicator")

    assert summary.loc["entries", "value"] == 5
    assert summary.loc["folders", "value"] == 1
    assert summary.loc["files", "value"] == 4
    assert summary.loc["known_bytes", "value"] == 45
    assert summary.loc["files_without_sha256", "value"] == 1
    assert summary.loc["exact_duplicate_groups", "value"] == 1
    assert summary.loc["exact_duplicate_rows", "value"] == 2
    assert summary.loc["entries", "measurement_type"] == "observed"
    assert summary.loc["exact_duplicate_groups", "measurement_type"] == "calculated"


def test_exact_duplicate_candidates_group_by_sha256() -> None:
    duplicates = exact_duplicate_candidates(sample_inventory())

    assert len(duplicates) == 2
    assert set(duplicates["relative_path"]) == {"raw/a.csv", "raw/nested/b.csv"}
    assert set(duplicates["group_size"]) == {2}
    assert set(duplicates["duplicate_class"]) == {"EXACT_DUPLICATE"}


def test_top_level_and_extension_summaries() -> None:
    top_level = top_level_summary(sample_inventory()).set_index("top_level")
    extensions = extension_summary(sample_inventory()).set_index("extension_group")

    assert top_level.loc["raw", "entries"] == 3
    assert top_level.loc["raw", "files"] == 2
    assert top_level.loc["exports", "known_bytes"] == 25
    assert extensions.loc["csv", "files"] == 2
    assert extensions.loc["xlsx", "known_bytes"] == 25
    assert extensions.loc["(sem extensão)", "missing_size"] == 1
