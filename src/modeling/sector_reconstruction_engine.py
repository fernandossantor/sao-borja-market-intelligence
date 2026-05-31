import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

print("\n===================================")
print("SECTOR RECONSTRUCTION ENGINE")
print("===================================\n")

# =========================================
# LOAD
# =========================================

agro = pd.read_csv(
    f"{EXPORT_PATH}/agro_vab_projection.csv"
)

public = pd.read_csv(
    f"{EXPORT_PATH}/public_vab_projection.csv"
)

# =========================================
# SELECT
# =========================================

agro = agro[
    [
        "year",
        "vab_agro_estimated"
    ]
].copy()

public = public[
    [
        "year",
        "vab_public_estimated"
    ]
].copy()

# =========================================
# MERGE
# =========================================

df = pd.merge(
    agro,
    public,
    on="year",
    how="outer"
)

df = df.sort_values(
    "year"
)

# =========================================
# TOTAL
# =========================================

df["vab_reconstructed"] = (

    df["vab_agro_estimated"]
    .fillna(0)

    +

    df["vab_public_estimated"]
    .fillna(0)

)

# =========================================
# GROWTH
# =========================================

df["growth_pct"] = (

    df["vab_reconstructed"]

    .pct_change()

    * 100

)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("RECONSTRUCTED VAB")
print("===================================\n")

print(df)

# =========================================
# EXPORT
# =========================================

output = os.path.join(
    EXPORT_PATH,
    "sector_reconstruction.csv"
)

df.to_csv(
    output,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(output)
