from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

# Create Spark session
spark = (
    SparkSession.builder
    .appName("Bronze Customers")
    .getOrCreate()
)

# Read raw CSV
df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("data/raw/customers.csv")
)

# Add ingestion timestamp
df = df.withColumn("ingestion_timestamp", current_timestamp())

# Write Bronze layer as Parquet
(
    df.write
    .mode("overwrite")
    .parquet("data/bronze/customers")
)

print("Bronze customers created successfully!")
spark.stop()