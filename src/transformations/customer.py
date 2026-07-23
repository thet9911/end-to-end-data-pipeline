from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    upper,
    trim,
    col,
    when,
    to_date
)


def clean_customer(df: DataFrame) -> DataFrame:
    """
    Clean customer data for Silver layer.
    """

    return (
        df
        .dropDuplicates(["customer_id"])
        .filter(col("customer_id").isNotNull())
        .withColumn(
            "membership",
            upper(trim(col("membership")))
        )
        .withColumn(
            "gender",
            when(
                upper(col("gender")) == "MALE",
                "Male"
            ).otherwise("Female")
        )
        .withColumn(
            "signup_date",
            to_date(col("signup_date"))
        )
        .filter(
            col("age").between(18, 70)
        )
    )