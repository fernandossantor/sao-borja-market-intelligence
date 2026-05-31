import pandas as pd
import os

print("\n===================================")
print("PRIVATE SECTOR MASTER BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =====================================
# LOAD
# =====================================

df6449 = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "rais_6449_panel.csv"
    )
)

df6450 = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "rais_6450_panel.csv"
    )
)

print("6449:", df6449.shape)
print("6450:", df6450.shape)

# =====================================
# PIVOT 6449
# =====================================

p6449 = (
    df6449
    .pivot_table(
        index=["year", "sector"],
        columns="metric",
        values="value",
        aggfunc="first"
    )
    .reset_index()
)

p6449.columns.name = None

print("\n6449 Pivot:")
print(p6449.shape)

# =====================================
# PIVOT 6450
# =====================================

p6450 = (
    df6450
    .pivot_table(
        index=["year", "sector"],
        columns="metric",
        values="value",
        aggfunc="first"
    )
    .reset_index()
)

p6450.columns.name = None

print("\n6450 Pivot:")
print(p6450.shape)

# =====================================
# MERGE
# =====================================

master = pd.merge(
    p6449,
    p6450,
    on=[
        "year",
        "sector"
    ],
    how="outer"
)

# =====================================
# ORGANIZAÇÃO
# =====================================

preferred_order = [

    "year",
    "sector",

    "empresas",

    "unidades_locais",

    "emprego_total",

    "emprego_assalariado",

    "salarios"

]

cols = []

for c in preferred_order:

    if c in master.columns:
        cols.append(c)

for c in master.columns:

    if c not in cols:
        cols.append(c)

master = master[cols]

master = master.sort_values(
    [
        "year",
        "sector"
    ]
)

# =====================================
# OUTPUT
# =====================================

print("\n===================================")
print("MASTER PANEL")
print("===================================\n")

print(master.head(30))

print("\nShape:")
print(master.shape)

print("\nAnos:")
print(
    master.year.min(),
    "-",
    master.year.max()
)

print("\nSetores:")
print(
    master.sector.nunique()
)

# =====================================
# EXPORT
# =====================================

export_file = os.path.join(
    EXPORT_PATH,
    "private_sector_master_panel.csv"
)

master.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
