import pandas as pd

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    EXPORT_PATH +
    "/private_employment_long_history.csv"
)

print("\n===================================")
print("EMPLOYMENT AUDIT")
print("===================================\n")

print("Shape:")
print(df.shape)

print("\nAnos:")

print(
    df["year"].min(),
    "-",
    df["year"].max()
)

print("\nDuplicados:")

print(
    df["year"].duplicated().sum()
)

print("\nValores faltantes:")

print(
    df["employment_total"]
    .isna()
    .sum()
)

print("\nSérie:")

print(df)
