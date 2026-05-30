import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# LOAD
# =========================================

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

signals = pd.read_csv(
    f"{EXPORT_PATH}/domain_signals.csv"
)

print("\n===================================")
print("DOMAIN COVERAGE AUDIT")
print("===================================\n")

# =========================================
# INVENTORY COUNTS
# =========================================

inventory_summary = (

    inventory
    .groupby("category")
    .agg({
        "file_name":"nunique"
    })
    .reset_index()

)

inventory_summary.columns = [
    "category",
    "inventory_files"
]

# =========================================
# DETECTED COUNTS
# =========================================

detected_summary = (

    signals
    .groupby("category")
    .agg({
        "file_name":"nunique"
    })
    .reset_index()

)

detected_summary.columns = [
    "category",
    "detected_files"
]

# =========================================
# MERGE
# =========================================

coverage = pd.merge(
    inventory_summary,
    detected_summary,
    on="category",
    how="left"
)

coverage["detected_files"] = (
    coverage["detected_files"]
    .fillna(0)
    .astype(int)
)

coverage["missing_files"] = (
    coverage["inventory_files"]
    - coverage["detected_files"]
)

coverage["coverage_pct"] = (

    coverage["detected_files"]
    /
    coverage["inventory_files"]

) * 100

coverage = coverage.sort_values(
    "coverage_pct",
    ascending=False
)

# =========================================
# MISSING FILES
# =========================================

detected_pairs = set(

    zip(
        signals["category"],
        signals["file_name"]
    )

)

missing_rows = []

for _, row in inventory.iterrows():

    pair = (
        row["category"],
        row["file_name"]
    )

    if pair not in detected_pairs:

        missing_rows.append({

            "category":
                row["category"],

            "file_name":
                row["file_name"],

            "full_path":
                row["full_path"]

        })

missing_df = pd.DataFrame(
    missing_rows
)

# =========================================
# MISSING BY DOMAIN
# =========================================

missing_summary = (

    missing_df
    .groupby("category")
    .size()
    .reset_index(
        name="missing_files"
    )

)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("COVERAGE SUMMARY")
print("===================================\n")

print(
    coverage
)

print("\n===================================")
print("MISSING FILES BY DOMAIN")
print("===================================\n")

print(
    missing_summary
)

print("\n===================================")
print("FIRST 50 MISSING FILES")
print("===================================\n")

print(
    missing_df.head(50)
)

# =========================================
# EXPORTS
# =========================================

coverage_file = os.path.join(
    EXPORT_PATH,
    "domain_coverage_summary.csv"
)

missing_file = os.path.join(
    EXPORT_PATH,
    "domain_missing_files.csv"
)

coverage.to_csv(
    coverage_file,
    index=False
)

missing_df.to_csv(
    missing_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(coverage_file)
print(missing_file)
