import pandas as pd


# ==========================================
# NORMALIZAÇÃO DE TEXTO
# ==========================================

def normalize_text(text):

    if pd.isna(text):
        return ""

    text = str(text).strip().lower()

    replacements = {
        "ã": "a",
        "á": "a",
        "à": "a",
        "â": "a",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u",
        "ç": "c"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


# ==========================================
# TERRITORIAL FILTER
# ==========================================

def filter_sao_borja(
    df,
    file_name=""
):

    # ==========================================
    # 1. DETECÇÃO SEMÂNTICA PELO NOME DO ARQUIVO
    # ==========================================

    semantic_name = normalize_text(file_name)

    semantic_signals = [
        "sao borja",
        "sb",
    ]

    if any(signal in semantic_name for signal in semantic_signals):

        print(
            "[INFO] Dataset semanticamente territorializado"
        )

        return (
            df.copy(),
            "semantic_prefiltered_dataset"
        )

    # ==========================================
    # 2. NORMALIZAÇÃO DAS COLUNAS
    # ==========================================

    normalized_columns = {
        col: normalize_text(col)
        for col in df.columns
    }

    municipality_cols = []
    uf_cols = []
    ibge_cols = []

    # ==========================================
    # 3. DETECÇÃO DE COLUNAS TERRITORIAIS
    # ==========================================

    for original_col, normalized_col in normalized_columns.items():

        # MUNICÍPIO

        municipality_keywords = [
            "municipio",
            "nome do municipio",
            "cidade",
            "município"
        ]

        if any(
            keyword in normalized_col
            for keyword in municipality_keywords
        ):
            municipality_cols.append(original_col)

        # UF

        uf_keywords = [
            "uf",
            "estado",
            "sigla uf"
        ]

        if any(
            keyword in normalized_col
            for keyword in uf_keywords
        ):
            uf_cols.append(original_col)

        # IBGE

        ibge_keywords = [
            "codigo do municipio",
            "cod municipio",
            "ibge",
            "codigo ibge"
        ]

        if any(
            keyword in normalized_col
            for keyword in ibge_keywords
        ):
            ibge_cols.append(original_col)

    print(f"[DEBUG] municipality_cols={municipality_cols}")
    print(f"[DEBUG] uf_cols={uf_cols}")
    print(f"[DEBUG] ibge_cols={ibge_cols}")

    # ==========================================
    # 4. FILTRO POR MUNICÍPIO
    # ==========================================

    for col in municipality_cols:

        try:

            normalized_values = (
                df[col]
                .astype(str)
                .apply(normalize_text)
            )

            city_mask = normalized_values.str.contains(
                "sao borja",
                na=False
            )

            if city_mask.sum() > 0:

                filtered_df = df[city_mask].copy()

                # ==========================================
                # FILTRO ADICIONAL POR UF
                # ==========================================

                if len(uf_cols) > 0:

                    uf_col = uf_cols[0]

                    uf_mask = (
                        filtered_df[uf_col]
                        .astype(str)
                        .str.upper()
                        .str.strip()
                        == "RS"
                    )

                    filtered_df = filtered_df[uf_mask]

                    print(
                        f"[INFO] filtro UF -> {uf_col}"
                    )

                print(
                    f"[INFO] filtro por município -> {col}"
                )

                return (
                    filtered_df,
                    "filtered_by_city"
                )

        except Exception as e:

            print(
                f"[WARNING] erro filtro município {col} -> {e}"
            )

    # ==========================================
    # 5. FILTRO POR CÓDIGO IBGE
    # ==========================================

    for col in ibge_cols:

        try:

            ibge_mask = (
                df[col]
                .astype(str)
                .str.strip()
                == "4318002"
            )

            if ibge_mask.sum() > 0:

                filtered_df = df[ibge_mask].copy()

                print(
                    f"[INFO] filtro por código IBGE -> {col}"
                )

                return (
                    filtered_df,
                    "filtered_by_ibge"
                )

        except Exception as e:

            print(
                f"[WARNING] erro filtro IBGE {col} -> {e}"
            )

    # ==========================================
    # 6. SEM MATCH
    # ==========================================

    print(
        "[WARNING] Nenhum registro territorial encontrado"
    )

    return (
        pd.DataFrame(),
        "no_match"
    )
