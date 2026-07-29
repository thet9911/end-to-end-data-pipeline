from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim, initcap, to_timestamp

from src.validation.data_quality import drop_nulls, check_positive


def clean_payment(df: DataFrame) -> DataFrame:
    """
    Clean payment data for Silver layer.
    """

    df = drop_nulls(df, ["payment_id", "booking_id"], "payments")

    df = (
        df
        .dropDuplicates(["payment_id"])
        .withColumn("payment_method", initcap(trim(col("payment_method"))))
        .withColumn("payment_status", initcap(trim(col("payment_status"))))
        .withColumn("payment_time", to_timestamp(col("payment_time")))
    )

    df = check_positive(df, "amount", "payments")

    return df