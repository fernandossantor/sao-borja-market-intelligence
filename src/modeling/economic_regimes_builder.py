import pandas as pd
import os

print("\n===================================")
print("ECONOMIC REGIMES BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_structure_long.csv"
    )
)

# --------------------------------------------------
# CLASSIFICAÇÃO
# --------------------------------------------------

def classify(row):

    agro = row["agro_share"]
    private = row["private_share"]
    public = row["public_share"]

    if agro >= 30:
        return "Agro Boom"

    if agro >= 25:
        return "Agro Forte"

    if private >= 80:
        return "Economia Privada Forte"

    if public >= 18:
        return "Dependência Pública"

    return "Equilíbrio"

df["regime"] = df.apply(
    classify,
    axis=1
)

# --------------------------------------------------
# RESULTADOS
# --------------------------------------------------

print("\n===================================")
print("REGIMES")
print("===================================\n")

print(
    df[
        [
            "year",
            "agro_share",
            "private_share",
            "public_share",
            "regime"
        ]
    ]
)

print("\n===================================")
print("DISTRIBUIÇÃO")
print("===================================\n")

print(
    df["regime"]
    .value_counts()
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "economic_regimes.csv"
)

df.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
