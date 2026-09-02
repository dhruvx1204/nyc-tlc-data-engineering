import pandas as pd

file_path = "data/yellow_tripdata_2025-01.parquet"

df = pd.read_parquet(file_path)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistics:")
print(df.describe())
print("\nPayment Types:")
print(df["payment_type"].value_counts())
print("\nVendor IDs:")
print(df["VendorID"].value_counts())
print("\nPassenger Count:")
print(df["passenger_count"].value_counts().sort_index())
print("\nPayment Types:")
print(df["payment_type"].value_counts())

print("\nVendor IDs:")
print(df["VendorID"].value_counts())

print("\nStore and Forward Flag:")
print(df["store_and_fwd_flag"].value_counts())

print("\nPassenger Count:")
print(df["passenger_count"].value_counts().sort_index())
print("\nNegative Trip Distances:")
print((df["trip_distance"] < 0).sum())

print("\nNegative Fare Amounts:")
print((df["fare_amount"] < 0).sum())

print("\nNegative Total Amounts:")
print((df["total_amount"] < 0).sum())

print("\nZero Passenger Trips:")
print((df["passenger_count"] == 0).sum())
print("\nNegative Fare Records:")
negative_fares = df[df["fare_amount"] < 0]

print(negative_fares[
    [
        "payment_type",
        "fare_amount",
        "total_amount",
        "trip_distance",
        "passenger_count"
    ]
].head(10))
print("\nNegative Fare Payment Types:")
print(negative_fares["payment_type"].value_counts())
print("\nNegative Fare + Negative Total:")
print(
    (
        (df["fare_amount"] < 0) &
        (df["total_amount"] < 0)
    ).sum()
)
print("\nNegative Fare + Positive Distance:")
print(
    (
        (df["fare_amount"] < 0) &
        (df["trip_distance"] > 0)
    ).sum()
)
print("\nPayment Type 0 + Missing Passenger Count:")

check = (
    (df["payment_type"] == 0) &
    (df["passenger_count"].isna())
)

print(check.sum())
print("\nPayment Type 0 Records:")
print((df["payment_type"] == 0).sum())
payment_zero = df["payment_type"] == 0

print("\nPayment Type 0 Records:", payment_zero.sum())

print(
    "Missing passenger_count:",
    (payment_zero & df["passenger_count"].isna()).sum()
)

print(
    "Missing RatecodeID:",
    (payment_zero & df["RatecodeID"].isna()).sum()
)

print(
    "Missing store_and_fwd_flag:",
    (payment_zero & df["store_and_fwd_flag"].isna()).sum()
)

print(
    "Missing congestion_surcharge:",
    (payment_zero & df["congestion_surcharge"].isna()).sum()
)

print(
    "Missing Airport_fee:",
    (payment_zero & df["Airport_fee"].isna()).sum()
)
df["trip_duration"] = (
    df["tpep_dropoff_datetime"] -
    df["tpep_pickup_datetime"]
)
print("\nTrip Duration:")
print(df["trip_duration"].describe())
print("\nNegative Trip Durations:")
print((df["trip_duration"] < pd.Timedelta(0)).sum())
negative_duration = df[df["trip_duration"] < pd.Timedelta(0)]

print("\nNegative Duration Examples:")
print(
    negative_duration[
        [
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "trip_duration",
            "trip_distance",
            "fare_amount"
        ]
    ].head(10)
)
long_trips = df[df["trip_duration"] > pd.Timedelta(hours=24)]

print("\nTrips Longer Than 24 Hours:")
print(len(long_trips))
print(
    long_trips[
        [
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "trip_duration",
            "trip_distance",
            "fare_amount"
        ]
    ].head(10)
)
print("\nNegative Trip Durations:")
print((df["trip_duration"] < pd.Timedelta(0)).sum())

negative_duration = df[df["trip_duration"] < pd.Timedelta(0)]

print("\nNegative Duration Examples:")
print(
    negative_duration[
        [
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "trip_duration",
            "trip_distance",
            "fare_amount"
        ]
    ].head(10)
)

long_trips = df[df["trip_duration"] > pd.Timedelta(hours=24)]

print("\nTrips Longer Than 24 Hours:")
print(len(long_trips))