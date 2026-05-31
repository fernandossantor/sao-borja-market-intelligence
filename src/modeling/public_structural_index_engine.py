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
print("PUBLIC STRUCTURAL INDEX ENGINE")
print("===================================\n")

print(
    f"Registros carregados: {len(panel)}"
)

# =========================================
# CLASSIFICATION
# =========================================

def classify_source(source):

    s = str(source).lower()

    # ---------------------------------
    # EXCLUSÕES
    # ---------------------------------

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

    # ---------------------------------
    # RECEITA ESTRUTURAL
    # ---------------------------------

    if any(
        x in s
        for x in [
            "fpm",
            "fundeb",
            "itr"
        ]
    ):
        return "receita"

    # ---------------------------------
    # SAÚDE
    # ---------------------------------

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

    # ---------------------------------
    # EDUCAÇÃO
    # ---------------------------------

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

    # ---------------------------------
    # ASSISTÊNCIA
    # ---------------------------------

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

print("\n===================================")
print("GROUP DISTRIBUTION")
print("===================================\n")

print(
    panel["group"]
    .value_counts()
)

# =========================================
# ANNUAL
# =========================================

annual = (

    panel

    .groupby(
        ["year","group"]
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
# BASE
# =========================================

base = pivot.loc[
    BASE_YEAR
]

print("\n===================================")
print("BASE 2021")
print("===================================\n")

print(base)

# =========================================
# INDICES
# =========================================

groups = [
    "receita",
    "saude",
    "educacao",
    "assistencia"
]

for g in groups:

    if g not in pivot.columns:
        continue

    pivot[f"{g}_index"] = (

        pivot[g]
        /
        base[g]
        *
        100

    )

# =========================================
# WEIGHTS
# =========================================

weights = {

    "receita_index": 0.40,
    "saude_index": 0.30,
    "educacao_index": 0.20,
    "assistencia_index": 0.10

}

pivot["public_structural_index"] = 0

for col, w in weights.items():

    if col in pivot.columns:

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
print("STRUCTURAL INDEX")
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
    "public_structural_index.csv"
)

post_file = os.path.join(
    EXPORT_PATH,
    "public_structural_index_post2021.csv"
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
