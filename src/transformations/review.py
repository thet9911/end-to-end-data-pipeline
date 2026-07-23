from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def clean_review(df: DataFrame) -> DataFrame:

    return (
        df
        .dropDuplicates(["booking_id"])
        .filter(col("rating").between(1, 5))
    )