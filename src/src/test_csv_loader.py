from loaders.smart_csv_loader import (
    load_csv_smart
)

FILE = (
    "/CAMINHO/DE/UM/CSV/FISCAL.csv"
)

df = load_csv_smart(FILE)

print(df.head())

print("\nCOLUNAS:\n")

print(df.columns.tolist())
