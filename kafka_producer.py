import json
import time
import pandas as pd
from kafka import KafkaProducer


# ==============================
# Kafka Producer
# ==============================

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8")
)


# ==============================
# Dataset
# ==============================

file_path = "data/yellow_tripdata_2025-01.parquet"

df = pd.read_parquet(file_path)


print(f"Loaded {len(df):,} taxi records")
print("Starting Kafka streaming...")


# ==============================
# Send records to Kafka
# ==============================

for _, row in df.iterrows():

    event = {
        "VendorID": row["VendorID"],
        "tpep_pickup_datetime": row["tpep_pickup_datetime"],
        "tpep_dropoff_datetime": row["tpep_dropoff_datetime"],
        "passenger_count": row["passenger_count"],
        "trip_distance": row["trip_distance"],
        "fare_amount": row["fare_amount"],
        "total_amount": row["total_amount"],
        "payment_type": row["payment_type"]
    }

    producer.send(
        "nyc-tlc-trips",
        value=event
    )

    print(
        f"Sent → Vendor: {event['VendorID']} | "
        f"Distance: {event['trip_distance']} miles | "
        f"Total: ${event['total_amount']}"
    )

    # Small delay to simulate real-time streaming
    time.sleep(0.05)


producer.flush()

print("Finished streaming all records.")