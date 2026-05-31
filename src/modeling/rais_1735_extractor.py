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

def clean_value(v):

    if pd.isna(v):
        return np.nan

    v = str(v).strip()

    if v in [
        "-",
        "X",
        "x",
        "..",
        "...",
        ""
    ]:
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
print("RAIS 1735 EXTRACTOR")
print("===================================\n")

# =====================================
# LOAD
# =====================================

df = pd.read_excel(
    FILE_PATH,
    sheet_name=SHEET_NAME,
    header=None
)

print("Shape:")
print(df.shape)

# =====================================
# CNAE LINES
# =====================================

sector_rows = []

for row_idx in range(len(df)):

    sector = df.iloc[row_idx, 3]

    if pd.isna(sector):
        continue

    sector = str(sector).strip()

    if sector in [

        "Total",

        "A Agricultura, pecuária, silvicultura e exploração florestal",
        "B Pesca",
        "C Indústrias extrativas",
        "D Indústrias de transformação",
        "E Produção e distribuição de eletricidade, gás e água",
        "F Construção",
        "G Comércio; reparação de veículos automotores, objetos pessoais e domésticos",
        "H Alojamento e alimentação",
        "I Transporte, armazenagem e comunicações",
        "J Intermediação financeira, seguros, previdência complementar e serviços relacionados",
        "K Atividades imobiliárias, aluguéis e serviços prestados às empresas",
        "L Administração pública, defesa e seguridade social",
        "M Educação",
        "N Saúde e serviços sociais",
        "O Outros serviços coletivos, sociais e pessoais",
        "P Serviços domésticos",
        "Q Organismos internacionais e outras instituições extraterritoriais"

    ]:

        sector_rows.append(
            (row_idx, sector)
        )

print(
    f"Setores encontrados: "
    f"{len(sector_rows)}"
)

# =====================================
# YEAR BLOCKS
# =====================================

year_blocks = []

for col in range(df.shape[1]):

    value = df.iloc[3, col]

    try:

        year = int(value)

        if (
            year >= 1990
            and year <= 2035
        ):

            year_blocks.append(
                (
                    year,
                    col
                )
            )

    except:

        pass

print("\nAnos encontrados:")
print(
    [x[0] for x in year_blocks]
)

# =====================================
# EXTRACT
# =====================================

records = []

for year, year_col in year_blocks:

    total_col = year_col

    for row_idx, sector in sector_rows:

        value = clean_value(
            df.iloc[
                row_idx,
                total_col
            ]
        )

        records.append({

            "year":
                year,

            "sector":
                sector,

            "employment":
                value

        })

# =====================================
# OUTPUT
# =====================================

result = pd.DataFrame(
    records
)

result = result.dropna(
    subset=["employment"]
)

result = result.sort_values(
    [
        "year",
        "sector"
    ]
)

print("\n===================================")
print("EMPLOYMENT SERIES")
print("===================================\n")

print(
    result.head(100)
)

print(
    f"\nRegistros: {len(result)}"
)

print(
    f"Anos: "
    f"{result['year'].min()} - "
    f"{result['year'].max()}"
)

print(
    f"Setores: "
    f"{result['sector'].nunique()}"
)

# =====================================
# EXPORT
# =====================================

export_file = os.path.join(
    EXPORT_PATH,
    "rais_1735_employment_series.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
