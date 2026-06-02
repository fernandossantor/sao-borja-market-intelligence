import pandas as pd
import os
import unicodedata

print("\n===================================")
print("SOCIAL IDSC SUMMARY BUILDER")
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

# --------------------------------------------------
# MUNICÍPIO
# --------------------------------------------------

df["_mun_norm"] = (
    df["Município"]
    .apply(normalize)
)

sb = df[
    df["_mun_norm"] == "sao borja"
].copy()

if len(sb) == 0:

    raise ValueError(
        "São Borja não encontrado na base IDSC."
    )

# --------------------------------------------------
# COLUNAS ODS
# --------------------------------------------------

ods_cols = [
    c
    for c in df.columns
    if (
        "Goal" in c
        and
        "Score" in c
    )
]

# --------------------------------------------------
# TABELA RESUMO
# --------------------------------------------------

records = []

for col in ods_cols:

    ods = (
        col
        .replace("Goal ", "ODS ")
        .replace(" Score", "")
    )

    score = float(
        sb[col].iloc[0]
    )

    records.append(
        {
            "ods": ods,
            "score": score
        }
    )

summary = pd.DataFrame(records)

summary = summary.sort_values(
    "score",
    ascending=False
)

summary["rank"] = (
    range(
        1,
        len(summary) + 1
    )
)

# --------------------------------------------------
# CLASSIFICAÇÃO
# --------------------------------------------------

def classify(score):

    if score >= 70:
        return "forte"

    if score >= 50:
        return "intermediario"

    return "critico"

summary["classification"] = (
    summary["score"]
    .apply(classify)
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("IDSC SUMMARY")
print("===================================\n")

print(summary)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "social_idsc_summary.csv"
)

summary.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
