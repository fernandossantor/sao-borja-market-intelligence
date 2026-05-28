%%writefile src/domains/rais/semantic/rais_semantic_mapper.py

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
# LOAD RAIS
# =========================================

rais_df = pd.read_csv(
    f"{EXPORT_PATH}/rais_consolidated.csv"
)

print("\n===================================")
print("RAIS CONSOLIDATED LOADED")
print("===================================\n")

print(f"Linhas: {len(rais_df)}")
print(f"Colunas: {len(rais_df.columns)}")

# =========================================
# DOMAIN RULES
# =========================================

DOMAIN_RULES = {

    "year": [
        "ano"
    ],

    "municipality": [
        "município",
        "municipio"
    ],

    "cnae": [
        "cnae",
        "atividade"
    ],

    "companies": [
        "empresa"
    ],

    "employees": [
        "empregado",
        "pessoal ocupado",
        "vínculo",
        "vinculo"
    ],

    "salary_mass": [
        "salários",
        "salarios",
        "remuneração",
        "remuneracao"
    ],

    "salary_avg": [
        "salário médio",
        "salario medio"
    ]
}

# =========================================
# COLUMN MAPPING
# =========================================

mapping_results = []

for col in rais_df.columns:

    col_lower = str(col).lower()

    assigned_domain = "unmapped"

    # =====================================
    # STRUCTURAL NOISE
    # =====================================

    if (
        "unnamed" in col_lower
        or col_lower.startswith("_")
    ):

        assigned_domain = "structural_noise"

    else:

        for domain, keywords in DOMAIN_RULES.items():

            for kw in keywords:

                if kw in col_lower:

                    assigned_domain = domain
                    break

            if assigned_domain != "unmapped":
                break

    mapping_results.append({

        "column_name": col,
        "economic_domain": assigned_domain

    })

mapping_df = pd.DataFrame(
    mapping_results
)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("RAIS DOMAIN MAPPING")
print("===================================\n")

print(mapping_df)

# =========================================
# EXPORT
# =========================================

export_path = os.path.join(
    EXPORT_PATH,
    "rais_semantic_mapping.csv"
)

mapping_df.to_csv(
    export_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_path)
