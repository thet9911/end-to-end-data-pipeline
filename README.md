# End-to-End Ride Booking Data Engineering Pipeline

A production-style Data Engineering project built with **PySpark** that simulates a real-world ride-booking platform (similar to Grab or Uber). This project demonstrates the complete data engineering lifecycle—from raw data generation and ingestion to data warehousing and analytics-ready datasets for business intelligence.

---

## Project Overview

This project showcases the design and implementation of a modern ETL pipeline using the **Medallion Architecture (Bronze → Silver → Gold)**.

Raw CSV and JSON datasets are ingested into a Bronze layer, cleaned and standardized in a Silver layer, and transformed into a dimensional data warehouse in the Gold layer. The final datasets are optimized for SQL analytics and Power BI dashboards.

---

## Architecture

```
                Raw Data (CSV / JSON)
                         │
                         ▼
                 Bronze Layer
              (Raw Parquet Storage)
                         │
                         ▼
                 Silver Layer
          (Cleaned & Standardized)
                         │
                         ▼
                  Gold Warehouse
       (Fact & Dimension Tables)
                         │
                         ▼
              Analytics Data Marts
                         │
                         ▼
                 Power BI Dashboard
```

---

## Dataset

The project simulates a ride-booking business.

### Raw Data Sources

- customers.csv
- bookings.csv
- drivers.csv
- payments.json
- reviews.json

Generated records include:

- Customer information
- Driver information
- Trip bookings
- Payment transactions
- Customer reviews

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| Processing | PySpark |
| Engine | Apache Spark |
| Storage | Parquet |
| Analytics | SQL |
| Dashboard | Power BI |
| Container | Docker |
| Version Control | Git |
| IDE | VS Code |

---

# Project Structure

```
end-to-end-data-pipeline/
│
├── config/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── docs/
│
├── logs/
│
├── notebooks/
│
├── scripts/
│
├── sql/
│   └── analytics/
│
├── src/
│   ├── config/
│   ├── generators/
│   ├── gold/
│   │   └── analytics/
│   ├── pipelines/
│   ├── transformations/
│   ├── quality/
│   ├── utils/
│   └── validation/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run_pipeline.py
└── README.md
```

---

# ETL Pipeline

## Bronze Layer

Purpose:

- Ingest raw CSV & JSON files
- Preserve original data
- Add ingestion timestamp
- Store as Parquet

Output:

```
data/bronze/
```

---

## Silver Layer

Purpose:

- Clean invalid records
- Standardize schemas
- Convert data types
- Remove duplicates
- Prepare analytics-ready data

Output:

```
data/silver/
```

---

## Gold Layer

Purpose:

Build a dimensional warehouse.

### Fact Table

- fact_trip

### Dimension Tables

- dim_customer
- dim_driver
- dim_payment

### Analytics Tables

- revenue_daily
- customer_summary
- driver_summary
- payment_summary
- trip_summary

Output:

```
data/gold/
```

---

# Star Schema

```
                    dim_customer
                          │
                          │
dim_driver ─────── fact_trip ─────── dim_payment
                          │
                          │
               Analytics Tables
```

---

# Analytics Tables

## revenue_daily

Daily revenue and trip counts.

---

## customer_summary

Customer KPIs including:

- Total trips
- Total spending
- Average trip fare

---

## driver_summary

Driver KPIs including:

- Total trips
- Revenue generated
- Average rating

---

## payment_summary

Revenue breakdown by payment method.

---

## trip_summary

Trip counts grouped by trip status.

---

# 🔍 SQL Analytics

Included SQL queries:

- Daily Revenue
- Top Customers
- Top Drivers
- Revenue by Payment Method
- Peak Hours
- Trip Status Analysis
- Business KPIs
- Customer Retention
- Revenue by City
- Driver Performance

Located in:

```
sql/analytics/
```

---

# Data Quality

The pipeline performs automatic validation including:

- Null value detection
- Duplicate record detection
- Row count validation
- Negative value detection

Example report:

```
========================================
DATA QUALITY REPORT
========================================

Rows: 100000

Duplicate booking_id: 0

Negative amount: 0

========================================
```

---

# Power BI Dashboard

The project includes an interactive Power BI dashboard with the following pages:

### Executive Dashboard

- Total Revenue
- Total Trips
- Active Customers
- Active Drivers
- Average Rating

---

### Revenue Dashboard

- Daily Revenue
- Revenue by Payment Method
- Revenue by City

---

### Customer Dashboard

- Customer Spending
- Membership Distribution
- Top Customers

---

### Driver Dashboard

- Top Drivers
- Driver Ratings
- Revenue by Driver

---

### Trip Dashboard

- Trip Status
- Average Distance
- Average Fare
- Surge Pricing

---

# Running the Project

## Clone

```bash
git clone https://github.com/thet9911/end-to-end-data-pipeline.git
```

---

## Install

```bash
pip install -r requirements.txt
```

---

## Run Entire Pipeline

```bash
python run_pipeline.py
```

---

## Run Individual Pipelines

Bronze

```bash
python -m src.pipelines.bronze_pipeline customers csv
```

Silver

```bash
python -m src.pipelines.silver_pipeline
```

Gold

```bash
python -m src.pipelines.gold_pipeline
```

---

# Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

# Screenshots

Architecture

```
docs/architecture.png
```

Pipeline

```
docs/pipeline.png
```

Dashboard

```
dashboard/screenshots/
```

---

# Future Improvements

- Apache Airflow orchestration
- AWS S3 integration
- Delta Lake
- Databricks deployment
- Kafka streaming
- Great Expectations for data quality
- GitHub Actions CI/CD
- Unit and integration testing

---

# Skills Demonstrated

- Data Engineering
- ETL Pipeline Development
- PySpark
- Apache Spark
- Data Warehousing
- Medallion Architecture
- Star Schema Design
- SQL Analytics
- Data Quality Validation
- Docker
- Power BI
- Git
- Python

---

# Author

**Thet Myat Noe**

Data Engineer

Singapore

GitHub:
https://github.com/thet9911

LinkedIn:
https://www.linkedin.com/in/thet-myat-noe-a8036426a/

---
