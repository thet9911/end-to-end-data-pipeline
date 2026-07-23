import argparse
from pathlib import Path

from pyspark.sql.functions import current_timestamp

from src.config.config import RAW_PATH, BRONZE_PATH
from src.utils.spark_session import create_spark
from src.utils.logger import logger
from src.validation.schema_validator import validate_columns
from src.validation.rules import CUSTOMER_COLUMNS


def load_data(spark, dataset, file_type):
    """
    Load raw data from CSV or JSON.
    """

    path = RAW_PATH / f"{dataset}.{file_type}"

    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")

    if file_type == "csv":
        df = (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(str(path))
        )

    elif file_type == "json":
        # Your JSON files are formatted as a JSON array,
        # so Spark needs multiLine=True.
        df = (
            spark.read
            .option("multiLine", True)
            .json(str(path))
        )

    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    return df


def main():

    parser = argparse.ArgumentParser(
        description="Bronze Layer Pipeline"
    )

    parser.add_argument(
        "dataset",
        help="Dataset name (customers, drivers, bookings, payments, reviews)"
    )

    parser.add_argument(
        "file_type",
        choices=["csv", "json"],
        help="Input file type"
    )

    args = parser.parse_args()

    spark = create_spark(f"Bronze - {args.dataset}")

    logger.info(f"Reading dataset: {args.dataset}")

    df = load_data(
        spark,
        args.dataset,
        args.file_type
    )

    # Validate customer schema
    if args.dataset == "customers":
        validate_columns(df, CUSTOMER_COLUMNS)

    # Show schema for debugging
    logger.info("Schema:")
    df.printSchema()

    logger.info(f"Rows loaded: {df.count()}")

    # Add ingestion timestamp
    df = df.withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )

    output_path = BRONZE_PATH / args.dataset

    logger.info(f"Writing Bronze data to {output_path}")

    (
        df.write
        .mode("overwrite")
        .parquet(str(output_path))
    )

    logger.info("Bronze layer created successfully.")

    spark.stop()


if __name__ == "__main__":
    main()