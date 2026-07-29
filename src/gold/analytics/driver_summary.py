from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    avg,
    count,
    sum,
)


def build_driver_summary(df: DataFrame) -> DataFrame:

    return (
        df.groupBy("driver_id")
        .agg(
            count("*").alias("total_trips"),
            sum("amount").alias("total_revenue"),
            avg("rating").alias("average_rating")
        )
        .orderBy("total_revenue", ascending=False)
    )