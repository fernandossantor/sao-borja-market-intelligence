import pandas as pd
import os
import sys
import re

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
print("RAIS TIMESERIES SCANNER V2")
print("===================================\n")

results = []

# =====================================
# SCAN
# =====================================

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

            blob = " ".join(
                map(
                    str,
                    df.head(200)
                    .astype(str)
                    .values
                    .flatten()
                )
            )

            years = set()

            for year in re.findall(
                r"(19\d{2}|20\d{2})",
                blob
            ):

                y = int(year)

                if (
                    y >= 1980
                    and y <= 2035
                ):
                    years.add(y)

            if len(years) < 5:
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

    except Exception as e:

        print(e)

# =====================================
# OUTPUT
# =====================================

if len(results) == 0:

    print(
        "\nNenhum dataset temporal encontrado."
    )

    raise SystemExit()

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

print(
    result.head(100)
)

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
