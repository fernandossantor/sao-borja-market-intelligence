import pandas as pd
import os

print("\n===================================")
print("PRIVATE VAB PROJECTION V2")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# CARREGAR PIB
# --------------------------------------------------

pib = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "pib_canonical.csv"
    )
)

# --------------------------------------------------
# CARREGAR VAB PRIVADO OBSERVADO
# --------------------------------------------------

private_obs = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_vab_observed.csv"
    )
)

private_obs = private_obs.dropna(
    subset=["vab_private"]
)

# --------------------------------------------------
# SHARE ESTRUTURAL
# --------------------------------------------------

share_private = (
    private_obs[
        (private_obs["year"] >= 2017)
        &
        (private_obs["year"] <= 2020)
    ]["private_share_pct"]
    .mean()
) / 100

print("Share estrutural:")
print(round(share_private * 100, 2), "%")

# --------------------------------------------------
# BASE OBSERVADA
# --------------------------------------------------

projection = private_obs[
    [
        "year",
        "vab_private"
    ]
].copy()

projection["type"] = "observed"

# --------------------------------------------------
# 2022 E 2023
# --------------------------------------------------

future = pib[
    pib["year"] >= 2022
].copy()

future["vab_private"] = (
    future["pib_total"]
    * share_private
)

future["type"] = "estimated"

future = future[
    [
        "year",
        "vab_private",
        "type"
    ]
]

# --------------------------------------------------
# 2024
# --------------------------------------------------

vab_2023 = (
    future[
        future["year"] == 2023
    ]["vab_private"]
    .iloc[0]
)

vab_2024 = vab_2023 * 1.05

future = pd.concat(
    [
        future,
        pd.DataFrame(
            {
                "year": [2024],
                "vab_private": [vab_2024],
                "type": ["estimated"]
            }
        )
    ],
    ignore_index=True
)

# --------------------------------------------------
# 2025
# --------------------------------------------------

vab_2025 = vab_2024 * 1.05

future = pd.concat(
    [
        future,
        pd.DataFrame(
            {
                "year": [2025],
                "vab_private": [vab_2025],
                "type": ["estimated"]
            }
        )
    ],
    ignore_index=True
)

# --------------------------------------------------
# COMBINAR
# --------------------------------------------------

result = pd.concat(
    [
        projection,
        future
    ],
    ignore_index=True
)

result = result.sort_values(
    "year"
)

result["growth_pct"] = (
    result["vab_private"]
    .pct_change()
    * 100
)

print("\n===================================")
print("RESULTADO")
print("===================================\n")

print(
    result.tail(10)
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "private_vab_projection.csv"
)

result.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
