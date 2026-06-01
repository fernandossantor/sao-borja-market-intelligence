import pandas as pd
import numpy as np
import os

print("\n===================================")
print("ECONOMIC STRUCTURE BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

master = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_master_series.csv"
    )
)

# --------------------------------------------------
# APENAS ANOS OBSERVADOS
# --------------------------------------------------

observed = master[
    master["source"] == "observed"
].copy()

# --------------------------------------------------
# PARTICIPAÇÕES
# --------------------------------------------------

observed["agro_share"] = (
    observed["vab_agro"]
    /
    observed["vab_total"]
    * 100
)

observed["private_share"] = (
    observed["vab_private"]
    /
    observed["vab_total"]
    * 100
)

observed["public_share"] = (
    observed["vab_public"]
    /
    observed["vab_total"]
    * 100
)

result = observed[
    [
        "year",
        "agro_share",
        "private_share",
        "public_share"
    ]
]

print("\n===================================")
print("STRUCTURE")
print("===================================\n")

print(result.head())

print("\nÚltimos anos:")
print(result.tail())

print("\nMédias históricas:")

print(
    result[
        [
            "agro_share",
            "private_share",
            "public_share"
        ]
    ].mean()
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "economic_structure_long.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
