CUSTOMER_COLUMNS = [
    "customer_id",
    "first_name",
    "last_name",
    "gender",
    "age",
    "email",
    "phone",
    "city",
    "signup_date",
    "membership",
    "is_active"
]

BOOKING_COLUMNS = [
    "booking_id",
    "customer_id",
    "driver_id",
    "booking_time",
    "pickup_location",
    "dropoff_location",
    "distance_km",
    "duration_min",
    "fare",
    "trip_status",
    "payment_method",
    "surge_multiplier"
]

DRIVER_COLUMNS = [
    "driver_id",
    "driver_name",
    "vehicle_type",
    "city",
    "join_date",
    "rating",
    "status"
]

PAYMENT_COLUMNS = [
    "payment_id",
    "booking_id",
    "payment_method",
    "amount",
    "payment_status",
    "payment_time"
]

REVIEW_COLUMNS = [
    "booking_id",
    "rating",
    "review_text",
    "review_date"
]