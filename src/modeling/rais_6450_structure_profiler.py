import pandas as pd

FILE = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/rais/"
    "tabela6450.xlsx"
)

xls = pd.ExcelFile(FILE)

print(xls.sheet_names)

for sheet in xls.sheet_names:

    print("\n====================")
    print(sheet)
    print("====================\n")

    df = pd.read_excel(
        FILE,
        sheet_name=sheet,
        header=None
    )

    print(df.shape)

    print(df.iloc[:7,:40])
