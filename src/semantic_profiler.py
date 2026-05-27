import os
import pandas as pd
import numpy as np

# =========================================
# CONFIG
# =========================================

BASE_PATH = "/content/drive/MyDrive/Colab Notebooks/_sao_borja/raw"

EXPORT_PATH = "/content/drive/MyDrive/Colab Notebooks/_sao_borja/exports"

SUPPORTED_EXTENSIONS = [
    ".csv",
    ".xlsx",
    ".xls"
]

# =========================================
# HELPERS
# =========================================

def detect_semantic_type(series, column_name):

    col = column_name.lower()

    # -------------------------------------
    # IDENTIFIERS
    # -------------------------------------

    if any(x in col for x in [
        "codigo",
        "cod",
        "ibge",
        "cnae",
        "cbo",
        "id"
    ]):
        return "identifier"

    # -------------------------------------
    # DATES
    # -------------------------------------

    if any(x in col for x in [
        "ano",
        "mes",
        "data"
    ]):
        return "date"

    # -------------------------------------
    # COLUMN ANALYSIS
    # -------------------------------------

    if pd.api.types.is_numeric_dtype(series):

        unique_ratio = (
            series.nunique(dropna=True)
            / max(len(series), 1)
        )

        has_decimal = (
            (series.dropna() % 1 != 0).any()
            if not series.dropna().empty
            else False
        )

        max_value = series.max(skipna=True)
        min_value = series.min(skipna=True)

        # ---------------------------------
        # POSSIBLE IDENTIFIER
        # ---------------------------------

        if (
            not has_decimal and
            unique_ratio > 0.9 and
            max_value > 100000
        ):
            return "possible_identifier"

        # ---------------------------------
        # POSSIBLE CURRENCY
        # ---------------------------------

        if (
            has_decimal and
            max_value > 1000
        ):
            return "possible_currency"

        # ---------------------------------
        # POSSIBLE PERCENTAGE
        # ---------------------------------

        if (
            min_value >= 0 and
            max_value <= 100
        ):
            return "possible_percentage"

        # ---------------------------------
        # POSSIBLE QUANTITY
        # ---------------------------------

        return "possible_quantity"

    # -------------------------------------
    # TEXT
    # -------------------------------------

    return "text"

# =========================================
# FILE PROCESSOR
# =========================================

profiles = []

for root, dirs, files in os.walk(BASE_PATH):

    for file in files:

        extension = os.path.splitext(file)[1].lower()

        if extension not in SUPPORTED_EXTENSIONS:
            continue

        path = os.path.join(root, file)

        print(f"\n[PROCESSANDO] {file}")

        try:

            # ---------------------------------
            # CSV
            # ---------------------------------

            if extension == ".csv":

                df = pd.read_csv(
                    path,
                    low_memory=False
                )

            # ---------------------------------
            # EXCEL
            # ---------------------------------

            else:

                df = pd.read_excel(path)

            # ---------------------------------
            # COLUMN PROFILING
            # ---------------------------------

            for col in df.columns:

                series = df[col]

                profile = {
                    "file_name": file,
                    "column_name": col,
                    "dtype": str(series.dtype),
                    "nulls": int(series.isna().sum()),
                    "unique_values": int(series.nunique(dropna=True)),
                    "semantic_type": detect_semantic_type(series, col)
                }

                # Numeric stats
                if pd.api.types.is_numeric_dtype(series):

                    profile["min"] = float(series.min(skipna=True))
                    profile["max"] = float(series.max(skipna=True))
                    profile["mean"] = float(series.mean(skipna=True))

                else:

                    profile["min"] = None
                    profile["max"] = None
                    profile["mean"] = None

                profiles.append(profile)

        except Exception as e:

            print(f"[ERRO] {file} -> {e}")

# =========================================
# EXPORT
# =========================================

profile_df = pd.DataFrame(profiles)

os.makedirs(EXPORT_PATH, exist_ok=True)

csv_path = os.path.join(
    EXPORT_PATH,
    "semantic_profiles.csv"
)

profile_df.to_csv(csv_path, index=False)

# =========================================
# SUMMARY
# =========================================

print("\n===================================")
print("SEMANTIC PROFILING FINALIZADO")
print("===================================\n")

print(profile_df["semantic_type"].value_counts())

print(f"\nArquivo exportado:\n{csv_path}")
