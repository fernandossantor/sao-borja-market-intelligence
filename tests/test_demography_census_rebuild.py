from pathlib import Path

import pandas as pd
import pytest

from sbmi.demography_census_rebuild import rebuild_census_products


def _inputs(tmp_path: Path):
    source = tmp_path / "source"
    historical = tmp_path / "historical"
    source.mkdir()
    historical.mkdir()
    composition = pd.DataFrame(
        {
            "Composição domiciliar": ["A", "B", "C"],
            "Porcentagem de domicílios": [23.18, 21.31, 0.31],
            "Município": ["São Borja "] * 3,
            "Sigla UF": ["RS"] * 3,
            "Código do Município": [4318002] * 3,
        }
    )
    territory = pd.DataFrame(
        {
            "Ano da pesquisa": [2022],
            "Área(km²)": [3616.69],
            "Densidade demográfica(hab/km²)": [16.5],
            "Município": ["São Borja "],
            "Sigla UF": ["RS"],
            "Código do Município": [4318002],
        }
    )
    composition.to_excel(
        source / "Censo 2022 - Composição domiciliar - São Borja (RS).xlsx",
        index=False,
    )
    territory.to_excel(source / "Censo 2022 - Território - São Borja (RS).xlsx", index=False)
    composition.rename(
        columns={
            "Composição domiciliar": "composicao_domiciliar",
            "Porcentagem de domicílios": "porcentagem_de_domicilios",
            "Município": "municipio",
            "Sigla UF": "sigla_uf",
            "Código do Município": "codigo_do_municipio",
        }
    ).assign(porcentagem_de_domicilios=[2318, 2131, 31]).to_parquet(
        historical / "Censo 2022 - Composição domiciliar - São Borja (RS)_Sheet1.parquet",
        index=False,
    )
    territory.rename(
        columns={
            "Ano da pesquisa": "ano_da_pesquisa",
            "Área(km²)": "area_km2",
            "Densidade demográfica(hab/km²)": "densidade_demografica_hab_km2",
            "Município": "municipio",
            "Sigla UF": "sigla_uf",
            "Código do Município": "codigo_do_municipio",
        }
    ).assign(area_km2=[361669], densidade_demografica_hab_km2=[1650]).to_parquet(
        historical / "Censo 2022 - Território - São Borja (RS)_Sheet1.parquet",
        index=False,
    )
    return source, historical


def _run(tmp_path: Path, run_id="test-run"):
    source, historical = _inputs(tmp_path)
    return rebuild_census_products(
        source_root=source,
        historical_root=historical,
        staging_root=tmp_path / "staging",
        curated_root=tmp_path / "curated",
        audit_root=tmp_path / "audit",
        run_id=run_id,
    )


def test_rebuilds_only_expected_decimal_corrections(tmp_path: Path):
    result = _run(tmp_path)
    composition = pd.read_parquet(result.curated_path / "household_composition.parquet")
    territory = pd.read_parquet(result.curated_path / "territory.parquet")
    assert composition["porcentagem_de_domicilios"].tolist() == [23.18, 21.31, 0.31]
    assert set(composition["municipio"]) == {"São Borja"}
    assert territory["area_km2"].tolist() == [3616.69]
    assert territory["densidade_demografica_hab_km2"].tolist() == [16.5]
    assert len(result.comparison) == 5
    assert set(result.comparison["classification"]) == {"EXPECTED_CHANGE"}


def test_outputs_are_atomic_and_refuse_overwrite(tmp_path: Path):
    result = _run(tmp_path)
    assert (result.audit_path / "census_rebuild_manifest.csv").is_file()
    with pytest.raises(FileExistsError):
        rebuild_census_products(
            source_root=tmp_path / "source",
            historical_root=tmp_path / "historical",
            staging_root=tmp_path / "staging",
            curated_root=tmp_path / "curated",
            audit_root=tmp_path / "audit",
            run_id="test-run",
        )
    assert not (tmp_path / "staging" / ".test-run.partial").exists()


@pytest.mark.parametrize("run_id", ["", ".", "..", "nested/name"])
def test_rejects_unsafe_run_id(tmp_path: Path, run_id):
    with pytest.raises(ValueError, match="identificador|nome simples"):
        rebuild_census_products(
            source_root=tmp_path,
            historical_root=tmp_path,
            staging_root=tmp_path / "staging",
            curated_root=tmp_path / "curated",
            audit_root=tmp_path / "audit",
            run_id=run_id,
        )


def test_rejects_wrong_geography(tmp_path: Path):
    source, historical = _inputs(tmp_path)
    path = source / "Censo 2022 - Território - São Borja (RS).xlsx"
    frame = pd.read_excel(path)
    frame["Código do Município"] = 0
    frame.to_excel(path, index=False)
    with pytest.raises(ValueError, match="Município"):
        rebuild_census_products(
            source_root=source,
            historical_root=historical,
            staging_root=tmp_path / "staging",
            curated_root=tmp_path / "curated",
            audit_root=tmp_path / "audit",
            run_id="test-run",
        )
