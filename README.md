# Data-Engineering
My end-to-end data engineering learning path: ETL pipelines, Advanced SQL, and Automation
# 🚀 Data Engineering Journey

A comprehensive, step-by-step portfolio demonstrating end-to-end data engineering skills, from basic ETL to advanced analytics and automation.

## 🎯 Project Overview
This repository documents my progression in data engineering. Instead of multiple fragmented projects, I am building a single, robust data pipeline that evolves in complexity. The core scenario revolves around extracting cryptocurrency market data, transforming it for analytical use, and generating actionable insights.

## 🏗️ Architecture & Phases

### Phase 1: Python ETL Pipeline (Completed)
*   **Objective:** Ingest raw financial data from an external API, clean it, and load it into a local relational database.
*   **Tech Stack:** Python, Pandas, SQLite, REST API
*   **Process:**
    *   **Extract:** Fetches top 50 cryptocurrencies by market cap using the CoinGecko API.
    *   **Transform:** Flattens JSON data, standardizes column names, filters out missing values (Null handling), and adds ingestion timestamps.
    *   **Load:** Appends the cleaned, structured data into a local `SQLite` database (`kripto_piyasa.db`) for historical tracking.

### Phase 2: Advanced Analytical SQL (Completed)
*   **Objective:** Utilize `CTEs` and `Window Functions` (e.g., `RANK()`) to segment data and extract business insights, such as identifying the "Top 3 highest gaining coins in the last 24 hours."

### Phase 3: Data Visualization & BI (Upcoming)
*   **Objective:** Connect the local database to a BI tool (Power BI/Tableau) to build interactive dashboards for business stakeholders.

### Phase 4: Workflow Orchestration (Completed)
*   **Objective:** Automate the entire pipeline using Apache Airflow, implementing retry mechanisms and daily scheduling.

## ⚙️ How to Run Locally

1. Clone this repository:
 git clone [https://github.com/ceydauzn/Data-Engineering-Journey.git](https://github.com/ceydauzn/Data-Engineering-Journey.git)
