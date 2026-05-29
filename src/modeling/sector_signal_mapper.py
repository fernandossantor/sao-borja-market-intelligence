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
# LOAD
# =========================================

signals = pd.read_csv(
    f"{EXPORT_PATH}/domain_signals.csv"
)

print("\n===================================")
print("SECTOR SIGNAL MAPPER")
print("===================================\n")

# =========================================
# KEYWORDS
# =========================================

AGRO = [
    "soja",
    "arroz",
    "milho",
    "trigo",
    "rebanho",
    "bovino",
    "produção",
    "plantada",
    "colhida",
    "pecuária"
]

INDUSTRIA = [
    "indústria",
    "industrial",
    "fábrica",
    "transformação",
    "cnae"
]

SERVICOS = [
    "comércio",
    "varejo",
    "serviços",
    "iss",
    "empresa",
    "emprego",
    "salário"
]

PUBLICO = [
    "servidor",
    "pessoal",
    "folha",
    "saúde",
    "educação",
    "assistência",
    "prefeitura",
    "administração"
]

# =========================================
# CLASSIFIER
# =========================================

def classify_signal(text):

    text = str(text).lower()

    agro_score = sum(
        kw in text
        for kw in AGRO
    )

    industria_score = sum(
        kw in text
        for kw in INDUSTRIA
    )

    servicos_score = sum(
        kw in text
        for kw in SERVICOS
    )

    publico_score = sum(
        kw in text
        for kw in PUBLICO
    )

    scores = {

        "agro":
            agro_score,

        "industria":
            industria_score,

        "servicos":
            servicos_score,

        "publico":
            publico_score

    }

    best = max(
        scores,
        key=scores.get
    )

    if scores[best] == 0:

        return "unclassified"

    return best

# =========================================
# APPLY
# =========================================

signals["sector"] = (

    signals["file_name"]
    .astype(str)

    + " "

    + signals["sheet"]
    .astype(str)

    + " "

    + signals["column_names"]
    .astype(str)

).apply(
    classify_signal
)

# =========================================
# SUMMARY
# =========================================

summary = (

    signals["sector"]
    .value_counts()
    .reset_index()

)

summary.columns = [
    "sector",
    "count"
]

print("\n===================================")
print("SECTOR DISTRIBUTION")
print("===================================\n")

print(summary)

# =========================================
# EXPORTS
# =========================================

signals_file = os.path.join(
    EXPORT_PATH,
    "sector_signals.csv"
)

summary_file = os.path.join(
    EXPORT_PATH,
    "sector_signals_summary.csv"
)

signals.to_csv(
    signals_file,
    index=False
)

summary.to_csv(
    summary_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(signals_file)
print(summary_file)
