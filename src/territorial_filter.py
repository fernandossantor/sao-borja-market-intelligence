import pandas as pd
import unicodedata

# =========================================
# TARGET TERRITORY
# =========================================

TARGET_CITY = "SAO BORJA"
TARGET_UF = "RS"
TARGET_IBGE = "4318002"

TARGET_ALIASES = [
    "SAO BORJA",
    "SÃO BORJA",
    "SB"
]

# =========================================
# NORMALIZATION
# =========================================

def normalize_text(text):

    if pd.isna(text):
        return ""

    text = str(text).upper()

    text = unicodedata.normalize(
        "NFKD",
        text
    ).encode(
        "ASCII",
        "ignore"
    ).decode(
        "utf-8"
    )

    return text.strip()

# =========================================
# PREFILTER DETECTION
# =========================================

def detect_prefiltered_dataset(file_name):

    normalized = normalize_text(file_name)

    for alias in TARGET_ALIASES:

        if alias in normalized:
            return True

    return False

# =========================================
# COLUMN DETECTION
# =========================================

def detect_territorial_columns(df):

    municipality_cols = []
    uf_cols = []
    ibge_cols = []

    for col in df.columns:

        normalized = normalize_text(col)

        # Municipality
        if any(x in normalized for x in [
            "MUNICIP",
            "CIDADE"
        ]):
            municipality_cols.append(col)

        # UF
        if "UF" in normalized:
            uf_cols.append(col)

        # IBGE
        if "IBGE" in normalized:
            ibge_cols.append(col)

    return {
        "municipality": municipality_cols,
        "uf": uf_cols,
        "ibge": ibge_cols
    }

# =========================================
# FILTER FUNCTION
# =========================================

def filter_sao_borja(df, file_name):

    # -------------------------------------
    # PREFILTERED DATASET
    # -------------------------------------

    if detect_prefiltered_dataset(file_name):

        print(
            "[INFO] Dataset já territorializado"
        )

        return df, "prefiltered_dataset"

    # -------------------------------------
    # DETECT COLUMNS
    # -------------------------------------

    cols = detect_territorial_columns(df)

    municipality_cols = cols["municipality"]
    uf_cols = cols["uf"]
    ibge_cols = cols["ibge"]

    filtered_df = df.copy()

    # -------------------------------------
    # FILTER BY IBGE
    # -------------------------------------

    if ibge_cols:

        col = ibge_cols[0]

        filtered_df = filtered_df[
            filtered_df[col]
            .astype(str)
            .str.contains(TARGET_IBGE, na=False)
        ]

        print(
            f"[INFO] filtro por IBGE -> {col}"
        )

        return filtered_df, "filtered_by_ibge"

    # -------------------------------------
    # FILTER BY MUNICIPALITY
    # -------------------------------------

    if municipality_cols:

        col = municipality_cols[0]

        filtered_df = filtered_df[
            filtered_df[col]
            .astype(str)
            .apply(normalize_text)
            .isin(TARGET_ALIASES)
        ]

        print(
            f"[INFO] filtro por município -> {col}"
        )

        # UF validation
        if uf_cols:

            uf_col = uf_cols[0]

            filtered_df = filtered_df[
                filtered_df[uf_col]
                .astype(str)
                .apply(normalize_text)
                == TARGET_UF
            ]

            print(
                f"[INFO] filtro UF -> {uf_col}"
            )

        return filtered_df, "filtered_by_city"

    # -------------------------------------
    # NO FILTER FOUND
    # -------------------------------------

    print(
        "[WARNING] Nenhum filtro territorial encontrado"
    )

    return df, "no_territorial_filter"
