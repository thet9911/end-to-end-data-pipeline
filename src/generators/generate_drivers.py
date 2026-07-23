from faker import Faker
import pandas as pd
import random
from pathlib import Path

# Configuration

fake = Faker()

NUM_DRIVERS = 10000

OUTPUT_PATH = Path("data/raw/drivers.csv")

VEHICLE_TYPES = [
    "Sedan",
    "SUV",
    "Hatchback",
    "MPV",
    "Premium",
    "Electric"
]

CITIES = [
    "Singapore",
    "Jurong",
    "Woodlands",
    "Tampines",
    "Yishun",
    "Punggol",
    "Bedok",
    "Toa Payoh",
    "Bishan",
    "Ang Mo Kio"
]

STATUS = [
    "Active",
    "Inactive",
    "Suspended"
]

# Generate Drivers

drivers = []

for i in range(1, NUM_DRIVERS + 1):

    driver = {
        "driver_id": f"D{i:05d}",
        "driver_name": fake.name(),
        "vehicle_type": random.choice(VEHICLE_TYPES),
        "city": random.choice(CITIES),
        "join_date": fake.date_between(
            start_date="-8y",
            end_date="today"
        ),
        "rating": round(random.uniform(3.5, 5.0), 2),
        "status": random.choices(
            STATUS,
            weights=[90, 8, 2],
            k=1
        )[0]
    }

    drivers.append(driver)

# Save CSV

df = pd.DataFrame(drivers)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {len(df)} drivers")
print(df.head())
