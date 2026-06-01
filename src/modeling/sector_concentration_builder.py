import pandas as pd
import os

print("\n===================================")
print("SECTOR CONCENTRATION BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "sector_snapshot_2021.csv"
    )
)

# ----------------------------------------
# REMOVER TOTAL
# ----------------------------------------

exclude = [
    "Total",
    "U Organismos internacionais e outras instituições extraterritoriais"
]

df = df[
    ~df["sector"].isin(exclude)
].copy()

# ----------------------------------------
# SHARE EMPREGO
# ----------------------------------------

df = df.sort_values(
    "share_emprego_pct",
    ascending=False
)

# ----------------------------------------
# TOP 3
# ----------------------------------------

top3_share = (
    df.head(3)
    ["share_emprego_pct"]
    .sum()
)

# ----------------------------------------
# TOP 5
# ----------------------------------------

top5_share = (
    df.head(5)
    ["share_emprego_pct"]
    .sum()
)

# ----------------------------------------
# HHI
# ----------------------------------------

hhi = (
    (df["share_emprego_pct"] ** 2)
    .sum()
)

# ----------------------------------------
# CLASSIFICAÇÃO
# ----------------------------------------

if hhi < 1000:
    concentration = "Diversificada"

elif hhi < 1800:
    concentration = "Moderadamente Concentrada"

else:
    concentration = "Concentrada"

# ----------------------------------------
# RESULTADO
# ----------------------------------------

result = pd.DataFrame([
    ["Top 3 Share (%)", top3_share],
    ["Top 5 Share (%)", top5_share],
    ["HHI", hhi],
    ["Classificação", concentration]
],
columns=[
    "indicator",
    "value"
])

print(result)

# ----------------------------------------
# EXPORT
# ----------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "sector_concentration.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
