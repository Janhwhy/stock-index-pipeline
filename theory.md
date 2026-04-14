# Theory Behind the Stock Index Pipeline

This document explains the key concepts and technologies used in the project. It connects theory with implementation to provide a deeper understanding of the system.

---

## 1. Apache Spark

Apache Spark is a distributed data processing engine designed to handle large-scale data efficiently.

Instead of processing data on a single machine, Spark distributes the workload across multiple nodes, enabling parallel execution.

### Key Idea

* Parallel processing of data
* High performance for large datasets
* Fault-tolerant execution

### In This Project

Spark is used to:

* Process stock data at scale
* Perform transformations and aggregations
* Execute analytics efficiently

---

## 2. Spark DataFrames

A Spark DataFrame is a distributed collection of data organized into rows and columns, similar to a pandas DataFrame.

### Key Differences from pandas

* Distributed (runs across multiple machines)
* Lazy execution (operations are not executed immediately)
* Optimized query execution

### In This Project

* Used to store and transform stock data
* Supports operations like filtering, grouping, and aggregation

---

## 3. Lazy Evaluation

Spark uses lazy evaluation, meaning transformations are not executed immediately. Instead, Spark builds a logical plan and executes it only when an action is triggered.

### Actions include:

* `.show()`
* `.write()`

### Benefits

* Optimized execution plans
* Reduced computation overhead

---

## 4. Medallion Architecture

This project follows the Medallion Architecture, which organizes data into three layers:

### Bronze Layer (Raw Data)

* Stores raw ingested data
* No transformations applied

### Silver Layer (Cleaned Data)

* Data is cleaned and validated
* Feature engineering is performed (e.g., daily returns)

### Gold Layer (Analytics)

* Aggregated data
* Business-level insights (e.g., stock ranking)

### Benefits

* Clear separation of concerns
* Easier debugging
* Scalable pipeline design

---

## 5. Delta Lake

Delta Lake is a storage layer that enhances data lakes by adding reliability and structure.

### Features

* ACID transactions (ensures data consistency)
* Schema enforcement (prevents invalid data)
* Versioning (supports time travel)

### In This Project

Data is stored as Delta tables:

* bronze_stock_data
* silver_stock_data
* gold_stock_rankings

---

## 6. Window Functions

Window functions allow operations across a set of rows related to the current row.

### Problem Solved

Standard aggregations cannot access previous rows.

### Solution

Window functions maintain row-level context.

### Example Used

* `lag()` to access previous day's stock price

### Use Case

Daily return calculation:

* Compare today's price with yesterday's price

---

## 7. Aggregations

Aggregations summarize data using functions like:

* Average (mean)
* Standard deviation

### In This Project

For each stock:

* Average return → performance
* Volatility (standard deviation) → risk

---

## 8. Sharpe Ratio

The Sharpe Ratio measures risk-adjusted return.

### Formula

Sharpe Ratio = Average Return / Volatility

### Interpretation

* Higher Sharpe Ratio → better performance per unit of risk
* Helps compare stocks based on risk vs return

### In This Project

Used to rank stocks in the Gold layer.

---

## 9. ETL Pipeline

The pipeline follows the ETL process:

### Extract

* Fetch stock data using API (yfinance)

### Transform

* Clean data
* Compute daily returns
* Generate metrics

### Load

* Store processed data in Delta tables

---

## 10. Databricks

Databricks is a platform built on top of Spark that provides:

* Interactive notebooks
* Cluster management
* Integration with Delta Lake

### In This Project

* Used to run Spark jobs
* Store and query Delta tables
* Execute the full pipeline

---

## Final Summary

This project combines multiple core concepts:

* Distributed computing using Spark
* Structured data pipelines using Medallion Architecture
* Reliable storage using Delta Lake
* Time-series processing using window functions
* Financial analytics using Sharpe Ratio

Together, these form a complete data engineering and analytics system.
