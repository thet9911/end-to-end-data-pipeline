from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    avg,
    count,
    sum,
)


def build_customer_summary(df: DataFrame) -> DataFrame:

    return (
        df.groupBy("customer_id")
        .agg(
            count("*").alias("total_trips"),
            sum("amount").alias("total_spending"),
            avg("amount").alias("average_trip_fare")
        )
        .orderBy("total_spending", ascending=False)
    )