import pandas as pd
import os

# =====================================
# CONFIG
# =====================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

# =====================================
# FILTRO INSTITUCIONAL
# =====================================

institutional = inventory[
    inventory["category"] == "institutional"
]

print("\n===================================")
print("INSTITUTIONAL CSV PROFILER")
print("===================================\n")

print(
    f"Arquivos encontrados: "
    f"{len(institutional)}"
)

# =====================================
# TESTE DE LEITURA
# =====================================

encodings = [
    "utf-8",
    "latin1",
    "cp1252"
]

separators = [
    ";",
    ",",
    "|",
    "\t"
]

results = []

for _, row in institutional.iterrows():

    file_name = row["file_name"]
    full_path = row["full_path"]

    if not str(file_name).lower().endswith(".csv"):
        continue

    print("\n-----------------------------------")
    print(file_name)
    print("-----------------------------------")

    success = False

    for enc in encodings:

        for sep in separators:

            try:

                df = pd.read_csv(
                    full_path,
                    encoding=enc,
                    sep=sep,
                    low_memory=False,
                    nrows=20
                )

                print(
                    f"OK | enc={enc} | sep={repr(sep)} "
                    f"| shape={df.shape}"
                )

                results.append({

                    "file_name": file_name,
                    "encoding": enc,
                    "separator": sep,
                    "rows": len(df),
                    "cols": len(df.columns)

                })

                success = True
                break

            except:
                pass

        if success:
            break

    if not success:

        print("FALHOU")

        results.append({

            "file_name": file_name,
            "encoding": None,
            "separator": None,
            "rows": None,
            "cols": None

        })

# =====================================
# EXPORT
# =====================================

results_df = pd.DataFrame(results)

export_file = (
    f"{EXPORT_PATH}/institutional_csv_profile.csv"
)

results_df.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
