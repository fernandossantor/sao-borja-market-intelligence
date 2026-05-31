import pandas as pd
import os
import re

# =====================================
# CONFIG
# =====================================

RAIS_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/rais"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =====================================
# START
# =====================================

print("\n===================================")
print("RAIS SIDRA CENSUS")
print("===================================\n")

results = []

# =====================================
# FILE LOOP
# =====================================

for file_name in sorted(os.listdir(RAIS_PATH)):

    if not file_name.endswith(
        (".xlsx", ".xls")
    ):
        continue

    full_path = os.path.join(
        RAIS_PATH,
        file_name
    )

    print(file_name)

    try:

        xls = pd.ExcelFile(
            full_path
        )

        for sheet in xls.sheet_names:

            try:

                df = pd.read_excel(
                    full_path,
                    sheet_name=sheet,
                    header=None,
                    nrows=30
                )

                blob = " ".join(
                    map(
                        str,
                        df.astype(str)
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

                sample = (
                    blob[:300]
                    .replace("\n", " ")
                )

                results.append({

                    "file_name":
                        file_name,

                    "sheet":
                        sheet,

                    "rows_sample":
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
                        if years else None,

                    "sample":
                        sample

                })

            except Exception:
                pass

    except Exception as e:

        print(
            f"[ERRO] {file_name}"
        )

        print(e)

# =====================================
# OUTPUT
# =====================================

census = pd.DataFrame(
    results
)

census = census.sort_values(
    [
        "years_found",
        "cols"
    ],
    ascending=False
)

print("\n===================================")
print("TOP DATASETS")
print("===================================\n")

print(
    census[
        [
            "file_name",
            "sheet",
            "years_found",
            "start_year",
            "end_year",
            "cols"
        ]
    ]
    .head(100)
)

# =====================================
# EXPORT
# =====================================

out = os.path.join(
    EXPORT_PATH,
    "rais_sidra_census.csv"
)

census.to_csv(
    out,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(out)
