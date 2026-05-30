import pandas as pd
import numpy as np
import sys
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(__file__)
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from loaders.smart_dataset_extractor import (
    extract_datasets
)

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# LOAD INVENTORY
# =========================================

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

print("\n===================================")
print("DOMAIN SIGNAL INVENTORY")
print("===================================\n")

print(
    f"Arquivos encontrados: "
    f"{len(inventory)}"
)

# =========================================
# YEAR DETECTOR
# =========================================

def detect_year_range(df):

    years = []

    for col in df.columns:

        try:

            numeric = pd.to_numeric(
                df[col],
                errors="coerce"
            )

            valid = numeric[
                (numeric >= 1900)
                &
                (numeric <= 2100)
            ]

            years.extend(
                valid.tolist()
            )

        except Exception:

            pass

    if len(years) == 0:

        return None, None

    return (
        int(min(years)),
        int(max(years))
    )

# =========================================
# PROCESS FILES
# =========================================

signals = []

for _, row in inventory.iterrows():

    category = row["category"]
    file_name = row["file_name"]
    full_path = row["full_path"]

    ext = str(file_name).lower()

    from loaders.smart_csv_loader import (
    load_csv_smart
    )

    # EXCEL
if (
    ext.endswith(".xlsx")
    or ext.endswith(".xls")
    ):

    datasets = extract_datasets(
        full_path
    )

    # CSV
elif ext.endswith(".csv"):

    try:

        df = load_csv_smart(
            full_path
        )

        datasets = [{
            "sheet": "csv",
            "header": 0,
            "score": len(df),
            "rows": len(df),
            "cols": len(df.columns),
            "df": df
        }]

    except Exception as e:

        print(e)
        continue

    else:

    continue

    print("\n-----------------------------------")
    print(file_name)
    print("-----------------------------------")

    try:

        datasets = extract_datasets(
            full_path
        )

        print(
            f"datasets encontrados: "
            f"{len(datasets)}"
        )

        for ds in datasets[:20]:

            df = ds["df"]

            start_year, end_year = (
                detect_year_range(df)
            )

            signals.append({

                "category":
                    category,

                "file_name":
                    file_name,

                "sheet":
                    ds["sheet"],

                "header":
                    ds["header"],

                "score":
                    round(
                        ds["score"],
                        2
                    ),

                "rows":
                    ds["rows"],

                "cols":
                    ds["cols"],

                "start_year":
                    start_year,

                "end_year":
                    end_year,

                "column_names":
                    " | ".join(
                        map(
                            str,
                            df.columns[:20]
                        )
                    )

            })

    except Exception as e:

        print(
            f"[ERRO] {file_name}"
        )

        print(e)

# =========================================
# OUTPUT
# =========================================

signals_df = pd.DataFrame(
    signals
)

print("\n===================================")
print("SIGNALS INVENTORIED")
print("===================================\n")

print(
    signals_df.head(30)
)

print(
    f"\nTotal sinais: "
    f"{len(signals_df)}"
)

# =========================================
# EXPORT
# =========================================

export_file = os.path.join(
    EXPORT_PATH,
    "domain_signals.csv"
)

signals_df.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
