import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# LOAD INVENTORY
# =========================================

inventory = pd.read_csv(
    f"{EXPORT_PATH}/inventory.csv"
)

census_files = inventory[
    inventory["file_name"]
    .str.contains(
        "Censo 2022",
        case=False,
        na=False
    )
]

print("\n===================================")
print("CENSUS FILE PROFILER")
print("===================================\n")

print(
    f"Arquivos encontrados: "
    f"{len(census_files)}"
)

results = []

# =========================================
# PROCESS
# =========================================

for _, row in census_files.iterrows():

    file_name = row["file_name"]
    full_path = row["full_path"]

    print("\n-----------------------------------")
    print(file_name)
    print("-----------------------------------")

    try:

        excel = pd.ExcelFile(
            full_path
        )

        print(
            f"Abas: {excel.sheet_names}"
        )

        for sheet in excel.sheet_names:

            try:

                raw = pd.read_excel(
                    full_path,
                    sheet_name=sheet,
                    header=None
                )

                results.append({

                    "file_name":
                        file_name,

                    "sheet":
                        sheet,

                    "rows":
                        len(raw),

                    "cols":
                        len(raw.columns),

                    "first_row":
                        str(
                            raw.iloc[0]
                            .tolist()
                        ),

                    "second_row":
                        str(
                            raw.iloc[1]
                            .tolist()
                        )

                })

            except Exception as e:

                print(e)

    except Exception as e:

        print(e)

# =========================================
# OUTPUT
# =========================================

profile = pd.DataFrame(
    results
)

print("\n===================================")
print("PROFILE")
print("===================================\n")

print(
    profile.head(50)
)

profile.to_csv(
    f"{EXPORT_PATH}/census_profile.csv",
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(
    f"{EXPORT_PATH}/census_profile.csv"
)
