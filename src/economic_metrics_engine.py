import pandas as pd
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

INPUT_FILE = os.path.join(
    EXPORT_PATH,
    "pib_deduplicated.csv"
)

# =========================================
# LOAD
# =========================================

df = pd.read_csv(INPUT_FILE)

print("\n===================================")
print("DEDUPLICATED DATASET LOADED")
print("===================================\n")

print(df.shape)

# =========================================
# SORT
# =========================================

df = df.sort_values(
    by="year"
)

# =========================================
# GROWTH RATES
# =========================================

growth_columns = [
    "pib_total",
    "vab_agro",
    "vab_industria",
    "vab_servicos",
    "vab_publico"
]

for col in growth_columns:

    growth_col = f"{col}_growth_pct"

    df[growth_col] = (
        df[col]
        .pct_change() * 100
    )

# =========================================
# CAGR
# =========================================

metrics = []

for col in growth_columns:

    first_value = df[col].dropna().iloc[0]

    last_value = df[col].dropna().iloc[-1]

    first_year = df["year"].dropna().iloc[0]

    last_year = df["year"].dropna().iloc[-1]

    periods = last_year - first_year

    cagr = (
        (
            last_value / first_value
        ) ** (
            1 / periods
        ) - 1
    ) * 100

    metrics.append({
        "metric": col,
        "first_year": first_year,
        "last_year": last_year,
        "cagr_pct": round(cagr, 2)
    })

metrics_df = pd.DataFrame(metrics)

# =========================================
# ECONOMIC STRUCTURE
# =========================================

df["share_agro_pct"] = (
    df["vab_agro"] /
    df["vab_total"]
) * 100

df["share_industria_pct"] = (
    df["vab_industria"] /
    df["vab_total"]
) * 100

df["share_servicos_pct"] = (
    df["vab_servicos"] /
    df["vab_total"]
) * 100

df["share_publico_pct"] = (
    df["vab_publico"] /
    df["vab_total"]
) * 100

# =========================================
# STATE DEPENDENCY
# =========================================

df["state_dependency_ratio"] = (
    df["vab_publico"] /
    df["vab_total"]
)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("CAGR METRICS")
print("===================================\n")

print(metrics_df)

print("\n===================================")
print("ECONOMIC STRUCTURE")
print("===================================\n")

print(df[[
    "year",
    "share_agro_pct",
    "share_industria_pct",
    "share_servicos_pct",
    "share_publico_pct"
]].tail(10))

# =========================================
# EXPORTS
# =========================================

metrics_output = os.path.join(
    EXPORT_PATH,
    "economic_metrics.csv"
)

df_output = os.path.join(
    EXPORT_PATH,
    "economic_structure.csv"
)

metrics_df.to_csv(
    metrics_output,
    index=False
)

df.to_csv(
    df_output,
    index=False
)

print("\n===================================")
print("EXPORTS FINALIZADOS")
print("===================================\n")

print(metrics_output)
print(df_output)
