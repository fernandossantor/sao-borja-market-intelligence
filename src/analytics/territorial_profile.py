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
# BASIC METRICS
# =========================================

row = economic.iloc[0]

pib = row["pib_total"]

jobs = row["formal_jobs"]

salary = row["avg_salary"]

prod = row["productivity_per_job"]

agro = row["vab_agro"]

industria = row["vab_industria"]

servicos = row["vab_servicos"]

publico = row["vab_publico"]

# =========================================
# SHARES
# =========================================

share_agro = agro / pib * 100
share_industria = industria / pib * 100
share_servicos = servicos / pib * 100
share_publico = publico / pib * 100

# =========================================
# TOP CNAE
# =========================================

top_cnae = cnae.iloc[0]["cnae_class"]

top_jobs = cnae.iloc[0]["jobs"]

# =========================================
# DIAGNOSTICS
# =========================================

diagnostics = []

if share_agro >= 25:
    diagnostics.append(
        "Economia fortemente dependente do agro."
    )

if share_industria <= 15:
    diagnostics.append(
        "Baixa densidade industrial."
    )

if share_publico >= 10:
    diagnostics.append(
        "Forte presença da administração pública."
    )

if share_servicos >= 40:
    diagnostics.append(
        "Serviços representam o principal motor econômico."
    )

if prod >= 100000:
    diagnostics.append(
        "Produtividade econômica relativamente elevada."
    )

# =========================================
# PROFILE
# =========================================

profile = []

if share_agro >= 20:
    profile.append("agro")

if share_servicos >= 30:
    profile.append("serviços")

if share_publico >= 10:
    profile.append("estado")

profile_text = " + ".join(profile)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("STRUCTURAL PROFILE")
print("===================================\n")

print("Perfil:")

print(profile_text)

print("\nIndicadores:")

print(f"PIB: R$ {round(pib,2):,.0f}")
print(f"Empregos formais: {jobs}")
print(f"Salário médio: R$ {round(salary,2)}")

print("\nParticipações:")

print(f"Agro: {round(share_agro,1)}%")
print(f"Indústria: {round(share_industria,1)}%")
print(f"Serviços: {round(share_servicos,1)}%")
print(f"Setor público: {round(share_publico,1)}%")

print("\nDiagnósticos:")

for d in diagnostics:
    print("-", d)

print("\nTop CNAE:")

print(
    f"{top_cnae} "
    f"({top_jobs} vínculos)"
)

# =========================================
# EXPORT
# =========================================

profile_df = pd.DataFrame({

    "profile": [profile_text],

    "share_agro": [share_agro],

    "share_industria": [share_industria],

    "share_servicos": [share_servicos],

    "share_publico": [share_publico],

    "productivity": [prod],

    "avg_salary": [salary]

})

export_path = os.path.join(
    EXPORT_PATH,
    "territorial_profile.csv"
)

profile_df.to_csv(
    export_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_path)
