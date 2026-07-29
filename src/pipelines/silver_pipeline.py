import argparse

from src.utils.spark_session import create_spark
from src.utils.logger import logger
from src.config.config import BRONZE_PATH, SILVER_PATH

from src.transformations.customer import clean_customer
from src.transformations.booking import clean_booking
from src.transformations.driver import clean_driver
from src.transformations.payment import clean_payment
from src.transformations.review import clean_review

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
    elif args.dataset == "bookings":
        df = clean_booking(df)
    elif args.dataset == "drivers":
        df = clean_driver(df)
    elif args.dataset == "payments":
        df = clean_payment(df)
    elif args.dataset == "reviews":
        df = clean_review(df)
    else:
        logger.warning(f"No cleaning function defined for dataset: {args.dataset}")

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