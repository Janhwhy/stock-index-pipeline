import pandas as pd

def compute_metrics(df):
    print("Computing metrics.")

    # group by stock
    metrics = df.groupby("symbol").agg({
        "daily_return": ["mean", "std"]
    }).reset_index()

    # flatten column names
    metrics.columns = ["symbol", "avg_return", "volatility"]

    return metrics


def rank_stocks(metrics):
    print("Ranking stocks.")

    # simple scoring formula
    metrics["score"] = metrics["avg_return"] - metrics["volatility"]

    # sort by score
    ranked = metrics.sort_values(by="score", ascending=False)

    return ranked