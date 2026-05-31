import pandas as pd
import os
import sys

# =========================================
# PROJECT ROOT
# =========================================

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

files = (

    inventory[
        inventory["category"] == "rais"
    ]

    [
        [
            "file_name",
            "full_path"
        ]
    ]

    .drop_duplicates()

)

print("\n===================================")
print("RAIS DATASET PROFILER")
print("===================================\n")

print(
    f"Arquivos RAIS encontrados: "
    f"{len(files)}"
)

# =========================================
# PROFILE
# =========================================

results = []

for _, row in files.iterrows():

    file_name = row["file_name"]
    full_path = row["full_path"]

    print("\n-----------------------------------")
    print(file_name)
    print("-----------------------------------")

    try:

        datasets = extract_datasets(
            full_path
        )

        print(
            f"Datasets encontrados: "
            f"{len(datasets)}"
        )

        for ds in datasets[:20]:

            df = ds["df"]

            cols = " | ".join(
                map(
                    str,
                    df.columns
                )
            )

            results.append({

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

                "column_names":
                    cols[:2000]

            })

    except Exception as e:

        print(
            f"[ERRO] {file_name}"
        )

        print(e)

# =========================================
# OUTPUT
# =========================================

profile = pd.DataFrame(
    results
)

print("\n===================================")
print("TOP DATASETS")
print("===================================\n")

print(

    profile[
        [
            "file_name",
            "sheet",
            "header",
            "rows",
            "cols"
        ]
    ]

    .head(100)

)

# =========================================
# EXPORT
# =========================================

output_file = os.path.join(
    EXPORT_PATH,
    "rais_dataset_profile.csv"
)

profile.to_csv(
    output_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(output_file)
