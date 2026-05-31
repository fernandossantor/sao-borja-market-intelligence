import pandas as pd
import os

print("\n===================================")
print("PRIVATE SECTOR ANNUAL BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

master = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_sector_master_panel.csv"
    )
)

annual = (
    master
    .groupby("year")
    [
        [
            "empresas",
            "unidades_locais",
            "emprego_total",
            "emprego_assalariado_empresas",
            "emprego_assalariado_unidades",
            "salarios_empresas",
            "salarios_unidades"
        ]
    ]
    .sum()
    .reset_index()
)

print("\n===================================")
print("ANNUAL PANEL")
print("===================================\n")

print(annual)

print("\nShape:")
print(annual.shape)

export_file = os.path.join(
    EXPORT_PATH,
    "private_sector_annual_panel.csv"
)

annual.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
