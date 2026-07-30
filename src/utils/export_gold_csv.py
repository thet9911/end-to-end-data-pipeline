from pathlib import Path

from src.utils.spark_session import create_spark
from src.config.config import GOLD_PATH

spark = create_spark("Export CSV")

tables = [
    "fact_trip",
    "dim_customer",
    "dim_driver",
    "dim_payment",
    "revenue_daily",
    "customer_summary",
    "driver_summary",
    "payment_summary",
    "trip_summary",
]

output_dir = Path("dashboard/data")
output_dir.mkdir(parents=True, exist_ok=True)

for table in tables:
    print(f"Exporting {table}...")
    df = spark.read.parquet(str(GOLD_PATH / table))

    (
        df.coalesce(1)
        .write.mode("overwrite")
        .option("header", True)
        .csv(str(output_dir / table))
    )

print("✅ Export Complete")

spark.stop()