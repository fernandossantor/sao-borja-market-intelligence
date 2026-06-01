import pandas as pd
import os

print("\n===================================")
print("SECTOR SNAPSHOT 2021")
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

# ----------------------------------------
# FILTRAR 2021
# ----------------------------------------

df = df[
    df["year"] == 2021
].copy()

# ----------------------------------------
# REMOVER TOTAL
# ----------------------------------------

df = df[
    df["sector"] != "Total"
].copy()

# ----------------------------------------
# SHARES
# ----------------------------------------

total_emprego = df["emprego_total"].sum()

total_salarios = df["salarios_empresas"].sum()

df["share_emprego_pct"] = (
    df["emprego_total"]
    /
    total_emprego
) * 100

df["share_salarios_pct"] = (
    df["salarios_empresas"]
    /
    total_salarios
) * 100

# ----------------------------------------
# RANKINGS
# ----------------------------------------

df["rank_emprego"] = (
    df["emprego_total"]
    .rank(
        ascending=False,
        method="dense"
    )
)

df["rank_salarios"] = (
    df["salarios_empresas"]
    .rank(
        ascending=False,
        method="dense"
    )
)

# ----------------------------------------
# ORDENAR
# ----------------------------------------

snapshot = df.sort_values(
    "rank_emprego"
)

print(snapshot.head(15))

export_file = os.path.join(
    EXPORT_PATH,
    "sector_snapshot_2021.csv"
)

snapshot.to_csv(
    export_file,
    index=False
)

print("\nExportado:")
print(export_file)
