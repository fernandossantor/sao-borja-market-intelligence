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

sector_signals = pd.read_csv(
    f"{EXPORT_PATH}/sector_signals.csv"
)

print("\n===================================")
print("UNCLASSIFIED SIGNAL AUDIT")
print("===================================\n")

print(
    f"Signals: {len(sector_signals)}"
)

# =========================================
# UNCLASSIFIED
# =========================================

unclassified = sector_signals[
    sector_signals["sector"]
    == "unclassified"
].copy()

print(
    f"Unclassified: {len(unclassified)}"
)

# =========================================
# MERGE DETAILS
# =========================================

audit = pd.merge(

    unclassified,

    signals[[
        "category",
        "file_name",
        "column_names",
        "score",
        "start_year",
        "end_year"
    ]],

    on=[
        "category",
        "file_name"
    ],

    how="left"

)

# =========================================
# DOMAIN SUMMARY
# =========================================

domain_summary = (

    audit
    .groupby("category")
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
print("UNCLASSIFIED BY DOMAIN")
print("===================================\n")

print(domain_summary)

# =========================================
# TOP FILES
# =========================================

top_files = (

    audit
    .groupby([
        "category",
        "file_name"
    ])
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
print("TOP FILES")
print("===================================\n")

print(
    top_files.head(50)
)

# =========================================
# TOP SIGNALS
# =========================================

top_signals = (

    audit
    .sort_values(
        "score",
        ascending=False
    )

)

print("\n===================================")
print("TOP UNCLASSIFIED SIGNALS")
print("===================================\n")

print(

    top_signals[[
        "category",
        "file_name",
        "score",
        "start_year",
        "end_year",
        "column_names"
    ]]

    .head(100)

)

# =========================================
# EXPORTS
# =========================================

audit_file = os.path.join(
    EXPORT_PATH,
    "unclassified_signal_audit.csv"
)

summary_file = os.path.join(
    EXPORT_PATH,
    "unclassified_domain_summary.csv"
)

files_file = os.path.join(
    EXPORT_PATH,
    "unclassified_top_files.csv"
)

audit.to_csv(
    audit_file,
    index=False
)

domain_summary.to_csv(
    summary_file,
    index=False
)

top_files.to_csv(
    files_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(audit_file)
print(summary_file)
print(files_file)
