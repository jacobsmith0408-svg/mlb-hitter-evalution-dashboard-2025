import pandas as pd
import numpy as np
from pybaseball import playerid_reverse_lookup

df = pd.read_csv("data_processed/final_player_table_2025.csv")

def zscore(series):
    return (series - series.mean()) / series.std()

df["z_xwOBA"] = zscore(df["xwOBA"])
df["z_roll_xwOBA"] = zscore(df["roll_xwOBA"])
df["z_HardHit"] = zscore(df["HardHit_pct"])

df["ContactScore"] = (
    0.5 * df["z_xwOBA"] +
    0.3 * df["z_roll_xwOBA"] +
    0.2 * df["z_HardHit"]
)

df["z_K"] = zscore(-df["K_pct"])
df["z_BB"] = zscore(df["BB_pct"])

df["DisciplineScore"] = (
    0.6 * df["z_K"] +
    0.4 * df["z_BB"]
)

df["z_Trend"] = zscore(df["Trend_xwOBA"])

df["TrendScore"] = df["z_Trend"]

df["RawScore"] = (
    0.5 * df["ContactScore"] +
    0.3 * df["DisciplineScore"] +
    0.2 * df["TrendScore"]
)

min_score = df["RawScore"].min()
max_score = df["RawScore"].max()

df["PlayerValueScore"] = 100 * (
    (df["RawScore"] - min_score) / (max_score - min_score)
)

df = df.sort_values("PlayerValueScore", ascending=False)

ids = df["batter"].astype(int).unique().tolist()
lookup = playerid_reverse_lookup(ids, key_type="mlbam")[["key_mlbam", "name_first", "name_last"]]
lookup = lookup.rename(columns={"key_mlbam": "batter"})

df = df.merge(lookup, on="batter", how="left")
df["player_name"] = df["name_first"].fillna("") + " " + df["name_last"].fillna("")


df.to_csv("data_processed/player_value_scores_2025.csv", index=False)

print("Top 10 Players by PlayerValueScore:")
print(df[["player_name", "PlayerValueScore"]].head(10))

print("\nPositive Regression Candidates (Skill > Results + Trending Up):")

pos_reg = df[
    (df["LuckGap_wOBA_minus_xwOBA"] < 0) &
    (df["PlayerValueScore"] > 60) &
    (df["Trend_xwOBA"] > 0)
].sort_values(
    ["Trend_xwOBA", "LuckGap_wOBA_minus_xwOBA"],
    ascending=[False, True]
)

print(pos_reg[[
    "player_name",
    "PlayerValueScore",
    "LuckGap_wOBA_minus_xwOBA",
    "Trend_xwOBA",
    "Trend_K_pct"
]].head(15))


print("\nRegression Risk (Results > Skill + Trending Down):")

reg_risk = df[
    (df["LuckGap_wOBA_minus_xwOBA"] > 0) &
    (df["PlayerValueScore"] < 50) &
    (df["Trend_xwOBA"] < 0)
].sort_values(
    ["LuckGap_wOBA_minus_xwOBA", "Trend_xwOBA"],
    ascending=[False, True]
)

print(reg_risk[[
    "player_name",
    "PlayerValueScore",
    "LuckGap_wOBA_minus_xwOBA",
    "Trend_xwOBA",
    "Trend_K_pct"
]].head(15))


