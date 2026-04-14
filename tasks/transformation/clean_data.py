import pandas as pd

def clean_data(df):
    print("Cleaning data")

    # sort properly
    df = df.sort_values(by=["symbol", "Date"])

    # handle missing values
    df = df.dropna()

    return df


def calculate_returns(df):
    print("Calculating returns")

    # group by stock
    df["daily_return"] = df.groupby("symbol")["Close"].pct_change()

    return df