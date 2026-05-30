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
# PROCESS
# =========================================

for sheet_name, variable in (
    SHEET_MAPPING.items()
):

    print(
        f"Processando: {sheet_name}"
    )

    raw = pd.read_excel(
        AGRO_FILE,
        sheet_name=sheet_name,
        header=None
    )

    # -----------------------------
    # Linha 1 contém os anos
    # -----------------------------

    years = raw.iloc[1]

    # -----------------------------
    # Produtos começam na linha 2
    # -----------------------------

    data = raw.iloc[2:].copy()

    data.columns = years

    product_col = data.columns[0]

    # -----------------------------
    # Loop produtos
    # -----------------------------

    for _, row in data.iterrows():

        product = str(
            row[product_col]
        ).strip()

        if (
            product == ""
            or product.lower() == "nan"
        ):
            continue

        for col in data.columns[1:]:

            try:

                year = int(col)

            except:

                continue

            value = row[col]

            if pd.isna(value):
                continue

            value = str(value).strip()

            if value in [
                "-",
                "...",
                ""
            ]:
                continue

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
                    year,

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

print(
    f"Produtos: {series_df['product'].nunique()}"
)

print(
    f"Anos: "
    f"{series_df['year'].min()} - "
    f"{series_df['year'].max()}"
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
