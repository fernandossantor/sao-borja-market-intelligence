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
BASE_VAB = 351229400

# =========================================
# LOAD
# =========================================

df = pd.read_csv(
    f"{EXPORT_PATH}/public_structural_index_v2.csv"
)

print("\n===================================")
print("PUBLIC VAB PROJECTION")
print("===================================\n")

print(
    f"VAB Público {BASE_YEAR}: "
    f"R$ {BASE_VAB:,.2f}"
)

# =========================================
# BASE INDEX
# =========================================

base_index = float(

    df.loc[
        df["year"] == BASE_YEAR,
        "public_structural_index"
    ].iloc[0]

)

# =========================================
# PROJECTION
# =========================================

df["public_index_norm"] = (

    df["public_structural_index"]
    /
    base_index
    * 100

)

df["vab_public_estimated"] = (

    BASE_VAB
    *
    df["public_index_norm"]
    / 100

)

df["vab_growth_pct"] = (

    df["vab_public_estimated"]
    .pct_change()
    * 100

)

# =========================================
# POST 2021
# =========================================

post = df[
    (df["year"] >= 2021)
    &
    (df["year"] <= 2025)
].copy()

print("\n===================================")
print("POST-2021 PUBLIC VAB")
print("===================================\n")

print(

    post[
        [
            "year",
            "public_index_norm",
            "vab_public_estimated",
            "vab_growth_pct"
        ]
    ]

)

# =========================================
# EXPORT
# =========================================

file_all = os.path.join(
    EXPORT_PATH,
    "public_vab_projection.csv"
)

file_post = os.path.join(
    EXPORT_PATH,
    "public_vab_post2021.csv"
)

df.to_csv(
    file_all,
    index=False
)

post.to_csv(
    file_post,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(file_all)
print(file_post)
