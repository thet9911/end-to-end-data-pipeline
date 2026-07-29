from pyspark.sql import DataFrame


def build_dim_driver(df: DataFrame) -> DataFrame:

    return (
        df.select(
            "driver_id",
            "driver_name",
            "vehicle_type",
            "city",
            "rating",
            "status"
        ).dropDuplicates(["driver_id"])
    )