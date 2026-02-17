import pandas as pd

season = pd.read_csv("data_processed/season_metrics_2025.csv")
rolling = pd.read_csv("data_processed/rolling_150_snapshot_2025.csv")

final = season.merge(rolling, on="batter", how="left")

print(f"Final merged players: {len(final)}")

final["Trend_xwOBA"] = final["roll_xwOBA"] - final["xwOBA"]
final["Trend_K_pct"] = final["roll_K_pct"] - final["K_pct"]
final["Trend_BB_pct"] = final["roll_BB_pct"] - final["BB_pct"]

final.to_csv("data_processed/final_player_table_2025.csv", index=False)

print("Saved final_player_table_2025.csv")
