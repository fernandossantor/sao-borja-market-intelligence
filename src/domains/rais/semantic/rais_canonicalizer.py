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
print("RAIS CONSOLIDATED LOADED")
print("===================================\n")

print(df.shape)

# =========================================
# COLUMN MAPPING
# =========================================

COLUMN_MAP = {

    # ================================
    # CNAE
    # ================================

    "CNAE 2.0 Classe - Código":
        "cnae_class",

    "CNAE 2.0 Subclasse - Código":
        "cnae_subclass",

    # ================================
    # TERRITORIAL
    # ================================

    "Município - Código":
        "municipality_code",

    "Município Trab - Código":
        "work_municipality_code",

    # ================================
    # DEMOGRAPHICS
    # ================================

    "Sexo - Código":
        "gender",

    "Raça Cor - Código":
        "race",

    "Idade":
        "age",

    "Escolaridade Após 2005 - Código":
        "education_level",

    "Nacionalidade - Código":
        "nationality",

    # ================================
    # EMPLOYMENT
    # ================================

    "Tempo Emprego":
        "tenure",

    "Tipo Vínculo - Código":
        "employment_type",

    "Tipo Admissão Trabalhador - Código":
        "admission_type",

    "Ind Vínculo Ativo 31/12 - Código":
        "active_link",

    # ================================
    # WAGES
    # ================================

    "Vl Rem Média Nom":
        "avg_salary",

    "Vl Rem Dezembro Nom":
        "dec_salary",

    "Vl Rem Média (SM)":
        "avg_salary_sm",

    "Vl Rem Dezembro (SM)":
        "dec_salary_sm",

    # ================================
    # HOURS
    # ================================

    "Qtd Hora Contr":
        "contracted_hours",

    # ================================
    # ESTABLISHMENT
    # ================================

    "Tamanho Estabelecimento - Código":
        "establishment_size",

    "Tipo Estabelecimento - Nome":
        "establishment_type"

}

# =========================================
# VALID COLUMNS
# =========================================

valid_columns = []

for original_col in COLUMN_MAP.keys():

    if original_col in df.columns:

        valid_columns.append(
            original_col
        )

print("\n===================================")
print("VALID COLUMNS")
print("===================================\n")

print(valid_columns)

# =========================================
# FILTER
# =========================================

canonical_df = df[
    valid_columns
].copy()

# =========================================
# RENAME
# =========================================

rename_dict = {}

for col in valid_columns:

    rename_dict[col] = COLUMN_MAP[col]

canonical_df = canonical_df.rename(
    columns=rename_dict
)

# =========================================
# NUMERIC CONVERSION
# =========================================

numeric_cols = [

    "age",
    "tenure",
    "avg_salary",
    "dec_salary",
    "avg_salary_sm",
    "dec_salary_sm",
    "contracted_hours"

]

for col in numeric_cols:

    if col in canonical_df.columns:

        canonical_df[col] = (
            canonical_df[col]
            .astype(str)
            .str.replace("R$", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.strip()
        )

        canonical_df[col] = pd.to_numeric(
            canonical_df[col],
            errors="coerce"
        )

# =========================================
# DROP EMPTY
# =========================================

canonical_df = canonical_df.dropna(
    how="all"
)

# =========================================
# REMOVE DUPLICATES
# =========================================

canonical_df = canonical_df.drop_duplicates()

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("RAIS CANONICAL DATASET")
print("===================================\n")

print(canonical_df.head())

print("\nShape:")
print(canonical_df.shape)

print("\nColumns:")
print(canonical_df.columns.tolist())

# =========================================
# EXPORT
# =========================================

export_path = os.path.join(
    EXPORT_PATH,
    "rais_canonical.csv"
)

canonical_df.to_csv(
    export_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_path)
