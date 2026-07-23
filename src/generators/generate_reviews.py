import pandas as pd
import random
import json
from pathlib import Path
from faker import Faker

#Configuration

fake = Faker()

RAW_PATH = Path("data/raw")

bookings = pd.read_csv(RAW_PATH / "bookings.csv")

#Generate Reviews

reviews = []

for _, booking in bookings.iterrows():

    if booking["trip_status"] != "Completed":
        continue

    if random.random() > 0.35:
        continue

    review = {

        "booking_id": booking["booking_id"],

        "rating": random.randint(1,5),

        "review_text": fake.sentence(),

        "review_date": str(
            fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        )

    }

    reviews.append(review)

with open(RAW_PATH / "reviews.json","w") as f:
    json.dump(reviews,f,indent=4)

print(f"Generated {len(reviews)} reviews")