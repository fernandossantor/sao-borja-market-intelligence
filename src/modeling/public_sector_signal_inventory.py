import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# LOAD
# =========================================

signals = pd.read_csv(
    f"{EXPORT_PATH}/domain_signals.csv"
)

print("\n===================================")
print("PUBLIC SECTOR SIGNAL INVENTORY")
print("===================================\n")

print(
    f"Sinais carregados: {len(signals)}"
)

# =========================================
# KEYWORDS
# =========================================

KEYWORDS = [

    "fpm",
    "fundeb",
    "saúde",
    "educação",
    "assistência",
    "social",
    "suas",
    "pessoal",
    "remuneração",
    "servidor",
    "cadastro",
    "afastamento",
    "salário",
    "transfer",
    "royalties",
    "mac",
    "enfermagem",
    "prefeitura",
    "governo",
    "administração"

]

# =========================================
# FILTER
# =========================================

public_rows = []

for _, row in signals.iterrows():

    text = (

        str(
            row.get(
                "file_name",
                ""
            )
        )
        +
        " "
        +
        str(
            row.get(
                "column_names",
                ""
            )
        )

    ).lower()

    score = 0

    for kw in KEYWORDS:

        if kw in text:

            score += 1

    if score > 0:

        row = row.copy()

        row[
            "public_score"
        ] = score

        public_rows.append(
            row
        )

# =========================================
# DATAFRAME
# =========================================

public_df = pd.DataFrame(
    public_rows
)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("PUBLIC SIGNALS")
print("===================================\n")

print(
    f"Total: {len(public_df)}"
)

print(
    public_df[
        [
            "category",
            "file_name",
            "public_score"
        ]
    ]
    .sort_values(
        "public_score",
        ascending=False
    )
    .head(50)
)

# =========================================
# DOMAIN SUMMARY
# =========================================

summary = (

    public_df

    .groupby(
        "category"
    )

    .size()

    .reset_index(
        name="signals"
    )

    .sort_values(
        "signals",
        ascending=False
    )

)

print("\n===================================")
print("DOMAIN SUMMARY")
print("===================================\n")

print(summary)

# =========================================
# EXPORT
# =========================================

signals_file = os.path.join(
    EXPORT_PATH,
    "public_sector_signals.csv"
)

summary_file = os.path.join(
    EXPORT_PATH,
    "public_sector_signal_summary.csv"
)

public_df.to_csv(
    signals_file,
    index=False
)

summary.to_csv(
    summary_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(signals_file)
print(summary_file)
