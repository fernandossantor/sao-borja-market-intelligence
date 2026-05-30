import pandas as pd
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

agro_index = pd.read_csv(
    f"{EXPORT_PATH}/agro_index.csv"
)

economic = pd.read_csv(
    f"{EXPORT_PATH}/territorial_economic_model.csv"
)

print("\n===================================")
print("AGRO VAB PROJECTION")
print("===================================\n")

# =========================================
# BASE VAB
# =========================================

base_row = economic[
    economic["year"] == BASE_YEAR
]

if len(base_row) == 0:

    raise Exception(
        f"Ano base {BASE_YEAR} não encontrado."
    )

base_vab = float(
    base_row["vab_agro"].iloc[0]
)

print(
    f"VAB Agro {BASE_YEAR}: "
    f"R$ {base_vab:,.2f}"
)

# =========================================
# INDEX
# =========================================

projection = agro_index.copy()

# Normalização para garantir
# 2021 = 100

base_index = float(

    projection[
        projection["year"] == BASE_YEAR
    ]["agro_index"]

    .iloc[0]

)

projection[
    "agro_index_norm"
] = (

    projection["agro_index"]
    /
    base_index
    *
    100

)

# =========================================
# VAB PROJECTION
# =========================================

projection[
    "vab_agro_estimated"
] = (

    base_vab
    *
    projection[
        "agro_index_norm"
    ]
    / 100

)

# =========================================
# POST 2021
# =========================================

post2021 = projection[
    projection["year"] >= 2021
].copy()

# =========================================
# GROWTH
# =========================================

post2021[
    "vab_growth_pct"
] = (

    post2021[
        "vab_agro_estimated"
    ]
    .pct_change()
    * 100

)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("POST-2021 AGRO VAB")
print("===================================\n")

print(

    post2021[[
        "year",
        "agro_index_norm",
        "vab_agro_estimated",
        "vab_growth_pct"
    ]]

)

# =========================================
# EXPORT
# =========================================

projection_file = os.path.join(
    EXPORT_PATH,
    "agro_vab_projection.csv"
)

post_file = os.path.join(
    EXPORT_PATH,
    "agro_vab_post2021.csv"
)

projection.to_csv(
    projection_file,
    index=False
)

post2021.to_csv(
    post_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(projection_file)
print(post_file)
