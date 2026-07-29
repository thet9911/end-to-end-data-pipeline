from src.quality.checks import (
    check_duplicates,
    check_negative_values,
    check_nulls,
    check_row_count,
)


def generate_report(df):

    print("=" * 50)
    print("DATA QUALITY REPORT")
    print("=" * 50)

    print("Rows:", check_row_count(df))

    if "booking_id" in df.columns:
        print("Duplicate booking_id:", check_duplicates(df, "booking_id"))

    if "amount" in df.columns:
        print("Negative amount:", check_negative_values(df, "amount"))

    print("=" * 50)