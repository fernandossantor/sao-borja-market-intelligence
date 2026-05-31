import pandas as pd
import numpy as np
import os

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

SHEET_NAME = "Pessoal ocupado total"

# =====================================
# HELPERS
# =====================================

def to_number(v):

    if pd.isna(v):
        return np.nan

    v = str(v).strip()

    if v in ["-", "X", "x", "..", "...", ""]:
        return np.nan

    try:
        return float(
            v.replace(".", "")
             .replace(",", ".")
        )
    except:
        return np.nan


# =====================================
# START
# =====================================

print("\n===================================")
print("RAIS 1735 RECONSTRUCTED EMPLOYMENT")
print("===================================\n")

df = pd.read_excel(
    FILE_PATH,
    sheet_name=SHEET_NAME,
    header=None
)

print("Shape:", df.shape)

# =====================================
# YEARS
# =====================================

year_cols = {}

for col in range(df.shape[1]):

    year = df.iloc[3, col]

    try:

        year = int(year)

        if 1990 <= year <= 2035:

            year_cols[year] = col

    except:
        pass

print("\nAnos encontrados:")
print(sorted(year_cols.keys()))

# =====================================
# SECTORS
# =====================================

sector_rows = []

for row in range(5, 23):

    sector = str(df.iloc[row, 3]).strip()

    if sector and sector != "nan":

        sector_rows.append(
            (row, sector)
        )

print(
    f"\nSetores encontrados: "
    f"{len(sector_rows)}"
)

# =====================================
# EXTRACT
# =====================================

records = []

for year, start_col in year_cols.items():

    total_col = start_col

    # faixas dentro do bloco anual
    band_cols = [
        start_col + 2,
        start_col + 4,
        start_col + 6,
        start_col + 8,
        start_col + 10,
        start_col + 12,
        start_col + 14,
        start_col + 16,
        start_col + 18
    ]

    for row, sector in sector_rows:

        total_value = to_number(
            df.iloc[row, total_col]
        )

        if pd.notna(total_value):

            employment = total_value
            source = "observed"

        else:

            values = []

            for c in band_cols:

                if c >= df.shape[1]:
                    continue

                v = to_number(
                    df.iloc[row, c]
                )

                if pd.notna(v):
                    values.append(v)

            if len(values) > 0:

                employment = sum(values)
                source = "reconstructed"

            else:

                employment = np.nan
                source = "missing"

        records.append({

            "year": year,
            "sector": sector,
            "employment_total": employment,
            "source": source

        })

# =====================================
# OUTPUT
# =====================================

result = pd.DataFrame(records)

result = result.dropna(
    subset=["employment_total"]
)

result = result.sort_values(
    ["year", "sector"]
)

print("\n===================================")
print("SERIES")
print("===================================\n")

print(result.head(50))

print(
    "\nRegistros:",
    len(result)
)

print(
    "Anos:",
    result.year.min(),
    "-",
    result.year.max()
)

print(
    "Setores:",
    result.sector.nunique()
)

print(
    "\nSource distribution:"
)

print(
    result["source"]
    .value_counts()
)

# =====================================
# EXPORT
# =====================================

export_file = os.path.join(
    EXPORT_PATH,
    "rais_1735_reconstructed_employment.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
