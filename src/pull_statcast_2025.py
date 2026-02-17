import os
import pandas as pd
from pybaseball import statc

OUT_DIR = "data_raw"
OUT_FILE = os.path.join(OUT_DIR, "statcast_2025_pitch_level.csv")

DATE_RANGES = [
    ("2025-03-01", "2025-03-31"),
    ("2025-04-01", "2025-04-30"),
    ("2025-05-01", "2025-05-31"),
    ("2025-06-01", "2025-06-30"),
    ("2025-07-01", "2025-07-31"),
    ("2025-08-01", "2025-08-31"),
    ("2025-09-01", "2025-09-30"),
    ("2025-10-01", "2025-10-02"),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    chunks = []
    for start_dt, end_dt in DATE_RANGES:
        print(f"Pulling {start_dt} to {end_dt} ...")
        df = statcast(start_dt=start_dt, end_dt=end_dt)

        df = df[df["batter"].notna()].copy()

        print(f"  Rows: {len(df):,}")
        chunks.append(df)

    full = pd.concat(chunks, ignore_index=True)

    full = full.drop_duplicates()

    print("\nFINAL")
    print(f"Total rows: {len(full):,}")
    print(f"Columns: {len(full.columns)}")

    full.to_csv(OUT_FILE, index=False)
    print(f"\nSaved to: {OUT_FILE}")

    must_have = ["game_pk", "at_bat_number", "pitch_number", "batter", "game_date", "events"]
    print("\nColumn checks:")
    for c in must_have:
        print(f"  {c}: {'YES' if c in full.columns else 'NO'}")

    optional = ["estimated_woba_using_speedangle", "woba_value", "woba_denom", "barrel"]
    print("\nOptional columns:")
    for c in optional:
        print(f"  {c}: {'YES' if c in full.columns else 'NO'}")

if __name__ == "__main__":
    main()
