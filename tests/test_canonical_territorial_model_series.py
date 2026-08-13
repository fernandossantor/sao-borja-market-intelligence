import warnings
from pathlib import Path

import pandas as pd
import pytest

from sbmi.canonical_territorial_model import KEY_COLUMNS, _row
from sbmi.canonical_territorial_model_series import build_series_canonical_model


def _write_inputs(root: Path) -> tuple[Path, dict[str, Path]]:
    base = root / "base"
    base.mkdir()
    pd.DataFrame([
        _row(indicator_id="base.value", indicator_name="Base", year=2022,
             theme="base", subtheme="base", value=1, value_text="1", unit="unit",
             dataset="base", source=root / "source", source_hash="a" * 64)
    ]).to_parquet(base / "fact_territorial_indicator.parquet", index=False)
    common = {"municipality_code": "4318002", "reference_year": 2020,
              "numeric_value": 1.0, "nature": "observed"}
    frames = {
        "demography_historical": [{**common, "table_id": "156", "variable_id": "134",
            "variable_name": "Pessoas", "unit_code": "45", "unit_name": "Pessoas",
            "raw_value": "1", "value_status": "OBSERVED_NUMERIC"}],
        "demography_census": [{**common, "table_id": "200", "variable_id": "93",
            "variable_name": "População", "unit_code": "45", "unit_name": "Pessoas",
            "raw_value": "1", "value_status": "OBSERVED_NUMERIC", "category_key": "Sexo=Total",
            "category_dimensions_json": "[]", "comparability_note": "amostra"},
            {**common, "table_id": "200", "variable_id": "93", "variable_name": "População",
            "unit_code": "45", "unit_name": "Pessoas", "raw_value": "...",
            "numeric_value": None, "value_status": "MISSING_OR_SUPPRESSED",
            "category_key": "Sexo=Homens", "category_dimensions_json": "[1]",
            "comparability_note": "amostra"}],
        "economy_gdp": [{**common, "indicator_id": "gdp", "indicator_name": "PIB",
            "variable_id": "37", "unit": "Mil Reais", "raw_value": "1",
            "value_status": "OBSERVED_NUMERIC", "value_kind": "absolute",
            "methodology_series": "current"}],
        "business_employment": [{**common, "indicator_id": "jobs",
            "indicator_name": "Vínculos", "unit": "Vínculos"}],
        "education": [{**common, "indicator_id": "ideb", "indicator_name": "IDEB",
            "category": "Anos iniciais", "unit": "índice", "source_id": "ideb"}],
        "public_finance": [{**common, "indicator_id": "revenue", "indicator_name": "Receita",
            "account_code": "", "unit": "R$ correntes", "source_id": "revenue",
            "accounting_stage": "não comprovado", "limitation": "limite"}],
        "siconfi_dca": [{**common, "dimension": "expense", "account_code": "DO3",
            "indicator_name": "Despesa", "measure": "Despesas Pagas", "unit": "R$ correntes"}],
    }
    paths = {}
    for family, rows in frames.items():
        path = root / f"{family}.csv"
        pd.DataFrame(rows).to_csv(path, index=False)
        paths[family] = path
    return base, paths


def test_builds_parallel_series_model_and_records_exclusions(tmp_path: Path):
    base, paths = _write_inputs(tmp_path)
    with warnings.catch_warnings():
        warnings.simplefilter("error", FutureWarning)
        result = build_series_canonical_model(base_root=base, series_paths=paths,
            output_root=tmp_path / "output", run_id="run")
    assert len(result.facts) == 8
    assert not result.facts.duplicated(KEY_COLUMNS).any()
    decisions = result.reconciliation.set_index("dataset")
    assert decisions.loc["demography_census", "rows_excluded"] == 1
    assert decisions.loc["canonical_extended_previous", "decision"] == "PRESERVE"
    assert set(result.facts["source_dataset"]) >= {
        "base", "demography_census_sidra", "siconfi_dca_official_series"
    }
    local_finance = result.facts.loc[
        result.facts["source_dataset"].eq("public_finance_local_series")
    ].iloc[0]
    assert local_finance["category_id"] == "revenue"
    assert local_finance["category_name"] == "revenue"
    assert (result.output_path / "canonical_manifest.csv").is_file()


def test_preserves_missing_text_and_categories_without_nan(tmp_path: Path):
    base, paths = _write_inputs(tmp_path)
    economy = pd.read_csv(paths["economy_gdp"])
    economy["raw_value"] = None
    economy.to_csv(paths["economy_gdp"], index=False)
    education = pd.read_csv(paths["education"])
    education["category"] = None
    education.to_csv(paths["education"], index=False)

    result = build_series_canonical_model(
        base_root=base,
        series_paths=paths,
        output_root=tmp_path / "output",
        run_id="run",
    )
    gdp = result.facts.loc[result.facts.source_dataset.eq("economy_gdp_series")].iloc[0]
    assert gdp.value_text == "1.0"
    education_row = result.facts.loc[
        result.facts.source_dataset.eq("education_series")
    ].iloc[0]
    assert education_row.category_name == ""
    assert education_row.category_id == ""


def test_refuses_overwrite_and_removes_partial_on_error(tmp_path: Path):
    base, paths = _write_inputs(tmp_path)
    build_series_canonical_model(base_root=base, series_paths=paths,
        output_root=tmp_path / "output", run_id="run")
    with pytest.raises(FileExistsError):
        build_series_canonical_model(base_root=base, series_paths=paths,
            output_root=tmp_path / "output", run_id="run")
    paths["education"] = tmp_path / "missing.csv"
    with pytest.raises(FileNotFoundError):
        build_series_canonical_model(base_root=base, series_paths=paths,
            output_root=tmp_path / "output", run_id="failed")
    assert not (tmp_path / "output" / ".failed.partial").exists()


def test_rejects_wrong_geography(tmp_path: Path):
    base, paths = _write_inputs(tmp_path)
    frame = pd.read_csv(paths["education"])
    frame["municipality_code"] = "0"
    frame.to_csv(paths["education"], index=False)
    with pytest.raises(ValueError, match="Geografia divergente"):
        build_series_canonical_model(base_root=base, series_paths=paths,
            output_root=tmp_path / "output", run_id="run")
