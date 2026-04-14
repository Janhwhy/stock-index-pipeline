print("🚀 FILE STARTED")

import sys
import os

sys.path.append(os.path.abspath("."))

from tasks.ingestion.fetch_yfinance import fetch_data

def run_bronze():
    print("▶ Running Bronze Pipeline")

    # ✅multiple stocks now works
    df = fetch_data(["AAPL", "TSLA", "MSFT"])

    print(" Data received")

    os.makedirs("data/bronze", exist_ok=True)

    file_path = "data/bronze/stock_data.csv"
    df.to_csv(file_path, index=False)

    print(f"💾 Saved to {file_path}")

if __name__ == "__main__":
    print("MAIN BLOCK RUNNING")
    run_bronze()