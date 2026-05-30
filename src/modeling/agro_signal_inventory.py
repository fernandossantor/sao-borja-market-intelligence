import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# LOAD
# =========================================

signals = pd.read_csv(
    f"{EXPORT_PATH}/domain_signals.csv"
)

sector_signals = pd.read_csv(
    f"{EXPORT_PATH}/sector_signals_v2.csv"
)

print("\n===================================")
print("AGRO SIGNAL INVENTORY")
print("===================================\n")

# =========================================
# AGRO ONLY
# =========================================

agro = sector_signals[
    sector_signals["sector"] == "agro"
].copy()

print(
    f"Sinais agro: {len(agro)}"
)

# =========================================
# JOIN DETAILS
# =========================================

agro_details = pd.merge(

    agro,

    signals[[
        "category",
        "file_name",
        "sheet",
        "start_year",
        "end_year",
        "rows",
        "cols",
        "column_names",
        "score"
    ]],

    on=[
        "category",
        "file_name",
        "start_year",
        "end_year",
        "score"
    ],

    how="left"

)

# =========================================
# SUMMARY FILES
# =========================================

summary = (

    agro_details
    .groupby([
        "file_name"
    ])
    .agg({

        "start_year": "min",
        "end_year": "max",
        "sheet": "nunique"

    })
    .reset_index()

    .sort_values(
        "file_name"
    )

)

print("\n===================================")
print("AGRO FILES")
print("===================================\n")

print(summary)

# =========================================
# TOP SIGNALS
# =========================================

print("\n===================================")
print("TOP AGRO SIGNALS")
print("===================================\n")

print(

    agro_details[[
        "file_name",
        "sheet",
        "start_year",
        "end_year",
        "rows",
        "cols",
        "column_names"
    ]]

    .head(100)

)

# =========================================
# EXPORT
# =========================================

inventory_file = os.path.join(
    EXPORT_PATH,
    "agro_signal_inventory.csv"
)

summary_file = os.path.join(
    EXPORT_PATH,
    "agro_file_summary.csv"
)

agro_details.to_csv(
    inventory_file,
    index=False
)

summary.to_csv(
    summary_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(inventory_file)
print(summary_file)
