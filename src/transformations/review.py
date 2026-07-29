from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim, to_date

from src.validation.data_quality import drop_nulls, check_range


def clean_review(df: DataFrame) -> DataFrame:
    """
    Clean review data for Silver layer.
    """

    df = drop_nulls(df, ["booking_id"], "reviews")

    df = (
        df
        .dropDuplicates(["booking_id"])
        .withColumn("review_text", trim(col("review_text")))
        .withColumn("review_date", to_date(col("review_date")))
    )

    df = check_range(df, "rating", 1, 5, "reviews")

    return df