import pandas as pd

from sbmi.inbox_audit import (
    CLASS_MISSING,
    CLASS_OUTSIDE,
    CLASS_UNIQUE,
    CLASS_WITHIN,
    classify_inbox_files,
    inbox_source_summary,
    inbox_summary,
)


def sample_inventory() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": "raw/new_files/Federal/a.xlsx",
                "is_folder": False,
                "size_bytes": 10,
                "sha256_checksum": "hash-a",
            },
            {
                "relative_path": "raw/fiscal/a.xlsx",
                "is_folder": False,
                "size_bytes": 10,
                "sha256_checksum": "hash-a",
            },
            {
                "relative_path": "raw/new_files/Estadual/b.xlsx",
                "is_folder": False,
                "size_bytes": 20,
                "sha256_checksum": "hash-b",
            },
            {
                "relative_path": "raw/new_files/Estadual/c.xlsx",
                "is_folder": False,
                "size_bytes": 20,
                "sha256_checksum": "hash-b",
            },
            {
                "relative_path": "raw/new_files/Municipal/d.xlsx",
                "is_folder": False,
                "size_bytes": 30,
                "sha256_checksum": "hash-d",
            },
            {
                "relative_path": "raw/new_files/Municipal/e.gsheet",
                "is_folder": False,
                "size_bytes": None,
                "sha256_checksum": None,
            },
            {
                "relative_path": "raw/new_files/Municipal",
                "is_folder": True,
                "size_bytes": None,
                "sha256_checksum": None,
            },
            {
                "relative_path": "raw/new_files_backup/f.xlsx",
                "is_folder": False,
                "size_bytes": 40,
                "sha256_checksum": "hash-f",
            },
        ]
    )


def test_classify_inbox_files_separates_duplicate_scopes() -> None:
    classified = classify_inbox_files(sample_inventory())

    assert len(classified) == 5
    classes = dict(zip(classified["relative_path"], classified["audit_class"], strict=True))
    assert classes["raw/new_files/Federal/a.xlsx"] == CLASS_OUTSIDE
    assert classes["raw/new_files/Estadual/b.xlsx"] == CLASS_WITHIN
    assert classes["raw/new_files/Estadual/c.xlsx"] == CLASS_WITHIN
    assert classes["raw/new_files/Municipal/d.xlsx"] == CLASS_UNIQUE
    assert classes["raw/new_files/Municipal/e.gsheet"] == CLASS_MISSING

    federal = classified.loc[
        classified["relative_path"].eq("raw/new_files/Federal/a.xlsx")
    ].iloc[0]
    assert federal["outside_group_size"] == 1
    assert federal["inbox_source"] == "Federal"


def test_inbox_summary_distinguishes_observed_and_calculated_values() -> None:
    summary = inbox_summary(classify_inbox_files(sample_inventory()))
    values = dict(zip(summary["indicator"], summary["value"], strict=True))

    assert values["inbox_files"] == 5
    assert values["inbox_known_bytes"] == 100
    assert values["inbox_files_without_sha256"] == 1
    assert values["unique_by_sha256_rows"] == 1
    assert values["exact_duplicate_outside_groups"] == 1
    assert values["exact_duplicate_outside_rows"] == 1
    assert values["exact_duplicate_within_groups"] == 1
    assert values["exact_duplicate_within_rows"] == 2


def test_inbox_source_summary_groups_declared_sources() -> None:
    result = inbox_source_summary(classify_inbox_files(sample_inventory()))
    indexed = result.set_index("inbox_source")

    assert set(indexed.index) == {"Federal", "Estadual", "Municipal"}
    assert indexed.loc["Federal", "files"] == 1
    assert indexed.loc["Federal", "exact_duplicate_outside_rows"] == 1
    assert indexed.loc["Estadual", "exact_duplicate_within_rows"] == 2
    assert indexed.loc["Municipal", "unique_by_sha256_rows"] == 1
    assert indexed.loc["Municipal", "missing_sha256_rows"] == 1


def test_classification_accepts_boolean_text_from_csv() -> None:
    inventory = sample_inventory()
    inventory["is_folder"] = inventory["is_folder"].map({True: "True", False: "False"})

    classified = classify_inbox_files(inventory)
    assert len(classified) == 5
