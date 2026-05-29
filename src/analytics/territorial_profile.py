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
print("FILES LOADED")
print("===================================\n")

# =========================================
# ECONOMIC FACTS
# =========================================

row = economic.iloc[0]

facts = {

    "year":
        row["year"],

    "pib_total":
        row["pib_total"],

    "formal_jobs":
        row["formal_jobs"],

    "avg_salary":
        row["avg_salary"],

    "median_salary":
        row["median_salary"],

    "productivity_per_job":
        row["productivity_per_job"],

    "vab_agro":
        row["vab_agro"],

    "vab_industria":
        row["vab_industria"],

    "vab_servicos":
        row["vab_servicos"],

    "vab_publico":
        row["vab_publico"]

}

# =========================================
# SHARES
# =========================================

pib = row["pib_total"]

facts["share_agro_pct"] = (
    row["vab_agro"] / pib * 100
)

facts["share_industria_pct"] = (
    row["vab_industria"] / pib * 100
)

facts["share_servicos_pct"] = (
    row["vab_servicos"] / pib * 100
)

facts["share_publico_pct"] = (
    row["vab_publico"] / pib * 100
)

# =========================================
# TOP CNAE
# =========================================

top10 = cnae.head(10)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("TERRITORIAL FACTS")
print("===================================\n")

for k, v in facts.items():

    print(f"{k}: {v}")

print("\n===================================")
print("TOP CNAE")
print("===================================\n")

print(top10)

# =========================================
# EXPORT FACTS
# =========================================

facts_df = pd.DataFrame([facts])

facts_path = os.path.join(
    EXPORT_PATH,
    "territorial_facts.csv"
)

facts_df.to_csv(
    facts_path,
    index=False
)

top_path = os.path.join(
    EXPORT_PATH,
    "territorial_top_cnae.csv"
)

top10.to_csv(
    top_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(facts_path)
print(top_path)
