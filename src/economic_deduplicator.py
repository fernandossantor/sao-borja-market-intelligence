import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

INPUT_FILE = os.path.join(
    EXPORT_PATH,
    "pib_canonical.csv"
)

# =========================================
# LOAD
# =========================================

df = pd.read_csv(INPUT_FILE)

print("\n===================================")
print("CANONICAL DATASET LOADED")
print("===================================\n")

print(df.shape)

# =========================================
# SORT BY COMPLETENESS
# =========================================

df["_non_null_count"] = df.notna().sum(axis=1)

df = df.sort_values(
    by="_non_null_count",
    ascending=False
)

# =========================================
# GROUP KEYS
# =========================================

group_keys = [
    "year",
    "municipality",
    "ibge_code"
]

# =========================================
# MERGE DUPLICATES
# =========================================

merged_rows = []

for keys, group in df.groupby(group_keys):

    merged = {}

    # KEEP GROUP KEYS
    for idx, key in enumerate(group_keys):
        merged[key] = keys[idx]

    # MERGE REMAINING COLUMNS
    for col in df.columns:

        if col in group_keys:
            continue

        if col == "_non_null_count":
            continue

        values = group[col].dropna()

        if len(values) > 0:

            merged[col] = values.iloc[0]

        else:

            merged[col] = None

    merged_rows.append(merged)

# =========================================
# FINAL DF
# =========================================

dedup_df = pd.DataFrame(merged_rows)

# =========================================
# SORT
# =========================================

dedup_df = dedup_df.sort_values(
    by="year"
)

# =========================================
# VALIDATION
# =========================================

duplicates = dedup_df.duplicated(
    subset=group_keys
).sum()

print("\n===================================")
print("DEDUP VALIDATION")
print("===================================\n")

print(f"Duplicatas restantes: {duplicates}")

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("DEDUPLICATED DATASET")
print("===================================\n")

print(dedup_df.head(20))

print("\nShape:")
print(dedup_df.shape)

# =========================================
# EXPORT
# =========================================

output_path = os.path.join(
    EXPORT_PATH,
    "pib_deduplicated.csv"
)

dedup_df.to_csv(
    output_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(output_path)
