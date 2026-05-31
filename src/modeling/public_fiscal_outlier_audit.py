import pandas as pd

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

panel = pd.read_csv(
    f"{EXPORT_PATH}/public_fiscal_panel.csv"
)

print("\n===================================")
print("PUBLIC FISCAL OUTLIER AUDIT")
print("===================================\n")

annual = (

    panel

    .groupby(
        ["year","source"]
    )["value"]

    .sum()

    .reset_index()

)

pivot = annual.pivot(
    index="source",
    columns="year",
    values="value"
)

pivot = pivot.fillna(0)

if 2021 in pivot.columns:

    for year in pivot.columns:

        if year == 2021:
            continue

        pivot[f"growth_{year}"] = (
            pivot[year]
            /
            pivot[2021]
            * 100
        )

print(
    pivot.sort_values(
        "growth_2024",
        ascending=False
    )
    .head(30)
)
