import pandas as pd
import numpy as np

# =========================================
# ECONOMIC KEYWORDS
# =========================================

KEYWORDS = [
    "são borja",
    "sb",
    "pib",
    "valor adicionado",
    "vab",
    "agro",
    "indústria",
    "serviços",
    "setor público",
    "impostos",
    "emprego",
    "empresa",
    "salário",
    "remuneração",
    "receita",
    "despesa",
    "produção",
    "município",
    "ano"
]

# =========================================
# NEGATIVE KEYWORDS
# =========================================

NEGATIVE_KEYWORDS = [
    "nota",
    "notas",
    "metodologia",
    "conceito",
    "observação",
    "observacoes",
    "explicação",
    "explicacao",
    "fonte",
    "glossário",
    "glossario"
]

# =========================================
# HEADER QUALITY
# =========================================

def calculate_header_quality(df):

    score = 0

    valid_cols = 0

    for col in df.columns:

        col_str = str(col).strip().lower()

        if (
            "unnamed" not in col_str
            and "nan" not in col_str
            and len(col_str) > 1
        ):
            valid_cols += 1

    score += valid_cols * 15

    return score

# =========================================
# YEAR STRUCTURE
# =========================================

def calculate_year_score(df):

    score = 0

    year_count = 0

    for col in df.columns:

        col_str = str(col)

        for y in range(1990, 2035):

            if str(y) in col_str:

                year_count += 1
                break

    score += year_count * 50

    return score

# =========================================
# ECONOMIC COLUMN SCORE
# =========================================

def calculate_economic_column_score(df):

    score = 0

    economic_terms = [
        "pib",
        "vab",
        "valor",
        "salário",
        "remuneração",
        "emprego",
        "receita",
        "despesa",
        "produção",
        "agro",
        "indústria",
        "serviços"
    ]

    for col in df.columns:

        col_lower = str(col).lower()

        for term in economic_terms:

            if term in col_lower:

                score += 80

    return score

# =========================================
# NUMERIC DENSITY
# =========================================

def calculate_numeric_density(df):

    numeric_cells = 0

    for col in df.columns:

        numeric_cells += pd.to_numeric(
            df[col],
            errors="coerce"
        ).notna().sum()

    return numeric_cells * 0.05

# =========================================
# MAIN SCORE FUNCTION
# =========================================

def calculate_sheet_score(df):

    score = 0

    # =====================================
    # BASIC SIZE
    # =====================================

    score += len(df) * 0.1
    score += len(df.columns) * 0.2

    # =====================================
    # PENALIZE SMALL TABLES
    # =====================================

    if len(df) < 10:
        score -= 500

    if len(df.columns) < 5:
        score -= 300

    # =====================================
    # HEADER QUALITY
    # =====================================

    score += calculate_header_quality(df)

    # =====================================
    # YEAR STRUCTURE
    # =====================================

    score += calculate_year_score(df)

    # =====================================
    # ECONOMIC COLUMNS
    # =====================================

    score += calculate_economic_column_score(df)

    # =====================================
    # NUMERIC DENSITY
    # =====================================

    score += calculate_numeric_density(df)

    # =====================================
    # TEXT BLOB
    # =====================================

    try:

        text_blob = " ".join(
            map(str, df.astype(str).values.flatten())
        ).lower()

    except:

        text_blob = ""

    # =====================================
    # POSITIVE KEYWORDS
    # =====================================

    for kw in KEYWORDS:

        if kw in text_blob:
            score += 20

    # =====================================
    # NEGATIVE KEYWORDS
    # =====================================

    for kw in NEGATIVE_KEYWORDS:

        if kw in text_blob:
            score -= 1000

    # =====================================
    # TERRITORIAL BONUS
    # =====================================

    if "são borja" in text_blob:
        score += 100

    # =====================================
    # HEAVY BONUS FOR REAL TABLES
    # =====================================

    if len(df) > 100:
        score += 500

    if len(df.columns) > 10:
        score += 200

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
    # ANALYZE SHEETS
    # =====================================

    for sheet in excel.sheet_names:

        print(f"\n[ANALISANDO ABA] {sheet}")

        for header_row in range(0, 20):

            try:

                df = pd.read_excel(
                    file_path,
                    sheet_name=sheet,
                    header=header_row
                )

                # =================================
                # CLEAN
                # =================================

                df = df.dropna(
                    axis=1,
                    how="all"
                )

                df = df.dropna(
                    axis=0,
                    how="all"
                )

                # =================================
                # HARD FILTERS
                # =================================

                if len(df) < 15:
                    continue

                if len(df.columns) < 5:
                    continue

                # =================================
                # SCORE
                # =================================

                score = calculate_sheet_score(df)

                # =================================
                # MINIMUM SCORE
                # =================================

                if score < 0:
                    continue

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
                    f"rows={len(df)} "
                    f"cols={len(df.columns)}"
                )

            except Exception:
                continue

    # =====================================
    # NO VALID TABLES
    # =====================================

    if len(candidates) == 0:

        raise Exception(
            "Nenhuma tabela econômica válida encontrada."
        )

    # =====================================
    # BEST TABLE
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
    
    # =====================================
    # OUTPUT
    # =====================================

    print("\n===================================")
    print("BEST SHEET DETECTED")
    print("===================================\n")

    print(f"Aba: {best['sheet']}")
    print(f"Header: {best['header']}")
    print(f"Score: {round(best['score'],2)}")
    print(f"Rows: {best['rows']}")
    print(f"Cols: {best['cols']}")

    return best["df"]
