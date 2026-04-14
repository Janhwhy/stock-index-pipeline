import pandas as pd

def compute_metrics(df):
    print("Computing metrics")

    metrics = df.groupby("symbol").agg({
        "daily_return": ["mean", "std"]
    }).reset_index()

    metrics.columns = ["symbol", "avg_return", "volatility"]

    # Sharpe Ratio (risk-adjusted return)
    metrics["sharpe_ratio"] = metrics["avg_return"] / metrics["volatility"]

    return metrics


def rank_stocks(metrics):
    print("Ranking stocks")

    ranked = metrics.sort_values(by="sharpe_ratio", ascending=False)

    return ranked