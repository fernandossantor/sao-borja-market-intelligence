import pandas as pd
import numpy as np
import os
import re

ROOT = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/rais"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

FILES = [
    "tabela1734.xlsx",
    "tabela1735.xlsx",
    "tabela2933.xlsx",
    "tabela3421.xlsx",
    "tabela6449.xlsx",
    "tabela6450.xlsx",
    "tabela1685.xlsx",
    "tabela993.xlsx",
    "tabela10206.xlsx",
    "tabela10299.xlsx",
    "tabela10381.xlsx"
]

print("\n===================================")
print("RAIS HISTORICAL COVERAGE AUDIT")
print("===================================\n")

records = []

for file_name in FILES:

    file_path = os.path.join(
        ROOT,
        file_name
    )

    if not os.path.exists(file_path):

        print(
            f"[MISSING] {file_name}"
        )
        continue

    print(file_name)

    try:

        xls = pd.ExcelFile(file_path)

        all_years = set()

        max_rows = 0
        max_cols = 0

        for sheet in xls.sheet_names:

            try:

                df = pd.read_excel(
                    file_path,
                    sheet_name=sheet,
                    header=None
                )

                max_rows = max(
                    max_rows,
                    len(df)
                )

                max_cols = max(
                    max_cols,
                    len(df.columns)
                )

                text = " ".join(
                    map(
                        str,
                        df.head(50)
                        .astype(str)
                        .values
                        .flatten()
                    )
                )

                years = re.findall(
                    r"(19\d{2}|20\d{2})",
                    text
                )

                years = [
                    int(y)
                    for y in years
                    if 1980 <= int(y) <= 2035
                ]

                all_years.update(years)

            except:
                pass

        if len(all_years) > 0:

            records.append({

                "file_name":
                    file_name,

                "start_year":
                    min(all_years),

                "end_year":
                    max(all_years),

                "years":
                    len(all_years),

                "rows":
                    max_rows,

                "cols":
                    max_cols

            })

    except Exception as e:

        print(e)

coverage = pd.DataFrame(
    records
)

coverage = coverage.sort_values(
    [
        "start_year",
        "end_year"
    ]
)

print("\n===================================")
print("COVERAGE")
print("===================================\n")

print(coverage)

export_file = os.path.join(
    EXPORT_PATH,
    "rais_historical_coverage.csv"
)

coverage.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
