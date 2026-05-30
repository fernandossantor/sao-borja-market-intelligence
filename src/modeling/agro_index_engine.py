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

print("\n===================================")
print("AGRO INDEX ENGINE")
print("===================================\n")

# =========================================
# PESOS OBSERVADOS
# =========================================

weights = {

    "Soja (em grão)": 0.4461,
    "Arroz (em casca)": 0.4178,
    "Trigo (em grão)": 0.0667,
    "Milho (em grão)": 0.0664

}

print("Pesos utilizados:\n")

for product, weight in weights.items():

    print(
        f"{product}: "
        f"{round(weight*100,2)}%"
    )

# =========================================
# PRODUÇÃO
# =========================================

production = agro[

    agro["variable"]
    ==
    "quantidade_produzida"

].copy()

pivot = production.pivot_table(

    index="year",
    columns="product",
    values="value",
    aggfunc="sum"

)

pivot = pivot.sort_index()

print("\n===================================")
print("BASE 2021")
print("===================================\n")

print(
    pivot.loc[BASE_YEAR]
)

# =========================================
# PRODUCT INDICES
# =========================================

index_df = pd.DataFrame(
    index=pivot.index
)

for product in weights.keys():

    if product not in pivot.columns:

        print(
            f"[WARN] Produto ausente: "
            f"{product}"
        )

        continue

    base_value = pivot.loc[
        BASE_YEAR,
        product
    ]

    index_df[product] = (

        pivot[product]
        /
        base_value
        *
        100

    )

# =========================================
# AGRO INDEX
# =========================================

agro_index = []

for year in index_df.index:

    score = 0

    for product, weight in weights.items():

        if product not in index_df.columns:
            continue

        value = index_df.loc[
            year,
            product
        ]

        if pd.isna(value):
            continue

        score += (
            value * weight
        )

    agro_index.append(
        score
    )

index_df["agro_index"] = (
    agro_index
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

index_df = (
    index_df
    .reset_index()
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
