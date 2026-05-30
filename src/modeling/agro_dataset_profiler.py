import pandas as pd
import os
import sys

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

RAW_AGRO = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/agro"
)

# =========================================
# LOAD INVENTORY
# =========================================

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

agro_files = inventory[
    inventory["category"] == "agro"
]

print("\n===================================")
print("AGRO DATASET PROFILER")
print("===================================\n")

rows = []

# =========================================
# YEAR DETECTOR
# =========================================

def detect_years(df):

    years = []

    for col in df.columns:

        try:

            vals = pd.to_numeric(
                df[col],
                errors="coerce"
            )

            vals = vals[
                (vals >= 1900)
                &
                (vals <= 2100)
            ]

            years.extend(
                vals.tolist()
            )

        except:
            pass

    if len(years) == 0:
        return None, None

    return int(min(years)), int(max(years))

# =========================================
# PROCESS
# =========================================

for _, row in agro_files.iterrows():

    file_name = row["file_name"]
    full_path = row["full_path"]

    print("\n-----------------------------------")
    print(file_name)
    print("-----------------------------------")

    try:

        datasets = extract_datasets(
            full_path
        )

        for ds in datasets[:20]:

            df = ds["df"]

            start_year, end_year = (
                detect_years(df)
            )

            if start_year is None:
                continue

            rows.append({

                "file_name":
                    file_name,

                "sheet":
                    ds["sheet"],

                "header":
                    ds["header"],

                "rows":
                    len(df),

                "cols":
                    len(df.columns),

                "start_year":
                    start_year,

                "end_year":
                    end_year,

                "column_names":
                    " | ".join(
                        map(
                            str,
                            df.columns[:15]
                        )
                    )

            })

    except Exception as e:

        print(e)

# =========================================
# OUTPUT
# =========================================

profile = pd.DataFrame(rows)

print("\n===================================")
print("VALID ECONOMIC DATASETS")
print("===================================\n")

print(profile)

# =========================================
# EXPORT
# =========================================

export_file = os.path.join(
    EXPORT_PATH,
    "agro_dataset_profile.csv"
)

profile.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
