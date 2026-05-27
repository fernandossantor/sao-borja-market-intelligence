import pandas as pd
import json
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = "/content/drive/MyDrive/Colab Notebooks/_sao_borja/exports"

# =========================================
# SEMANTIC RULES
# =========================================

SEMANTIC_RULES = {

    "identifier": [
        "codigo",
        "cod",
        "id",
        "ibge",
        "cnae",
        "cbo"
    ],

    "currency": [
        "valor",
        "salario",
        "massa",
        "receita",
        "despesa",
        "fpm",
        "fundeb",
        "rendimento",
        "remuneracao"
    ],

    "percentage": [
        "percent",
        "%",
        "participacao"
    ],

    "area": [
        "hectare",
        "ha",
        "area"
    ],

    "weight": [
        "kg",
        "ton",
        "peso"
    ],

    "people_count": [
        "populacao",
        "habitantes",
        "beneficiarios",
        "servidores",
        "empregados",
        "vinculos"
    ],

    "livestock_count": [
        "rebanho",
        "cabecas",
        "bovinos",
        "suinos"
    ],

    "date": [
        "ano",
        "mes",
        "data"
    ],

    "productivity": [
        "produtividade",
        "rendimento"
    ]
}

# =========================================
# CLASSIFIER
# =========================================

def classify_column(column_name):

    column = column_name.lower()

    for semantic_type, keywords in SEMANTIC_RULES.items():

        for keyword in keywords:

            if keyword in column:
                return semantic_type

    return "unknown"

# =========================================
# TEST EXAMPLES
# =========================================

sample_columns = [
    "cod_municipio",
    "valor_pib",
    "area_colhida",
    "producao_ton",
    "rebanho_bovino",
    "ano",
    "beneficiarios",
    "massa_salarial"
]

results = []

for col in sample_columns:

    semantic_type = classify_column(col)

    results.append({
        "column_name": col,
        "semantic_type": semantic_type
    })

df = pd.DataFrame(results)

# =========================================
# EXPORT
# =========================================

os.makedirs(EXPORT_PATH, exist_ok=True)

csv_path = os.path.join(
    EXPORT_PATH,
    "semantic_registry_examples.csv"
)

json_path = os.path.join(
    EXPORT_PATH,
    "semantic_registry_examples.json"
)

df.to_csv(csv_path, index=False)

df.to_json(
    json_path,
    orient="records",
    force_ascii=False,
    indent=4
)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("SEMANTIC REGISTRY CREATED")
print("===================================\n")

print(df)

print(f"\nCSV salvo em:\n{csv_path}")
print(f"\nJSON salvo em:\n{json_path}")
