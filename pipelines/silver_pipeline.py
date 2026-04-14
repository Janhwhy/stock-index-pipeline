import sys
import os
import pandas as pd

sys.path.append(os.path.abspath("."))

from tasks.utils.config_loader import load_config
from tasks.transformation.clean_data import clean_data, calculate_returns
from tasks.monitoring.data_quality import validate_data


def run_silver():
    print("Running Silver Pipeline")

    # load config
    config = load_config()

    bronze_path = config["paths"]["bronze"]
    silver_path = config["paths"]["silver"]

    # load data
    df = pd.read_csv(bronze_path)
    print("Loaded bronze data")

    # validation
    validate_data(df)

    # cleaning
    df = clean_data(df)

    # feature engineering
    df = calculate_returns(df)

    # ensure directory exists
    os.makedirs(os.path.dirname(silver_path), exist_ok=True)

    # save
    df.to_csv(silver_path, index=False)

    print(f"Saved to {silver_path}")


if __name__ == "__main__":
    run_silver()