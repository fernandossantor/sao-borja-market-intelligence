import pandas as pd
import os

print("\n===================================")
print("MODEL ASSUMPTIONS REGISTRY")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

registry = pd.DataFrame([

    # --------------------------------------------------
    # PIB
    # --------------------------------------------------

    [
        "economic",
        "pib_canonical.csv",
        "pib_total",
        "observed",
        "PIB municipal oficial IBGE"
    ],

    [
        "economic",
        "pib_canonical.csv",
        "vab_agro",
        "observed",
        "VAB agropecuário oficial IBGE"
    ],

    [
        "economic",
        "pib_canonical.csv",
        "vab_industria",
        "observed",
        "VAB indústria oficial IBGE"
    ],

    [
        "economic",
        "pib_canonical.csv",
        "vab_servicos",
        "observed",
        "VAB serviços oficial IBGE"
    ],

    [
        "economic",
        "pib_canonical.csv",
        "vab_publico",
        "observed",
        "VAB administração pública oficial IBGE"
    ],

    # --------------------------------------------------
    # VAB PRIVADO
    # --------------------------------------------------

    [
        "economic",
        "private_vab_observed.csv",
        "vab_private",
        "identity",
        "VAB privado = VAB total - VAB público"
    ],

    # --------------------------------------------------
    # RAIS
    # --------------------------------------------------

    [
        "labor",
        "private_employment_long_history.csv",
        "employment_total",
        "observed",
        "Emprego formal privado RAIS"
    ],

    # --------------------------------------------------
    # SHARES
    # --------------------------------------------------

    [
        "economic",
        "economic_structure_v2.csv",
        "agro_share",
        "derived",
        "Participação agropecuária no VAB"
    ],

    [
        "economic",
        "economic_structure_v2.csv",
        "industry_share",
        "derived",
        "Participação industrial no VAB"
    ],

    [
        "economic",
        "economic_structure_v2.csv",
        "services_share",
        "derived",
        "Participação serviços no VAB"
    ],

    [
        "economic",
        "economic_structure_v2.csv",
        "public_share",
        "derived",
        "Participação pública no VAB"
    ],

    # --------------------------------------------------
    # REGIMES
    # --------------------------------------------------

    [
        "economic",
        "economic_regimes.csv",
        "regime",
        "classification",
        "Classificação analítica criada pelo projeto"
    ],

    # --------------------------------------------------
    # PROJEÇÕES
    # --------------------------------------------------

    [
        "economic",
        "private_vab_projection.csv",
        "vab_private",
        "projection",
        "Estimativa do VAB privado pós-2021"
    ],

    [
        "economic",
        "private_vab_projection.csv",
        "share_privado_estrutural",
        "assumption",
        "Participação privada média 2017-2020 utilizada na projeção"
    ]

],
columns=[
    "domain",
    "artifact",
    "variable",
    "category",
    "description"
])

print(registry)

export_file = os.path.join(
    EXPORT_PATH,
    "model_assumptions_registry.csv"
)

registry.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
