print("GOLD PIPELINE STARTED")

import sys
import os
import pandas as pd

sys.path.append(os.path.abspath("."))

from tasks.analytics.compute_metrics import compute_metrics, rank_stocks

def run_gold():
    print("▶ Running Gold Pipeline")

    # Step 1: Load silver data
    df = pd.read_csv("data/silver/stock_data_cleaned.csv")

    print("Loaded silver data")

    # Step 2: Compute metrics
    metrics = compute_metrics(df)

    # Step 3: Rank stocks
    ranked = rank_stocks(metrics)

    # Step 4: Save
    os.makedirs("data/gold", exist_ok=True)

    file_path = "data/gold/stock_rankings.csv"
    ranked.to_csv(file_path, index=False)

    print(f"Saved to {file_path}")

if __name__ == "__main__":
    run_gold()