from pathlib import Path
import csv
import json


# This file lives in evidence/boris_danailov/, the project root is two levels up.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "sample"


def load_instruments(filepath=DATA_DIR / "instruments.json"):
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)


def load_prices(filepath=DATA_DIR / "prices.csv"):
    with open(filepath, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    return float(prices[0]["close"])


def get_last_close(prices):
    return float(prices[-1]["close"])
