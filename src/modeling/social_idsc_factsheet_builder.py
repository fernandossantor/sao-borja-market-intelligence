import pandas as pd
import os
import unicodedata

print("\n===================================")
print("SOCIAL IDSC FACTSHEET BUILDER")
print("===================================\n")

RAW_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/social"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# NORMALIZAÇÃO
# --------------------------------------------------

def normalize(text):

    text = str(text)

    text = unicodedata.normalize(
        "NFKD",
        text
    )

    text = "".join(
        c
        for c in text
        if not unicodedata.combining(c)
    )

    return text.lower().strip()

# --------------------------------------------------
# CARREGAR IDSC
# --------------------------------------------------

file = os.path.join(
    RAW_PATH,
    "Base_de_Dados_IDSC-BR_2025.xlsx"
)

df = pd.read_excel(
    file,
    sheet_name="Todos os Dados"
)

df["_mun_norm"] = (
    df["Município"]
    .apply(normalize)
)

sb = df[
    df["_mun_norm"] == "sao borja"
].copy()

if len(sb) == 0:

    raise ValueError(
        "São Borja não encontrado."
    )

# --------------------------------------------------
# DADOS GERAIS
# --------------------------------------------------

overall_score = float(
    sb["Pontuação Indice ODS 2025"]
    .iloc[0]
)

national_rank = int(
    sb["Classificação 2025"]
    .iloc[0]
)

missing_values = int(
    sb["Valores faltantes"]
    .iloc[0]
)

# --------------------------------------------------
# ODS
# --------------------------------------------------

summary = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "social_idsc_summary.csv"
    )
)

best_ods = summary.iloc[0]
worst_ods = summary.iloc[-1]

excellent_count = (
    summary["classification"]
    == "excelente"
).sum()

strong_count = (
    summary["classification"]
    == "forte"
).sum()

fragile_count = (
    summary["classification"]
    == "fragil"
).sum()

critical_count = (
    summary["classification"]
    == "critico"
).sum()

# --------------------------------------------------
# FACTSHEET
# --------------------------------------------------

factsheet = pd.DataFrame(
    [
        [
            "Pontuação ODS Geral",
            overall_score
        ],
        [
            "Ranking Nacional",
            national_rank
        ],
        [
            "Valores Faltantes",
            missing_values
        ],
        [
            "ODS Mais Forte",
            best_ods["ods"]
        ],
        [
            "Score ODS Mais Forte",
            best_ods["score"]
        ],
        [
            "ODS Mais Fraco",
            worst_ods["ods"]
        ],
        [
            "Score ODS Mais Fraco",
            worst_ods["score"]
        ],
        [
            "ODS Fortes",
            strong_count
        ],
        [
            "ODS Críticos",
            critical_count
        ]
    ],
    columns=[
        "indicator",
        "value"
    ]
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("IDSC FACTSHEET")
print("===================================\n")

print(factsheet)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "social_idsc_factsheet.csv"
)

factsheet.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
