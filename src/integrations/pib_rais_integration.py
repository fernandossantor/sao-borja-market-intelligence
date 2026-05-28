import pandas as pd
import numpy as np
import os

# =========================================
# CONFIG
# =========================================

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# =========================================
# LOAD FILES
# =========================================

pib_df = pd.read_csv(
    f"{EXPORT_PATH}/pib_canonical.csv"
)

rais_df = pd.read_csv(
    f"{EXPORT_PATH}/rais_canonical.csv"
)

print("\n===================================")
print("FILES LOADED")
print("===================================\n")

print("PIB:", pib_df.shape)
print("RAIS:", rais_df.shape)

# =========================================
# BASIC RAIS METRICS
# =========================================

total_jobs = len(rais_df)

avg_salary = rais_df[
    "avg_salary"
].dropna().mean()

median_salary = rais_df[
    "avg_salary"
].dropna().median()

# =========================================
# CNAE CONCENTRATION
# =========================================

cnae_distribution = (
    rais_df["cnae_class"]
    .value_counts()
    .reset_index()
)

cnae_distribution.columns = [
    "cnae_class",
    "jobs"
]

top_cnae = cnae_distribution.head(20)

# =========================================
# PIB LAST YEAR
# =========================================

latest_pib = (
    pib_df[
        pib_df["vab_total"].notna()
    ]
    .sort_values("year")
    .iloc[-1]
)

# =========================================
# PRODUCTIVITY
# =========================================

productivity = (
    latest_pib["pib_total"]
    / total_jobs
)

# =========================================
# SUMMARY TABLE
# =========================================

summary = pd.DataFrame([{

    "year": latest_year,

    "pib_total":
        latest_pib["pib_total"],

    "formal_jobs":
        total_jobs,

    "avg_salary":
        avg_salary,

    "median_salary":
        median_salary,

    "productivity_per_job":
        productivity,

    "vab_agro":
        latest_pib["vab_agro"],

    "vab_industria":
        latest_pib["vab_industria"],

    "vab_servicos":
        latest_pib["vab_servicos"],

    "vab_publico":
        latest_pib["vab_publico"]

}])

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("ECONOMIC SUMMARY")
print("===================================\n")

print(summary.T)

print("\n===================================")
print("TOP CNAE")
print("===================================\n")

print(top_cnae.head(20))

# =========================================
# EXPORTS
# =========================================

summary_path = os.path.join(
    EXPORT_PATH,
    "territorial_economic_model.csv"
)

cnae_path = os.path.join(
    EXPORT_PATH,
    "cnae_structure.csv"
)

summary.to_csv(
    summary_path,
    index=False
)

top_cnae.to_csv(
    cnae_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(summary_path)
print(cnae_path)
