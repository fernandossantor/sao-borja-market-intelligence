import pandas as pd
import os

print("\n===================================")
print("FISCAL CATALOG BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

inventory = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_inventory.csv"
    )
)

def classify(name):

    name = name.lower()

    structural = [
        "fpm",
        "fundeb",
        "itr",
        "royalties",
        "petróleo",
        "petroleo",
        "compens"
    ]

    if any(x in name for x in structural):

        return "structural_transfer"

    return "programmatic_transfer"

inventory["category"] = (
    inventory["file"]
    .apply(classify)
)

catalog = inventory[
    [
        "file",
        "category"
    ]
]

print(catalog)

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_catalog.csv"
)

catalog.to_csv(
    export_file,
    index=False
)

print("\nExportado:")
print(export_file)
