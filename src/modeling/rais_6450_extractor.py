import pandas as pd
import numpy as np
import os

FILE = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/rais/"
    "tabela6450.xlsx"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

SHEETS = {
    "Número de empresas e outras ...": "empresas",
    "Pessoal ocupado assalariado": "emprego",
    "Salários e outras remunerações": "salarios"
}

def to_number(v):

    if pd.isna(v):
        return np.nan

    v = str(v).strip()

    if v in ["-", "X", "..", "...", ""]:
        return np.nan

    try:
        return float(
            v.replace(".", "")
             .replace(",", ".")
        )
    except:
        return np.nan

print("\n===================================")
print("RAIS 6450 EXTRACTOR")
print("===================================\n")

records = []

for sheet, metric in SHEETS.items():

    print("Processando:", metric)

    df = pd.read_excel(
        FILE,
        sheet_name=sheet,
        header=None
    )

    current_year = None

    for col in range(df.shape[1]):

        year = df.iloc[3, col]

        if pd.notna(year):

            try:
                current_year = int(year)
            except:
                pass

        sector = df.iloc[4, col]
        value = to_number(
            df.iloc[5, col]
        )

        if (
            current_year is not None
            and pd.notna(sector)
        ):

            records.append({

                "year":
                    current_year,

                "sector":
                    str(sector).strip(),

                "metric":
                    metric,

                "value":
                    value

            })

result = pd.DataFrame(records)

print("\n===================================")
print("RESULTADO")
print("===================================\n")

print(result.head(30))

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

export_file = os.path.join(
    EXPORT_PATH,
    "rais_6450_panel.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
