import pandas as pd
import numpy as np
import os

print("\n===================================")
print("SECTOR WINNERS LOSERS BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_sector_master_panel.csv"
    )
)

# --------------------------------------------------
# REMOVER TOTAL
# --------------------------------------------------

df = df[
    df["sector"] != "Total"
].copy()

# --------------------------------------------------
# EMPREGO
# --------------------------------------------------

employment = (
    df.pivot_table(
        index="sector",
        columns="year",
        values="emprego_total",
        aggfunc="sum"
    )
)

# --------------------------------------------------
# SALÁRIOS
# --------------------------------------------------

salaries = (
    df.pivot_table(
        index="sector",
        columns="year",
        values="salarios_empresas",
        aggfunc="sum"
    )
)

# --------------------------------------------------
# TOTAL MUNICIPAL
# --------------------------------------------------

total_2007 = employment[2007].sum()
total_2021 = employment[2021].sum()

# --------------------------------------------------
# BASE
# --------------------------------------------------

result = pd.DataFrame()

result["sector"] = employment.index

result["emprego_2007"] = employment[2007].values
result["emprego_2021"] = employment[2021].values

result["salarios_2007"] = salaries[2007].values
result["salarios_2021"] = salaries[2021].values

# --------------------------------------------------
# SHARES
# --------------------------------------------------

result["share_2007"] = (
    result["emprego_2007"]
    / total_2007
) * 100

result["share_2021"] = (
    result["emprego_2021"]
    / total_2021
) * 100

# --------------------------------------------------
# CRESCIMENTO
# --------------------------------------------------

result["crescimento_emprego_pct"] = (
    (
        result["emprego_2021"]
        /
        result["emprego_2007"]
    )
    - 1
) * 100

# --------------------------------------------------
# GANHO ESTRUTURAL
# --------------------------------------------------

result["delta_share_pp"] = (
    result["share_2021"]
    -
    result["share_2007"]
)

# --------------------------------------------------
# CLASSIFICAÇÃO
# --------------------------------------------------

conditions = [
    result["delta_share_pp"] > 1,
    result["delta_share_pp"] < -1
]

choices = [
    "winner",
    "loser"
]

result["classification"] = np.select(
    conditions,
    choices,
    default="neutral"
)

# --------------------------------------------------
# ORDENAR
# --------------------------------------------------

result = result.sort_values(
    "delta_share_pp",
    ascending=False
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("TOP WINNERS")
print("===================================\n")

print(
    result.head(10)
)

print("\n===================================")
print("TOP LOSERS")
print("===================================\n")

print(
    result.tail(10)
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "sector_winners_losers.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
