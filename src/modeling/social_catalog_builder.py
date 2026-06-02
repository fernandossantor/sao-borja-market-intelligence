import pandas as pd
import os
import unicodedata

print("\n===================================")
print("SOCIAL CATALOG BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# CARREGAR INVENTÁRIO
# --------------------------------------------------

inventory = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "social_inventory.csv"
    )
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

    return text.lower()

# --------------------------------------------------
# CLASSIFICAÇÃO
# --------------------------------------------------

def classify(filename):

    name = normalize(filename)

    # -------------------------
    # Bolsa Família
    # -------------------------

    if "bolsa familia" in name:
        return "income_support"

    # -------------------------
    # Índices sintéticos
    # -------------------------

    if "idsc" in name:
        return "social_index"

    if "ips" in name:
        return "social_index"

    # -------------------------
    # Educação
    # -------------------------

    if any(
        x in name
        for x in [
            "alfabetizacao",
            "instrucao"
        ]
    ):
        return "education"

    # -------------------------
    # Habitação
    # -------------------------

    if any(
        x in name
        for x in [
            "domicilio",
            "domicilios",
            "composicao domiciliar",
            "favela",
            "entorno"
        ]
    ):
        return "housing"

    # -------------------------
    # Minorias
    # -------------------------

    if any(
        x in name
        for x in [
            "indigena",
            "quilombola"
        ]
    ):
        return "minorities"

    # -------------------------
    # Saúde e inclusão
    # -------------------------

    if any(
        x in name
        for x in [
            "deficiencia",
            "autismo"
        ]
    ):
        return "health_social"

    # -------------------------
    # Mobilidade
    # -------------------------

    if any(
        x in name
        for x in [
            "transporte"
        ]
    ):
        return "mobility"

    # -------------------------
    # Demografia
    # -------------------------

    return "demography"

# --------------------------------------------------
# APLICAR
# --------------------------------------------------

catalog = inventory.copy()

catalog["domain"] = (
    catalog["file"]
    .apply(classify)
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("SOCIAL CATALOG")
print("===================================\n")

print(
    catalog[
        [
            "file",
            "domain"
        ]
    ]
)

print("\n===================================")
print("DISTRIBUIÇÃO")
print("===================================\n")

print(
    catalog["domain"]
    .value_counts()
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "social_catalog.csv"
)

catalog.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
