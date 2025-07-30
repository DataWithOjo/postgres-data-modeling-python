# Postgres Data Modeling with Python

This project demonstrates how to design a PostgreSQL data model with proper schema constraints, and load CSV data into the database using Python and the `psycopg2` library.

## 🚀 Project Overview

- 🧱 Design and implement PostgreSQL `CREATE TABLE` statements with proper data types, indexes, primary and foreign keys.
- 🔌 Use Python and `psycopg2` to connect to Postgres.
- 📄 Ingest and load data from CSV files into the tables.

## 🛠️ Tech Stack

- Python 3
- PostgreSQL
- psycopg2
- Docker & Docker Compose

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/postgres-data-modeling-python.git
cd postgres-data-modeling-python
docker build --tag=exercise-5 .
docker-compose up

