import pandas as pd
import numpy as np
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

BASE_YEAR = 2021

# =========================================
# LOAD
# =========================================

agro = pd.read_csv(
    f"{EXPORT_PATH}/agro_series.csv"
)

structure = pd.read_csv(
    f"{EXPORT_PATH}/agro_structure.csv"
)

print("\n===================================")
print("AGRO INDEX ENGINE")
print("===================================\n")

# =========================================
# TOP PRODUCTS
# =========================================

weights = {

    "Soja (em grão)": 0.4461,
    "Arroz (em casca)": 0.4178,
    "Trigo (em grão)": 0.0667,
    "Milho (em grão)": 0.0664

}

print("Pesos utilizados:\n")

for k, v in weights.items():

    print(
        f"{k}: {round(v*100,2)}%"
    )

# =========================================
# QUANTIDADE PRODUZIDA
# =========================================

production = agro[

    (agro["variable"] == "quantidade_produzida")
    &
    (agro["product"].isin(
        weights.keys()
    ))

].copy()

print(
    f"\nRegistros produção: "
    f"{len(production)}"
)

# =========================================
# PIVOT
# =========================================

pivot = production.pivot_table(

    index="year",
    columns="product",
    values="value",
    aggfunc="sum"

)

pivot = pivot.sort_index()

# =========================================
# BASE 2021
# =========================================

if BASE_YEAR not in pivot.index:

    raise Exception(
        f"Ano base {BASE_YEAR} não encontrado."
    )

base = pivot.loc[
    BASE_YEAR
]

# =========================================
# INDICES
# =========================================

index_df = pd.DataFrame()

index_df["year"] = pivot.index

for product in weights:

    if product not in pivot.columns:
        continue

    index_df[product] = (

        pivot[product]
        /
        base[product]
        *
        100

    )

# =========================================
# AGRO INDEX
# =========================================

weighted_index = []

for _, row in index_df.iterrows():

    score = 0

    for product, weight in weights.items():

        if product not in row:
            continue

        value = row[product]

        if pd.isna(value):
            continue

        score += (
            value * weight
        )

    weighted_index.append(
        score
    )

index_df["agro_index"] = (
    weighted_index
)

# =========================================
# GROWTH
# =========================================

index_df[
    "agro_growth_pct"
] = (

    index_df["agro_index"]
    .pct_change()
    * 100

)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("AGRO INDEX")
print("===================================\n")

print(
    index_df.tail(15)
)

# =========================================
# 2021+
# =========================================

recent = index_df[
    index_df["year"] >= 2021
]

print("\n===================================")
print("POST-2021")
print("===================================\n")

print(recent)

# =========================================
# EXPORT
# =========================================

index_file = os.path.join(
    EXPORT_PATH,
    "agro_index.csv"
)

recent_file = os.path.join(
    EXPORT_PATH,
    "agro_index_post2021.csv"
)

index_df.to_csv(
    index_file,
    index=False
)

recent.to_csv(
    recent_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(index_file)
print(recent_file)
