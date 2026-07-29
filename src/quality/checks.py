from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def check_nulls(df: DataFrame, column: str) -> int:
    return df.filter(col(column).isNull()).count()


def check_duplicates(df: DataFrame, column: str) -> int:
    return (
        df.groupBy(column)
        .count()
        .filter(col("count") > 1)
        .count()
    )


def check_row_count(df: DataFrame) -> int:
    return df.count()


def check_negative_values(df: DataFrame, column: str) -> int:
    return df.filter(col(column) < 0).count()