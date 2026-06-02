import pandas as pd
import os

print("\n===================================")
print("FISCAL CATEGORY SUMMARY")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# -----------------------------------
# CARREGAR PAINEL FISCAL
# -----------------------------------

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_transfer_panel.csv"
    )
)

# -----------------------------------
# RESUMO POR CATEGORIA
# -----------------------------------

summary = (
    df.groupby("category")["value"]
    .agg(
        total_value="sum",
        records="count"
    )
    .reset_index()
)

summary["share_pct"] = (
    summary["total_value"]
    /
    summary["total_value"].sum()
    * 100
)

summary = summary.sort_values(
    "total_value",
    ascending=False
)

# -----------------------------------
# RESULTADO
# -----------------------------------

print(summary)

# -----------------------------------
# EXPORT
# -----------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_category_summary.csv"
)

summary.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
