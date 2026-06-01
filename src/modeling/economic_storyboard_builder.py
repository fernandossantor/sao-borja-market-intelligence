import pandas as pd
import os

print("\n===================================")
print("ECONOMIC STORYBOARD BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# CARREGAR
# --------------------------------------------------

factsheet = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_factsheet.csv"
    )
)

concentration = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "sector_concentration.csv"
    )
)

private_structure = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "sector_structural_private.csv"
    )
)

winners = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "sector_winners_losers.csv"
    )
)

# --------------------------------------------------
# VALORES PRINCIPAIS
# --------------------------------------------------

pib_cagr = factsheet.loc[
    factsheet["indicator"]
    ==
    "PIB CAGR 2002-2023 (%)",
    "value"
].iloc[0]

private_cagr = factsheet.loc[
    factsheet["indicator"]
    ==
    "VAB Privado CAGR 2002-2021 (%)",
    "value"
].iloc[0]

employment_growth = factsheet.loc[
    factsheet["indicator"]
    ==
    "Crescimento Emprego 1996-2021 (%)",
    "value"
].iloc[0]

agro_share = factsheet.loc[
    factsheet["indicator"]
    ==
    "Participação Média Agro (%)",
    "value"
].iloc[0]

industry_share = factsheet.loc[
    factsheet["indicator"]
    ==
    "Participação Média Indústria (%)",
    "value"
].iloc[0]

services_share = factsheet.loc[
    factsheet["indicator"]
    ==
    "Participação Média Serviços (%)",
    "value"
].iloc[0]

regime = factsheet.loc[
    factsheet["indicator"]
    ==
    "Regime Predominante",
    "value"
].iloc[0]

# --------------------------------------------------
# CONCENTRAÇÃO
# --------------------------------------------------

top5_share = (
    private_structure
    .sort_values(
        "ranking_emprego_privado"
    )
    .head(5)
    ["share_emprego_privado_pct"]
    .sum()
)

hhi = (
    private_structure[
        "share_emprego_privado_pct"
    ]
    .pow(2)
    .sum()
)

# --------------------------------------------------
# LÍDERES PRIVADOS
# --------------------------------------------------

largest_employer = (
    private_structure
    .sort_values(
        "ranking_emprego_privado"
    )
    .iloc[0]["sector"]
)

largest_salary = (
    private_structure
    .sort_values(
        "ranking_salarios_privado"
    )
    .iloc[0]["sector"]
)

# --------------------------------------------------
# WINNER
# --------------------------------------------------

winner = (
    winners
    .sort_values(
        "delta_share_pp",
        ascending=False
    )
    .iloc[0]["sector"]
)

# --------------------------------------------------
# STORYBOARD
# --------------------------------------------------

storyboard = pd.DataFrame(
    [
        ["economic","growth","PIB CAGR 2002-2023 (%)", pib_cagr],
        ["economic","growth","VAB Privado CAGR 2002-2021 (%)", private_cagr],
        ["economic","labor","Crescimento Emprego 1996-2021 (%)", employment_growth],

        ["economic","structure","Participação Média Agro (%)", agro_share],
        ["economic","structure","Participação Média Indústria (%)", industry_share],
        ["economic","structure","Participação Média Serviços (%)", services_share],

        ["economic","concentration","HHI Privado", hhi],
        ["economic","concentration","Top 5 Share Privado (%)", top5_share],

        ["economic","sectors","Maior Empregador Privado", largest_employer],
        ["economic","sectors","Maior Massa Salarial Privada", largest_salary],
        ["economic","sectors","Principal Winner", winner],

        ["economic","regimes","Regime Predominante", regime]
    ],
    columns=[
        "domain",
        "category",
        "indicator",
        "value"
    ]
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("ECONOMIC STORYBOARD")
print("===================================\n")

print(storyboard)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "economic_storyboard.csv"
)

storyboard.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
