import pandas as pd

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

panel = pd.read_csv(
    f"{EXPORT_PATH}/public_fiscal_panel.csv"
)

print("\n===================================")
print("PUBLIC FISCAL COVERAGE AUDIT")
print("===================================\n")

coverage = (

    panel

    .groupby(
        ["year","source"]
    )["month"]

    .nunique()

    .reset_index(
        name="months"
    )

)

print(
    coverage
    .sort_values(
        ["year","source"]
    )
)

print("\n===================================")
print("MONTHS BY YEAR")
print("===================================\n")

summary = (

    coverage

    .groupby("year")

    ["months"]

    .mean()

    .reset_index()

)

print(summary)
