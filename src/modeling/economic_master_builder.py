import pandas as pd
import numpy as np
import os

print("\n===================================")
print("ECONOMIC MASTER BUILDER")
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
# VAB PRIVADO
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
# BASE OBSERVADA
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
# FONTE
# --------------------------------------------------

master["source"] = np.where(
    master["year"] <= 2021,
    "observed",
    "estimated"
)

# --------------------------------------------------
# ORDENAR
# --------------------------------------------------

master = master.sort_values(
    "year"
)

# --------------------------------------------------
# COLUNAS FINAIS
# --------------------------------------------------

cols = [
    "year",
    "vab_agro",
    "vab_private",
    "vab_public",
    "vab_total",
    "pib_total",
    "source",
    "private_source"
]

cols = [c for c in cols if c in master.columns]

master = master[cols]

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("MASTER SERIES")
print("===================================\n")

print(master.tail(15))

print("\nShape:")
print(master.shape)

print("\nAnos:")
print(
    int(master["year"].min()),
    "-",
    int(master["year"].max())
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "economic_master_series.csv"
)

master.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
