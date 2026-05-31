import pandas as pd

obs = pd.read_csv(
    EXPORT_PATH + "/private_vab_observed.csv"
)

share = (
    obs[
        (obs["year"] >= 2017) &
        (obs["year"] <= 2021)
    ]["private_share_pct"]
    .mean()
)

print("Share médio:", share)
