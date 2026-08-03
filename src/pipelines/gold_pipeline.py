from pathlib import Path

from src.utils.spark_session import create_spark
from src.utils.logger import logger
from src.config.config import SILVER_PATH, GOLD_PATH

from src.gold.dim_customer import build_dim_customer
from src.gold.dim_driver import build_dim_driver
from src.gold.dim_payment import build_dim_payment
from src.gold.fact_trip import build_fact_trip

from src.gold.analytics.revenue_daily import build_revenue_daily
from src.gold.analytics.customer_summary import build_customer_summary
from src.gold.analytics.driver_summary import build_driver_summary
from src.gold.analytics.payment_summary import build_payment_summary
from src.gold.analytics.trip_summary import build_trip_summary

from src.quality.report import generate_report

def write_table(df, path: Path):
    (
        df.write
        .mode("overwrite")
        .parquet(str(path))
    )


def main():

    spark = create_spark("Gold Pipeline")

    logger.info("Loading Silver tables...")

    customers = spark.read.parquet(str(SILVER_PATH / "customers"))
    drivers = spark.read.parquet(str(SILVER_PATH / "drivers"))
    bookings = spark.read.parquet(str(SILVER_PATH / "bookings"))
    payments = spark.read.parquet(str(SILVER_PATH / "payments"))
    reviews = spark.read.parquet(str(SILVER_PATH / "reviews"))

    logger.info("Building dimension tables...")

    dim_customer = build_dim_customer(customers)
    dim_driver = build_dim_driver(drivers)
    dim_payment = build_dim_payment(payments)

    logger.info("Building fact table...")

    fact_trip = build_fact_trip(
        bookings,
        payments,
        reviews
    )
    
    logger.info("Building analytics tables...")
    generate_report(fact_trip)

    revenue_daily = build_revenue_daily(fact_trip)
    customer_summary = build_customer_summary(fact_trip)
    driver_summary = build_driver_summary(fact_trip)
    payment_summary = build_payment_summary(fact_trip)
    trip_summary = build_trip_summary(fact_trip)

    logger.info("Writing Gold tables...")

    write_table(dim_customer, GOLD_PATH / "dim_customer")
    write_table(dim_driver, GOLD_PATH / "dim_driver")
    write_table(dim_payment, GOLD_PATH / "dim_payment")
    write_table(fact_trip, GOLD_PATH / "fact_trip")

    write_table(revenue_daily, GOLD_PATH / "revenue_daily")
    write_table(customer_summary, GOLD_PATH / "customer_summary")
    write_table(driver_summary, GOLD_PATH / "driver_summary")
    write_table(payment_summary, GOLD_PATH / "payment_summary")
    write_table(trip_summary, GOLD_PATH / "trip_summary")

    logger.info("Gold Pipeline Complete!")

    spark.stop()


if __name__ == "__main__":
    main()