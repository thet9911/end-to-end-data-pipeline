from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def clean_booking(df: DataFrame) -> DataFrame:

    return (
        df
        .dropDuplicates(["booking_id"])
        .filter(col("booking_id").isNotNull())
        .filter(col("distance_km") > 0)
        .filter(col("duration_min") > 0)
        .filter(col("fare") >= 0)
    )