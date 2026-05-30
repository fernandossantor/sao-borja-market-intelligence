import pandas as pd
import numpy as np

# =====================================
# ECONOMIC KEYWORDS
# =====================================

ECONOMIC_KEYWORDS = [

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
# SOCIAL KEYWORDS
# =====================================

SOCIAL_KEYWORDS = [

    "população",
    "sexo",
    "idade",
    "religião",
    "alfabetização",
    "domicílio",
    "raça",
    "cor",
    "quilombola",
    "indígena",
    "autismo",
    "deficiência",
    "favela",
    "favelas",
    "instrução",
    "escolaridade",
    "crescimento populacional",
    "urbana",
    "rural"

]

# =====================================
# SCORE
# =====================================

def calculate_table_score(df):

    score = 0

    # =========================
    # SIZE
    # =========================

    score += len(df) * 0.1
    score += len(df.columns) * 0.5

    # =========================
    # NUMERIC DENSITY
    # =========================

    numeric = 0

    for c in df.columns:

        try:

            numeric += pd.to_numeric(
                df[c],
                errors="coerce"
            ).notna().sum()

        except:

            pass

    score += numeric * 0.05

    # =========================
    # TEXT BLOB
    # =========================

    blob = (
        " ".join(
            map(
                str,
                df.head(100)
                .astype(str)
                .values
                .flatten()
            )
        )
        .lower()
    )

    # =========================
    # ECONOMIC BONUS
    # =========================

    for kw in ECONOMIC_KEYWORDS:

        if kw in blob:

            score += 20

    # =========================
    # SOCIAL BONUS
    # =========================

    for kw in SOCIAL_KEYWORDS:

        if kw in blob:

            score += 20

    # =========================
    # TERRITORIAL BONUS
    # =========================

    if "são borja" in blob:

        score += 100

    return score

# =====================================
# EXTRACT DATASETS
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

                if len(df) < 2:
                    continue

                score = calculate_table_score(df)

                if score < 20:
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
