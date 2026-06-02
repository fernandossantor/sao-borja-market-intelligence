import pandas as pd
import os

print("\n===================================")
print("FISCAL STORYBOARD BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# ----------------------------------
# CARREGAR FACTSHEET
# ----------------------------------

factsheet = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_factsheet.csv"
    )
)

# ----------------------------------
# FUNÇÃO AUXILIAR
# ----------------------------------

def get_value(indicator):

    return factsheet.loc[
        factsheet["indicator"] == indicator,
        "value"
    ].iloc[0]

# ----------------------------------
# STORYBOARD
# ----------------------------------

storyboard = pd.DataFrame(
    [
        [
            "fiscal",
            "fiscal_cagr_pct",
            "Fiscal Growth",
            get_value("CAGR Fiscal (%)")
        ],

        [
            "fiscal",
            "total_transfers",
            "Total Transfers 2020-2025",
            get_value(
                "Transferências Totais (2020-2025)"
            )
        ],

        [
            "fiscal",
            "main_domain",
            "Largest Fiscal Domain",
            get_value(
                "Domínio Principal"
            )
        ],

        [
            "fiscal",
            "main_domain_share_pct",
            "Largest Domain Share",
            get_value(
                "Share Domínio Principal (%)"
            )
        ],

        [
            "fiscal",
            "main_category",
            "Largest Fiscal Category",
            get_value(
                "Categoria Principal"
            )
        ],

        [
            "fiscal",
            "main_category_share_pct",
            "Largest Category Share",
            get_value(
                "Share Categoria Principal (%)"
            )
        ],

        [
            "fiscal",
            "programmatic_dependency_pct",
            "Programmatic Dependency",
            get_value(
                "Dependência Programática Média (%)"
            )
        ],

        [
            "fiscal",
            "structural_dependency_pct",
            "Structural Dependency",
            get_value(
                "Dependência Estrutural Média (%)"
            )
        ],

        [
            "fiscal",
            "dependency_class",
            "Fiscal Dependency Class",
            get_value(
                "Classificação Fiscal"
            )
        ],

        [
            "fiscal",
            "peak_year",
            "Peak Transfer Year",
            get_value(
                "Ano Pico Transferências"
            )
        ],

        [
            "fiscal",
            "peak_transfer_value",
            "Peak Transfer Value",
            get_value(
                "Valor Pico Transferências"
            )
        ]
    ],
    columns=[
        "domain",
        "metric",
        "label",
        "value"
    ]
)

# ----------------------------------
# RESULTADO
# ----------------------------------

print("\n===================================")
print("FISCAL STORYBOARD")
print("===================================\n")

print(storyboard)

# ----------------------------------
# EXPORT
# ----------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_storyboard.csv"
)

storyboard.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
