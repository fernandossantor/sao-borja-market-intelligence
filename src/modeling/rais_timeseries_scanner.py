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

# =====================================
# CONFIG
# =====================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

files = inventory[
    inventory["category"] == "rais"
]

print("\n===================================")
print("RAIS TIMESERIES SCANNER")
print("===================================\n")

results = []

for _, row in files.iterrows():

    file_name = row["file_name"]
    full_path = row["full_path"]

    print(file_name)

    try:

        datasets = extract_datasets(
            full_path
        )

        for ds in datasets[:50]:

            df = ds["df"]

            years = []

            for col in df.columns:

                try:

                    val = int(col)

                    if (
                        val >= 1980
                        and val <= 2035
                    ):
                        years.append(val)

                except:
                    pass

            if len(years) < 3:
                continue

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

                "years_found":
                    len(years),

                "start_year":
                    min(years),

                "end_year":
                    max(years)

            })

    except Exception:

        continue

# =====================================
# OUTPUT
# =====================================

result = pd.DataFrame(
    results
)

result = result.sort_values(
    [
        "years_found",
        "rows"
    ],
    ascending=False
)

print("\n===================================")
print("TOP TIMESERIES DATASETS")
print("===================================\n")

print(result.head(100))

# =====================================
# EXPORT
# =====================================

out = os.path.join(
    EXPORT_PATH,
    "rais_timeseries_scan.csv"
)

result.to_csv(
    out,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(out)
