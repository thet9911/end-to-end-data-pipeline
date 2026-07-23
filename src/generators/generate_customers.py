from faker import Faker
import pandas as pd
import random
from pathlib import Path


# Configuration


fake = Faker()

NUM_CUSTOMERS = 50000

OUTPUT_PATH = Path("data/raw/customers.csv")

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

MEMBERSHIP = [
    "Standard",
    "Silver",
    "Gold",
    "Platinum"
]


# Generate Customers


customers = []

for i in range(1, NUM_CUSTOMERS + 1):

    customer = {
        "customer_id": f"C{i:06d}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 70),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "city": random.choice(CITIES),
        "signup_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        ),
        "membership": random.choice(MEMBERSHIP),
        "is_active": random.choice([True, True, True, False])
    }

    customers.append(customer)


# Save CSV


df = pd.DataFrame(customers)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {len(df)} customers")
print(df.head())