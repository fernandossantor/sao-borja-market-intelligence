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
# LOAD MISSING FILES
# =========================================

missing = pd.read_csv(
    f"{EXPORT_PATH}/domain_missing_files.csv"
)

print("\n===================================")
print("MISSING DOMAIN PROFILER")
print("===================================\n")

print(
    f"Arquivos não detectados: "
    f"{len(missing)}"
)

results = []

# =========================================
# PROCESS
# =========================================

for _, row in missing.iterrows():

    category = row["category"]
    file_name = row["file_name"]
    full_path = row["full_path"]

    print("\n-----------------------------------")
    print(file_name)
    print("-----------------------------------")

    try:

        extension = (
            os.path.splitext(
                file_name
            )[1]
            .lower()
        )

        file_size_mb = round(
            os.path.getsize(
                full_path
            ) / 1024 / 1024,
            2
        )

        # =================================
        # EXCEL
        # =================================

        if extension in [
            ".xlsx",
            ".xls"
        ]:

            excel = pd.ExcelFile(
                full_path
            )

            for sheet in excel.sheet_names:

                try:

                    df = pd.read_excel(
                        full_path,
                        sheet_name=sheet,
                        header=None
                    )

                    results.append({

                        "category":
                            category,

                        "file_name":
                            file_name,

                        "extension":
                            extension,

                        "size_mb":
                            file_size_mb,

                        "sheet":
                            sheet,

                        "rows":
                            len(df),

                        "cols":
                            len(df.columns),

                        "sample_columns":
                            str(
                                list(
                                    df.iloc[
                                        0
                                    ].values[:10]
                                )
                            )

                    })

                except Exception:

                    continue

        # =================================
        # CSV
        # =================================

        elif extension == ".csv":

            df = pd.read_csv(
                full_path,
                nrows=50,
                low_memory=False
            )

            results.append({

                "category":
                    category,

                "file_name":
                    file_name,

                "extension":
                    extension,

                "size_mb":
                    file_size_mb,

                "sheet":
                    "csv",

                "rows":
                    len(df),

                "cols":
                    len(df.columns),

                "sample_columns":
                    str(
                        list(
                            df.columns[:10]
                        )
                    )

            })

    except Exception as e:

        results.append({

            "category":
                category,

            "file_name":
                file_name,

            "extension":
                "error",

            "size_mb":
                None,

            "sheet":
                None,

            "rows":
                None,

            "cols":
                None,

            "sample_columns":
                str(e)

        })

# =========================================
# OUTPUT
# =========================================

profile = pd.DataFrame(
    results
)

print("\n===================================")
print("PROFILE SUMMARY")
print("===================================\n")

print(
    profile.head(50)
)

print(
    f"\nTotal registros: "
    f"{len(profile)}"
)

# =========================================
# DOMAIN SUMMARY
# =========================================

domain_summary = (

    profile
    .groupby("category")
    .size()
    .reset_index(
        name="records"
    )

)

print("\n===================================")
print("DOMAIN SUMMARY")
print("===================================\n")

print(domain_summary)

# =========================================
# EXPORT
# =========================================

profile_file = os.path.join(
    EXPORT_PATH,
    "missing_domain_profile.csv"
)

profile.to_csv(
    profile_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(profile_file)
