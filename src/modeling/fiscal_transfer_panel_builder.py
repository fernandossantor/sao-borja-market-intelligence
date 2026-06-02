import pandas as pd
import numpy as np
import os
from pathlib import Path

print("\n===================================")
print("FISCAL TRANSFER PANEL BUILDER")
print("===================================\n")

RAW_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/raw/fiscal"
)

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

# --------------------------------------------------
# METADADOS
# --------------------------------------------------

catalog = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_catalog.csv"
    )
)

domain_map = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "fiscal_domain_map.csv"
    )
)

meta = (
    catalog.merge(
        domain_map[
            [
                "file",
                "domain"
            ]
        ],
        on="file",
        how="left"
    )
)

print("\n===================================")
print("META AUDIT")
print("===================================\n")

print(meta.head())

print("\nColunas:")

print(meta.columns.tolist())

# --------------------------------------------------
# LEITOR ROBUSTO
# --------------------------------------------------

def read_fiscal_file(path):

    tests = [
        ("utf-8-sig", ";"),
        ("latin1", ";"),
        ("cp1252", ";"),
        ("utf-8-sig", "\t"),
        ("latin1", "\t"),
        ("cp1252", "\t")
    ]

    for enc, sep in tests:

        try:

            df = pd.read_csv(
                path,
                encoding=enc,
                sep=sep,
                engine="python"
            )

            if len(df.columns) > 3:
                return df

        except:
            pass

    raise ValueError(path)

# --------------------------------------------------
# CONVERSOR MONETÁRIO
# --------------------------------------------------

def parse_brl(x):

    if pd.isna(x):
        return np.nan

    return float(
        str(x)
        .replace(".", "")
        .replace(",", ".")
    )

# --------------------------------------------------
# CONSOLIDAÇÃO
# --------------------------------------------------

frames = []

for file in sorted(Path(RAW_PATH).glob("*.csv")):

    df = read_fiscal_file(file)

    filename = file.name

    cat = meta.loc[
        meta["file"] == filename,
        "category"
    ].iloc[0]

    dom = meta.loc[
        meta["file"] == filename,
        "domain"
    ].iloc[0]

    df["value"] = (
        df["Valor Transferido"]
        .apply(parse_brl)
    )

    df["source_file"] = filename

    df["category"] = cat

    df["domain"] = dom

    # --------------------------
    # DATA
    # --------------------------

    month_map = {
        "jan":1,
        "fev":2,
        "mar":3,
        "abr":4,
        "mai":5,
        "jun":6,
        "jul":7,
        "ago":8,
        "set":9,
        "out":10,
        "nov":11,
        "dez":12
    }

    def parse_date(x):

        x = str(x)

        if "/" in x:

            p1, p2 = x.split("/")

            # formato 01/2020

            if p1.isdigit():

                month = int(p1)

                year = int(p2)

            else:

                month = month_map[
                    p1.lower()[:3]
                ]

                year = 2000 + int(p2)

            return year, month

        return np.nan, np.nan

    parsed = (
        df["Mês/Ano"]
        .apply(parse_date)
    )

    df["year"] = parsed.str[0]

    df["month"] = parsed.str[1]

    df["date"] = pd.to_datetime(
        dict(
            year=df["year"],
            month=df["month"],
            day=1
        )
    )

    panel = pd.DataFrame({

        "date": df["date"],
        "year": df["year"],
        "month": df["month"],

        "category": df["category"],
        "domain": df["domain"],

        "program": df[
            "Linguagem Cidadã"
        ],

        "beneficiary": df[
            "Nome do Favorecido"
        ],

        "function": df[
            "Função"
        ],

        "value": df["value"],

        "source_file": df[
            "source_file"
        ]
    })

    frames.append(panel)

# --------------------------------------------------
# FINAL
# --------------------------------------------------

panel = pd.concat(
    frames,
    ignore_index=True
)

panel = panel.sort_values(
    [
        "date",
        "program"
    ]
)

print("\n===================================")
print("TRANSFER PANEL")
print("===================================\n")

print(panel.head())

print("\nShape:")
print(panel.shape)

print("\nPeríodo:")

print(
    panel["year"].min(),
    "-",
    panel["year"].max()
)

print("\nValor total:")

print(
    round(
        panel["value"].sum(),
        2
    )
)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------

export_file = os.path.join(
    EXPORT_PATH,
    "fiscal_transfer_panel.csv"
)

panel.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
