# Stock Index Pipeline (Bronze–Silver–Gold Architecture)

## Overview

This project implements an end-to-end data pipeline to ingest, transform, and analyze stock market data using both local (pandas) and distributed (PySpark on Databricks) processing.

The pipeline follows the industry-standard **Bronze–Silver–Gold architecture** for data engineering workflows.

---

## Architecture

### Bronze Layer (Raw Data)

* Fetches stock data using `yfinance`
* Stores raw data without transformation
* Output: CSV (local) / Delta table (Databricks)

### Silver Layer (Cleaned Data)

* Removes missing values and duplicates
* Sorts data by symbol and date
* Computes **daily returns** using:

  * pandas (local)
  * Spark window functions (Databricks)

### Gold Layer (Analytics)

* Aggregates metrics:

  * Average return
  * Volatility
* Computes **Sharpe Ratio (risk-adjusted return)**
* Ranks stocks based on performance

---

## Tech Stack

* Python
* pandas
* PySpark
* Delta Lake
* Databricks
* YAML (config-driven pipelines)

---

## Key Features

* Modular pipeline design (Bronze–Silver–Gold)
* Config-driven architecture (no hardcoding)
* Data validation checks
* Spark window functions for time-series processing
* Risk-based ranking using Sharpe Ratio

---

## Project Structure

```
stock-index-pipeline/
│
├── config/
│   └── config.yaml
│
├── pipelines/
│   ├── bronze_pipeline.py
│   ├── silver_pipeline.py
│   └── gold_pipeline.py
│
├── tasks/
│   ├── ingestion/
│   ├── transformation/
│   ├── analytics/
│   ├── monitoring/
│   └── utils/
│
├── data/
├── requirements.txt
└── README.md
```

---

## How to Run (Local)

```bash
python3 pipelines/bronze_pipeline.py
python3 pipelines/silver_pipeline.py
python3 pipelines/gold_pipeline.py
```

---

## Databricks Implementation

The pipeline was also implemented using PySpark on Databricks:

* Bronze layer: Ingested stock data and stored as Delta table
* Silver layer: Applied cleaning and computed daily returns using window functions
* Gold layer: Calculated Sharpe ratio and ranked stocks

Tables created:

* bronze_stock_data
* silver_stock_data
* gold_stock_rankings

---

## Future Improvements

* Dashboard for visualization (Streamlit/Tableau)
* Scheduled jobs using Databricks Workflows
* Machine learning for stock prediction
* Real-time streaming pipeline

---

## Author

Built as a data engineering + analytics project to demonstrate pipeline design, Spark processing, and financial data analysis.
