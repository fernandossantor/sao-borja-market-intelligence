import pandas as pd
import os

print("\n===================================")
print("DASHBOARD DATASET BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# CARREGAR BASES
# --------------------------------------------------

master = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_master_series_v2.csv"
    )
)

structure = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_structure_v2.csv"
    )
)

regimes = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_regimes.csv"
    )
)

history = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_long_history.csv"
    )
)

# --------------------------------------------------
# SELECIONAR COLUNAS
# --------------------------------------------------

structure = structure[
    [
        "year",
        "agro_share",
        "industry_share",
        "services_share",
        "public_share"
    ]
]

regimes = regimes[
    [
        "year",
        "regime"
    ]
]

history = history[
    [
        "year",
        "employment_private",
        "employment_growth_pct",
        "pib_growth_pct",
        "private_vab_growth_pct"
    ]
]

# --------------------------------------------------
# MERGES
# --------------------------------------------------

dashboard = master.merge(
    structure,
    on="year",
    how="left"
)

dashboard = dashboard.merge(
    regimes,
    on="year",
    how="left"
)

dashboard = dashboard.merge(
    history,
    on="year",
    how="left"
)

# --------------------------------------------------
# ORDENAR
# --------------------------------------------------

dashboard = dashboard.sort_values(
    "year"
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("DASHBOARD DATASET")
print("===================================\n")

print(dashboard.head())

print("\nShape:")
print(dashboard.shape)

print("\nColunas:")
print(list(dashboard.columns))

print("\nAnos:")
print(
    dashboard["year"].min(),
    "-",
    dashboard["year"].max()
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "dashboard_dataset.csv"
)

dashboard.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
