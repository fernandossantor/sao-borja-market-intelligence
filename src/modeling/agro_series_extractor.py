import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

AGRO_FILE = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/agro/"
    "Área plantada e colhida SB.xlsx"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# SHEETS
# =========================================

SHEET_MAPPING = {

    "Área plantada ou destinada":
        "area_plantada",

    "Área colhida":
        "area_colhida",

    "Quantidade produzida":
        "quantidade_produzida",

    "Rendimento médio":
        "rendimento_medio",

    "Valor da produção":
        "valor_producao"

}

print("\n===================================")
print("AGRO SERIES EXTRACTOR")
print("===================================\n")

all_rows = []

# =========================================
# PROCESS SHEETS
# =========================================

for sheet_name, variable in (
    SHEET_MAPPING.items()
):

    print(
        f"Processando: {sheet_name}"
    )

    df = pd.read_excel(
        AGRO_FILE,
        sheet_name=sheet_name,
        header=0
    )

    product_col = df.columns[0]

    years = []

    for col in df.columns[1:]:

        try:

            year = int(col)
            years.append(col)

        except:
            pass

    for _, row in df.iterrows():

        product = str(
            row[product_col]
        )

        if (
            pd.isna(product)
            or product.lower()
            == "nan"
        ):
            continue

        for year_col in years:

            value = row[year_col]

            try:

                value = float(
                    str(value)
                    .replace(".", "")
                    .replace(",", ".")
                )

            except:
                continue

            all_rows.append({

                "year":
                    int(year_col),

                "product":
                    product,

                "variable":
                    variable,

                "value":
                    value

            })

# =========================================
# OUTPUT
# =========================================

series_df = pd.DataFrame(
    all_rows
)

print("\n===================================")
print("SERIES")
print("===================================\n")

print(
    series_df.head(30)
)

print(
    f"\nRegistros: {len(series_df)}"
)

# =========================================
# EXPORT
# =========================================

export_file = os.path.join(
    EXPORT_PATH,
    "agro_series.csv"
)

series_df.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
