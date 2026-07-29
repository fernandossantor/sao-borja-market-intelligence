from pathlib import Path

import pandas as pd
import pytest

from sbmi.canonical_territorial_model import KEY_COLUMNS, build_canonical_territorial_model


def _inputs(tmp_path: Path) -> tuple[Path, Path, Path]:
    census, idsc, ips = (tmp_path / name for name in ("census", "idsc", "ips"))
    for path in (census, idsc, ips):
        path.mkdir()
    pd.DataFrame({"composicao_domiciliar": ["A", "B", "C"],
                  "porcentagem_de_domicilios": [23.18, 21.31, 0.31],
                  "codigo_do_municipio": [4318002] * 3}).to_parquet(
        census / "household_composition.parquet", index=False)
    pd.DataFrame({"ano_da_pesquisa": [2022], "area_km2": [3616.69],
                  "densidade_demografica_hab_km2": [16.5],
                  "codigo_do_municipio": [4318002]}).to_parquet(
        census / "territory.parquet", index=False)
    pd.DataFrame({"ods": [f"ODS {n}" for n in range(1, 18)],
                  "score": [float(n) for n in range(1, 18)], "rank": range(1, 18),
                  "classification": ["fragil"] * 17}).to_csv(
        idsc / "social_idsc_summary.csv", index=False)
    pd.DataFrame({"indicator": [f"Indicador {n}" for n in range(11)],
                  "value": range(11)}).to_csv(
        idsc / "social_idsc_factsheet.csv", index=False)
    pd.DataFrame({"dataset": ["summary", "factsheet"], "status": ["IDENTICAL"] * 2,
                  "rows_current": [17, 11], "rows_historical": [17, 11],
                  "mismatched_cells": [0, 0]}).to_csv(
        idsc / "historical_comparison.csv", index=False)
    rows = []
    for year in (2024, 2025, 2026):
        for number in range(16):
            rows.append({"reference_year": year,
                         "comparability_status": "NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS",
                         "ibge_code": 4318002, "indicator_label": f"Indicador {number}",
                         "indicator_key": f"indicator_{number}", "indicator_level": "component",
                         "value_text": f"{number},00", "value_numeric": float(number),
                         "unit": "score_0_100", "nature": "observed"})
    ips_frame = pd.DataFrame(rows)
    ips_frame.to_csv(ips / "ips_published_summary_2024_2026.csv", index=False)
    ips_2026 = ips_frame.loc[ips_frame["reference_year"].eq(2026)]
    ips_2026.to_csv(ips / "ips_2026_summary.csv", index=False)
    return census, idsc, ips


def _run(tmp_path: Path, run_id: str = "test-run"):
    census, idsc, ips = _inputs(tmp_path)
    return build_canonical_territorial_model(census_root=census, idsc_root=idsc,
        ips_root=ips, output_root=tmp_path / "canonical", run_id=run_id)


def test_builds_reconciled_canonical_model(tmp_path: Path):
    result = _run(tmp_path)
    assert (len(result.facts), len(result.indicators), len(result.territories)) == (70, 36, 1)
    assert not result.facts.duplicated(KEY_COLUMNS).any()
    assert set(result.facts["reference_year"]) == {2022, 2024, 2025, 2026}
    assert result.facts.groupby("source_dataset")["indicator_id"].nunique().to_dict() == {
        "census_2022_household_composition": 1,
        "census_2022_territory": 2,
        "idsc_br_2025": 17,
        "ips_brasil_published_original": 16,
    }
    manifest = pd.read_csv(result.output_path / "canonical_manifest.csv")
    assert len(manifest.loc[manifest["role"].eq("input")]) == 7
    assert (result.output_path / "canonical_manifest.csv").is_file()


def test_records_exclusions(tmp_path: Path):
    decisions = _run(tmp_path).reconciliation.set_index("dataset")
    assert decisions.loc["ips_2026_summary", "overlap_classification"] == "CONTENT_DUPLICATE"
    assert decisions.loc["ips_2026_summary", "decision"] == "EXCLUDE"
    assert decisions.loc["idsc_factsheet", "overlap_classification"] == "COMPLEMENTARY"


def test_outputs_are_atomic_and_refuse_overwrite(tmp_path: Path):
    result = _run(tmp_path)
    with pytest.raises(FileExistsError):
        build_canonical_territorial_model(census_root=tmp_path / "census",
            idsc_root=tmp_path / "idsc", ips_root=tmp_path / "ips",
            output_root=tmp_path / "canonical", run_id="test-run")
    assert result.output_path.is_dir()
    assert not (tmp_path / "canonical" / ".test-run.partial").exists()


@pytest.mark.parametrize("run_id", ["", ".", "..", "nested/name"])
def test_rejects_unsafe_run_id(tmp_path: Path, run_id: str):
    with pytest.raises(ValueError, match="identificador|nome simples"):
        build_canonical_territorial_model(census_root=tmp_path, idsc_root=tmp_path,
            ips_root=tmp_path, output_root=tmp_path / "canonical", run_id=run_id)


def test_rejects_wrong_ips_geography(tmp_path: Path):
    census, idsc, ips = _inputs(tmp_path)
    path = ips / "ips_published_summary_2024_2026.csv"
    frame = pd.read_csv(path)
    frame["ibge_code"] = 0
    frame.to_csv(path, index=False)
    with pytest.raises(ValueError, match="Geografia IPS"):
        build_canonical_territorial_model(census_root=census, idsc_root=idsc,
            ips_root=ips, output_root=tmp_path / "canonical", run_id="test-run")
    assert not (tmp_path / "canonical" / ".test-run.partial").exists()


def test_rejects_ips_summary_that_is_not_content_duplicate(tmp_path: Path):
    census, idsc, ips = _inputs(tmp_path)
    path = ips / "ips_2026_summary.csv"
    frame = pd.read_csv(path)
    frame.loc[0, "value_numeric"] = -1
    frame.to_csv(path, index=False)
    with pytest.raises(ValueError, match="não é duplicata de conteúdo"):
        build_canonical_territorial_model(
            census_root=census,
            idsc_root=idsc,
            ips_root=ips,
            output_root=tmp_path / "canonical",
            run_id="test-run",
        )
    assert not (tmp_path / "canonical" / ".test-run.partial").exists()
