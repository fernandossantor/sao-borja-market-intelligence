from loaders.smart_csv_loader import (
    load_csv_smart
)

FILE = (
    "/content/drive/MyDrive/Colab Notebooks/_sao_borja/raw/fiscal/Constitucionais e Royalties FPM 2020 - 2026.csv"
)

df = load_csv_smart(FILE)

print(df.head())

print("\nCOLUNAS:\n")

print(df.columns.tolist())
