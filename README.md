Data-Engineering
My end-to-end data engineering learning path: ETL pipelines, Advanced SQL, and Automation

🚀 Data Engineering Journey
A comprehensive, step-by-step portfolio demonstrating end-to-end data engineering skills, from basic ETL to advanced analytics and automation.

🎯 Project Overview
This repository documents my progression in data engineering. Instead of multiple fragmented projects, I am building a single, robust data pipeline that evolves in complexity. The core scenario revolves around extracting cryptocurrency market data, transforming it for analytical use, and generating actionable insights.

🏗️ Architecture & Phases
Phase 1: Python ETL Pipeline & Database Migration (Completed)
Objective: Ingest raw financial data from an external API, clean it, and load it into a relational database, evolving from a local prototype to a production-ready architecture.
Tech Stack: Python, Pandas, SQLite (Initial), PostgreSQL (Current), SQLAlchemy, REST API

Process:

Extract: Fetches top 50 cryptocurrencies by market cap using the CoinGecko API.

Transform: Flattens JSON data, standardizes column names, filters out missing values (Null handling), and adds ingestion timestamps.

Load & Architecture Migration: Initially appended the cleaned, structured data into a local SQLite database (kripto_piyasa.db) for rapid prototyping. The infrastructure was subsequently modernized and migrated to a robust PostgreSQL server. The data flow and connection management are now orchestrated using the SQLAlchemy engine for production-level reliability and data integrity.

Phase 2: Advanced Analytical SQL (Completed)
Objective: Utilize CTEs and Window Functions (e.g., RANK()) on the new PostgreSQL architecture to segment data and extract business insights, such as identifying the "Top 3 highest gaining coins in the last 24 hours."

Phase 3: Data Visualization & BI (Upcoming)
Live Dashboard: Tableau Public Profilimde İnceleyin (Connecting directly to the PostgreSQL instance)

Phase 4: Workflow Orchestration (Completed)
Objective: Automate the entire pipeline using Apache Airflow. Implemented retry mechanisms and daily scheduling (Cron format) to ensure consistent, autonomous data ingestion into the PostgreSQL database.
