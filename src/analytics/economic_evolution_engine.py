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

pib = pd.read_csv(
    f"{EXPORT_PATH}/pib_canonical.csv"
)

print("\n===================================")
print("PIB EVOLUTION ENGINE")
print("===================================\n")

print("Shape:", pib.shape)

# =========================================
# SORT
# =========================================

pib = pib.sort_values(
    "year"
).reset_index(drop=True)

# =========================================
# SHARES
# =========================================

for col in [
    "vab_agro",
    "vab_industria",
    "vab_servicos",
    "vab_publico"
]:

    pib[f"{col}_share_pct"] = (
        pib[col]
        / pib["pib_total"]
        * 100
    )

# =========================================
# CAGR
# =========================================

def calculate_cagr(series):

    valid = series.dropna()

    if len(valid) < 2:
        return None

    first = valid.iloc[0]
    last = valid.iloc[-1]

    years = len(valid) - 1

    if first <= 0:
        return None

    return (
        ((last / first) ** (1 / years))
        - 1
    ) * 100

cagr_table = []

for metric in [
    "pib_total",
    "vab_agro",
    "vab_industria",
    "vab_servicos",
    "vab_publico"
]:

    cagr_table.append({
        "metric": metric,
        "cagr_pct": round(
            calculate_cagr(
                pib[metric]
            ),
            2
        )
    })

cagr_df = pd.DataFrame(
    cagr_table
)

# =========================================
# STRUCTURAL EVOLUTION
# =========================================

structure = pib[
    [
        "year",
        "vab_agro_share_pct",
        "vab_industria_share_pct",
        "vab_servicos_share_pct",
        "vab_publico_share_pct"
    ]
].copy()

# =========================================
# GROWTH RATES
# =========================================

growth_metrics = [
    "pib_total",
    "vab_agro",
    "vab_industria",
    "vab_servicos",
    "vab_publico"
]

growth_df = pib[
    ["year"]
].copy()

for metric in growth_metrics:

    growth_df[
        f"{metric}_growth_pct"
    ] = (
        pib[metric]
        .pct_change(fill_method=None)
        * 100
    )

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("CAGR")
print("===================================\n")

print(cagr_df)

print("\n===================================")
print("STRUCTURAL EVOLUTION")
print("===================================\n")

print(
    structure.tail(10)
)

print("\n===================================")
print("ANNUAL GROWTH")
print("===================================\n")

print(
    growth_df.tail(10)
)

# =========================================
# EXPORTS
# =========================================

cagr_path = os.path.join(
    EXPORT_PATH,
    "economic_cagr.csv"
)

structure_path = os.path.join(
    EXPORT_PATH,
    "economic_structure_evolution.csv"
)

growth_path = os.path.join(
    EXPORT_PATH,
    "economic_growth_rates.csv"
)

cagr_df.to_csv(
    cagr_path,
    index=False
)

structure.to_csv(
    structure_path,
    index=False
)

growth_df.to_csv(
    growth_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(cagr_path)
print(structure_path)
print(growth_path)
