import pandas as pd
import os

print("\n===================================")
print("PRIVATE EMPLOYMENT LONG HISTORY")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =====================================
# 1735 HISTÓRICO
# =====================================

hist = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "rais_1735_reconstructed_employment.csv"
    )
)

hist = (
    hist
    .groupby("year")["employment_total"]
    .sum()
    .reset_index()
)

hist.columns = [
    "year",
    "employment_total"
]

hist["source"] = "rais_1735"

# =====================================
# 6450 MODERNO
# =====================================

modern = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_sector_annual_panel.csv"
    )
)

modern = modern[
    [
        "year",
        "emprego_total"
    ]
].copy()

modern.columns = [
    "year",
    "employment_total"
]

modern["source"] = "rais_6450"

# =====================================
# REMOVE 2006 DA 1735
# (usar 6450 como fonte oficial)
# =====================================

hist = hist[
    hist["year"] < 2006
]

# =====================================
# CONCATENA
# =====================================

long = pd.concat(
    [
        hist,
        modern
    ],
    ignore_index=True
)

long = (
    long
    .sort_values("year")
    .reset_index(drop=True)
)

# =====================================
# CRESCIMENTO
# =====================================

long["growth_pct"] = (
    long["employment_total"]
    .pct_change()
    * 100
)

# =====================================
# OUTPUT
# =====================================

print("\n===================================")
print("LONG HISTORY")
print("===================================\n")

print(long)

print("\nAnos:")
print(
    long.year.min(),
    "-",
    long.year.max()
)

print("\nObservações:")
print(len(long))

# =====================================
# EXPORT
# =====================================

export_file = os.path.join(
    EXPORT_PATH,
    "private_employment_long_history.csv"
)

long.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
