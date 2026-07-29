from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim, initcap, to_timestamp

from src.validation.data_quality import drop_nulls, check_positive


def clean_booking(df: DataFrame) -> DataFrame:
    """
    Clean booking data for Silver layer.
    """

    df = drop_nulls(df, ["booking_id", "customer_id", "driver_id", "booking_time"], "bookings")

    df = (
        df
        .dropDuplicates(["booking_id"])
        .withColumn("booking_time", to_timestamp(col("booking_time")))
        .withColumn("trip_status", initcap(trim(col("trip_status"))))
        .withColumn("payment_method", initcap(trim(col("payment_method"))))
        .withColumn("pickup_location", initcap(trim(col("pickup_location"))))
        .withColumn("dropoff_location", initcap(trim(col("dropoff_location"))))
        .filter(col("distance_km") > 0)
        .filter((col("trip_status") != "Completed") | (col("fare") > 0))
    )

    return df