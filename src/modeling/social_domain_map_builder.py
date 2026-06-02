import pandas as pd
import os

print("\n===================================")
print("SOCIAL DOMAIN MAP")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

catalog = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "social_catalog.csv"
    )
)

summary = (
    catalog.groupby("domain")
    .size()
    .reset_index(name="files")
)

summary["share_pct"] = (
    summary["files"]
    /
    summary["files"].sum()
    * 100
)

summary = summary.sort_values(
    "files",
    ascending=False
)

print(summary)

export_file = os.path.join(
    EXPORT_PATH,
    "social_domain_map.csv"
)

summary.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
