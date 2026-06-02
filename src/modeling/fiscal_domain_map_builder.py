import pandas as pd
import os

print("\n===================================")
print("FISCAL DOMAIN MAP")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

catalog = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_catalog.csv"
    )
)

def map_domain(name):

    name = str(name).lower()

    # --------------------------------
    # EDUCAÇÃO
    # --------------------------------

    if any(
        token in name
        for token in [
            "fundeb",
            "salario",
            "educ",
            "merenda",
            "pdde"
        ]
    ):
        return "education"

    # --------------------------------
    # SAÚDE
    # --------------------------------

    if any(
        token in name
        for token in [
            "saud",
            "farm",
            "prim",
            "mac",
            "vigil",
            "enferm",
            "agente",
            "hospital",
            "ambulator",
            "covid"
        ]
    ):
        return "health"

    # --------------------------------
    # ASSISTÊNCIA SOCIAL
    # --------------------------------

    if any(
        token in name
        for token in [
            "suas",
            "social",
            "protec"
        ]
    ):
        return "social_assistance"

    # --------------------------------
    # AGRO
    # --------------------------------

    if any(
        token in name
        for token in [
            "agro"
        ]
    ):
        return "agriculture"

    # --------------------------------
    # INFRAESTRUTURA
    # --------------------------------

    if any(
        token in name
        for token in [
            "urban",
            "ponte",
            "invest",
            "contribu"
        ]
    ):
        return "infrastructure"

    # --------------------------------
    # RECEITA GERAL
    # --------------------------------

    if any(
        token in name
        for token in [
            "fpm",
            "itr",
            "royalt",
            "compens",
            "petrol"
        ]
    ):
        return "general_revenue"

    return "other"
    
catalog["domain"] = (
    catalog["file"]
    .apply(map_domain)
)

print(catalog)

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_domain_map.csv"
)

catalog.to_csv(
    export_file,
    index=False
)

print("\nExportado:")
print(export_file)
