from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    count,
    sum,
    to_date,
)


def build_revenue_daily(fact_trip: DataFrame) -> DataFrame:
    """
    Daily revenue and trip summary.
    """

    return (
        fact_trip
        .withColumn(
            "trip_date",
            to_date(col("booking_time"))
        )
        .groupBy("trip_date")
        .agg(
            sum("amount").alias("total_revenue"),
            count("*").alias("total_trips")
        )
        .orderBy("trip_date")
    )