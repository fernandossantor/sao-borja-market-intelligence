"""Filtros reproduzíveis para fontes oficiais secundárias de São Borja.

O módulo deliberadamente não faz download nem promove dados. Ele recebe
DataFrames materializados a partir das fontes oficiais e aplica filtros
municipais auditáveis, preservando o conceito original de cada fonte.
"""

from __future__ import annotations

import unicodedata

import pandas as pd

IBGE_CODE = 4318002
MUNICIPALITY = "SAO BORJA"
UF = "RS"

ANP_ANNUAL_SALES_REQUIRED = {
    "ANO",
    "UF",
    "MUNICÍPIO",
    "CÓDIGO IBGE",
    "VENDAS",
}

ANP_RETAILERS_REQUIRED = {
    "CODIGOISIMP",
    "AUTORIZACAO",
    "RAZAOSOCIAL",
    "CNPJ",
    "UF",
    "MUNICIPIO",
    "BANDEIRA",
}

COMEX_MUNICIPAL_REQUIRED = {
    "CO_ANO",
    "CO_MES",
    "SH4",
    "CO_PAIS",
    "SG_UF_MUN",
    "CO_MUN",
    "KG_LIQUIDO",
    "VL_FOB",
}


def _ascii_upper(value: object) -> str:
    text = "" if pd.isna(value) else str(value)
    normalized = unicodedata.normalize("NFKD", text)
    return (\n        "".join(char for char in normalized if not unicodedata.combining(char))\n        .upper()\n        .strip()\n    )


def _require_columns(frame: pd.DataFrame, required: set[str], source: str) -> None:
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise ValueError(f"{source}: colunas obrigatórias ausentes: {missing}")


def filter_anp_annual_sales(frame: pd.DataFrame) -> pd.DataFrame:
    """Filtra vendas anuais municipais da ANP para São Borja/RS.

    Conceito preservado: volume anual vendido no município segundo a ANP.
    A função não converte litros/kg em gasto, fluxo turístico ou consumo
    por perfil de usuário.
    """
    _require_columns(frame, ANP_ANNUAL_SALES_REQUIRED, "ANP vendas anuais")
    code = pd.to_numeric(frame["CÓDIGO IBGE"], errors="coerce")
    uf = frame["UF"].map(_ascii_upper)
    result = frame.loc[code.eq(IBGE_CODE) & uf.eq(UF)].copy()
    return result.reset_index(drop=True)


def filter_anp_retailers(frame: pd.DataFrame) -> pd.DataFrame:
    """Filtra revendedores varejistas em operação para São Borja/RS."""
    _require_columns(frame, ANP_RETAILERS_REQUIRED, "ANP revendedores")
    municipality = frame["MUNICIPIO"].map(_ascii_upper)
    uf = frame["UF"].map(_ascii_upper)
    result = frame.loc[municipality.eq(MUNICIPALITY) & uf.eq(UF)].copy()
    return result.reset_index(drop=True)


def filter_comex_municipal(frame: pd.DataFrame) -> pd.DataFrame:
    """Filtra a base municipal do Comex Stat pelo domicílio fiscal da empresa.

    O resultado permanece em SH4. Não deve ser interpretado como origem física
    da mercadoria nem convertido para NCM de 8 dígitos.
    """
    _require_columns(frame, COMEX_MUNICIPAL_REQUIRED, "Comex Stat municipal")
    code = pd.to_numeric(frame["CO_MUN"], errors="coerce")
    uf = frame["SG_UF_MUN"].map(_ascii_upper)
    result = frame.loc[code.eq(IBGE_CODE) & uf.eq(UF)].copy()
    return result.reset_index(drop=True)


def aggregate_comex_by_month_sh4(frame: pd.DataFrame) -> pd.DataFrame:
    """Agrega somente o recorte São Borja por ano, mês e SH4."""
    filtered = filter_comex_municipal(frame)
    if filtered.empty:
        return pd.DataFrame(
            columns=["CO_ANO", "CO_MES", "SH4", "KG_LIQUIDO", "VL_FOB"]
        )
    numeric = filtered.copy()
    for column in ("KG_LIQUIDO", "VL_FOB"):
        numeric[column] = pd.to_numeric(numeric[column], errors="raise")
    result = (
        numeric.groupby(["CO_ANO", "CO_MES", "SH4"], as_index=False, dropna=False)[
            ["KG_LIQUIDO", "VL_FOB"]
        ]
        .sum()
        .sort_values(["CO_ANO", "CO_MES", "SH4"])
        .reset_index(drop=True)
    )
    return result
