import pandas as pd
import os

from loaders.smart_excel_loader import (
    load_excel_smart
)

from loaders.robust_file_loader import (
    load_csv_robust
)

from territorial.territorial_filter import (
    filter_sao_borja
)

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# LOAD INVENTORY
# =========================================

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

# =========================================
# FILTER RAIS FILES
# =========================================

rais_files = inventory[
    inventory["category"] == "rais"
]

print("\n===================================")
print("RAIS FILES DETECTED")
print("===================================\n")

print(
    rais_files[[
        "file_name",
        "full_path"
    ]]
)

# =========================================
# STORAGE
# =========================================

valid_dataframes = []

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

        # =================================
        # LOAD
        # =================================

        if file_name.endswith(".csv"):

            df = load_csv_robust(file_path)

        else:

            df = load_excel_smart(file_path)

        print(f"[INFO] linhas carregadas: {len(df)}")
        print(f"[INFO] colunas carregadas: {len(df.columns)}")

        # =================================
        # MINIMUM STRUCTURE
        # =================================

        if len(df) < 5:

            print("[SKIP] poucas linhas")
            continue

        if len(df.columns) < 2:

            print("[SKIP] poucas colunas")
            continue

        # =================================
        # TERRITORIAL FILTER
        # =================================

        filtered_df, method = filter_sao_borja(
            df,
            file_name
        )

        print(f"[INFO] método territorial: {method}")
        print(f"[INFO] linhas após filtro: {len(filtered_df)}")

        # =================================
        # EMPTY
        # =================================

        if len(filtered_df) == 0:

            print("[SKIP] sem dados territoriais")
            continue

        # =================================
        # CLEAN EMPTY
        # =================================

        filtered_df = filtered_df.dropna(
            axis=1,
            how="all"
        )

        # =================================
        # REMOVE UNNAMED
        # =================================

        filtered_df = filtered_df.loc[
            :,
            ~filtered_df.columns.astype(str)
            .str.contains("^Unnamed")
        ]

        # =================================
        # REJECT HORIZONTAL GARBAGE
        # =================================

        if len(filtered_df.columns) > 40:

            print("[SKIP] estrutura horizontal inválida")
            continue

        # =================================
        # ADD METADATA
        # =================================

        filtered_df["_source_file"] = file_name
        filtered_df["_territorial_method"] = method

        # =================================
        # STORE
        # =================================

        valid_dataframes.append(
            filtered_df
        )

        print("[OK] dataframe válido armazenado")

    except Exception as e:

        print(f"[ERRO] {file_name} -> {e}")

# =========================================
# FINAL CONSOLIDATION
# =========================================

if len(valid_dataframes) == 0:

    raise Exception(
        "Nenhum dataframe RAIS válido."
    )

rais_df = pd.concat(
    valid_dataframes,
    ignore_index=True
)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("RAIS CONSOLIDATED")
print("===================================\n")

print(rais_df.shape)

print("\nColunas:\n")

print(rais_df.columns.tolist())

# =========================================
# EXPORT
# =========================================

export_path = os.path.join(
    EXPORT_PATH,
    "rais_consolidated.csv"
)

rais_df.to_csv(
    export_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_path)
