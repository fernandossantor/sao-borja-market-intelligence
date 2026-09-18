from pathlib import Path

import pandas as pd

from sbmi.radar_open_data import RICE_NCMS, audit_radar_open_data


def test_filters_rice_ncms_and_calculates_wide_composition(tmp_path: Path):
    source = tmp_path / "source"
    source.mkdir()
    pd.DataFrame(
        {
            "NCM": ["10062010", "10063021", "99999999"],
            "Produção Interna": [80, 20, 1],
            "Entradas OUF": [15, 60, 1],
            "Importações": [5, 20, 1],
        }
    ).to_csv(source / "Composicao_de_Mercado.csv", index=False)

    result = audit_radar_open_data(
        source_dir=source,
        output_root=tmp_path / "out",
        execution_id="run-1",
    )

    assert set(result.ncm_matches["ncm_sbmi"]) == {"10062010", "10063021"}
    rows = result.composition_summary.set_index("ncm")
    assert rows.loc["10062010", "part_rs"] == 0.8
    assert rows.loc["10063021", "part_rs"] == 0.2
    assert rows.loc["10062010", "dependencia_nt"] == "FORA_DAS_FAIXAS_NT"
    assert rows.loc["10063021", "dependencia_nt"] == "MEDIA"


def test_calculates_long_composition_and_dependency(tmp_path: Path):
    source = tmp_path / "source"
    source.mkdir()
    pd.DataFrame(
        {
            "Código NCM": ["10064000"] * 3,
            "Tipo de operação": ["INT", "OUF", "EXT"],
            "Valor (R$)": [4, 76, 20],
        }
    ).to_csv(source / "composicao_mercado.csv", index=False)

    result = audit_radar_open_data(
        source_dir=source,
        output_root=tmp_path / "out",
        execution_id="run-2",
    )

    row = result.composition_summary.iloc[0]
    assert row["part_rs"] == 0.04
    assert row["dependencia_nt"] == "CRITICA"


def test_export_file_filters_without_calculating_market_share(tmp_path: Path):
    source = tmp_path / "source"
    source.mkdir()
    pd.DataFrame(
        {
            "CO_NCM": list(RICE_NCMS[:2]) + ["01010101"],
            "VL_FOB": [10, 20, 30],
            "NO_PAIS": ["A", "B", "C"],
        }
    ).to_csv(source / "Exportacoes_por_NCM.csv", index=False)

    result = audit_radar_open_data(
        source_dir=source,
        output_root=tmp_path / "out",
        execution_id="run-3",
    )

    assert len(result.ncm_matches) == 2
    assert result.composition_summary.empty


def test_unknown_composition_schema_does_not_invent_values(tmp_path: Path):
    source = tmp_path / "source"
    source.mkdir()
    pd.DataFrame(
        {"NCM": ["10062010"], "Campo Desconhecido": [100]}
    ).to_csv(source / "Composicao_de_Mercado.csv", index=False)

    result = audit_radar_open_data(
        source_dir=source,
        output_root=tmp_path / "out",
        execution_id="run-4",
    )

    assert result.composition_summary.empty
    assert "COMPOSITION_FIELDS_NOT_IDENTIFIED" in set(result.limitations["code"])


def test_accepts_custom_ncm_basket_beyond_rice(tmp_path: Path):
    source = tmp_path / "source"
    source.mkdir()
    pd.DataFrame(
        {
            "NCM": ["22021000", "10062010"],
            "INT": [60, 1],
            "OUF": [30, 1],
            "EXT": [10, 1],
        }
    ).to_csv(source / "Composicao_de_Mercado.csv", index=False)

    basket = {"22021000": "Produto teste — cesta multissetorial"}
    result = audit_radar_open_data(
        source_dir=source,
        output_root=tmp_path / "out",
        execution_id="run-5",
        ncm_basket=basket,
        basket_name="teste_multissetorial",
    )

    assert set(result.ncm_matches["ncm_sbmi"]) == {"22021000"}
    row = result.composition_summary.iloc[0]
    assert row["part_rs"] == 0.6
    assert row["descricao_ncm"] == "Produto teste — cesta multissetorial"
    assert (result.output_path / "ncm_basket.csv").exists()
    assert not (result.output_path / "rice_ncm_matches.csv").exists()
