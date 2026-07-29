from pathlib import Path

from pyspark.sql import SparkSession


GOLD = Path("data/gold")
EXPORT = Path("data/export")


spark = (
    SparkSession.builder
    .appName("Export Gold Tables")
    .getOrCreate()
)


tables = [
    "fact_trip",
    "dim_customer",
    "dim_driver",
    "dim_payment",
    "customer_summary",
    "driver_summary",
    "payment_summary",
    "revenue_daily",
    "trip_summary"
]


for table in tables:

    print(f"Exporting {table}")

    df = spark.read.parquet(str(GOLD / table))

    (
        df.coalesce(1)
        .write
        .mode("overwrite")
        .option("header", True)
        .csv(str(EXPORT / table))
    )


print("Done!")

spark.stop()