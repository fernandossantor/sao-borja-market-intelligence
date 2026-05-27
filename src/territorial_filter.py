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
# TEXT NORMALIZATION
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
# PREFILTERED DATASET DETECTION
# =========================================

def detect_prefiltered_dataset(file_name):

    normalized = normalize_text(file_name)

    for alias in TARGET_ALIASES:

        if alias in normalized:
            return True

    return False

# =========================================
# TERRITORIAL COLUMN DETECTION
# =========================================

def detect_territorial_columns(df):

    municipality_cols = []
    uf_cols = []
    ibge_cols = []

    for col in df.columns:

        normalized = normalize_text(col)

        # ---------------------------------
        # IBGE IDENTIFIER
        # ---------------------------------

        if (
            "CODIGO" in normalized
            and "MUNIC" in normalized
        ):

            ibge_cols.append(col)

        elif "IBGE" in normalized:

            ibge_cols.append(col)

        # ---------------------------------
        # MUNICIPALITY NAME
        # ---------------------------------

        elif any(x in normalized for x in [
            "NOME DO MUNICIPIO",
            "MUNICIPIO",
            "CIDADE"
        ]):

            municipality_cols.append(col)

        # ---------------------------------
        # UF
        # ---------------------------------

        elif "UF" in normalized:

            uf_cols.append(col)

    return {
        "municipality": municipality_cols,
        "uf": uf_cols,
        "ibge": ibge_cols
    }

# =========================================
# FILTER BY MUNICIPALITY
# =========================================

def filter_by_municipality(df, municipality_cols, uf_cols):

    col = municipality_cols[0]

    filtered_df = df[
        df[col]
        .astype(str)
        .apply(normalize_text)
        == TARGET_CITY
    ]

    print(
        f"[INFO] filtro município -> {col}"
    )

    # -------------------------------------
    # UF VALIDATION
    # -------------------------------------

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

    return filtered_df

# =========================================
# FILTER BY IBGE
# =========================================

def filter_by_ibge(df, ibge_cols):

    col = ibge_cols[0]

    normalized_ibge = (
        df[col]
        .astype(str)
        .str.replace(".0", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.strip()
    )

    filtered_df = df[
        normalized_ibge == TARGET_IBGE
    ]

    print(
        f"[INFO] filtro IBGE -> {col}"
    )

    return filtered_df

# =========================================
# MAIN FILTER FUNCTION
# =========================================

def filter_sao_borja(df, file_name):

    # =====================================
    # REMOVE EMPTY COLUMNS
    # =====================================

    df = df.dropna(
        axis=1,
        how="all"
    )

    # =====================================
    # PREFILTERED DATASET
    # =====================================

    if detect_prefiltered_dataset(file_name):

        print(
            "[INFO] Dataset já territorializado"
        )

        return df, "prefiltered_dataset"

    # =====================================
    # DETECT COLUMNS
    # =====================================

    cols = detect_territorial_columns(df)

    municipality_cols = cols["municipality"]
    uf_cols = cols["uf"]
    ibge_cols = cols["ibge"]

    print(
        f"[DEBUG] municipality_cols={municipality_cols}"
    )

    print(
        f"[DEBUG] uf_cols={uf_cols}"
    )

    print(
        f"[DEBUG] ibge_cols={ibge_cols}"
    )

    # =====================================
    # PRIORITY 1:
    # MUNICIPALITY + UF
    # =====================================

    if municipality_cols:

        filtered_df = filter_by_municipality(
            df,
            municipality_cols,
            uf_cols
        )

        if len(filtered_df) > 0:

            return (
                filtered_df,
                "filtered_by_city"
            )

    # =====================================
    # PRIORITY 2:
    # IBGE
    # =====================================

    if ibge_cols:

        filtered_df = filter_by_ibge(
            df,
            ibge_cols
        )

        if len(filtered_df) > 0:

            return (
                filtered_df,
                "filtered_by_ibge"
            )

    # =====================================
    # NO TERRITORIAL MATCH
    # =====================================

    print(
        "[WARNING] Nenhum registro territorial encontrado"
    )

    return df.iloc[0:0], "no_match"
