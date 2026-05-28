import pandas as pd
import numpy as np
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

df = pd.read_csv(
    f"{EXPORT_PATH}/rais_consolidated.csv",
    low_memory=False
)

print("\n===================================")
print("RAIS RAW LOADED")
print("===================================\n")

print(df.shape)

# =========================================
# DETECT CNAE COLUMN
# =========================================

first_col = df.columns[0]

print("\n===================================")
print("FIRST COLUMN")
print("===================================\n")

print(first_col)

# =========================================
# KEEP VALID ROWS
# =========================================

valid_rows = []

for idx, row in df.iterrows():

    value = str(row[first_col])

    # ================================
    # REMOVE NOISE
    # ================================

    if (
        value == "nan"
        or "fonte" in value.lower()
        or "são borja" in value.lower()
        or "unnamed" in value.lower()
    ):
        continue

    # ================================
    # KEEP ECONOMIC ROWS
    # ================================

    numeric_values = pd.to_numeric(
        row,
        errors="coerce"
    )

    numeric_count = numeric_values.notna().sum()

    if numeric_count > 0:

        valid_rows.append({

            "cnae": value,
            "value": numeric_values.max()

        })

# =========================================
# CLEAN DATAFRAME
# =========================================

normalized_df = pd.DataFrame(valid_rows)

# =========================================
# CLEAN CNAE
# =========================================

normalized_df["cnae"] = (
    normalized_df["cnae"]
    .astype(str)
    .str.strip()
)

# =========================================
# REMOVE DUPLICATES
# =========================================

normalized_df = normalized_df.drop_duplicates()

# =========================================
# REMOVE EMPTY
# =========================================

normalized_df = normalized_df.dropna()

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("NORMALIZED RAIS")
print("===================================\n")

print(normalized_df.head(30))

print("\nShape:")
print(normalized_df.shape)

# =========================================
# EXPORT
# =========================================

export_path = os.path.join(
    EXPORT_PATH,
    "rais_normalized.csv"
)

normalized_df.to_csv(
    export_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_path)
