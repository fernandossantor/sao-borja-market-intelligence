import pandas as pd
import os

print("\n===================================")
print("ECONOMIC MASTER BUILDER V2")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# PIB CANÔNICO
# --------------------------------------------------

pib = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "pib_canonical.csv"
    )
)

# --------------------------------------------------
# PRIVADO OBSERVADO / ESTIMADO
# --------------------------------------------------

private = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_vab_projection.csv"
    )
)

private = private[
    [
        "year",
        "vab_private",
        "type"
    ]
].copy()

private = private.rename(
    columns={
        "type": "private_source"
    }
)

# --------------------------------------------------
# MERGE
# --------------------------------------------------

master = pib.merge(
    private,
    on="year",
    how="outer"
)

# --------------------------------------------------
# RENOMEAR
# --------------------------------------------------

master = master.rename(
    columns={
        "vab_publico": "vab_public"
    }
)

# --------------------------------------------------
# PRIVADO OBSERVADO
# --------------------------------------------------

master["vab_private_observed"] = (
    master["vab_industria"]
    +
    master["vab_servicos"]
)

# --------------------------------------------------
# FONTE
# --------------------------------------------------

master["source"] = master["year"].apply(
    lambda x:
    "observed"
    if x <= 2021
    else "estimated"
)

# --------------------------------------------------
# COLUNAS
# --------------------------------------------------

master = master[
    [
        "year",
        "vab_agro",
        "vab_industria",
        "vab_servicos",
        "vab_private_observed",
        "vab_private",
        "vab_public",
        "vab_total",
        "pib_total",
        "source"
    ]
]

master = master.sort_values(
    "year"
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("MASTER V2")
print("===================================\n")

print(master.tail(10))

print("\nShape:")
print(master.shape)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "economic_master_series_v2.csv"
)

master.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
