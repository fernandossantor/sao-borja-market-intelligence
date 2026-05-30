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
print("SECTOR SIGNAL BUILDER V2")
print("===================================\n")

print(
    f"Sinais carregados: {len(signals)}"
)

# =========================================
# CLASSIFIER
# =========================================

def classify_signal(text):

    text = str(text).lower()

    # =====================================
    # PIB
    # =====================================

    pib_keywords = [

        "pib",
        "vab",
        "valor adicionado",
        "per capita",
        "impostos"

    ]

    # =====================================
    # MERCADO DE TRABALHO
    # =====================================

    labor_keywords = [

        "rais",
        "vínculo",
        "vinculo",
        "emprego",
        "empregados",
        "pessoal ocupado",
        "salário",
        "salario",
        "remuneração",
        "remuneracao",
        "cnae",
        "cbo",
        "fundação",
        "fundacao"

    ]

    # =====================================
    # AGRO
    # =====================================

    agro_keywords = [

        "agro",
        "plantada",
        "colhida",
        "produção",
        "producao",
        "pecuária",
        "pecuaria",
        "rebanho",
        "silvicultura",
        "soja",
        "milho",
        "arroz"

    ]

    # =====================================
    # SETOR PÚBLICO
    # =====================================

    public_keywords = [

        "fundeb",
        "fpm",
        "orçamentária",
        "orcamentaria",
        "servidor",
        "afastamento",
        "remuneracao",
        "remuneração",
        "cadastro",
        "prefeitura",
        "governo",
        "saúde",
        "saude",
        "educação",
        "educacao",
        "assistência",
        "assistencia"

    ]

    # =====================================
    # DEMOGRAFIA
    # =====================================

    demographic_keywords = [

        "censo",
        "população",
        "populacao",
        "sexo",
        "idade",
        "religião",
        "religiao",
        "alfabetização",
        "alfabetizacao",
        "domicílio",
        "domicilio",
        "escolaridade",
        "instrução",
        "instrucao",
        "raça",
        "raca",
        "quilombola",
        "indígena",
        "indigena",
        "autismo",
        "deficiência",
        "deficiencia"

    ]

    # =====================================
    # SERVIÇOS
    # =====================================

    services_keywords = [

        "bolsa familia",
        "ips",
        "idsc",
        "comércio",
        "comercio",
        "serviços",
        "servicos",
        "varejo"

    ]

    # =====================================
    # INDÚSTRIA
    # =====================================

    industry_keywords = [

        "indústria",
        "industria",
        "industrial",
        "energia",
        "transformação",
        "transformacao",
        "fabricação",
        "fabricacao"

    ]

    # =====================================
    # CLASSIFICATION
    # =====================================

    for kw in pib_keywords:
        if kw in text:
            return "pib"

    for kw in labor_keywords:
        if kw in text:
            return "mercado_trabalho"

    for kw in agro_keywords:
        if kw in text:
            return "agro"

    for kw in public_keywords:
        if kw in text:
            return "publico"

    for kw in demographic_keywords:
        if kw in text:
            return "demografia"

    for kw in services_keywords:
        if kw in text:
            return "servicos"

    for kw in industry_keywords:
        if kw in text:
            return "industria"

    return "unclassified"

# =========================================
# BUILD
# =========================================

rows = []

for _, row in signals.iterrows():

    text = " ".join([

        str(row.get("category", "")),
        str(row.get("file_name", "")),
        str(row.get("column_names", ""))

    ])

    sector = classify_signal(text)

    rows.append({

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
    rows
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
    "sector_signals_v2.csv"
)

summary_file = os.path.join(
    EXPORT_PATH,
    "sector_signals_summary_v2.csv"
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
