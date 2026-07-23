from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    trim,
    initcap,
    when
)


def clean_driver(df: DataFrame) -> DataFrame:

    return (
        df
        .dropDuplicates(["driver_id"])
        .filter(col("driver_id").isNotNull())
        .withColumn(
            "driver_name",
            initcap(trim(col("driver_name")))
        )
        .withColumn(
            "vehicle_type",
            initcap(trim(col("vehicle_type")))
        )
        .filter(
            col("rating").between(1, 5)
        )
        .withColumn(
            "status",
            when(col("status") == "Active", "Active")
            .when(col("status") == "Inactive", "Inactive")
            .otherwise("Suspended")
        )
    )