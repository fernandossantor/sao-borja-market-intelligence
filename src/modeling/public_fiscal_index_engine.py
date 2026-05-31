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

panel = pd.read_csv(
    f"{EXPORT_PATH}/public_fiscal_panel.csv"
)

print("\n===================================")
print("PUBLIC FISCAL INDEX ENGINE")
print("===================================\n")

print(
    f"Registros carregados: {len(panel)}"
)

# =========================================
# ANNUAL AGGREGATION
# =========================================

annual = (

    panel

    .groupby(
        ["year", "source"]
    )["value"]

    .sum()

    .reset_index()

)

# =========================================
# SOURCE CLASSIFICATION
# =========================================

def classify_source(source):

    s = str(source).lower()

    # FPM

    if "fpm" in s:
        return "fpm"

    # EDUCACAO

    if any(
        x in s
        for x in [
            "fundeb",
            "merenda",
            "pdde",
            "salário",
            "educa",
            "manuten"
        ]
    ):
        return "educacao"

    # SAUDE

    if any(
        x in s
        for x in [
            "mac",
            "farm",
            "primária",
            "saúde",
            "vigil",
            "enferm",
            "agentes comunit",
            "endemias"
        ]
    ):
        return "saude"

    # ASSISTENCIA

    if any(
        x in s
        for x in [
            "suas",
            "proteção social",
            "assist"
        ]
    ):
        return "assistencia"

    # OUTROS

    return "outros"

annual["group"] = (
    annual["source"]
    .apply(classify_source)
)

# =========================================
# GROUP TOTALS
# =========================================

groups = (

    annual

    .groupby(
        ["year", "group"]
    )["value"]

    .sum()

    .reset_index()

)

pivot = groups.pivot(
    index="year",
    columns="group",
    values="value"
)

pivot = pivot.fillna(0)

# =========================================
# BASE 2021
# =========================================

base = pivot.loc[
    BASE_YEAR
]

print("\n===================================")
print("BASE 2021")
print("===================================\n")

print(base)

# =========================================
# INDEXES
# =========================================

for col in pivot.columns:

    base_value = base[col]

    if base_value == 0:
        continue

    pivot[f"{col}_index"] = (
        pivot[col]
        /
        base_value
        *
        100
    )

# =========================================
# WEIGHTS
# =========================================

weights = {

    "fpm_index": 0.35,
    "saude_index": 0.25,
    "educacao_index": 0.20,
    "assistencia_index": 0.10,
    "outros_index": 0.10

}

# =========================================
# COMPOSITE INDEX
# =========================================

pivot["public_index"] = 0

for col, weight in weights.items():

    if col in pivot.columns:

        pivot["public_index"] += (
            pivot[col]
            * weight
        )

# =========================================
# GROWTH
# =========================================

pivot["public_growth_pct"] = (

    pivot["public_index"]

    .pct_change()

    * 100

)

# =========================================
# OUTPUT
# =========================================

result = (
    pivot
    .reset_index()
)

print("\n===================================")
print("PUBLIC INDEX")
print("===================================\n")

print(

    result[
        [
            "year",
            "public_index",
            "public_growth_pct"
        ]
    ]

)

# =========================================
# POST 2021
# =========================================

post2021 = result[
    result["year"] >= 2021
]

print("\n===================================")
print("POST-2021")
print("===================================\n")

print(

    post2021[
        [
            "year",
            "public_index",
            "public_growth_pct"
        ]
    ]

)

# =========================================
# EXPORT
# =========================================

index_file = os.path.join(
    EXPORT_PATH,
    "public_fiscal_index.csv"
)

post_file = os.path.join(
    EXPORT_PATH,
    "public_fiscal_index_post2021.csv"
)

result.to_csv(
    index_file,
    index=False
)

post2021.to_csv(
    post_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(index_file)
print(post_file)
