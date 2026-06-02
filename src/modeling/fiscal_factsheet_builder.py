import pandas as pd
import os

print("\n===================================")
print("FISCAL FACTSHEET BUILDER")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# ----------------------------------
# CARREGAR
# ----------------------------------

annual = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_annual_summary.csv"
    )
)

domain = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_domain_summary.csv"
    )
)

category = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_category_summary.csv"
    )
)

dependency = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_dependency_index.csv"
    )
)

# ----------------------------------
# BASE HISTÓRICA VÁLIDA
# ----------------------------------

valid = annual[
    annual["year"] <= 2025
].copy()

# ----------------------------------
# CAGR
# ----------------------------------

start_value = valid.iloc[0]["transfer_total"]

end_value = valid.iloc[-1]["transfer_total"]

years = (
    valid.iloc[-1]["year"]
    -
    valid.iloc[0]["year"]
)

fiscal_cagr = (
    (
        end_value
        /
        start_value
    )
    ** (1 / years)
    - 1
) * 100

# ----------------------------------
# DOMÍNIO PRINCIPAL
# ----------------------------------

main_domain = domain.loc[
    domain["total_value"].idxmax(),
    "domain"
]

main_domain_share = domain.loc[
    domain["total_value"].idxmax(),
    "share_pct"
]

# ----------------------------------
# CATEGORIA PRINCIPAL
# ----------------------------------

main_category = category.loc[
    category["total_value"].idxmax(),
    "category"
]

main_category_share = category.loc[
    category["total_value"].idxmax(),
    "share_pct"
]

# ----------------------------------
# DEPENDÊNCIA MÉDIA
# ----------------------------------

valid_dep = dependency[
    dependency["year"] <= 2025
]

avg_programmatic = (
    valid_dep[
        "programmatic_share_pct"
    ].mean()
)

avg_structural = (
    valid_dep[
        "structural_share_pct"
    ].mean()
)

dependency_class = (
    valid_dep[
        "dependency_class"
    ]
    .value_counts()
    .idxmax()
)

# ----------------------------------
# ANO DE PICO
# ----------------------------------

peak_year = valid.loc[
    valid["transfer_total"].idxmax(),
    "year"
]

peak_value = valid.loc[
    valid["transfer_total"].idxmax(),
    "transfer_total"
]

# ----------------------------------
# FACTSHEET
# ----------------------------------

factsheet = pd.DataFrame(
    [
        ["Transferências Totais (2020-2025)", valid["transfer_total"].sum()],
        ["Transferências 2025", end_value],
        ["CAGR Fiscal (%)", fiscal_cagr],
        ["Domínio Principal", main_domain],
        ["Share Domínio Principal (%)", main_domain_share],
        ["Categoria Principal", main_category],
        ["Share Categoria Principal (%)", main_category_share],
        ["Dependência Programática Média (%)", avg_programmatic],
        ["Dependência Estrutural Média (%)", avg_structural],
        ["Classificação Fiscal", dependency_class],
        ["Ano Pico Transferências", peak_year],
        ["Valor Pico Transferências", peak_value]
    ],
    columns=[
        "indicator",
        "value"
    ]
)

# ----------------------------------
# RESULTADO
# ----------------------------------

print(factsheet)

# ----------------------------------
# EXPORT
# ----------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_factsheet.csv"
)

factsheet.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
