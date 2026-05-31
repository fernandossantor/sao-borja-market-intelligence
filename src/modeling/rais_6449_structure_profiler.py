import pandas as pd

FILE = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/rais/"
    "tabela6449.xlsx"
)

print("\n===================================")
print("RAIS 6449 STRUCTURE PROFILER")
print("===================================\n")

xls = pd.ExcelFile(FILE)

print("ABAS:")
print(xls.sheet_names)

for sheet in xls.sheet_names:

    print("\n===================================")
    print(sheet)
    print("===================================\n")

    try:

        df = pd.read_excel(
            FILE,
            sheet_name=sheet,
            header=None
        )

        print("SHAPE:")
        print(df.shape)

        print("\nPRIMEIRAS 20 LINHAS x 40 COLUNAS:")
        print(
            df.iloc[:20, :40]
        )

    except Exception as e:

        print("[ERRO]")
        print(e)
