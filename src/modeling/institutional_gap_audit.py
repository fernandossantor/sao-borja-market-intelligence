import pandas as pd

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

signals = pd.read_csv(
    f"{EXPORT_PATH}/domain_signals.csv"
)

institutional_inventory = inventory[
    inventory["category"] == "institutional"
]

institutional_detected = set(
    signals[
        signals["category"] == "institutional"
    ]["file_name"]
)

missing = institutional_inventory[
    ~institutional_inventory["file_name"]
    .isin(institutional_detected)
]

print("\n===================================")
print("INSTITUTIONAL GAP AUDIT")
print("===================================\n")

print(
    missing[
        [
            "file_name",
            "full_path"
        ]
    ]
)

print(
    "\nTotal faltantes:",
    len(missing)
)
