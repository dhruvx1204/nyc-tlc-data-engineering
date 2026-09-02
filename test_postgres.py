import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="nyc_tlc",
    user="postgres",
    password="Dhruv@1204",
    port=5432
)

print("PostgreSQL connection successful!")

conn.close()