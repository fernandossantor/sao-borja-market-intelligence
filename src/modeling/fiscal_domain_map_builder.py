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

    # -------------------------
    # EDUCAÇÃO
    # -------------------------

    if any(
        x in name
        for x in [
            "fundeb",
            "salário",
            "salario",
            "merenda",
            "pdde",
            "educação",
            "educacao",
            "manutenção da educação",
            "manutencao da educacao"
        ]
    ):
        return "education"

    # -------------------------
    # SAÚDE
    # -------------------------

    if any(
        x in name
        for x in [
            "saúde",
            "saude",
            "farmácia",
            "farmacia",
            "primária",
            "primaria",
            "mac",
            "enfermagem",
            "vigilância",
            "vigilancia",
            "agentes",
            "ambulatorial",
            "hospitalar",
            "covid"
        ]
    ):
        return "health"

    # -------------------------
    # ASSISTÊNCIA
    # -------------------------

    if any(
        x in name
        for x in [
            "suas",
            "proteção",
            "protecao",
            "social"
        ]
    ):
        return "social_assistance"

    # -------------------------
    # AGRO
    # -------------------------

    if "agro" in name:
        return "agriculture"

    # -------------------------
    # INFRA
    # -------------------------

    if any(
        x in name
        for x in [
            "urbano",
            "ponte",
            "investimentos"
        ]
    ):
        return "infrastructure"

    # -------------------------
    # RECEITA GERAL
    # -------------------------

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
