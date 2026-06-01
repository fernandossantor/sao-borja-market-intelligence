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

    name = name.lower()

    if any(
        x in name
        for x in [
            "fundeb",
            "salário",
            "salario",
            "merenda",
            "pdde",
            "educação",
            "educacao"
        ]
    ):
        return "education"

    if any(
        x in name
        for x in [
            "saúde",
            "saude",
            "farmácia",
            "farmacia",
            "mac",
            "enfermagem",
            "vigilância",
            "vigilancia",
            "agentes"
        ]
    ):
        return "health"

    if any(
        x in name
        for x in [
            "suas",
            "proteção",
            "protecao"
        ]
    ):
        return "social_assistance"

    if any(
        x in name
        for x in [
            "agro"
        ]
    ):
        return "agriculture"

    if any(
        x in name
        for x in [
            "urbano",
            "investimentos",
            "ponte"
        ]
    ):
        return "infrastructure"

    if any(
        x in name
        for x in [
            "fpm",
            "itr",
            "royalties",
            "compens"
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
