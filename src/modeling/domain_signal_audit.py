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
print("DOMAIN SIGNAL AUDIT")
print("===================================\n")

print(
    f"Sinais carregados: {len(signals)}"
)

# =========================================
# BASIC CLEANING
# =========================================

signals["column_names"] = (
    signals["column_names"]
    .fillna("")
    .astype(str)
)

signals["sheet"] = (
    signals["sheet"]
    .fillna("")
    .astype(str)
)

# =========================================
# SIGNATURE
# =========================================

signals["signature"] = (

    signals["category"].astype(str)

    + "|"

    + signals["file_name"].astype(str)

    + "|"

    + signals["sheet"].astype(str)

    + "|"

    + signals["column_names"]
        .str[:200]

)

# =========================================
# DEDUPLICATION
# =========================================

original_count = len(signals)

signals_dedup = signals.drop_duplicates(
    subset=["signature"]
).copy()

dedup_count = len(signals_dedup)

removed = (
    original_count
    - dedup_count
)

# =========================================
# DOMAIN SUMMARY
# =========================================

domain_summary = (

    signals_dedup
    .groupby("category")
    .agg({
        "file_name":"nunique",
        "signature":"count"
    })
    .reset_index()

)

domain_summary.columns = [
    "category",
    "files",
    "signals"
]

domain_summary = (
    domain_summary
    .sort_values(
        "signals",
        ascending=False
    )
)

# =========================================
# FILE SUMMARY
# =========================================

file_summary = (

    signals_dedup
    .groupby([
        "category",
        "file_name"
    ])
    .size()
    .reset_index(
        name="signals"
    )

)

file_summary = (
    file_summary
    .sort_values(
        "signals",
        ascending=False
    )
)

# =========================================
# YEAR COVERAGE
# =========================================

coverage = (

    signals_dedup[
        [
            "category",
            "file_name",
            "start_year",
            "end_year"
        ]
    ]
    .drop_duplicates()
)

# =========================================
# TOP SIGNALS
# =========================================

top_signals = (

    signals_dedup[
        [
            "category",
            "file_name",
            "sheet",
            "start_year",
            "end_year",
            "score"
        ]
    ]
    .sort_values(
        "score",
        ascending=False
    )
    .head(50)

)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("DEDUPLICATION")
print("===================================\n")

print(
    f"Originais: {original_count}"
)

print(
    f"Após dedup: {dedup_count}"
)

print(
    f"Removidos: {removed}"
)

print("\n===================================")
print("DOMAIN SUMMARY")
print("===================================\n")

print(domain_summary)

print("\n===================================")
print("TOP FILES")
print("===================================\n")

print(
    file_summary.head(30)
)

print("\n===================================")
print("TOP SIGNALS")
print("===================================\n")

print(top_signals)

# =========================================
# EXPORTS
# =========================================

domain_file = os.path.join(
    EXPORT_PATH,
    "domain_signal_audit.csv"
)

file_file = os.path.join(
    EXPORT_PATH,
    "domain_file_audit.csv"
)

coverage_file = os.path.join(
    EXPORT_PATH,
    "domain_signal_coverage.csv"
)

dedup_file = os.path.join(
    EXPORT_PATH,
    "domain_signals_dedup.csv"
)

domain_summary.to_csv(
    domain_file,
    index=False
)

file_summary.to_csv(
    file_file,
    index=False
)

coverage.to_csv(
    coverage_file,
    index=False
)

signals_dedup.to_csv(
    dedup_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(domain_file)
print(file_file)
print(coverage_file)
print(dedup_file)
