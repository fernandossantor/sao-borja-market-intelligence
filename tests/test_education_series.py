import json
from pathlib import Path

import pytest

from sbmi.education_series import curate_education_series


def fixture(tmp_path: Path):
    annotation = {"source_name": "INEP"}
    data = {
        "ideb": [
            {
                "Education Level ID": level,
                "Education Level": str(level),
                "Year": year,
                "IDEB Index": 4,
            }
            for level in (1, 2)
            for year in range(2005, 2025, 2)
        ],
        "rates": [
            {
                "Education Level ID": level,
                "Education Level": str(level),
                "Year": year,
                "Age-Grade Distortion Rate": 2,
                "Dropout Rate": 1,
            }
            for level in (0, 3)
            for year in range(2018, 2025)
        ],
        "basic_enrollment": [{"Year": year, "Enrollments": 10} for year in range(2018, 2026)],
        "early_enrollment": [{"Year": year, "Enrollments": 2} for year in range(2018, 2026)],
        "higher_education": [
            {
                "Municipality ID": 4318002,
                "Year": 2024,
                "Enrollments": 3,
                "Admissions": 2,
                "Graduates": 1,
            }
        ],
    }
    sources = {}
    for name, rows in data.items():
        path = tmp_path / f"{name}.json"
        path.write_text(json.dumps({"annotations": annotation, "data": rows}))
        sources[name] = path
    roots = {layer: tmp_path / layer for layer in ("staging", "curated", "exports", "audit")}
    return sources, roots


def test_curates_and_refuses_overwrite(tmp_path: Path):
    sources, roots = fixture(tmp_path)
    result = curate_education_series(sources=sources, roots=roots, execution_id="run")
    assert len(result.values) == 67
    assert result.values.indicator_id.nunique() == 11
    with pytest.raises(FileExistsError):
        curate_education_series(sources=sources, roots=roots, execution_id="run")


def test_rejects_wrong_source(tmp_path: Path):
    sources, roots = fixture(tmp_path)
    p = sources["ideb"]
    x = json.loads(p.read_text())
    x["annotations"]["source_name"] = "X"
    p.write_text(json.dumps(x))
    with pytest.raises(ValueError, match="Fonte"):
        curate_education_series(sources=sources, roots=roots, execution_id="run")
