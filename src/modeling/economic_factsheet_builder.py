import pandas as pd
import numpy as np
import os

print("\n===================================")
print("ECONOMIC FACTSHEET BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# CARREGAR DADOS
# --------------------------------------------------

structure = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_structure_v2.csv"
    )
)

vab_private = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_vab_observed.csv"
    )
)

employment = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_employment_long_history.csv"
    )
)

regimes = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_regimes.csv"
    )
)

pib = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "pib_canonical.csv"
    )
)

# --------------------------------------------------
# PIB CAGR
# --------------------------------------------------

pib_start = pib.iloc[0]["pib_total"]
pib_end = pib[pib["year"] == 2023]["pib_total"].iloc[0]

years = 2023 - 2002

pib_cagr = (
    (pib_end / pib_start) ** (1 / years)
    - 1
) * 100

# --------------------------------------------------
# VAB PRIVADO CAGR
# --------------------------------------------------

private_start = vab_private.iloc[0]["vab_private"]
private_end = vab_private.iloc[-1]["vab_private"]

years_private = (
    vab_private.iloc[-1]["year"]
    -
    vab_private.iloc[0]["year"]
)

private_cagr = (
    (private_end / private_start)
    ** (1 / years_private)
    - 1
) * 100

# --------------------------------------------------
# SHARES MÉDIOS
# --------------------------------------------------

agro_share = structure["agro_share"].mean()
industry_share = structure["industry_share"].mean()
services_share = structure["services_share"].mean()
public_share = structure["public_share"].mean()

# --------------------------------------------------
# EMPREGO
# --------------------------------------------------

emp_start = employment.iloc[0]["employment_total"]
emp_end = employment.iloc[-1]["employment_total"]

employment_growth = (
    (emp_end / emp_start)
    - 1
) * 100

# --------------------------------------------------
# ANOS DE DESTAQUE
# --------------------------------------------------

agro_peak_year = structure.loc[
    structure["agro_share"].idxmax(),
    "year"
]

industry_peak_year = structure.loc[
    structure["industry_share"].idxmax(),
    "year"
]

services_peak_year = structure.loc[
    structure["services_share"].idxmax(),
    "year"
]

# --------------------------------------------------
# REGIME PREDOMINANTE
# --------------------------------------------------

main_regime = (
    regimes["regime"]
    .value_counts()
    .idxmax()
)

# --------------------------------------------------
# FACTSHEET
# --------------------------------------------------

factsheet = pd.DataFrame(
    [
        ["PIB 2023", pib_end],
        ["PIB CAGR 2002-2023 (%)", pib_cagr],
        ["VAB Privado CAGR 2002-2021 (%)", private_cagr],
        ["Participação Média Agro (%)", agro_share],
        ["Participação Média Indústria (%)", industry_share],
        ["Participação Média Serviços (%)", services_share],
        ["Participação Média Pública (%)", public_share],
        ["Emprego Privado 1996", emp_start],
        ["Emprego Privado 2021", emp_end],
        ["Crescimento Emprego 1996-2021 (%)", employment_growth],
        ["Ano Pico Agro", agro_peak_year],
        ["Ano Pico Indústria", industry_peak_year],
        ["Ano Pico Serviços", services_peak_year],
        ["Regime Predominante", main_regime]
    ],
    columns=[
        "indicator",
        "value"
    ]
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("FACTSHEET")
print("===================================\n")

print(factsheet)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "economic_factsheet.csv"
)

factsheet.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
