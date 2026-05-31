import pandas as pd
import numpy as np
import os
import re

# =====================================
# CONFIG
# =====================================

FILE_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/rais/"
    "tabela1735.xlsx"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =====================================
# START
# =====================================

print("\n===================================")
print("RAIS 1735 PROFILER")
print("===================================\n")

# =====================================
# LOAD
# =====================================

xls = pd.ExcelFile(FILE_PATH)

print("ABAS:")
print(xls.sheet_names)

results = []

# =====================================
# SCAN SHEETS
# =====================================

for sheet in xls.sheet_names:

    if str(sheet).lower() == "notas":
        continue

    print("\n-----------------------------------")
    print(sheet)
    print("-----------------------------------")

    try:

        df = pd.read_excel(
            FILE_PATH,
            sheet_name=sheet,
            header=None
        )

        print("Shape:")
        print(df.shape)

        print("\nPrimeiras 20 linhas:")
        print(df.head(20))

        blob = " ".join(
            map(
                str,
                df.head(100)
                .astype(str)
                .values
                .flatten()
            )
        )

        years = sorted(
            set(
                int(x)
                for x in re.findall(
                    r"(19\d{2}|20\d{2})",
                    blob
                )
            )
        )

        print("\nAnos encontrados:")
        print(years[:20])

        results.append({

            "sheet":
                sheet,

            "rows":
                len(df),

            "cols":
                len(df.columns),

            "years_found":
                len(years),

            "start_year":
                min(years)
                if years else None,

            "end_year":
                max(years)
                if years else None

        })

    except Exception as e:

        print(e)

# =====================================
# SUMMARY
# =====================================

summary = pd.DataFrame(
    results
)

print("\n===================================")
print("SUMMARY")
print("===================================\n")

print(summary)

# =====================================
# EXPORT
# =====================================

export_file = os.path.join(
    EXPORT_PATH,
    "rais_1735_profile.csv"
)

summary.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
