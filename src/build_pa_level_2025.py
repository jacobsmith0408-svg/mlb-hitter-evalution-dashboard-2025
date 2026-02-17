import os
import pandas as pd

IN_FILE = "data_raw/statcast_2025_pitch_level.csv"
OUT_DIR = "data_processed"
OUT_FILE = os.path.join(OUT_DIR, "pa_level_2025.csv")

USECOLS = [
    "game_pk", "batter", "at_bat_number", "pitch_number",
    "game_date", "events",
    "woba_denom", "woba_value", "estimated_woba_using_speedangle",
    "launch_speed"
]

DTYPES = {
    "game_pk": "int64",
    "batter": "int64",
    "at_bat_number": "int16",
    "pitch_number": "int16",
    "events": "string",
    "woba_denom": "float32",
    "woba_value": "float32",
    "estimated_woba_using_speedangle": "float32",
    "launch_speed": "float32",
}

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print("Reading CSV (selected columns only)...")
    df = pd.read_csv(
        IN_FILE,
        usecols=USECOLS,
        dtype=DTYPES,
        parse_dates=["game_date"],
        low_memory=False
    )
    print(f"Rows read: {len(df):,}")

    print("Sorting...")
    df = df.sort_values(["game_pk", "batter", "at_bat_number", "pitch_number"])

    print("Collapsing to PA level (last pitch per PA)...")
    pa = (
        df.groupby(["game_pk", "batter", "at_bat_number"], as_index=False)
          .tail(1)
          .copy()
    )

    pa = pa[pa["woba_denom"].fillna(0) > 0].copy()

    events = pa["events"].fillna("").str.lower()

    pa_out = pd.DataFrame({
        "batter": pa["batter"].astype("int64"),
        "game_date": pa["game_date"],
        "PA": 1,
        "K": events.str.contains("strikeout").astype("int8"),
        "BB": (events == "walk").astype("int8"),
        "HBP": (events == "hit_by_pitch").astype("int8"),
        "woba_value": pa["woba_value"].fillna(0).astype("float32"),
        "xwoba_value": pa["estimated_woba_using_speedangle"].fillna(0).astype("float32"),
        "hard_hit": (pa["launch_speed"].fillna(-1) >= 95).astype("int8"),
    })

    print(f"Total PA rows: {len(pa_out):,}")

    print("Saving...")
    pa_out.to_csv(OUT_FILE, index=False)
    print(f"Saved: {OUT_FILE}")

if __name__ == "__main__":
    main()

