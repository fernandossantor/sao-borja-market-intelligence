import pandas as pd
import re
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

profile = pd.read_csv(
    f"{EXPORT_PATH}/rais_dataset_profile.csv"
)

print("\n===================================")
print("RAIS SEMANTIC AUDIT")
print("===================================\n")

# =========================================
# KEYWORDS
# =========================================

KEYWORDS = [

    "cnae",
    "atividade",
    "setor",
    "emprego",
    "empregados",
    "ocupado",
    "ocupação",
    "salário",
    "remuneração",
    "massa salarial",
    "empresa",
    "estabelecimento",
    "vínculo",
    "fundação"

]

# =========================================
# SCORE
# =========================================

def semantic_score(text):

    text = str(text).lower()

    score = 0

    for kw in KEYWORDS:

        if kw in text:
            score += 1

    return score

profile["semantic_score"] = (

    profile["column_names"]
    .apply(semantic_score)

)

# =========================================
# TOP
# =========================================

top = (

    profile

    .sort_values(
        "semantic_score",
        ascending=False
    )

)

print("\n===================================")
print("TOP SEMANTIC DATASETS")
print("===================================\n")

print(

    top[
        [
            "file_name",
            "sheet",
            "header",
            "rows",
            "cols",
            "semantic_score"
        ]
    ]

    .head(100)

)

# =========================================
# EXPORT
# =========================================

output = os.path.join(
    EXPORT_PATH,
    "rais_semantic_audit.csv"
)

top.to_csv(
    output,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(output)
