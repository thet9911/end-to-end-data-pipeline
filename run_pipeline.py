import subprocess
import sys


def run(cmd):
    print("=" * 70)
    print(f"Running: {' '.join(cmd)}")
    print("=" * 70)

    result = subprocess.run(cmd)

    if result.returncode != 0:
        print(f"\n❌ Failed: {' '.join(cmd)}")
        sys.exit(result.returncode)


def main():

    # -------------------------
    # Generate Data
    # -------------------------
    generators = [
        "generate_customers",
        "generate_drivers",
        "generate_bookings",
        "generate_payments",
        "generate_reviews",
    ]

    for g in generators:
        run(["python", "-m", f"src.generators.{g}"])

    # -------------------------
    # Bronze
    # -------------------------
    bronze = [
        ("customers", "csv"),
        ("drivers", "csv"),
        ("bookings", "csv"),
        ("payments", "json"),
        ("reviews", "json"),
    ]

    for dataset, filetype in bronze:
        run([
            "python",
            "-m",
            "src.pipelines.bronze_pipeline",
            dataset,
            filetype,
        ])

    # -------------------------
    # Silver
    # -------------------------
    silver = [
        "customers",
        "drivers",
        "bookings",
        "payments",
        "reviews",
    ]

    for dataset in silver:
        run([
            "python",
            "-m",
            "src.pipelines.silver_pipeline",
            dataset,
        ])

    # -------------------------
    # Gold
    # -------------------------
    run([
        "python",
        "-m",
        "src.pipelines.gold_pipeline",
    ])

    print("\n🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    main()