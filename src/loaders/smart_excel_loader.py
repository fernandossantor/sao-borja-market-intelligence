import pandas as pd
import numpy as np

# =========================================
# ECONOMIC KEYWORDS
# =========================================

KEYWORDS = [
    "são borja",
    "sb",
    "pib",
    "salário",
    "remuneração",
    "emprego",
    "empresa",
    "vínculo",
    "cnae",
    "cbo",
    "agro",
    "receita",
    "despesa",
    "valor",
    "produção",
    "município",
    "ano"
]

# =========================================
# CONTENT SCORE
# =========================================

def calculate_sheet_score(df):

    score = 0

    # ==========================
    # ROWS / COLS
    # ==========================

    score += len(df) * 0.1
    score += len(df.columns) * 0.2

    # ==========================
    # NUMERIC DENSITY
    # ==========================

    numeric_cells = 0

    for col in df.columns:

        numeric_cells += pd.to_numeric(
            df[col],
            errors="coerce"
        ).notna().sum()

    score += numeric_cells * 0.05

    # ==========================
    # TEXT SEARCH
    # ==========================

    text_blob = " ".join(
        map(str, df.astype(str).values.flatten())
    ).lower()

    for kw in KEYWORDS:

        if kw in text_blob:
            score += 20

    # ==========================
    # TERRITORIAL BONUS
    # ==========================

    if "são borja" in text_blob:
        score += 100

    return score


# =========================================
# HEADER QUALITY SCORE
# =========================================

def calculate_header_quality(df):

    score = 0

    columns = [
        str(c).strip().lower()
        for c in df.columns
    ]

    joined = " ".join(columns)

    # =====================================
    # SEMANTIC HEADERS
    # =====================================

    semantic_headers = [

        "município",
        "municipio",
        "uf",
        "estado",
        "ano",
        "pib",
        "vab",
        "agropecuária",
        "agropecuaria",
        "indústria",
        "industria",
        "serviços",
        "servicos",
        "empresas",
        "salários",
        "salarios",
        "emprego",
        "cnae",
        "vínculo",
        "vinculo",
        "total"

    ]

    for keyword in semantic_headers:

        if keyword in joined:
            score += 150

    # =====================================
    # PENALIZA unnamed
    # =====================================

    unnamed_count = sum(
        "unnamed" in c
        for c in columns
    )

    score -= unnamed_count * 80

    # =====================================
    # PENALIZA HEADERS NUMÉRICOS
    # =====================================

    numeric_headers = sum(

        c.replace(".", "").isdigit()

        for c in columns
    )

    score -= numeric_headers * 50

    return score


# =========================================
# SMART EXCEL LOADER
# =========================================

def load_excel_smart(file_path):

    excel = pd.ExcelFile(file_path)

    print("\n===================================")
    print("SMART EXCEL ANALYSIS")
    print("===================================\n")

    candidates = []

    # =====================================
    # TEST SHEETS
    # =====================================

    for sheet in excel.sheet_names:

        print(f"\n[ANALISANDO ABA] {sheet}")

        # =================================
        # TEST HEADERS
        # =================================

        for header_row in range(0, 20):

            try:

                df = pd.read_excel(
                    file_path,
                    sheet_name=sheet,
                    header=header_row
                )

                # ==========================
                # BASIC CLEANING
                # ==========================

                df = df.dropna(
                    axis=1,
                    how="all"
                )

                df = df.dropna(
                    axis=0,
                    how="all"
                )

                if len(df) == 0:
                    continue

                # ==========================
                # SCORES
                # ==========================

                content_score = calculate_sheet_score(df)

                header_score = calculate_header_quality(df)

                score = (
                    content_score +
                    header_score
                )

                candidates.append({
                    "sheet": sheet,
                    "header": header_row,
                    "score": score,
                    "rows": len(df),
                    "cols": len(df.columns),
                    "df": df
                })

                print(
                    f"[OK] "
                    f"header={header_row} "
                    f"score={round(score,2)} "
                    f"rows={len(df)}"
                )

            except Exception:
                continue

    # =====================================
    # NO CANDIDATES
    # =====================================

    if len(candidates) == 0:

        raise Exception(
            "Nenhuma tabela válida encontrada."
        )

    # =====================================
    # BEST CANDIDATE
    # =====================================

    best = sorted(
        candidates,
        key=lambda x: x["score"],
        reverse=True
    )[0]

    print("\n===================================")
    print("BEST SHEET DETECTED")
    print("===================================\n")

    print(f"Aba: {best['sheet']}")
    print(f"Header: {best['header']}")
    print(f"Score: {round(best['score'],2)}")
    print(f"Rows: {best['rows']}")
    print(f"Cols: {best['cols']}")

    return best["df"]
