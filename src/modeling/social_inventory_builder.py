import pandas as pd
from pathlib import Path
import os

print("\n===================================")
print("SOCIAL INVENTORY BUILDER")
print("===================================\n")

RAW_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/social"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

records = []

for file in sorted(Path(RAW_PATH).glob("*")):

    try:

        if file.suffix.lower() == ".csv":

            df = pd.read_csv(
                file,
                encoding="utf-8",
                sep=None,
                engine="python"
            )

        elif file.suffix.lower() in [
            ".xlsx",
            ".xls"
        ]:

            df = pd.read_excel(file)

        else:

            continue

        records.append(
            {
                "file": file.name,
                "extension": file.suffix,
                "rows": len(df),
                "columns": len(df.columns),
                "status": "ok"
            }
        )

    except Exception as e:

        records.append(
            {
                "file": file.name,
                "extension": file.suffix,
                "rows": None,
                "columns": None,
                "status": str(type(e).__name__)
            }
        )

inventory = pd.DataFrame(records)

print(inventory)

export_file = os.path.join(
    EXPORT_PATH,
    "social_inventory.csv"
)

inventory.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
