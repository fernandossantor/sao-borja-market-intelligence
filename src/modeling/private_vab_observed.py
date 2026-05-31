import pandas as pd
import os

print("\n===================================")
print("PRIVATE VAB OBSERVED")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "pib_canonical.csv"
    )
)

df["vab_private"] = (
    df["vab_industria"]
    +
    df["vab_servicos"]
)

df["private_share_pct"] = (
    df["vab_private"]
    /
    df["vab_total"]
    * 100
)

result = df[
    [
        "year",
        "vab_private",
        "private_share_pct"
    ]
].copy()

print(result.tail(10))

export_file = os.path.join(
    EXPORT_PATH,
    "private_vab_observed.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
