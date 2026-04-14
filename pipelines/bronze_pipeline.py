import sys
import os

sys.path.append(os.path.abspath("."))

from tasks.utils.config_loader import load_config
from tasks.ingestion.fetch_yfinance import fetch_data

def run_bronze():
    print("Running Bronze Pipeline")

    config = load_config()

    symbols = config["symbols"]
    file_path = config["paths"]["bronze"]

    df = fetch_data(symbols)

    # ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df.to_csv(file_path, index=False)

    print(f"Saved to {file_path}")


if __name__ == "__main__":
    run_bronze()