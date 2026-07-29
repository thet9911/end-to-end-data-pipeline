from pyspark.sql import DataFrame


def build_dim_payment(df: DataFrame) -> DataFrame:

    return (
        df.select(
            "payment_id",
            "booking_id",
            "payment_method",
            "payment_status",
            "amount"
        ).dropDuplicates(["payment_id"])
    )