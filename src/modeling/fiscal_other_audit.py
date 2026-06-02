import pandas as pd
import os

print("\n===================================")
print("FISCAL OTHER AUDIT")
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

other = df[
    df["domain"] == "other"
]

summary = (
    other.groupby("source_file")["value"]
    .agg(
        total_value="sum",
        records="count"
    )
    .reset_index()
)

summary["share_other_pct"] = (
    summary["total_value"]
    /
    summary["total_value"].sum()
    * 100
)

summary = summary.sort_values(
    "total_value",
    ascending=False
)

print(summary)

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_other_audit.csv"
)

summary.to_csv(
    export_file,
    index=False
)

print("\nExportado:")
print(export_file)
