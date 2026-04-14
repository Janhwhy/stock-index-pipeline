import yfinance as yf
import pandas as pd

def fetch_data(symbols=["AAPL"]):
    print("📡 Fetching data...")

    all_data = []

    for symbol in symbols:
        print(f"Fetching {symbol}...")

        df = yf.download(symbol, period="1mo", progress=False)

        df = df.reset_index()
        df["symbol"] = symbol

        all_data.append(df)

    # combine all stocks
    final_df = pd.concat(all_data, ignore_index=True)

    print("Shape:", final_df.shape)

    return final_df