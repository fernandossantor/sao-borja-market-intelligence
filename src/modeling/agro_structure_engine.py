import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# LOAD
# =========================================

agro = pd.read_csv(
    f"{EXPORT_PATH}/agro_series.csv"
)

print("\n===================================")
print("AGRO STRUCTURE ENGINE")
print("===================================\n")

print(
    f"Registros carregados: {len(agro)}"
)

# =========================================
# VALOR DA PRODUÇÃO
# =========================================

value_df = agro[
    agro["variable"]
    == "valor_producao"
].copy()

print(
    f"Registros valor_producao: "
    f"{len(value_df)}"
)

# =========================================
# HISTÓRICO TOTAL
# =========================================

historical = (

    value_df

    .groupby(
        "product"
    )["value"]

    .sum()

    .reset_index()

    .rename(
        columns={
            "value":
            "historical_value"
        }
    )

)

historical_total = (
    historical["historical_value"]
    .sum()
)

historical[
    "historical_share_pct"
] = (

    historical["historical_value"]
    /
    historical_total
    *
    100

)

# =========================================
# 2021
# =========================================

base_2021 = (

    value_df[
        value_df["year"] == 2021
    ]

    .groupby(
        "product"
    )["value"]

    .sum()

    .reset_index()

    .rename(
        columns={
            "value":
            "value_2021"
        }
    )

)

total_2021 = (
    base_2021["value_2021"]
    .sum()
)

base_2021[
    "share_2021_pct"
] = (

    base_2021["value_2021"]
    /
    total_2021
    *
    100

)

# =========================================
# 2024
# =========================================

latest = (

    value_df[
        value_df["year"] == 2024
    ]

    .groupby(
        "product"
    )["value"]

    .sum()

    .reset_index()

    .rename(
        columns={
            "value":
            "value_2024"
        }
    )

)

total_2024 = (
    latest["value_2024"]
    .sum()
)

latest[
    "share_2024_pct"
] = (

    latest["value_2024"]
    /
    total_2024
    *
    100

)

# =========================================
# MERGE
# =========================================

structure = (

    historical

    .merge(
        base_2021,
        on="product",
        how="outer"
    )

    .merge(
        latest,
        on="product",
        how="outer"
    )

)

structure = structure.sort_values(

    "historical_share_pct",
    ascending=False

)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("AGRO STRUCTURE")
print("===================================\n")

print(

    structure[[
        "product",
        "historical_share_pct",
        "share_2021_pct",
        "share_2024_pct"
    ]]

)

# =========================================
# TOP PRODUCTS
# =========================================

top_products = structure.head(10)

print("\n===================================")
print("TOP PRODUCTS")
print("===================================\n")

print(top_products)

# =========================================
# EXPORT
# =========================================

structure_file = os.path.join(
    EXPORT_PATH,
    "agro_structure.csv"
)

top_file = os.path.join(
    EXPORT_PATH,
    "agro_top_products.csv"
)

structure.to_csv(
    structure_file,
    index=False
)

top_products.to_csv(
    top_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(structure_file)
print(top_file)
