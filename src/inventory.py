import os
import json
import pandas as pd
from datetime import datetime

# =====================================
# CONFIG
# =====================================

BASE_PATH = "/content/drive/MyDrive/Colab Notebooks/_sao_borja/raw"

EXPORT_PATH = "/content/drive/MyDrive/Colab Notebooks/_sao_borja/exports"

VALID_EXTENSIONS = [
    "csv",
    "xlsx",
    "xls",
    "zip",
    "pdf"
]

# =====================================
# HELPERS
# =====================================

def infer_category(path):

    path_lower = path.lower()

    # PIB
    if "pib" in path_lower:
        return "pib"

    # RAIS / trabalho / empresas
    elif (
        "rais" in path_lower or
        "empreg" in path_lower or
        "empresa" in path_lower or
        "cbo" in path_lower or
        "cnae" in path_lower
    ):
        return "rais"

    # Agro
    elif (
        "agro" in path_lower or
        "pecu" in path_lower or
        "silvic" in path_lower or
        "lavoura" in path_lower or
        "rebanho" in path_lower
    ):
        return "agro"

    # Social
    elif (
        "bolsa" in path_lower or
        "social" in path_lower or
        "suas" in path_lower or
        "cadunico" in path_lower
    ):
        return "social"

    # Fiscal
    elif (
        "fpm" in path_lower or
        "fundeb" in path_lower or
        "itr" in path_lower or
        "royalt" in path_lower or
        "compensa" in path_lower or
        "fiscal" in path_lower or
        "orcament" in path_lower
    ):
        return "fiscal"

    # Institutional
    elif (
        "servid" in path_lower or
        "remuner" in path_lower or
        "aposent" in path_lower or
        "pens" in path_lower or
        "militar" in path_lower or
        "cadastro" in path_lower or
        "afast" in path_lower or
        "observ" in path_lower or
        "bacen" in path_lower
    ):
        return "institutional"

    # PDFs
    elif "pdf" in path_lower:
        return "pdf_context"

    return "unknown"
    
# =====================================
# INVENTORY
# =====================================

inventory = []

print("\nIniciando inventário...\n")

for root, dirs, files in os.walk(BASE_PATH):

    for file in files:

        try:

            extension = file.split(".")[-1].lower()

            if extension not in VALID_EXTENSIONS:
                continue

            full_path = os.path.join(root, file)

            size_mb = round(
                os.path.getsize(full_path) / (1024 * 1024),
                2
            )

            modified = datetime.fromtimestamp(
                os.path.getmtime(full_path)
            )

            category = infer_category(full_path)

            inventory.append({
                "file_name": file,
                "full_path": full_path,
                "extension": extension,
                "size_mb": size_mb,
                "modified_at": modified,
                "category": category,
                "status": "valid"
            })

            print(f"[OK] {file}")

        except Exception as e:

            print(f"[ERRO] {file} -> {e}")

# =====================================
# EXPORT
# =====================================

df = pd.DataFrame(inventory)

os.makedirs(EXPORT_PATH, exist_ok=True)

csv_path = os.path.join(EXPORT_PATH, "inventory.csv")
json_path = os.path.join(EXPORT_PATH, "inventory.json")

df.to_csv(csv_path, index=False)

df.to_json(
    json_path,
    orient="records",
    force_ascii=False,
    indent=4
)

# =====================================
# SUMMARY
# =====================================

print("\n=====================================")
print("INVENTÁRIO FINALIZADO")
print("=====================================")

print(f"Total de arquivos: {len(df)}")

print("\nArquivos por categoria:\n")
print(df["category"].value_counts())

print(f"\nCSV exportado em:\n{csv_path}")
print(f"\nJSON exportado em:\n{json_path}")
