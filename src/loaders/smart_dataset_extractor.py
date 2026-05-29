import pandas as pd
import numpy as np

# =====================================
# KEYWORDS
# =====================================

KEYWORDS = [

    "ano",
    "município",
    "são borja",
    "valor",
    "produção",
    "receita",
    "despesa",
    "emprego",
    "salário",
    "empresa",
    "pessoal",
    "área",
    "colhida",
    "plantada",
    "rebanho",
    "cnae",
    "vab",
    "pib",
    "tributária",
    "educação",
    "saúde",
    "assistência",
    "servidor"

]

# =====================================
# SCORE
# =====================================

def calculate_table_score(df):

    score = 0

    score += len(df) * 0.1
    score += len(df.columns) * 0.5

    numeric = 0

    for c in df.columns:

        numeric += pd.to_numeric(
            df[c],
            errors="coerce"
        ).notna().sum()

    score += numeric * 0.05

    blob = (
        " ".join(
            map(
                str,
                df.head(50)
                .astype(str)
                .values
                .flatten()
            )
        )
        .lower()
    )

    for kw in KEYWORDS:

        if kw in blob:
            score += 20

    return score

# =====================================
# EXTRACT
# =====================================

def extract_datasets(file_path):

    excel = pd.ExcelFile(file_path)

    results = []

    for sheet in excel.sheet_names:

        for header in range(0, 12):

            try:

                df = pd.read_excel(
                    file_path,
                    sheet_name=sheet,
                    header=header
                )

                df = df.dropna(
                    axis=0,
                    how="all"
                )

                df = df.dropna(
                    axis=1,
                    how="all"
                )

                if len(df) < 3:
                    continue

                score = calculate_table_score(df)

                if score < 50:
                    continue

                results.append({

                    "sheet": sheet,
                    "header": header,
                    "score": score,
                    "rows": len(df),
                    "cols": len(df.columns),
                    "df": df

                })

            except Exception:

                continue

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return results
