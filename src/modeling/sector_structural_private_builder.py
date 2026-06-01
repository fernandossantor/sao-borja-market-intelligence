import pandas as pd
import os

print("\n===================================")
print("SECTOR STRUCTURAL PRIVATE")
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

# --------------------------------------------------
# EXCLUSÕES
# --------------------------------------------------

exclude = [
    "Total",
    "O Administração pública, defesa e seguridade social",
    "U Organismos internacionais e outras instituições extraterritoriais"
]

df = df[
    ~df["sector"].isin(exclude)
].copy()

# --------------------------------------------------
# SHARE EMPREGO PRIVADO
# --------------------------------------------------

total_emprego = df["emprego_total"].sum()

df["share_emprego_privado_pct"] = (
    df["emprego_total"]
    /
    total_emprego
) * 100

# --------------------------------------------------
# SHARE SALÁRIOS PRIVADOS
# --------------------------------------------------

total_salarios = df["salarios_empresas"].sum()

df["share_salarios_privado_pct"] = (
    df["salarios_empresas"]
    /
    total_salarios
) * 100

# --------------------------------------------------
# RANKINGS
# --------------------------------------------------

df["ranking_emprego_privado"] = (
    df["emprego_total"]
    .rank(
        ascending=False,
        method="dense"
    )
)

df["ranking_salarios_privado"] = (
    df["salarios_empresas"]
    .rank(
        ascending=False,
        method="dense"
    )
)

# --------------------------------------------------
# ORDENAR
# --------------------------------------------------

private_report = df.sort_values(
    "ranking_emprego_privado"
)

# --------------------------------------------------
# CONCENTRAÇÃO PRIVADA
# --------------------------------------------------

top3 = (
    private_report
    .head(3)
    ["share_emprego_privado_pct"]
    .sum()
)

top5 = (
    private_report
    .head(5)
    ["share_emprego_privado_pct"]
    .sum()
)

hhi = (
    (
        private_report[
            "share_emprego_privado_pct"
        ] ** 2
    ).sum()
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n===================================")
print("TOP EMPREGADORES PRIVADOS")
print("===================================\n")

print(
    private_report[
        [
            "sector",
            "emprego_total",
            "share_emprego_privado_pct",
            "ranking_emprego_privado"
        ]
    ]
    .head(10)
)

print("\n===================================")
print("TOP MASSA SALARIAL PRIVADA")
print("===================================\n")

print(
    private_report
    .sort_values(
        "ranking_salarios_privado"
    )[
        [
            "sector",
            "salarios_empresas",
            "share_salarios_privado_pct",
            "ranking_salarios_privado"
        ]
    ]
    .head(10)
)

print("\n===================================")
print("CONCENTRAÇÃO PRIVADA")
print("===================================\n")

print("Top 3:", round(top3, 2))
print("Top 5:", round(top5, 2))
print("HHI:", round(hhi, 2))

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "sector_structural_private.csv"
)

private_report.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
