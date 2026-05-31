import pandas as pd
import os
import glob

# =========================================
# CONFIG
# =========================================

RAW_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/fiscal"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

print("\n===================================")
print("PUBLIC FISCAL PANEL BUILDER")
print("===================================\n")

# =========================================
# FILES
# =========================================

files = glob.glob(
    os.path.join(
        RAW_PATH,
        "*.csv"
    )
)

print(
    f"Arquivos encontrados: {len(files)}"
)

# =========================================
# PANEL
# =========================================

rows = []

for file_path in files:

    file_name = os.path.basename(
        file_path
    )

    print(
        f"\nProcessando: {file_name}"
    )

    try:

        df = pd.read_csv(
            file_path,
            sep=";",
            encoding="utf-8"
        )

    except:

        try:

            df = pd.read_csv(
                file_path,
                sep=";",
                encoding="latin1"
            )

        except Exception as e:

            print(e)
            continue

    if (
        "Mês/Ano"
        not in df.columns
    ):
        continue

    if (
        "Valor Transferido"
        not in df.columns
    ):
        continue

    source = (
        str(file_name)
        .replace(".csv", "")
    )

    for _, row in df.iterrows():

        try:

            month, year = (
                str(
                    row["Mês/Ano"]
                )
                .split("/")
            )

            value = str(
                row[
                    "Valor Transferido"
                ]
            )

            value = (
                value
                .replace(".", "")
                .replace(",", ".")
            )

            value = float(value)

        except:

            continue

        rows.append({

            "year":
                int(year),

            "month":
                int(month),

            "source":
                source,

            "value":
                value

        })

# =========================================
# OUTPUT
# =========================================

panel = pd.DataFrame(
    rows
)

print("\n===================================")
print("PANEL")
print("===================================\n")

print(
    panel.head(30)
)

print(
    f"\nRegistros: {len(panel)}"
)

# =========================================
# SUMMARY
# =========================================

summary = (

    panel

    .groupby(
        "source"
    )["value"]

    .sum()

    .reset_index()

    .sort_values(
        "value",
        ascending=False
    )

)

print("\n===================================")
print("TOP SOURCES")
print("===================================\n")

print(
    summary.head(30)
)

# =========================================
# EXPORT
# =========================================

panel_file = os.path.join(
    EXPORT_PATH,
    "public_fiscal_panel.csv"
)

summary_file = os.path.join(
    EXPORT_PATH,
    "public_fiscal_summary.csv"
)

panel.to_csv(
    panel_file,
    index=False
)

summary.to_csv(
    summary_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(panel_file)
print(summary_file)
