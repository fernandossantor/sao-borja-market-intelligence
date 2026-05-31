import pandas as pd
import os

print("\n===================================")
print("POST 2021 PRIVATE AUDIT")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

files = [
    "rais_6449_panel.csv",
    "rais_6450_panel.csv",
    "private_sector_master_panel.csv",
    "private_sector_annual_panel.csv",
    "rais_canonical.csv",
    "rais_consolidated.csv"
]

for f in files:

    path = os.path.join(EXPORT_PATH, f)

    if not os.path.exists(path):
        continue

    print("\n===================================")
    print(f)
    print("===================================\n")

    try:

        df = pd.read_csv(path)

        print("Shape:")
        print(df.shape)

        print("\nColunas:")
        print(df.columns.tolist())

        if "year" in df.columns:

            print("\nAnos:")
            print(
                sorted(
                    df["year"]
                    .dropna()
                    .unique()
                )[-15:]
            )

    except Exception as e:

        print(e)
