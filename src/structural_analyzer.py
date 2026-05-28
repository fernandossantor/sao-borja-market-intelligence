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
    "economic_structure.csv"
)

# =========================================
# LOAD
# =========================================

df = pd.read_csv(INPUT_FILE)

print("\n===================================")
print("ECONOMIC STRUCTURE LOADED")
print("===================================\n")

print(df.shape)

# =========================================
# LATEST VALID YEAR
# =========================================

valid_df = df.dropna(
    subset=[
        "share_agro_pct",
        "share_servicos_pct",
        "share_publico_pct"
    ]
)

latest = valid_df.iloc[-1]

latest_year = latest["year"]

print(f"\nAno analisado: {latest_year}")

# =========================================
# THRESHOLDS
# =========================================

diagnostics = []

# =========================================
# AGRO DEPENDENCY
# =========================================

if latest["share_agro_pct"] >= 30:

    diagnostics.append(
        "Economia altamente dependente do agro."
    )

elif latest["share_agro_pct"] >= 20:

    diagnostics.append(
        "Economia com forte presença agropecuária."
    )

# =========================================
# SERVICES
# =========================================

if latest["share_servicos_pct"] >= 60:

    diagnostics.append(
        "Economia fortemente terciarizada."
    )

# =========================================
# PUBLIC SECTOR
# =========================================

if latest["share_publico_pct"] >= 18:

    diagnostics.append(
        "Elevada dependência do setor público."
    )

elif latest["share_publico_pct"] >= 12:

    diagnostics.append(
        "Setor público possui relevância econômica significativa."
    )

# =========================================
# INDUSTRIAL DENSITY
# =========================================

if latest["share_industria_pct"] <= 15:

    diagnostics.append(
        "Baixa densidade industrial."
    )

elif latest["share_industria_pct"] <= 25:

    diagnostics.append(
        "Estrutura industrial moderada."
    )

# =========================================
# ECONOMIC PROFILE
# =========================================

profile = []

if latest["share_agro_pct"] > 25:
    profile.append("agro")

if latest["share_servicos_pct"] > 50:
    profile.append("serviços")

if latest["share_publico_pct"] > 15:
    profile.append("estado")

economic_profile = " + ".join(profile)

# =========================================
# OUTPUT
# =========================================

print("\n===================================")
print("STRUCTURAL DIAGNOSTICS")
print("===================================\n")

for d in diagnostics:
    print(f"- {d}")

print("\n===================================")
print("ECONOMIC PROFILE")
print("===================================\n")

print(economic_profile)

# =========================================
# EXPORT REPORT
# =========================================

report = pd.DataFrame({
    "year": [latest_year],
    "economic_profile": [economic_profile],
    "diagnostics": [" | ".join(diagnostics)]
})

output_path = os.path.join(
    EXPORT_PATH,
    "structural_analysis.csv"
)

report.to_csv(
    output_path,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(output_path)
