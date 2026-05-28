import os
import pandas as pd

from loaders.smart_excel_loader import (
    load_excel_smart
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

PIB_KEYWORDS = [
    "pib",
    "valor adicionado",
    "per capita"
]

# =========================================
# FILE DISCOVERY
# =========================================

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

pib_files = inventory[
    inventory["category"] == "pib"
]

print("\n===================================")
print("PIB FILES DETECTED")
print("===================================\n")

print(
    pib_files[[
        "file_name",
        "full_path"
    ]]
)

# =========================================
# PROCESSING
# =========================================

all_dataframes = []

for _, row in pib_files.iterrows():

    file_name = row["file_name"]
    path = row["full_path"]

    print("\n-----------------------------------")
    print(f"PROCESSANDO: {file_name}")
    print("-----------------------------------")

    try:

        # ---------------------------------
        # LOAD
        # ---------------------------------

        if path.endswith(".csv"):

            df = load_csv_robust(path)

        else:

            df = load_excel_smart(file_path)

        # REMOVE COLUNAS TOTALMENTE VAZIAS
        df = df.dropna(axis=1, how="all")

        print(
            f"[INFO] linhas carregadas: {len(df)}"
        )

        # ---------------------------------
        # TERRITORIAL FILTER
        # ---------------------------------

        filtered_df, method = filter_sao_borja(
            df,
            file_name
        )

        print(
            f"[INFO] método territorial: {method}"
        )

        print(
            f"[INFO] linhas após filtro: "
            f"{len(filtered_df)}"
        )

        # ---------------------------------
        # METADATA
        # ---------------------------------

        filtered_df["_source_file"] = file_name

        filtered_df["_territorial_method"] = method

        all_dataframes.append(filtered_df)

    except Exception as e:

        print(
            f"[ERRO] {file_name} -> {e}"
        )

# =========================================
# CONSOLIDATION
# =========================================

if all_dataframes:

    pib_df = pd.concat(
        all_dataframes,
        ignore_index=True
    )

    print("\n===================================")
    print("CONSOLIDAÇÃO FINAL")
    print("===================================\n")

    print(
        f"Total linhas consolidadas: "
        f"{len(pib_df)}"
    )

    print("\nColunas encontradas:\n")

    print(pib_df.columns.tolist())

    # -------------------------------------
    # EXPORT
    # -------------------------------------

    csv_path = os.path.join(
        EXPORT_PATH,
        "pib_consolidated.csv"
    )

   # parquet_path = os.path.join(
#     EXPORT_PATH,
#     "pib_consolidated.parquet"
# )

# pib_df.to_parquet(
#     parquet_path,
#     index=False
# )

    pib_df.to_parquet(
        parquet_path,
        index=False
    )

    print("\n===================================")
    print("EXPORT FINALIZADO")
    print("===================================\n")

    print(csv_path)
    print(parquet_path)

else:

    print(
        "\n[WARNING] Nenhum dataframe PIB consolidado"
    )
