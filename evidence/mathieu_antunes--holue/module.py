from pathlib import Path
import csv
import json



CURRENT_DIR = Path("./mathieu_antunes--holue")
PROJECT_ROOT = CURRENT_DIR if (CURRENT_DIR / "data").exists() else CURRENT_DIR.parent
DATA_DIR = PROJECT_ROOT / "data" / "sample"


def load_instruments(filepath=DATA_DIR / "instruments.json"):
    """Load and parse JSON metadata file into a Python dictionary."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)

instruments = load_instruments()
print("Type of loaded JSON:", type(instruments))
print("Top-level keys     :", list(instruments.keys()))

instrument = instruments["instrument"]
benchmark = instruments["benchmark"]


def load_prices(filepath=DATA_DIR / "prices.csv"):
    """Load market observations from CSV into a list of dictionaries."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

prices = load_prices()




def filter_prices(prices, ticker):
    """Filter observation dictionaries matching a specific ticker."""
    return [row for row in prices if row["ticker"] == ticker]

instrument_prices = filter_prices(prices, instrument["ticker"])
benchmark_prices = filter_prices(prices, benchmark["ticker"])

print(f"Instrument observations ({instrument['ticker']}) : {len(instrument_prices)}")
print(f"Benchmark observations  ({benchmark['ticker']})  : {len(benchmark_prices)}")


def get_first_close(prices):
    """
    Return the initial close price of a price series as a float.
    """
    if not prices:
        return 0.0
    return float(prices[0]["close"])


def get_last_close(prices):
    """
    Return the final close price of a price series as a float.
    """
    if not prices:
        return 0.0
    return float(prices[-1]["close"])

# Test on AAPL
aapl_first = get_first_close(instrument_prices)
aapl_last = get_last_close(instrument_prices)
print(f"AAPL  -> First Close: {aapl_first:.2f} | Last Close: {aapl_last:.2f}")

# Test on SP500
sp_first = get_first_close(benchmark_prices)
sp_last = get_last_close(benchmark_prices)
print(f"SP500 -> First Close: {sp_first:.2f} | Last Close: {sp_last:.2f}")

# Verification against TD02 expected values
assert aapl_first == 250.00, f"Expected 250.00, got {aapl_first}"
assert aapl_last == 266.20, f"Expected 266.20, got {aapl_last}"
assert sp_first == 6600.00, f"Expected 6600.00, got {sp_first}"
assert sp_last == 6742.00, f"Expected 6742.00, got {sp_last}"

