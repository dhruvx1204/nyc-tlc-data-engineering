import json
import os
import psycopg2
from kafka import KafkaConsumer


# ==============================
# PostgreSQL connection
# ==============================

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="nyc_tlc",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()


# ==============================
# Kafka consumer
# ==============================

consumer = KafkaConsumer(
    "nyc-tlc-trips",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="python-taxi-processing-v3"
)

print("Waiting for NYC TLC events...")


# ==============================
# Process Kafka messages
# ==============================

for message in consumer:

    try:

        # Decode Kafka message
        raw_value = message.value.decode("utf-8")

        # Convert JSON text to Python dictionary
        data = json.loads(raw_value)

        # Check required TLC fields
        required_fields = [
            "VendorID",
            "trip_distance",
            "fare_amount",
            "total_amount"
        ]

        if not all(field in data for field in required_fields):
            print("Skipped non-TLC event")
            continue

        # Insert into PostgreSQL
        cursor.execute(
            """
            INSERT INTO taxi_trips (
                vendor_id,
                pickup_datetime,
                dropoff_datetime,
                passenger_count,
                trip_distance,
                fare_amount,
                total_amount,
                payment_type
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

            ON CONFLICT (
                vendor_id,
                pickup_datetime,
                dropoff_datetime,
                trip_distance
            )
            DO NOTHING
            """,
            (
                data.get("VendorID"),
                data.get("tpep_pickup_datetime"),
                data.get("tpep_dropoff_datetime"),
                data.get("passenger_count"),
                data.get("trip_distance"),
                data.get("fare_amount"),
                data.get("total_amount"),
                data.get("payment_type")
            )
        )

        conn.commit()

        # Check whether row was inserted
        if cursor.rowcount == 1:

            print(
                f"Stored → Vendor: {data.get('VendorID')} | "
                f"Distance: {data.get('trip_distance')} miles | "
                f"Total: ${data.get('total_amount')}"
            )

        else:

            print(
                f"Duplicate skipped → Vendor: {data.get('VendorID')} | "
                f"Distance: {data.get('trip_distance')} miles"
            )

    except json.JSONDecodeError:

        print("Skipped invalid JSON event")

    except Exception as e:

        conn.rollback()

        print(f"Error processing event: {e}")