from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim, initcap, to_date

from src.validation.data_quality import drop_nulls, check_range


def clean_driver(df: DataFrame) -> DataFrame:
    """
    Clean driver data for Silver layer.
    """

    df = drop_nulls(df, ["driver_id"], "drivers")

    df = (
        df
        .dropDuplicates(["driver_id"])
        .withColumn("vehicle_type", initcap(trim(col("vehicle_type"))))
        .withColumn("city", initcap(trim(col("city"))))
        .withColumn("status", initcap(trim(col("status"))))
        .withColumn("join_date", to_date(col("join_date")))
    )

    df = check_range(df, "rating", 1, 5, "drivers")

    return df