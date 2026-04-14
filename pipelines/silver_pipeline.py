print("SILVER PIPELINE STARTED")

import sys
import os
import pandas as pd

sys.path.append(os.path.abspath("."))

from tasks.transformation.clean_data import clean_data, calculate_returns

def run_silver():
    print("▶ Running Silver Pipeline")

    # Step 1: Load bronze data
    df = pd.read_csv("data/bronze/stock_data.csv")

    print("Loaded bronze data")

    # Step 2: Clean
    df = clean_data(df)

    # Step 3: Calculate returns
    df = calculate_returns(df)

    # Step 4: Save
    os.makedirs("data/silver", exist_ok=True)

    file_path = "data/silver/stock_data_cleaned.csv"
    df.to_csv(file_path, index=False)

    print(f"Saved to {file_path}")

if __name__ == "__main__":
    run_silver()