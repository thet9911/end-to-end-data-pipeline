from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from src.utils.logger import logger


def drop_nulls(df: DataFrame, columns: list, dataset: str) -> DataFrame:
    before = df.count()
    for c in columns:
        df = df.filter(col(c).isNotNull())
    after = df.count()
    if before != after:
        logger.warning(f"[{dataset}] dropped {before - after} rows with nulls in {columns}")
    return df


def check_range(df: DataFrame, column: str, low, high, dataset: str) -> DataFrame:
    before = df.count()
    df = df.filter(col(column).between(low, high))
    after = df.count()
    if before != after:
        logger.warning(f"[{dataset}] dropped {before - after} rows where {column} not in [{low}, {high}]")
    return df


def check_positive(df: DataFrame, column: str, dataset: str) -> DataFrame:
    before = df.count()
    df = df.filter(col(column) > 0)
    after = df.count()
    if before != after:
        logger.warning(f"[{dataset}] dropped {before - after} rows where {column} <= 0")
    return df