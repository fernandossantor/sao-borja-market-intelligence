import pandas as pd
import os
import glob

from loaders.smart_excel_loader import (
    load_excel_smart
)

from territorial.territorial_filter import (
    filter_sao_borja
)

# =========================================
# CONFIG
# =========================================

BASE_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja"
)

RAW_PATH = os.path.join(
    BASE_PATH,
    "raw"
)

EXPORT_PATH = os.path.join(
    BASE_PATH,
    "exports"
)

# =========================================
# INVENTORY
# =========================================

inventory_path = os.path.join(
    EXPORT_PATH,
    "inventory.csv"
)

inventory = pd.read_csv(inventory_path)

# =========================================
# FILTER RAIS FILES
# =========================================

rais_files = inventory[
    inventory["category"] == "rais"
]

print("\n===================================")
print("RAIS FILES DETECTED")
print("===================================\n")

print(rais_files[[
    "file_name",
    "full_path"
]])

# =========================================
# CONSOLIDATION
# =========================================

dfs = []

# =========================================
# PROCESS FILES
# =========================================

for _, row in rais_files.iterrows():

    file_name = row["file_name"]
    file_path = row["full_path"]

    print("\n-----------------------------------")
    print(f"PROCESSANDO: {file_name}")
    print("-----------------------------------")

    try:

        # ==========================
        # LOAD
        # ==========================

        if file_path.endswith(".csv"):

            df = load_csv_robust(file_path)

        else:

            df = load_excel_smart(file_path)

        print(f"[INFO] linhas carregadas: {len(df)}")

        # ==========================
        # FILTER
        # ==========================

        filtered_df, method = filter_sao_borja(
        df,
        file_name
        )

        print(f"[INFO] método territorial: {method}")
        print(f"[INFO] linhas após filtro: {len(filtered_df)}")

        if len(filtered_df) == 0:
            continue

        # ==========================
        # METADATA
        # ==========================

        filtered_df["_source_file"] = file_name
        filtered_df["_territorial_method"] = method

        dfs.append(filtered_df)

    except Exception as e:

        print(f"[ERRO] {file_name} -> {e}")

# =========================================
# FINAL CONSOLIDATION
# =========================================

rais_df = pd.concat(
    dfs,
    ignore_index=True
)

print("\n===================================")
print("RAIS CONSOLIDATED")
print("===================================\n")

print(f"Linhas: {len(rais_df)}")
print(f"Colunas: {len(rais_df.columns)}")

print("\nColunas encontradas:\n")
print(list(rais_df.columns))

# =========================================
# EXPORT
# =========================================

output_path = os.path.join(
    EXPORT_PATH,
    "rais_consolidated.csv"
)

rais_df.to_csv(
    output_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(output_path)
