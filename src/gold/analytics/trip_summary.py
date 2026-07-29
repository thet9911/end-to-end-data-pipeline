from pyspark.sql import DataFrame
from pyspark.sql.functions import count


def build_trip_summary(df: DataFrame) -> DataFrame:

    return (
        df.groupBy("trip_status")
        .agg(
            count("*").alias("total_trips")
        )
        .orderBy("total_trips", ascending=False)
    )