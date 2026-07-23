import argparse

from src.utils.spark_session import create_spark
from src.utils.logger import logger
from src.config.config import BRONZE_PATH, SILVER_PATH

from src.transformations.customer import clean_customer


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("dataset")

    args = parser.parse_args()

    spark = create_spark("Silver Pipeline")

    bronze_path = BRONZE_PATH / args.dataset

    logger.info(f"Reading {bronze_path}")

    df = spark.read.parquet(str(bronze_path))

    if args.dataset == "customers":
        df = clean_customer(df)

    output = SILVER_PATH / args.dataset

    (
        df.write
        .mode("overwrite")
        .parquet(str(output))
    )

    logger.info(f"Silver written -> {output}")

    spark.stop()


if __name__ == "__main__":
    main()