# NYC TLC Real-Time Taxi Analytics

An end-to-end Data Engineering and Business Intelligence project that simulates real-time NYC taxi trip processing using Kafka, Python, PostgreSQL, and Power BI.

## Project Overview

This project builds a streaming data pipeline using NYC TLC Yellow Taxi trip data.

The pipeline reads Parquet data, publishes taxi events to Apache Kafka, consumes the events using Python, stores them in PostgreSQL, and visualizes the processed data through Power BI.

## Architecture
```mermaid
flowchart LR
    A[NYC TLC Parquet Data] --> B[Python Producer]
    B --> C[Apache Kafka]
    C --> D[Python Consumer]
    D --> E[PostgreSQL]
    E --> F[Power BI Dashboard]
```

NYC TLC Parquet Dataset
        ↓
Python Kafka Producer
        ↓
Apache Kafka
        ↓
Python Kafka Consumer
        ↓
PostgreSQL
        ↓
Power BI Dashboard

## Technology Stack

- Python
- Apache Kafka
- kafka-python
- PostgreSQL
- SQL
- Pandas
- PyArrow
- Power BI
- Parquet

## Key Features

- Parquet-based NYC TLC data ingestion
- Kafka-based event streaming
- Python producer and consumer
- PostgreSQL data storage
- Duplicate-event protection using a database UNIQUE constraint
- Invalid JSON event handling
- Non-TLC event filtering
- Power BI analytics dashboard
- Revenue and trip-performance analysis
- Vendor-level revenue analysis
- Payment-type analysis
- Trip distance vs revenue analysis

## Data Pipeline

### 1. Data Source

NYC TLC Yellow Taxi trip records are used as the source dataset.

The source data is stored in Parquet format.

### 2. Kafka Producer

`kafka_producer.py` reads taxi records from the Parquet dataset and publishes them to the Kafka topic:

`nyc-tlc-trips`

A small delay between events is used to simulate real-time streaming.

### 3. Kafka Consumer

`kafka_consumer.py` consumes events from Kafka and validates the incoming data before inserting it into PostgreSQL.

The consumer handles:

- Invalid JSON events
- Non-TLC events
- Duplicate taxi events
- PostgreSQL insertion errors

### 4. PostgreSQL

Processed events are stored in the `taxi_trips` table inside the `nyc_tlc` database.

Duplicate protection is implemented using a composite UNIQUE constraint based on:

- Vendor ID
- Pickup timestamp
- Dropoff timestamp
- Trip distance

### 5. Power BI

Power BI connects to PostgreSQL and provides an analytics dashboard containing:

- Total Trips
- Total Revenue
- Average Trip Value
- Total Distance
- Average Trip Distance
- Revenue & Trip Performance
- Revenue by Vendor
- Trip Distance vs Revenue
- Payment Type Analysis

## Example Results

At the time of testing, the PostgreSQL pipeline processed:

- Total Trips: 8,718
- Total Revenue: $223,734.90
- Total Distance: 25,630.45 miles
- Average Trip Value: $25.66
- Average Trip Distance: 2.94 miles

## Project Structure

```text
nyc_tlc_data_engineering/
│
├── data/
│   └── NYC TLC Parquet dataset
│
├── sql/
│   └── SQL scripts
│
├── event_time_demo.py
├── inspect_data.py
├── kafka_consumer.py
├── kafka_producer.py
├── test_postgres.py
├── requirements.txt
├── .gitignore
└── README.md
