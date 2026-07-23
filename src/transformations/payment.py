from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def clean_payment(df: DataFrame) -> DataFrame:

    return (
        df
        .dropDuplicates(["payment_id"])
        .filter(col("payment_id").isNotNull())
        .filter(col("amount") >= 0)
    )
