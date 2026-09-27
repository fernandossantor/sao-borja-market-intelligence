import csv
from pathlib import Path

import pytest

from sbmi.rais_workers_extract import inspect_existing_extract, normalize_code


def test_normalize_code() -> None:
    assert normalize_code("431800.0") == "431800"
    assert normalize_code(" 431800 ") == "431800"
    assert normalize_code('"431800"') == "431800"


def test_inspect_existing_extract_validates_municipality_and_shape(tmp_path: Path) -> None:
    path = tmp_path / "rais.csv"
    header = ["Município - Código", "valor"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerow(["431800", "a"])
        writer.writerow(["431800.0", "b"])

    result = inspect_existing_extract(
        path,
        municipality_column="Município - Código",
        municipality_code="431800",
        expected_columns=2,
        expected_rows=2,
    )
    assert result.rows_selected == 2
    assert result.columns == 2
    assert result.reused_existing is True
    assert len(result.sha256) == 64


def test_inspect_existing_extract_rejects_other_municipality(tmp_path: Path) -> None:
    path = tmp_path / "rais.csv"
    path.write_text(
        'Município - Código,valor\n431800,a\n430000,b\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="município diferente"):
        inspect_existing_extract(
            path,
            municipality_column="Município - Código",
            municipality_code="431800",
            expected_columns=2,
            expected_rows=2,
        )
