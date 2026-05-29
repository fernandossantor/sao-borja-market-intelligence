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

df = pd.read_csv(
    f"{EXPORT_PATH}/economic_structure_evolution.csv"
)

print("\n===================================")
print("ECONOMIC REGIME ENGINE")
print("===================================\n")

print("Shape:", df.shape)

# =========================================
# VARIABLES
# =========================================

share_cols = [
    "vab_agro_share_pct",
    "vab_industria_share_pct",
    "vab_servicos_share_pct",
    "vab_publico_share_pct"
]

# Remove anos incompletos
analysis_df = df.dropna(
    subset=share_cols
).copy()

print(
    f"\nAnos válidos: "
    f"{analysis_df['year'].min()} - "
    f"{analysis_df['year'].max()}"
)

# =========================================
# STRUCTURAL STATISTICS
# =========================================

results = []

for col in share_cols:

    results.append({

        "metric":
            col,

        "mean_pct":
            analysis_df[col].mean(),

        "median_pct":
            analysis_df[col].median(),

        "min_pct":
            analysis_df[col].min(),

        "max_pct":
            analysis_df[col].max(),

        "std_pct":
            analysis_df[col].std(),

        "range_pct":
            analysis_df[col].max()
            - analysis_df[col].min()

    })

regime_df = pd.DataFrame(results)

# =========================================
# LAST YEAR VS HISTORICAL
# =========================================

latest = analysis_df.iloc[-1]

comparison = []

for col in share_cols:

    historical_mean = (
        analysis_df[col].mean()
    )

    comparison.append({

        "metric":
            col,

        "latest_year":
            latest["year"],

        "latest_value":
            latest[col],

        "historical_mean":
            historical_mean,

        "difference_pct_points":
            latest[col]
            - historical_mean

    })

comparison_df = pd.DataFrame(
    comparison
)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("STRUCTURAL REGIME")
print("===================================\n")

print(
    regime_df.round(2)
)

print("\n===================================")
print("LATEST VS HISTORICAL")
print("===================================\n")

print(
    comparison_df.round(2)
)

# =========================================
# EXPORTS
# =========================================

regime_path = os.path.join(
    EXPORT_PATH,
    "economic_regime.csv"
)

comparison_path = os.path.join(
    EXPORT_PATH,
    "economic_regime_comparison.csv"
)

regime_df.to_csv(
    regime_path,
    index=False
)

comparison_df.to_csv(
    comparison_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(regime_path)
print(comparison_path)
