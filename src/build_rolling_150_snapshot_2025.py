import os
import pandas as pd

IN_FILE = "data_processed/pa_level_2025.csv"
OUT_FILE = "data_processed/rolling_150_snapshot_2025.csv"

WINDOW = 150

def main():
    pa = pd.read_csv(IN_FILE, parse_dates=["game_date"])

    pa = pa.sort_values(["batter", "game_date"])

    def compute_roll(group):
        group = group.copy()
        group["roll_PA"] = group["PA"].rolling(WINDOW, min_periods=WINDOW).sum()
        group["roll_wOBA"] = (
            group["woba_value"].rolling(WINDOW, min_periods=WINDOW).sum() /
            group["PA"].rolling(WINDOW, min_periods=WINDOW).sum()
        )
        group["roll_xwOBA"] = (
            group["xwoba_value"].rolling(WINDOW, min_periods=WINDOW).sum() /
            group["PA"].rolling(WINDOW, min_periods=WINDOW).sum()
        )
        group["roll_K_pct"] = (
            group["K"].rolling(WINDOW, min_periods=WINDOW).sum() /
            group["PA"].rolling(WINDOW, min_periods=WINDOW).sum()
        )
        group["roll_BB_pct"] = (
            group["BB"].rolling(WINDOW, min_periods=WINDOW).sum() /
            group["PA"].rolling(WINDOW, min_periods=WINDOW).sum()
        )
        group["roll_HardHit_pct"] = (
            group["hard_hit"].rolling(WINDOW, min_periods=WINDOW).sum() /
            group["PA"].rolling(WINDOW, min_periods=WINDOW).sum()
        )
        return group

    print("Computing rolling windows...")
    roll = pa.groupby("batter", group_keys=False).apply(compute_roll)

    final_roll = (
        roll.dropna(subset=["roll_xwOBA"])
            .groupby("batter", as_index=False)
            .tail(1)
    )

    print(f"Hitters with full 150 PA rolling window: {len(final_roll):,}")

    final_roll = final_roll[[
        "batter",
        "roll_wOBA",
        "roll_xwOBA",
        "roll_K_pct",
        "roll_BB_pct",
        "roll_HardHit_pct"
    ]]

    final_roll.to_csv(OUT_FILE, index=False)
    print(f"Saved: {OUT_FILE}")

if __name__ == "__main__":
    main()
