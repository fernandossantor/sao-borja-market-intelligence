import pandas as pd
import os

print("\n===================================")
print("SOCIAL CATALOG BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

inventory = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "social_inventory.csv"
    )
)

# ----------------------------------
# CLASSIFICAÇÃO
# ----------------------------------

def classify(name):

    name = str(name).lower()

    if "bolsa familia" in name:
        return "income_support"

    if "idsc" in name:
        return "social_index"

    if "ips" in name:
        return "social_index"

    if any(
        x in name
        for x in [
            "alfabet",
            "instruc"
        ]
    ):
        return "education"

    if any(
        x in name
        for x in [
            "domic",
            "favela",
            "entorno"
        ]
    ):
        return "housing"

    if any(
        x in name
        for x in [
            "indígen",
            "indigena",
            "quilomb"
        ]
    ):
        return "minorities"

    if any(
        x in name
        for x in [
            "defici",
            "autismo"
        ]
    ):
        return "health_social"

    if any(
        x in name
        for x in [
            "transporte"
        ]
    ):
        return "mobility"

    return "demography"

# ----------------------------------
# APLICAR
# ----------------------------------

inventory["domain"] = (
    inventory["file"]
    .apply(classify)
)

print(inventory[
    [
        "file",
        "domain"
    ]
])

# ----------------------------------
# EXPORT
# ----------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "social_catalog.csv"
)

inventory.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
