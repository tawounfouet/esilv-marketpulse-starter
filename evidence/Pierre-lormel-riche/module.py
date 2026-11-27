from pathlib import Path
import csv
import json


# This file lives in evidence/Pierre-lormel-riche/, the project root is two levels up.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "sample"


def load_instruments(filepath=DATA_DIR / "instruments.json"):
    """Load the JSON metadata file into a Python dictionary."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)


def load_prices(filepath=DATA_DIR / "prices.csv"):
    """Load the CSV observations into a list of dictionaries."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    """Keep only the observations of one ticker."""
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    """Return the first close of a series as a float."""
    return float(prices[0]["close"])


def get_last_close(prices):
    """Return the last close of a series as a float."""
    return float(prices[-1]["close"])
