import pandas as pd
import os

print("\n===================================")
print("PRIVATE VAB PROJECTION")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# CARREGAR SÉRIE OBSERVADA
# --------------------------------------------------

obs = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_vab_observed.csv"
    )
)

obs = obs.dropna(
    subset=["private_share_pct"]
)

# --------------------------------------------------
# SHARE MÉDIO
# --------------------------------------------------

share_2017_2021 = (
    obs[
        (obs["year"] >= 2017)
        &
        (obs["year"] <= 2021)
    ]["private_share_pct"]
    .mean()
)

share_2017_2020 = (
    obs[
        (obs["year"] >= 2017)
        &
        (obs["year"] <= 2020)
    ]["private_share_pct"]
    .mean()
)

print("Share privado médio 2017-2021:")
print(round(share_2017_2021, 2))

print("\nShare privado médio 2017-2020:")
print(round(share_2017_2020, 2))

# --------------------------------------------------
# CAGR OBSERVADO
# --------------------------------------------------

start = obs.iloc[0]["vab_private"]
end = obs.iloc[-1]["vab_private"]

years = (
    obs.iloc[-1]["year"]
    -
    obs.iloc[0]["year"]
)

cagr = (
    (end / start) ** (1 / years)
    -
    1
)

print("\nCAGR 2002-2021:")
print(round(cagr * 100, 2), "%")

# --------------------------------------------------
# PIB CANÔNICO
# --------------------------------------------------

pib = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "pib_canonical.csv"
    )
)

print("\n===================================")
print("PIB 2020+")
print("===================================\n")

print(
    pib[
        pib["year"] >= 2020
    ][
        [
            "year",
            "pib_total",
            "vab_total"
        ]
    ]
)

# --------------------------------------------------
# EXPORT DE MÉTRICAS
# --------------------------------------------------

metrics = pd.DataFrame(
    {
        "metric": [
            "share_2017_2021",
            "share_2017_2020",
            "private_vab_cagr"
        ],
        "value": [
            share_2017_2021,
            share_2017_2020,
            cagr * 100
        ]
    }
)

export_file = os.path.join(
    EXPORT_PATH,
    "private_vab_projection_metrics.csv"
)

metrics.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
