import yfinance as yf
import pandas as pd

def fetch_data(symbols=["AAPL"]):
    print("Fetching data...")

    all_data = []

    for symbol in symbols:
        print(f"Fetching {symbol}...")

        df = yf.download(symbol, period="1mo", progress=False)

        # FLATTEN columns (IMPORTANT FIX)
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

        df = df.reset_index()

        df["symbol"] = symbol

        # keep only required columns
        df = df[["Date", "Open", "High", "Low", "Close", "Volume", "symbol"]]

        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)

    print("Shape:", final_df.shape)

    return final_df