from faker import Faker
import pandas as pd
import random
from pathlib import Path

# Configuration

fake = Faker()

NUM_BOOKINGS = 100000

RAW_PATH = Path("data/raw")

CUSTOMERS_FILE = RAW_PATH / "customers.csv"
DRIVERS_FILE = RAW_PATH / "drivers.csv"

OUTPUT_FILE = RAW_PATH / "bookings.csv"

TRIP_STATUS = [
    "Completed",
    "Cancelled",
    "No Show"
]

PAYMENT_METHOD = [
    "Cash",
    "Visa",
    "Mastercard",
    "PayNow"
]

LOCATIONS = [
    "Jurong",
    "Woodlands",
    "Tampines",
    "Yishun",
    "Punggol",
    "Bedok",
    "Bishan",
    "Orchard",
    "Changi",
    "Toa Payoh"
]

# Read Existing Data

customers = pd.read_csv(CUSTOMERS_FILE)
drivers = pd.read_csv(DRIVERS_FILE)

customer_ids = customers["customer_id"].tolist()
driver_ids = drivers["driver_id"].tolist()

# Generate Bookings

bookings = []

for i in range(1, NUM_BOOKINGS + 1):

    status = random.choices(
        TRIP_STATUS,
        weights=[90, 8, 2],
        k=1
    )[0]

    distance = round(random.uniform(2, 30), 2)

    duration = int(distance * random.uniform(2.5, 4))

    surge = random.choice([1.0, 1.2, 1.5, 2.0])

    fare = round((3 + distance * 1.2) * surge, 2)

    if status != "Completed":
        fare = 0

    booking = {

        "booking_id": f"B{i:08d}",

        "customer_id": random.choice(customer_ids),

        "driver_id": random.choice(driver_ids),

        "booking_time": fake.date_time_between(
            start_date="-2y",
            end_date="now"
        ),

        "pickup_location": random.choice(LOCATIONS),

        "dropoff_location": random.choice(LOCATIONS),

        "distance_km": distance,

        "duration_min": duration,

        "fare": fare,

        "trip_status": status,

        "payment_method": random.choice(PAYMENT_METHOD),

        "surge_multiplier": surge

    }

    bookings.append(booking)

# Save CSV

df = pd.DataFrame(bookings)

df.to_csv(OUTPUT_FILE, index=False)

print(df.head())

print(f"\nGenerated {len(df)} bookings")