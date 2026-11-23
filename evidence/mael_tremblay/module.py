from pathlib import Path
import csv
import json


# This file lives in evidence/mael_tremblay/, the project root is two levels up.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "sample"


def load_instruments(filepath=DATA_DIR / "instruments.json"):
    """Load and parse the JSON metadata file into a Python dictionary."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)


def load_prices(filepath=DATA_DIR / "prices.csv"):
    """Load market observations from CSV into a list of dictionaries."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    """Keep only the observations that match a specific ticker."""
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    """Return the first close price of a price series as a float."""
    return float(prices[0]["close"])


def get_last_close(prices):
    """Return the last close price of a price series as a float."""
    return float(prices[-1]["close"])
