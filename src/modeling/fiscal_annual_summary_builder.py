import pandas as pd
import os

print("\n===================================")
print("FISCAL ANNUAL SUMMARY")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_transfer_panel.csv"
    )
)

annual = (
    df.groupby("year")["value"]
    .sum()
    .reset_index()
)

annual.columns = [
    "year",
    "transfer_total"
]

annual["growth_pct"] = (
    annual["transfer_total"]
    .pct_change(fill_method=None)
    * 100
)

structural = (
    df[
        df["category"]
        ==
        "structural_transfer"
    ]
    .groupby("year")["value"]
    .sum()
)

programmatic = (
    df[
        df["category"]
        ==
        "programmatic_transfer"
    ]
    .groupby("year")["value"]
    .sum()
)

annual["structural_transfer"] = (
    annual["year"]
    .map(structural)
)

annual["programmatic_transfer"] = (
    annual["year"]
    .map(programmatic)
)

annual["structural_share_pct"] = (
    annual["structural_transfer"]
    /
    annual["transfer_total"]
    * 100
)

annual["programmatic_share_pct"] = (
    annual["programmatic_transfer"]
    /
    annual["transfer_total"]
    * 100
)

print(annual)

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_annual_summary.csv"
)

annual.to_csv(
    export_file,
    index=False
)

print("\nExportado:")
print(export_file)
