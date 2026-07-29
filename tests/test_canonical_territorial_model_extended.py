from pathlib import Path

import pandas as pd
import pytest

from sbmi.canonical_territorial_model_extended import _sidra


def _input(tmp_path: Path) -> Path:
    root = tmp_path / "sidra"
    root.mkdir()
    pd.DataFrame([
        {
            "table_id": "3939", "municipality_code": "4318002",
            "reference_year": 1996, "variable_id": "105",
            "variable_name": "Efetivo dos rebanhos", "category_id": "2670",
            "category_name": "Bovinos", "unit_code": "24", "unit_name": "Cabeças",
            "raw_value": "10", "numeric_value": 10.0,
            "value_status": "OBSERVED_NUMERIC",
        },
        {
            "table_id": "3939", "municipality_code": "4318002",
            "reference_year": 1997, "variable_id": "105",
            "variable_name": "Efetivo dos rebanhos", "category_id": "2670",
            "category_name": "Bovinos", "unit_code": "24", "unit_name": "Cabeças",
            "raw_value": "-", "numeric_value": None,
            "value_status": "MISSING_OR_SUPPRESSED",
        },
    ]).to_csv(root / "sidra_historical_values.csv", index=False)
    return root


def test_sidra_maps_numeric_rows_and_preserves_exclusion_count(tmp_path):
    rows, paths, excluded = _sidra(_input(tmp_path))
    assert len(rows) == 1
    assert excluded == 1
    assert len(paths) == 1
    assert rows[0]["indicator_id"] == "economy.sidra.t3939.v105.u24"
    assert rows[0]["category_id"] == "c2670"
    assert rows[0]["theme"] == "economy"


def test_sidra_rejects_wrong_geography(tmp_path):
    root = _input(tmp_path)
    path = root / "sidra_historical_values.csv"
    frame = pd.read_csv(path)
    frame["municipality_code"] = 0
    frame.to_csv(path, index=False)
    with pytest.raises(ValueError, match="Geografia SIDRA"):
        _sidra(root)
