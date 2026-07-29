from pyspark.sql import DataFrame


def build_dim_customer(df: DataFrame) -> DataFrame:

    return (
        df.select(
            "customer_id",
            "first_name",
            "last_name",
            "gender",
            "age",
            "city",
            "membership",
            "signup_date",
            "is_active"
        ).dropDuplicates(["customer_id"])
    )