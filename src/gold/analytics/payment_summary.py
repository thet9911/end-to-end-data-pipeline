from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    count,
    sum,
)


def build_payment_summary(df: DataFrame) -> DataFrame:

    return (
        df.groupBy("actual_payment_method")
        .agg(
            count("*").alias("total_payments"),
            sum("amount").alias("total_revenue")
        )
        .orderBy("total_revenue", ascending=False)
    )