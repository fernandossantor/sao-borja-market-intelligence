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

# =========================================
# LOAD SIGNALS
# =========================================

signals = pd.read_csv(
    f"{EXPORT_PATH}/domain_signals.csv"
)

signals = signals[
    signals["category"] == "rais"
]

files = (
    signals[
        ["file_name", "full_path"]
    ]
    .drop_duplicates()
)

print("\n===================================")
print("RAIS DATASET PROFILER")
print("===================================\n")

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

        for ds in datasets[:20]:

            cols = (
                " | ".join(
                    map(
                        str,
                        ds["df"].columns
                    )
                )
            )

            results.append({

                "file_name":
                    file_name,

                "sheet":
                    ds["sheet"],

                "header":
                    ds["header"],

                "rows":
                    ds["rows"],

                "cols":
                    ds["cols"],

                "score":
                    ds["score"],

                "column_names":
                    cols[:1000]

            })

    except Exception as e:

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

out = os.path.join(
    EXPORT_PATH,
    "rais_dataset_profile.csv"
)

profile.to_csv(
    out,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(out)
