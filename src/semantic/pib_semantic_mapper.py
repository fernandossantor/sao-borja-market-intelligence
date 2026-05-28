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
# LOAD PIB
# =========================================

pib_df = pd.read_csv(
    f"{EXPORT_PATH}/pib_consolidated.csv"
)

print("\n===================================")
print("PIB CONSOLIDATED LOADED")
print("===================================\n")

print(f"Linhas: {len(pib_df)}")
print(f"Colunas: {len(pib_df.columns)}")

# =========================================
# DOMAIN RULES
# =========================================

DOMAIN_RULES = {

    "year": [
        "ano"
    ],

    "municipality": [
    "nome do município",
    "nome do municipio"
    ],

    "ibge_code": [
    "código do município",
    "codigo do municipio"
    ],

    "ibge_code": [
        "código do município",
        "codigo do municipio"
    ],

    "vab_agro": [
        "agropecuária",
        "agropecuaria"
    ],

    "vab_industria": [
        "indústria",
        "industria"
    ],

    "vab_servicos": [
        "serviços",
        "servicos"
    ],

    "vab_publico": [
        "administração",
        "administracao",
        "seguridade"
    ],

    "vab_total": [
        "vab total"
    ],

    "taxes": [
        "impostos"
    ],

    "pib_total": [
        "pib (em r$)",
        "produto interno bruto"
    ],

    "pib_per_capita": [
        "per capita"
    ]
}

# =========================================
# COLUMN MAPPING
# =========================================

mapping_results = []

for col in pib_df.columns:

    col_lower = str(col).lower()

    assigned_domain = "unmapped"

    # ================================
    # STRUCTURAL NOISE
    # ================================

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
print("ECONOMIC DOMAIN MAPPING")
print("===================================\n")

print(mapping_df)

# =========================================
# EXPORT
# =========================================

export_path = os.path.join(
    EXPORT_PATH,
    "pib_semantic_mapping.csv"
)

mapping_df.to_csv(
    export_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_path)
