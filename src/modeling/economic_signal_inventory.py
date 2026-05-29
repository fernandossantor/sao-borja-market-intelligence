import pandas as pd
import numpy as np
import os
import glob

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# FILE DISCOVERY
# =========================================

csv_files = glob.glob(
    os.path.join(EXPORT_PATH, "*.csv")
)

print("\n===================================")
print("ECONOMIC SIGNAL INVENTORY")
print("===================================\n")

print(f"Arquivos encontrados: {len(csv_files)}")

inventory = []

# =========================================
# PROCESS FILES
# =========================================

for file_path in csv_files:

    file_name = os.path.basename(file_path)

    print(f"\n[PROCESSANDO] {file_name}")

    try:

        df = pd.read_csv(
            file_path,
            low_memory=False
        )

        rows = len(df)
        cols = len(df.columns)

        # ------------------------------
        # DETECT YEAR COLUMN
        # ------------------------------

        year_col = None

        for c in df.columns:

            if str(c).lower() in [
                "year",
                "ano",
                "ano_referencia",
                "ano de referência"
            ]:

                year_col = c
                break

        start_year = None
        end_year = None

        if year_col:

            years = pd.to_numeric(
                df[year_col],
                errors="coerce"
            ).dropna()

            if len(years) > 0:

                start_year = int(
                    years.min()
                )

                end_year = int(
                    years.max()
                )

        # ------------------------------
        # VARIABLE INVENTORY
        # ------------------------------

        for col in df.columns:

            null_pct = (
                df[col]
                .isna()
                .mean()
                * 100
            )

            inventory.append({

                "file_name":
                    file_name,

                "variable":
                    col,

                "rows":
                    rows,

                "columns":
                    cols,

                "start_year":
                    start_year,

                "end_year":
                    end_year,

                "non_null":
                    int(
                        df[col]
                        .notna()
                        .sum()
                    ),

                "null_pct":
                    round(
                        null_pct,
                        2
                    ),

                "dtype":
                    str(
                        df[col].dtype
                    )

            })

    except Exception as e:

        print(
            f"[ERRO] {file_name} -> {e}"
        )

# =========================================
# OUTPUT
# =========================================

inventory_df = pd.DataFrame(
    inventory
)

print("\n===================================")
print("SIGNAL INVENTORY")
print("===================================\n")

print(
    inventory_df.head(20)
)

print(
    f"\nVariáveis catalogadas: "
    f"{len(inventory_df)}"
)

# =========================================
# FILE SUMMARY
# =========================================

summary = (
    inventory_df
    .groupby("file_name")
    .agg({
        "variable":"count",
        "start_year":"first",
        "end_year":"first"
    })
    .reset_index()
)

summary.columns = [
    "file_name",
    "variables",
    "start_year",
    "end_year"
]

print("\n===================================")
print("FILE SUMMARY")
print("===================================\n")

print(summary)

# =========================================
# EXPORTS
# =========================================

inventory_path = os.path.join(
    EXPORT_PATH,
    "economic_signal_inventory.csv"
)

summary_path = os.path.join(
    EXPORT_PATH,
    "economic_signal_summary.csv"
)

inventory_df.to_csv(
    inventory_path,
    index=False
)

summary.to_csv(
    summary_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(inventory_path)
print(summary_path)
