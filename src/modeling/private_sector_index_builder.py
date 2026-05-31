import pandas as pd
import os

print("\n===================================")
print("PRIVATE SECTOR INDEX")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_sector_annual_panel.csv"
    )
)

BASE_YEAR = 2021

base = (
    df[
        df["year"] == BASE_YEAR
    ]
    .iloc[0]
)

df["empresas_norm"] = (
    df["empresas"] /
    base["empresas"]
) * 100

df["unidades_norm"] = (
    df["unidades_locais"] /
    base["unidades_locais"]
) * 100

df["emprego_norm"] = (
    df["emprego_total"] /
    base["emprego_total"]
) * 100

df["salarios_norm"] = (
    df["salarios_unidades"] /
    base["salarios_unidades"]
) * 100

df["private_index"] = (

    0.10 * df["empresas_norm"] +

    0.10 * df["unidades_norm"] +

    0.40 * df["emprego_norm"] +

    0.40 * df["salarios_norm"]

)

df["private_growth_pct"] = (
    df["private_index"]
    .pct_change()
    * 100
)

print("\n===================================")
print("PRIVATE INDEX")
print("===================================\n")

print(
    df[
        [
            "year",
            "private_index",
            "private_growth_pct"
        ]
    ]
)

export_file = os.path.join(
    EXPORT_PATH,
    "private_sector_index.csv"
)

df.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
