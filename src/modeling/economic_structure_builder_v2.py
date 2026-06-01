import pandas as pd
import os

print("\n===================================")
print("ECONOMIC STRUCTURE BUILDER V2")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# CARREGAR MASTER
# --------------------------------------------------

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_master_series_v2.csv"
    )
)

# --------------------------------------------------
# APENAS OBSERVADOS
# --------------------------------------------------

df = df[
    df["source"] == "observed"
].copy()

# --------------------------------------------------
# SHARES
# --------------------------------------------------

df["agro_share"] = (
    df["vab_agro"]
    /
    df["vab_total"]
    * 100
)

df["industry_share"] = (
    df["vab_industria"]
    /
    df["vab_total"]
    * 100
)

df["services_share"] = (
    df["vab_servicos"]
    /
    df["vab_total"]
    * 100
)

df["public_share"] = (
    df["vab_public"]
    /
    df["vab_total"]
    * 100
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

result = df[
    [
        "year",
        "agro_share",
        "industry_share",
        "services_share",
        "public_share"
    ]
]

print("\n===================================")
print("STRUCTURE V2")
print("===================================\n")

print(result.head())

print("\n===================================")
print("MÉDIAS HISTÓRICAS")
print("===================================\n")

print(
    result[
        [
            "agro_share",
            "industry_share",
            "services_share",
            "public_share"
        ]
    ].mean()
)

print("\n===================================")
print("ÚLTIMOS ANOS")
print("===================================\n")

print(result.tail())

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "economic_structure_v2.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
