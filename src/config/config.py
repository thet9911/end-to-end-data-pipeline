from pathlib import Path

# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "data"

RAW_PATH = DATA_PATH / "raw"

BRONZE_PATH = DATA_PATH / "bronze"

SILVER_PATH = DATA_PATH / "silver"

GOLD_PATH = DATA_PATH / "gold"