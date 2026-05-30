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
print("SECTOR SIGNAL BUILDER")
print("===================================\n")

print(
    f"Sinais carregados: {len(signals)}"
)

# =========================================
# SECTOR RULES
# =========================================

def classify_sector(text):

    text = str(text).lower()

    # -------------------------
    # AGRO
    # -------------------------

    agro = [

        "agro",
        "plantada",
        "colhida",
        "produção",
        "rebanho",
        "silvicultura",
        "pecuária",
        "lavoura",
        "soja",
        "milho",
        "arroz"

    ]

    # -------------------------
    # PUBLICO
    # -------------------------

    publico = [

        "servidor",
        "remuneração",
        "afastamento",
        "cadastro",
        "fundeb",
        "fpm",
        "saúde",
        "educação",
        "assistência",
        "prefeitura",
        "governo",
        "orçamentária"

    ]

    # -------------------------
    # SERVIÇOS
    # -------------------------

    servicos = [

        "comércio",
        "serviços",
        "varejo",
        "bolsa família",
        "censo",
        "população",
        "religião",
        "alfabetização",
        "domicílio",
        "ips",
        "idsc"

    ]

    # -------------------------
    # INDÚSTRIA
    # -------------------------

    industria = [

        "indústria",
        "industrial",
        "energia",
        "transformação",
        "fabricação"

    ]

    for k in agro:
        if k in text:
            return "agro"

    for k in publico:
        if k in text:
            return "publico"

    for k in servicos:
        if k in text:
            return "servicos"

    for k in industria:
        if k in text:
            return "industria"

    return "unclassified"

# =========================================
# BUILD SIGNALS
# =========================================

sector_rows = []

for _, row in signals.iterrows():

    text = " ".join([

        str(row.get("category", "")),
        str(row.get("file_name", "")),
        str(row.get("column_names", ""))

    ])

    sector = classify_sector(text)

    sector_rows.append({

        "category":
            row["category"],

        "file_name":
            row["file_name"],

        "sector":
            sector,

        "start_year":
            row.get("start_year"),

        "end_year":
            row.get("end_year"),

        "score":
            row.get("score")

    })

sector_df = pd.DataFrame(
    sector_rows
)

# =========================================
# SUMMARY
# =========================================

summary = (

    sector_df
    .groupby("sector")
    .size()
    .reset_index(
        name="signals"
    )
    .sort_values(
        "signals",
        ascending=False
    )

)

print("\n===================================")
print("SECTOR DISTRIBUTION")
print("===================================\n")

print(summary)

# =========================================
# EXPORT
# =========================================

signals_file = os.path.join(
    EXPORT_PATH,
    "sector_signals.csv"
)

summary_file = os.path.join(
    EXPORT_PATH,
    "sector_signals_summary.csv"
)

sector_df.to_csv(
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
