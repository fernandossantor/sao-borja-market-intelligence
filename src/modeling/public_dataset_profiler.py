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

from loaders.smart_csv_loader import (
    load_csv_smart
)

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

TARGET_DOMAINS = [
    "fiscal",
    "institutional",
    "social"
]

# =========================================
# LOAD
# =========================================

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

inventory = inventory[
    inventory["category"]
    .isin(TARGET_DOMAINS)
].copy()

print("\n===================================")
print("PUBLIC DATASET PROFILER")
print("===================================\n")

print(
    f"Arquivos analisados: "
    f"{len(inventory)}"
)

# =========================================
# YEAR DETECTOR
# =========================================

def detect_years(df):

    years = []

    for col in df.columns:

        try:

            values = pd.to_numeric(
                df[col],
                errors="coerce"
            )

            valid = values[
                (values >= 1900)
                &
                (values <= 2100)
            ]

            years.extend(
                valid.tolist()
            )

        except:
            pass

    years = list(set(years))

    if len(years) == 0:
        return None, None

    return (
        int(min(years)),
        int(max(years))
    )

# =========================================
# PROCESS
# =========================================

results = []

for _, row in inventory.iterrows():

    file_name = row["file_name"]
    category = row["category"]
    full_path = row["full_path"]

    print(
        f"\nAnalisando: {file_name}"
    )

    datasets = []

    try:

        if (
            file_name.lower().endswith(".csv")
        ):

            df = load_csv_smart(
                full_path
            )

            datasets = [{

                "sheet": "csv",
                "header": 0,
                "rows": len(df),
                "cols": len(df.columns),
                "score": len(df),
                "df": df

            }]

        else:

            datasets = extract_datasets(
                full_path
            )

    except Exception as e:

        print(
            f"[ERRO] {file_name}"
        )

        print(e)

        continue

    for ds in datasets[:10]:

        df = ds["df"]

        start_year, end_year = (
            detect_years(df)
        )

        cols = " | ".join(
            map(
                str,
                df.columns[:20]
            )
        )

        results.append({

            "category":
                category,

            "file_name":
                file_name,

            "sheet":
                ds["sheet"],

            "rows":
                ds["rows"],

            "cols":
                ds["cols"],

            "start_year":
                start_year,

            "end_year":
                end_year,

            "column_names":
                cols

        })

# =========================================
# OUTPUT
# =========================================

profile = pd.DataFrame(
    results
)

print("\n===================================")
print("PROFILE")
print("===================================\n")

print(
    profile.head(100)
)

print(
    f"\nDatasets: {len(profile)}"
)

# =========================================
# SUMMARY
# =========================================

summary = (

    profile

    .groupby(
        "category"
    )

    .size()

    .reset_index(
        name="datasets"
    )

)

print("\n===================================")
print("SUMMARY")
print("===================================\n")

print(summary)

# =========================================
# EXPORT
# =========================================

profile_file = os.path.join(
    EXPORT_PATH,
    "public_dataset_profile.csv"
)

summary_file = os.path.join(
    EXPORT_PATH,
    "public_dataset_summary.csv"
)

profile.to_csv(
    profile_file,
    index=False
)

summary.to_csv(
    summary_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(profile_file)
print(summary_file)
