import pandas as pd
from pathlib import Path
import os

print("\n===================================")
print("FISCAL INVENTORY BUILDER")
print("===================================\n")

RAW_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/fiscal"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# LEITOR ROBUSTO
# --------------------------------------------------

def read_fiscal_file(path):

    tests = [
        ("utf-8-sig", ";"),
        ("latin1", ";"),
        ("cp1252", ";"),
        ("utf-8-sig", "\t"),
        ("latin1", "\t"),
        ("cp1252", "\t")
    ]

    for enc, sep in tests:

        try:

            df = pd.read_csv(
                path,
                encoding=enc,
                sep=sep,
                engine="python"
            )

            if len(df.columns) > 3:
                return df

        except:
            pass

    raise ValueError(path)

# --------------------------------------------------
# INVENTÁRIO
# --------------------------------------------------

rows = []

for file in sorted(Path(RAW_PATH).glob("*.csv")):

    try:

        df = read_fiscal_file(file)

        rows.append([
            file.name,
            len(df),
            len(df.columns),
            "ok"
        ])

    except:

        rows.append([
            file.name,
            None,
            None,
            "erro"
        ])

inventory = pd.DataFrame(
    rows,
    columns=[
        "file",
        "rows",
        "columns",
        "status"
    ]
)

print(inventory)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_inventory.csv"
)

inventory.to_csv(
    export_file,
    index=False
)

print("\nExportado:")
print(export_file)
