import sys
import os
import pandas as pd

sys.path.append(os.path.abspath("."))

from tasks.utils.config_loader import load_config
from tasks.analytics.compute_metrics import compute_metrics, rank_stocks


def run_gold():
    print("Running Gold Pipeline")

    # load config
    config = load_config()

    silver_path = config["paths"]["silver"]
    gold_path = config["paths"]["gold"]

    # load data
    df = pd.read_csv(silver_path)
    print("Loaded silver data")

    # compute metrics
    metrics = compute_metrics(df)

    # rank stocks
    ranked = rank_stocks(metrics)

    # ensure directory exists
    os.makedirs(os.path.dirname(gold_path), exist_ok=True)

    # save
    ranked.to_csv(gold_path, index=False)

    print(f"Saved to {gold_path}")


if __name__ == "__main__":
    run_gold()