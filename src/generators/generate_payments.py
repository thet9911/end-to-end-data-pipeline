import pandas as pd
import random
import json
from pathlib import Path
from faker import Faker

#Configuration

fake = Faker()

RAW_PATH = Path("data/raw")

bookings = pd.read_csv(RAW_PATH / "bookings.csv")

payments = []

payment_methods = [
    "Visa",
    "Mastercard",
    "PayNow",
    "Cash"
]

payment_status = [
    "Success",
    "Failed",
    "Refunded"
]

# Generate Payments

payment_id = 1

for _, booking in bookings.iterrows():

    if booking["trip_status"] != "Completed":
        continue

    payment = {

        "payment_id": f"P{payment_id:08d}",

        "booking_id": booking["booking_id"],

        "payment_method": random.choice(payment_methods),

        "amount": float(booking["fare"]),

        "payment_status": random.choices(
            payment_status,
            weights=[96,3,1],
            k=1
        )[0],

        "payment_time": str(
            fake.date_time_between(
                start_date="-2y",
                end_date="now"
            )
        )

    }

    payments.append(payment)

    payment_id += 1

with open(RAW_PATH / "payments.json", "w") as f:
    json.dump(payments, f, indent=4)

print(f"Generated {len(payments)} payments")