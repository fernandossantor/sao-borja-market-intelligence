import pandas as pd
import numpy as np
import os

print("\n===================================")
print("SECTOR LONGITUDINAL SUMMARY")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_sector_master_panel.csv"
    )
)

# ----------------------------------------
# REMOVER TOTAL
# ----------------------------------------

df = df[
    df["sector"] != "Total"
].copy()

# ----------------------------------------
# RESUMO
# ----------------------------------------

rows = []

for sector in sorted(
    df["sector"].unique()
):

    temp = df[
        df["sector"] == sector
    ].sort_values("year")

    emp_start = temp.iloc[0]["emprego_total"]
    emp_end = temp.iloc[-1]["emprego_total"]

    sal_start = temp.iloc[0]["salarios_empresas"]
    sal_end = temp.iloc[-1]["salarios_empresas"]

    years = (
        temp.iloc[-1]["year"]
        -
        temp.iloc[0]["year"]
    )

    emp_cagr = np.nan
    sal_cagr = np.nan

    if (
        pd.notna(emp_start)
        and pd.notna(emp_end)
        and emp_start > 0
        and years > 0
    ):
        emp_cagr = (
            (
                emp_end
                /
                emp_start
            )
            ** (1 / years)
            - 1
        ) * 100

    if (
        pd.notna(sal_start)
        and pd.notna(sal_end)
        and sal_start > 0
        and years > 0
    ):
        sal_cagr = (
            (
                sal_end
                /
                sal_start
            )
            ** (1 / years)
            - 1
        ) * 100

    rows.append([
        sector,
        temp["emprego_total"].mean(),
        temp["salarios_empresas"].mean(),
        emp_cagr,
        sal_cagr,
        temp["emprego_total"].std()
    ])

summary = pd.DataFrame(
    rows,
    columns=[
        "sector",
        "emprego_medio",
        "salarios_medios",
        "emprego_cagr_pct",
        "salarios_cagr_pct",
        "emprego_volatilidade"
    ]
)

# ----------------------------------------
# RANKINGS
# ----------------------------------------

summary["rank_emprego_medio"] = (
    summary["emprego_medio"]
    .rank(
        ascending=False,
        method="dense"
    )
)

summary["rank_salarios_medios"] = (
    summary["salarios_medios"]
    .rank(
        ascending=False,
        method="dense"
    )
)

summary = summary.sort_values(
    "rank_emprego_medio"
)

print(summary.head(15))

export_file = os.path.join(
    EXPORT_PATH,
    "sector_longitudinal_summary.csv"
)

summary.to_csv(
    export_file,
    index=False
)

print("\nExportado:")
print(export_file)
