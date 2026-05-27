import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

PIB_FILE = os.path.join(
    EXPORT_PATH,
    "pib_consolidated.csv"
)

MAPPING_FILE = os.path.join(
    EXPORT_PATH,
    "pib_semantic_mapping.csv"
)

# =========================================
# LOAD FILES
# =========================================

pib_df = pd.read_csv(PIB_FILE)

mapping_df = pd.read_csv(MAPPING_FILE)

print("\n===================================")
print("FILES LOADED")
print("===================================\n")

print(f"PIB linhas: {len(pib_df)}")
print(f"PIB colunas: {len(pib_df.columns)}")

# =========================================
# VALID DOMAINS
# =========================================

valid_domains = [
    "year",
    "municipality",
    "ibge_code",
    "pib_total",
    "pib_per_capita",
    "vab_agro",
    "vab_industria",
    "vab_servicos",
    "vab_publico",
    "vab_total",
    "taxes"
]

valid_mapping = mapping_df[
    mapping_df["economic_domain"]
    .isin(valid_domains)
]

print("\n===================================")
print("VALID ECONOMIC DOMAINS")
print("===================================\n")

print(valid_mapping)

# =========================================
# COLUMN RENAMING
# =========================================

rename_dict = {}

selected_columns = []

for _, row in valid_mapping.iterrows():

    original_col = row["column_name"]

    canonical_name = row["economic_domain"]

    rename_dict[original_col] = canonical_name

    selected_columns.append(original_col)

# =========================================
# BUILD CANONICAL DF
# =========================================

canonical_df = pib_df[
    selected_columns
].copy()

canonical_df = canonical_df.rename(
    columns=rename_dict
)

# =========================================
# REMOVE DUPLICATED COLUMNS
# =========================================

canonical_df = canonical_df.loc[
    :,
    ~canonical_df.columns.duplicated()
]

# =========================================
# TYPE STANDARDIZATION
# =========================================

numeric_columns = [
    "year",
    "ibge_code",
    "pib_total",
    "pib_per_capita",
    "vab_agro",
    "vab_industria",
    "vab_servicos",
    "vab_publico",
    "vab_total",
    "taxes"
]

for col in numeric_columns:

    if col in canonical_df.columns:

        canonical_df[col] = pd.to_numeric(
            canonical_df[col],
            errors="coerce"
        )

# =========================================
# REMOVE EMPTY ROWS
# =========================================

canonical_df = canonical_df.dropna(
    how="all"
)

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

output_path = os.path.join(
    EXPORT_PATH,
    "pib_canonical.csv"
)

canonical_df.to_csv(
    output_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(output_path)
