from pathlib import Path

import pandas as pd

from sbmi.inventory import build_inventory, duplicate_candidates, sha256_file


def test_sha256_and_exact_duplicate_detection(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "nested" / "b.txt"
    second.parent.mkdir()

    first.write_text("São Borja", encoding="utf-8")
    second.write_text("São Borja", encoding="utf-8")

    assert sha256_file(first) == sha256_file(second)

    inventory = build_inventory(tmp_path)
    duplicates = duplicate_candidates(inventory)

    assert len(inventory) == 2
    assert len(duplicates) == 2
    assert set(duplicates["duplicate_class"]) == {"EXACT_DUPLICATE"}


def test_inventory_empty_directory_has_stable_schema(tmp_path: Path) -> None:
    inventory = build_inventory(tmp_path)

    assert inventory.empty
    assert inventory.columns.tolist() == [
        "relative_path",
        "file_name",
        "extension",
        "size_bytes",
        "modified_at_utc",
        "sha256",
        "audit_status",
    ]


def test_duplicate_candidates_requires_expected_columns() -> None:
    invalid = pd.DataFrame({"file_name": ["a.csv"]})

    try:
        duplicate_candidates(invalid)
    except ValueError as exc:
        assert "Colunas obrigatórias ausentes" in str(exc)
    else:
        raise AssertionError("Era esperado ValueError")
