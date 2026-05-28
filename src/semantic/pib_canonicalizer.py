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
# LOAD FILES
# =========================================

pib_df = pd.read_csv(
    f"{EXPORT_PATH}/pib_consolidated.csv"
)

mapping_df = pd.read_csv(
    f"{EXPORT_PATH}/pib_semantic_mapping.csv"
)

print("\n===================================")
print("FILES LOADED")
print("===================================\n")

print(f"PIB linhas: {len(pib_df)}")
print(f"PIB colunas: {len(pib_df.columns)}")

# =========================================
# VALID DOMAINS
# =========================================

valid_mapping = mapping_df[
    ~mapping_df["economic_domain"].isin([
        "structural_noise",
        "unmapped"
    ])
]

print("\n===================================")
print("VALID ECONOMIC DOMAINS")
print("===================================\n")

print(valid_mapping)

# =========================================
# RENAME MAP
# =========================================

rename_dict = {}

for _, row in valid_mapping.iterrows():

    rename_dict[
        row["column_name"]
    ] = row["economic_domain"]

# =========================================
# SELECT COLUMNS
# =========================================

canonical_df = pib_df[
    rename_dict.keys()
].copy()

# =========================================
# RENAME
# =========================================

canonical_df = canonical_df.rename(
    columns=rename_dict
)

# =========================================
# REMOVE DUPLICATES
# =========================================

canonical_df = canonical_df.drop_duplicates()

# =========================================
# SORT
# =========================================

if "year" in canonical_df.columns:

    canonical_df = canonical_df.sort_values(
        by="year"
    )

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("CANONICAL DATASET")
print("===================================\n")

print(canonical_df.head())

print("\nShape:")
print(canonical_df.shape)

print("\nColunas:")
print(canonical_df.columns.tolist())

# =========================================
# EXPORT
# =========================================

export_path = os.path.join(
    EXPORT_PATH,
    "pib_canonical.csv"
)

canonical_df.to_csv(
    export_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_path)
