import pandas as pd
import os

print("\n===================================")
print("PIB INVENTORY")
print("===================================\n")

CATALOG = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/catalog/files_catalog.csv"
)

catalog = pd.read_csv(CATALOG)

pib_files = catalog[
    catalog["category"] == "pib"
]

print("Arquivos PIB encontrados:")
print(len(pib_files))
print()

for _, row in pib_files.iterrows():

    path = row["full_path"]

    print("\n===================================")
    print(os.path.basename(path))
    print("===================================\n")

    try:

        xls = pd.ExcelFile(path)

        print("ABAS:")
        print(xls.sheet_names)

        for sheet in xls.sheet_names[:5]:

            print("\n--------------------")
            print(sheet)
            print("--------------------")

            try:

                df = pd.read_excel(
                    path,
                    sheet_name=sheet,
                    header=None
                )

                print("Shape:")
                print(df.shape)

                print(df.iloc[:10, :10])

            except Exception as e:
                print(e)

    except Exception as e:

        print(e)
