import pandas as pd
import os
import unicodedata

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

INPUT_FILE = os.path.join(
    EXPORT_PATH,
    "pib_consolidated.csv"
)

# =========================================
# NORMALIZATION
# =========================================

def normalize_text(text):

    if pd.isna(text):
        return ""

    text = str(text).upper()

    text = unicodedata.normalize(
        "NFKD",
        text
    ).encode(
        "ASCII",
        "ignore"
    ).decode(
        "utf-8"
    )

    return text.strip()

# =========================================
# ECONOMIC DOMAINS
# =========================================

DOMAIN_RULES = {

    "year": [
        "ANO"
    ],

    "municipality": [
        "MUNICIPIO"
    ],

    "ibge_code": [
        "CODIGO DO MUNICIPIO"
    ],

    "pib_total": [
        "PIB (EM R$)"
    ],

    "pib_per_capita": [
        "PIB PER CAPITA"
    ],

    "vab_agro": [
        "AGROPECUARIA"
    ],

    "vab_industria": [
        "INDUSTRIA"
    ],

    "vab_servicos": [
        "SERVICOS"
    ],

    "vab_publico": [
        "ADMINISTRACAO",
        "SEGURIDADE SOCIAL"
    ],

    "taxes": [
        "IMPOSTOS"
    ]
}

# =========================================
# DOMAIN DETECTOR
# =========================================

def detect_domain(column_name):

    normalized = normalize_text(column_name)

    # =====================================
    # STRUCTURAL NOISE (HIGHEST PRIORITY)
    # =====================================

    if any(x in normalized for x in [
        "TABELA ",
        "UNNAMED",
        "VARIAVEL -",
        "_SOURCE_FILE",
        "_TERRITORIAL_METHOD"
    ]):
        return "structural_noise"

    # =====================================
    # IDENTIFIERS
    # =====================================

    if (
        "CODIGO" in normalized
        and "MUNIC" in normalized
    ):
        return "ibge_code"

    if (
        "NOME" in normalized
        and "MUNIC" in normalized
    ):
        return "municipality"

    if "ANO" in normalized:
        return "year"

    # =====================================
    # PIB
    # =====================================

    if (
        "PIB" in normalized
        and "PER CAPITA" in normalized
    ):
        return "pib_per_capita"

    if (
        "PIB" in normalized
        and "PER CAPITA" not in normalized
    ):
        return "pib_total"

    # =====================================
    # VAB
    # =====================================

    if "AGROPECU" in normalized:
        return "vab_agro"

    if "INDUSTR" in normalized:
        return "vab_industria"

    if "SERVIC" in normalized:
        return "vab_servicos"

    if (
        "ADMINISTRAC" in normalized
        or "SEGURIDADE" in normalized
    ):
        return "vab_publico"

    if (
        "VAB TOTAL" in normalized
    ):
        return "vab_total"

    # =====================================
    # TAXES
    # =====================================

    if "IMPOST" in normalized:
        return "taxes"

    # =====================================
    # UNKNOWN
    # =====================================

    return "unmapped"

# =========================================
# LOAD DATA
# =========================================

df = pd.read_csv(INPUT_FILE)

print("\n===================================")
print("PIB CONSOLIDATED LOADED")
print("===================================\n")

print(f"Linhas: {len(df)}")
print(f"Colunas: {len(df.columns)}")

# =========================================
# COLUMN MAPPING
# =========================================

mapping_results = []

for col in df.columns:

    domain = detect_domain(col)

    mapping_results.append({
        "column_name": col,
        "economic_domain": domain
    })

mapping_df = pd.DataFrame(mapping_results)

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

csv_path = os.path.join(
    EXPORT_PATH,
    "pib_semantic_mapping.csv"
)

mapping_df.to_csv(
    csv_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(csv_path)
