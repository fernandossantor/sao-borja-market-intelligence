import pandas as pd
import os

print("\n===================================")
print("PRIVATE EMPLOYMENT CALIBRATOR")
print("===================================\n")

EXPORT_PATH = (
    "/content/drive/MyDrive/"
    "Colab Notebooks/_sao_borja/exports"
)

df = pd.read_csv(
    os.path.join(
        EXPORT_PATH,
        "private_employment_long_history.csv"
    )
)

# =====================================
# CALIBRATION FACTOR
# =====================================

employment_1735_2006 = 5966
employment_6450_2006 = 8493

factor = (
    employment_6450_2006 /
    employment_1735_2006
)

print("Calibration factor:")
print(round(factor, 6))

# =====================================
# APPLY
# =====================================

df["employment_calibrated"] = (
    df["employment_total"]
)

mask = (
    df["source"] == "rais_1735"
)

df.loc[
    mask,
    "employment_calibrated"
] = (
    df.loc[
        mask,
        "employment_total"
    ]
    * factor
)

# =====================================
# ROUND
# =====================================

df["employment_calibrated"] = (
    df["employment_calibrated"]
    .round(0)
)

# =====================================
# GROWTH
# =====================================

df["growth_calibrated_pct"] = (
    df["employment_calibrated"]
    .pct_change()
    * 100
)

# =====================================
# OUTPUT
# =====================================

print("\n===================================")
print("CALIBRATED SERIES")
print("===================================\n")

print(
    df[
        [
            "year",
            "employment_total",
            "employment_calibrated",
            "source"
        ]
    ]
)

print("\n1996:")
print(
    df.loc[
        df.year == 1996,
        "employment_calibrated"
    ].values[0]
)

print("\n2005:")
print(
    df.loc[
        df.year == 2005,
        "employment_calibrated"
    ].values[0]
)

print("\n2006:")
print(
    df.loc[
        df.year == 2006,
        "employment_calibrated"
    ].values[0]
)

# =====================================
# EXPORT
# =====================================

export_file = os.path.join(
    EXPORT_PATH,
    "private_employment_calibrated.csv"
)

df.to_csv(
    export_file,
    index=False
)

print("\n===================================")
print("EXPORT FINALIZADO")
print("===================================\n")

print(export_file)
