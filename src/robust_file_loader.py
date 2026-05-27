import pandas as pd
import csv
from brazilian_data_rules import (
    SUPPORTED_ENCODINGS,
    SUPPORTED_DELIMITERS
)

# =========================================
# DETECT DELIMITER
# =========================================

def detect_delimiter(file_path):

    with open(file_path, "r", encoding="latin1") as f:

        sample = f.read(5000)

        sniffer = csv.Sniffer()

        delimiter = sniffer.sniff(
            sample,
            delimiters=";,|\t"
        ).delimiter

    return delimiter

# =========================================
# LOAD CSV ROBUSTLY
# =========================================

def load_csv_robust(file_path):

    last_error = None

    for encoding in SUPPORTED_ENCODINGS:

        try:

            delimiter = detect_delimiter(file_path)

            print(
                f"[INFO] encoding={encoding} "
                f"delimiter='{delimiter}'"
            )

            df = pd.read_csv(
                file_path,
                encoding=encoding,
                delimiter=delimiter,
                low_memory=False,
                on_bad_lines="skip"
            )

            print(
                f"[OK] arquivo carregado "
                f"linhas={len(df)}"
            )

            return df

        except Exception as e:

            last_error = e

            print(
                f"[ERRO] encoding={encoding} "
                f"-> {e}"
            )

    raise Exception(
        f"Falha ao carregar arquivo: {last_error}"
    )

# =========================================
# LOAD EXCEL
# =========================================

def load_excel_robust(file_path):

    try:

        df = pd.read_excel(file_path)

        print(
            f"[OK] Excel carregado "
            f"linhas={len(df)}"
        )

        return df

    except Exception as e:

        raise Exception(
            f"Falha Excel: {e}"
        )
