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

economic = pd.read_csv(
    f"{EXPORT_PATH}/territorial_economic_model.csv"
)

cnae = pd.read_csv(
    f"{EXPORT_PATH}/cnae_structure.csv"
)

print("\n===================================")
print("ECONOMIC STRUCTURE ENGINE")
print("===================================\n")

# =========================================
# ECONOMIC SUMMARY
# =========================================

row = economic.iloc[0]

year = row["year"]

pib_total = row["pib_total"]

formal_jobs = row["formal_jobs"]

avg_salary = row["avg_salary"]

median_salary = row["median_salary"]

productivity = row["productivity_per_job"]

# =========================================
# PIB STRUCTURE
# =========================================

pib_structure = pd.DataFrame([
    {
        "component": "Agropecuária",
        "value": row["vab_agro"]
    },
    {
        "component": "Indústria",
        "value": row["vab_industria"]
    },
    {
        "component": "Serviços",
        "value": row["vab_servicos"]
    },
    {
        "component": "Administração Pública",
        "value": row["vab_publico"]
    }
])

pib_structure["share_pct"] = (
    pib_structure["value"]
    / pib_total
    * 100
)

pib_structure = pib_structure.sort_values(
    "share_pct",
    ascending=False
)

# =========================================
# EMPLOYMENT STRUCTURE
# =========================================

employment_structure = cnae.copy()

employment_structure["share_pct"] = (
    employment_structure["jobs"]
    / formal_jobs
    * 100
)

employment_structure = employment_structure.sort_values(
    "jobs",
    ascending=False
)

# =========================================
# CONCENTRATION METRICS
# =========================================

top5_share = (
    employment_structure
    .head(5)["jobs"]
    .sum()
    / formal_jobs
    * 100
)

top10_share = (
    employment_structure
    .head(10)["jobs"]
    .sum()
    / formal_jobs
    * 100
)

concentration = pd.DataFrame([
    {
        "metric": "top5_cnae_share_pct",
        "value": round(top5_share, 2)
    },
    {
        "metric": "top10_cnae_share_pct",
        "value": round(top10_share, 2)
    }
])

# =========================================
# LABOR MARKET
# =========================================

labor_market = pd.DataFrame([
    {
        "indicator": "formal_jobs",
        "value": formal_jobs
    },
    {
        "indicator": "avg_salary",
        "value": avg_salary
    },
    {
        "indicator": "median_salary",
        "value": median_salary
    },
    {
        "indicator": "productivity_per_job",
        "value": productivity
    }
])

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("PIB STRUCTURE")
print("===================================\n")

print(
    pib_structure[
        ["component", "value", "share_pct"]
    ]
)

print("\n===================================")
print("EMPLOYMENT STRUCTURE")
print("===================================\n")

print(
    employment_structure[
        ["cnae_class", "jobs", "share_pct"]
    ].head(20)
)

print("\n===================================")
print("CONCENTRATION")
print("===================================\n")

print(concentration)

print("\n===================================")
print("LABOR MARKET")
print("===================================\n")

print(labor_market)

# =========================================
# EXPORTS
# =========================================

pib_path = os.path.join(
    EXPORT_PATH,
    "economic_structure_pib.csv"
)

employment_path = os.path.join(
    EXPORT_PATH,
    "economic_structure_employment.csv"
)

concentration_path = os.path.join(
    EXPORT_PATH,
    "economic_concentration.csv"
)

labor_path = os.path.join(
    EXPORT_PATH,
    "labor_market_summary.csv"
)

pib_structure.to_csv(
    pib_path,
    index=False
)

employment_structure.to_csv(
    employment_path,
    index=False
)

concentration.to_csv(
    concentration_path,
    index=False
)

labor_market.to_csv(
    labor_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(pib_path)
print(employment_path)
print(concentration_path)
print(labor_path)
