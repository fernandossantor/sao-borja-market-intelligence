import pandas as pd
import pytest

from sbmi.secondary_official_sources import (
    aggregate_comex_by_month_sh4,
    filter_anp_annual_sales,
    filter_anp_retailers,
    filter_comex_municipal,
)


def test_filters_anp_annual_sales_by_ibge_code_and_uf():
    frame = pd.DataFrame(
        [
            {"ANO": 2024, "UF": "RS", "MUNICÍPIO": "São Borja", "CÓDIGO IBGE": 4318002, "VENDAS": 10.0},
            {"ANO": 2024, "UF": "RS", "MUNICÍPIO": "Itaqui", "CÓDIGO IBGE": 4310603, "VENDAS": 20.0},
            {"ANO": 2024, "UF": "SC", "MUNICÍPIO": "Outro", "CÓDIGO IBGE": 4318002, "VENDAS": 30.0},
        ]
    )
    result = filter_anp_annual_sales(frame)
    assert len(result) == 1
    assert result.iloc[0]["MUNICÍPIO"] == "São Borja"
    assert result.iloc[0]["VENDAS"] == 10.0


def test_filters_anp_retailers_normalizing_accents_and_case():
    frame = pd.DataFrame(
        [
            {
                "CODIGOISIMP": 1,
                "AUTORIZACAO": "PR/RS0000001",
                "RAZAOSOCIAL": "A",
                "CNPJ": "00000000000100",
                "UF": "rs",
                "MUNICIPIO": "São Borja",
                "BANDEIRA": "BANDEIRA BRANCA",
            },
            {
                "CODIGOISIMP": 2,
                "AUTORIZACAO": "PR/RS0000002",
                "RAZAOSOCIAL": "B",
                "CNPJ": "00000000000200",
                "UF": "RS",
                "MUNICIPIO": "ITAQUI",
                "BANDEIRA": "VIBRA",
            },
        ]
    )
    result = filter_anp_retailers(frame)
    assert result["RAZAOSOCIAL"].tolist() == ["A"]


def test_filters_and_aggregates_comex_by_fiscal_domicile_sh4():
    frame = pd.DataFrame(
        [
            {
                "CO_ANO": 2026,
                "CO_MES": 1,
                "SH4": "1006",
                "CO_PAIS": 32,
                "SG_UF_MUN": "RS",
                "CO_MUN": 4318002,
                "KG_LIQUIDO": 100,
                "VL_FOB": 200,
            },
            {
                "CO_ANO": 2026,
                "CO_MES": 1,
                "SH4": "1006",
                "CO_PAIS": 858,
                "SG_UF_MUN": "RS",
                "CO_MUN": "4318002",
                "KG_LIQUIDO": 50,
                "VL_FOB": 80,
            },
            {
                "CO_ANO": 2026,
                "CO_MES": 1,
                "SH4": "1006",
                "CO_PAIS": 32,
                "SG_UF_MUN": "RS",
                "CO_MUN": 4310603,
                "KG_LIQUIDO": 999,
                "VL_FOB": 999,
            },
        ]
    )
    filtered = filter_comex_municipal(frame)
    assert len(filtered) == 2
    aggregated = aggregate_comex_by_month_sh4(frame)
    assert aggregated.to_dict("records") == [
        {
            "CO_ANO": 2026,
            "CO_MES": 1,
            "SH4": "1006",
            "KG_LIQUIDO": 150,
            "VL_FOB": 280,
        }
    ]


def test_rejects_unexpected_schema_instead_of_guessing_columns():
    frame = pd.DataFrame([{"municipio": "São Borja"}])
    with pytest.raises(ValueError, match="colunas obrigatórias ausentes"):
        filter_anp_annual_sales(frame)
