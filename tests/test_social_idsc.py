from pathlib import Path

import pandas as pd
import pytest

from sbmi.social_idsc import (
    build_idsc,
    compare_factsheet,
    compare_summary,
    write_idsc_result,
)


def _source_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Município": "São Borja",
                "Pontuação Indice ODS 2025": 46.581251,
                "Classificação 2025": 4118,
                "Valores faltantes": 0,
                "Goal 1 Score": 85.0,
                "Goal 2 Score": 72.0,
                "Goal 3 Score": 60.0,
                "Goal 4 Score": 45.0,
                "Goal 5 Score": 20.0,
            },
            {
                "Município": "Outro Município",
                "Pontuação Indice ODS 2025": 50.0,
                "Classificação 2025": 100,
                "Valores faltantes": 1,
                "Goal 1 Score": 50.0,
                "Goal 2 Score": 50.0,
                "Goal 3 Score": 50.0,
                "Goal 4 Score": 50.0,
                "Goal 5 Score": 50.0,
            },
        ]
    )


def _write_source(path: Path, frame: pd.DataFrame | None = None) -> Path:
    source = frame if frame is not None else _source_frame()
    path.parent.mkdir(parents=True, exist_ok=True)
    source.to_excel(path, sheet_name="Todos os Dados", index=False)
    return path


def test_builds_summary_and_factsheet_with_explicit_nature(tmp_path: Path) -> None:
    result = build_idsc(_write_source(tmp_path / "idsc.xlsx"))

    assert list(result.summary["ods"]) == [
        "ODS 1",
        "ODS 2",
        "ODS 3",
        "ODS 4",
        "ODS 5",
    ]
    assert list(result.summary["classification"]) == [
        "excelente",
        "forte",
        "intermediario",
        "fragil",
        "critico",
    ]
    facts = result.factsheet.set_index("indicator")["value"]
    assert facts["ODS Mais Forte"] == "ODS 1"
    assert facts["ODS Mais Fraco"] == "ODS 5"
    assert facts["ODS Excelentes"] == 1
    assert facts["ODS Fortes"] == 1
    assert facts["ODS Frágeis"] == 1
    assert facts["ODS Críticos"] == 1
    assert result.metadata["classification_nature"] == "calculated_project_heuristic"
    assert result.metadata["source_rows_observed"] == 2


def test_rejects_duplicate_municipality_rows(tmp_path: Path) -> None:
    frame = pd.concat([_source_frame().iloc[[0]], _source_frame().iloc[[0]]])
    source = _write_source(tmp_path / "duplicate.xlsx", frame)
    with pytest.raises(ValueError, match="2 linhas"):
        build_idsc(source)


def test_compares_identical_historical_outputs(tmp_path: Path) -> None:
    first = build_idsc(_write_source(tmp_path / "source.xlsx"))
    baseline = tmp_path / "exports"
    baseline.mkdir()
    first.summary.to_csv(baseline / "social_idsc_summary.csv", index=False)
    first.factsheet.to_csv(baseline / "social_idsc_factsheet.csv", index=False)

    summary_comparison = compare_summary(
        first.summary,
        baseline / "social_idsc_summary.csv",
    )
    factsheet_comparison = compare_factsheet(
        first.factsheet,
        baseline / "social_idsc_factsheet.csv",
    )
    assert summary_comparison["status"] == "IDENTICAL"
    assert factsheet_comparison["status"] == "IDENTICAL"
    assert summary_comparison["mismatched_cells"] == 0
    assert factsheet_comparison["mismatched_cells"] == 0


def test_detects_historical_difference_and_writes_atomically(tmp_path: Path) -> None:
    source = _write_source(tmp_path / "source.xlsx")
    baseline = tmp_path / "exports"
    baseline.mkdir()
    pd.DataFrame(
        [{"ods": "ODS 1", "score": 0, "rank": 1, "classification": "critico"}]
    ).to_csv(baseline / "social_idsc_summary.csv", index=False)
    pd.DataFrame(
        [{"indicator": "Pontuação ODS Geral", "value": 0}]
    ).to_csv(baseline / "social_idsc_factsheet.csv", index=False)

    result = build_idsc(source, historical_exports_dir=baseline)
    assert set(result.comparison["status"]) == {"DIFFERENT"}

    target = write_idsc_result(result, tmp_path / "curated")
    assert (target / "social_idsc_summary.csv").is_file()
    assert (target / "social_idsc_factsheet.csv").is_file()
    assert (target / "historical_comparison.csv").is_file()
    assert (target / "social_idsc_metadata.json").is_file()
    with pytest.raises(FileExistsError):
        write_idsc_result(result, target)
