import os
import pandas as pd

IN_FILE = "data_processed/pa_level_2025.csv"
OUT_DIR = "data_processed"
OUT_FILE = os.path.join(OUT_DIR, "season_metrics_2025.csv")

def safe_div(n, d):
    return (n / d) if d != 0 else 0.0

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    pa = pd.read_csv(IN_FILE, parse_dates=["game_date"])

    g = pa.groupby("batter", as_index=False).agg(
        PA=("PA", "sum"),
        K=("K", "sum"),
        BB=("BB", "sum"),
        HBP=("HBP", "sum"),
        woba_sum=("woba_value", "sum"),
        xwoba_sum=("xwoba_value", "sum"),
        hard_hit=("hard_hit", "sum"),
    )

    # Rates
    g["K_pct"] = g["K"] / g["PA"]
    g["BB_pct"] = g["BB"] / g["PA"]
    g["HBP_pct"] = g["HBP"] / g["PA"]
    g["wOBA"] = g["woba_sum"] / g["PA"]
    g["xwOBA"] = g["xwoba_sum"] / g["PA"]
    g["HardHit_pct"] = g["hard_hit"] / g["PA"]
    g["LuckGap_wOBA_minus_xwOBA"] = g["wOBA"] - g["xwOBA"]

    g = g[g["PA"] >= 200].copy()

    print(f"Qualified hitters (PA>=200): {len(g):,}")

    g.to_csv(OUT_FILE, index=False)
    print(f"Saved: {OUT_FILE}")

if __name__ == "__main__":
    main()
