import pandas as pd

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    f"{EXPORT_PATH}/public_structural_index.csv"
)

cols = [

    "receita",
    "saude",
    "educacao",
    "assistencia"

]

existing = [
    c
    for c in cols
    if c in df.columns
]

print(
    df[
        ["year"] + existing
    ]
)
