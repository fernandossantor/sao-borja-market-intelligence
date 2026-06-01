import pandas as pd
import os

print("\n===================================")
print("ECONOMIC LONG HISTORY BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# EMPREGO PRIVADO
# --------------------------------------------------

employment = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_employment_long_history.csv"
    )
)

employment = employment[
    [
        "year",
        "employment_total"
    ]
].copy()

employment = employment.rename(
    columns={
        "employment_total": "employment_private"
    }
)

# --------------------------------------------------
# ECONOMIC MASTER V2
# --------------------------------------------------

master = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "economic_master_series_v2.csv"
    )
)

master = master[
    [
        "year",
        "vab_agro",
        "vab_industria",
        "vab_servicos",
        "vab_public",
        "vab_private",
        "pib_total"
    ]
].copy()

master = master.rename(
    columns={
        "vab_public": "vab_publico"
    }
)

# --------------------------------------------------
# MERGE
# --------------------------------------------------

history = pd.merge(
    employment,
    master,
    on="year",
    how="outer"
)

history = history.sort_values(
    "year"
)

# --------------------------------------------------
# INDICADORES AUXILIARES
# --------------------------------------------------

history["employment_growth_pct"] = (
    history["employment_private"]
    .pct_change()
    * 100
)

history["pib_growth_pct"] = (
    history["pib_total"]
    .pct_change()
    * 100
)

history["private_vab_growth_pct"] = (
    history["vab_private"]
    .pct_change()
    * 100
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("LONG HISTORY")
print("===================================\n")

print(history.head(10))

print("\n===================================")
print("ÚLTIMOS ANOS")
print("===================================\n")

print(history.tail(10))

print("\nShape:")
print(history.shape)

print("\nCobertura:")
print(
    int(history["year"].min()),
    "-",
    int(history["year"].max())
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "economic_long_history.csv"
)

history.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
