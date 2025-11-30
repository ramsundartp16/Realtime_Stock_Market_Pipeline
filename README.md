# 📈 Real-Time Stock Market Data Pipeline

## 🚀 Simple Overview

This project builds a complete **real-time data pipeline** that processes live stock market data from start to finish:

### 🔄 How It Works:

1. **📡 Grab Live Data** → Pull real-time stock prices from financial APIs
2. **⚡ Stream Instantly** → Use Kafka to handle live data streams  
3. **🔄 Process & Clean** → Transform raw data into analytics-ready formats
4. **📊 Visualize Insights** → Create interactive dashboards with Power BI

### 🛠️ In Technical Terms:

- **Kafka** streams live stock data
- **Airflow** orchestrates the entire workflow
- **Snowflake** stores and processes data at scale  
- **DBT** transforms raw data into clean analytics models
- **Power BI** displays real-time stock insights

### 💡 What You Get:

- **Live stock price monitoring**
- **Automated data processing** (no manual work needed)
- **Ready-to-use analytics** for trading decisions
- **Scalable architecture** that can handle millions of records

Think of it as a **factory assembly line for stock data** - raw numbers go in one end, and beautiful, actionable insights come out the other! 📈✨

## 🏗 Architecture
``` text
    Finnhub API → Kafka Producer → Kafka Cluster → Kafka Consumer → MinIO Storage
        ↓
    Snowflake (Bronze Layer) → DBT Transformations → Snowflake (Silver/Gold Layers)
        ↓
    Power BI → Real-time Dashboards
        ↑
    Apache Airflow (Orchestration)
```
## Project Structure

``` text
    stock_market_project/
    ├── producer/                 # Kafka producer components
    │   ├── producer.py          # Finnhub API data fetcher
    │   └── requirements.txt
    ├── consumer/                # Kafka consumer components
    │   ├── consumer.py          # MinIO data sink
    │   └── requirements.txt
    ├── dbt_stocks/              # Data transformation models
    │   └── models/
    │       ├── bronze/          # Raw data staging
    │       │   ├── bronze_stg_stock_quotes.sql
    │       │   └── sources.yml
    │       ├── silver/          # Cleaned & validated data
    │       │   └── silver_clean_stock_quotes.sql
    │       └── gold/            # Analytics-ready models
    │           ├── gold_candlestick.sql
    │           ├── gold_kpi.sql
    │           └── gold_treechart.sql
    ├── dag/                     # Airflow workflows
    │   └── minio_to_snowflake.py
    ├── snowflake/               # Snowflake configuration
    │   └── sql_init.sql
    ├── docker-compose.yml       # Service orchestration
    ├── requirements.txt         # Python dependencies
    └── README.md               # Project documentation
```
