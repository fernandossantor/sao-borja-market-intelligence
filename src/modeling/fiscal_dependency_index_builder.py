import pandas as pd
import os

print("\n===================================")
print("FISCAL DEPENDENCY INDEX")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

annual = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_annual_summary.csv"
    )
)

# ----------------------------------
# ÍNDICE
# ----------------------------------

dependency = annual[
    [
        "year",
        "structural_share_pct",
        "programmatic_share_pct"
    ]
].copy()

dependency["dependency_class"] = pd.cut(
    dependency["programmatic_share_pct"],
    bins=[
        0,
        40,
        55,
        70,
        85,
        100
    ],
    labels=[
        "Muito Baixa",
        "Baixa",
        "Moderada",
        "Alta",
        "Muito Alta"
    ]
)

# ----------------------------------
# MÉDIA HISTÓRICA
# ----------------------------------

valid = dependency[
    dependency["year"] <= 2025
].copy()

avg_programmatic = (
    valid["programmatic_share_pct"]
    .mean()
)

avg_structural = (
    valid["structural_share_pct"]
    .mean()
)

print(
    "\nSoma:",
    round(
        avg_programmatic
        +
        avg_structural,
        2
    )
)

print(dependency)

print("\n===================================")
print("MÉDIAS")
print("===================================\n")

print(
    "Programática:",
    round(avg_programmatic, 2)
)

print(
    "Estrutural:",
    round(avg_structural, 2)
)

# ----------------------------------
# EXPORT
# ----------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_dependency_index.csv"
)

dependency.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
