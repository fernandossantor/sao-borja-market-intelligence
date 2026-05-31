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
print("PUBLIC STRUCTURAL INDEX V2")
print("===================================\n")

print(
    f"Registros carregados: {len(panel)}"
)

# =========================================
# CLASSIFICATION
# =========================================

def classify_source(source):

    s = str(source).lower()

    # --------------------------------------
    # EXCLUSÕES
    # --------------------------------------

    excluded = [

        "covid",
        "ponte",
        "investimentos",
        "transferências especiais",
        "transferencias especiais",
        "desenvolvimento urbano",
        "fomento ao agro",
        "compensação",
        "compensasa"

    ]

    for e in excluded:

        if e in s:
            return "excluded"

    # --------------------------------------
    # RECEITA
    # --------------------------------------

    if any(
        x in s
        for x in [
            "fpm",
            "fundeb",
            "itr"
        ]
    ):
        return "receita"

    # --------------------------------------
    # SAÚDE
    # --------------------------------------

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

    # --------------------------------------
    # EDUCAÇÃO
    # --------------------------------------

    if any(
        x in s
        for x in [
            "pdde",
            "merenda",
            "salário",
            "educa",
            "manuten"
        ]
    ):
        return "educacao"

    # --------------------------------------
    # ASSISTÊNCIA
    # --------------------------------------

    if any(
        x in s
        for x in [
            "suas",
            "proteção social",
            "assist"
        ]
    ):
        return "assistencia"

    return "other"

# =========================================
# APPLY
# =========================================

panel["group"] = (
    panel["source"]
    .apply(classify_source)
)

panel = panel[
    panel["group"] != "excluded"
].copy()

# =========================================
# ANNUAL AGGREGATION
# =========================================

annual = (

    panel

    .groupby(
        ["year", "group"]
    )["value"]

    .sum()

    .reset_index()

)

pivot = annual.pivot(
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
# EMPIRICAL WEIGHTS
# =========================================

groups = [
    "receita",
    "saude",
    "educacao",
    "assistencia"
]

base_total = (
    base[groups]
    .sum()
)

weights = {}

for g in groups:

    if g not in base:
        continue

    weights[g] = (
        base[g]
        /
        base_total
    )

print("\n===================================")
print("EMPIRICAL WEIGHTS")
print("===================================\n")

for g, w in weights.items():

    print(
        f"{g}: {w:.2%}"
    )

# =========================================
# INDEXES
# =========================================

for g in groups:

    if g not in pivot.columns:
        continue

    base_value = base[g]

    if base_value == 0:
        continue

    pivot[f"{g}_index"] = (
        pivot[g]
        /
        base_value
        *
        100
    )

# =========================================
# COMPOSITE INDEX
# =========================================

pivot[
    "public_structural_index"
] = 0

for g, w in weights.items():

    col = f"{g}_index"

    if col not in pivot.columns:
        continue

    pivot[
        "public_structural_index"
    ] += (

        pivot[col]
        * w

    )

# =========================================
# GROWTH
# =========================================

pivot[
    "public_growth_pct"
] = (

    pivot[
        "public_structural_index"
    ]

    .pct_change()

    * 100

)

# =========================================
# RESULT
# =========================================

result = (
    pivot
    .reset_index()
)

print("\n===================================")
print("PUBLIC STRUCTURAL INDEX V2")
print("===================================\n")

print(

    result[
        [
            "year",
            "public_structural_index",
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
            "public_structural_index",
            "public_growth_pct"
        ]
    ]

)

# =========================================
# EXPORT
# =========================================

index_file = os.path.join(
    EXPORT_PATH,
    "public_structural_index_v2.csv"
)

post_file = os.path.join(
    EXPORT_PATH,
    "public_structural_index_v2_post2021.csv"
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
