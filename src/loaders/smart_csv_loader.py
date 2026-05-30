import pandas as pd

# =========================================
# SMART CSV LOADER
# =========================================

def load_csv_smart(file_path):

    delimiters = [
        ",",
        ";",
        "|",
        "\t"
    ]

    best_df = None
    best_cols = 0
    best_sep = None

    for sep in delimiters:

        try:

            df = pd.read_csv(
                file_path,
                sep=sep,
                low_memory=False
            )

            cols = len(df.columns)

            if cols > best_cols:

                best_cols = cols
                best_df = df
                best_sep = sep

        except Exception:

            continue

    if best_df is None:

        raise Exception(
            f"Não foi possível ler {file_path}"
        )

    print("\n===================================")
    print("SMART CSV DETECTED")
    print("===================================\n")

    print(
        f"Separador: {best_sep}"
    )

    print(
        f"Linhas: {len(best_df)}"
    )

    print(
        f"Colunas: {len(best_df.columns)}"
    )

    return best_df
