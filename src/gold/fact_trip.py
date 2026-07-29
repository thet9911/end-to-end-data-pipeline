from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def build_fact_trip(
    bookings: DataFrame,
    payments: DataFrame,
    reviews: DataFrame,
) -> DataFrame:

    b = bookings.alias("b")
    p = payments.alias("p")
    r = reviews.alias("r")

    fact = (
        b.join(
            p,
            b["booking_id"] == p["booking_id"],
            "left"
        )
        .join(
            r,
            b["booking_id"] == r["booking_id"],
            "left"
        )
    )

    return fact.select(
        col("b.booking_id").alias("booking_id"),
        col("b.customer_id").alias("customer_id"),
        col("b.driver_id").alias("driver_id"),

        col("b.booking_time").alias("booking_time"),
        col("b.pickup_location"),
        col("b.dropoff_location"),

        col("b.distance_km"),
        col("b.duration_min"),
        col("b.fare"),
        col("b.trip_status"),

        # Booking payment method
        col("b.payment_method").alias("booking_payment_method"),

        col("b.surge_multiplier"),

        # Payment table
        col("p.payment_id"),
        col("p.payment_method").alias("actual_payment_method"),
        col("p.payment_status"),
        col("p.amount"),
        col("p.payment_time"),

        # Review table
        col("r.rating"),
        col("r.review_text"),
        col("r.review_date"),

        # Metadata
        col("b.ingestion_timestamp")
    )