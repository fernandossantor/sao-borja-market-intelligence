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
# FIRST COLUMN
# =========================================

first_col = df.columns[0]

print("\n===================================")
print("FIRST COLUMN")
print("===================================\n")

print(first_col)

# =========================================
# NORMALIZATION
# =========================================

records = []

for idx, row in df.iterrows():

    try:

        cnae_value = str(row[first_col]).strip()

        # =================================
        # SKIP INVALID
        # =================================

        if (
            cnae_value == "nan"
            or cnae_value == ""
            or "fonte" in cnae_value.lower()
            or "são borja" in cnae_value.lower()
            or "unnamed" in cnae_value.lower()
        ):
            continue

        # =================================
        # FIND NUMERIC VALUES
        # =================================

        numeric_candidates = []

        for value in row.values:

            try:

                numeric = pd.to_numeric(
                    value,
                    errors="coerce"
                )

                if pd.notna(numeric):

                    numeric_candidates.append(
                        float(numeric)
                    )

            except:
                continue

        # =================================
        # NO NUMBERS
        # =================================

        if len(numeric_candidates) == 0:
            continue

        # =================================
        # STORE
        # =================================

        records.append({

            "cnae": cnae_value,
            "value": max(numeric_candidates)

        })

    except:
        continue

# =========================================
# BUILD DATAFRAME
# =========================================

normalized_df = pd.DataFrame(records)

# =========================================
# EMPTY CHECK
# =========================================

if len(normalized_df) == 0:

    raise Exception(
        "Nenhum registro econômico encontrado."
    )

# =========================================
# CLEAN
# =========================================

normalized_df = normalized_df.drop_duplicates()

normalized_df = normalized_df.dropna()

normalized_df["cnae"] = (
    normalized_df["cnae"]
    .astype(str)
    .str.strip()
)

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
