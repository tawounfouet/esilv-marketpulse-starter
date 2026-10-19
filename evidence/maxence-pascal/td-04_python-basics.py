from pathlib import Path
import csv
import json

# Robust project root resolution
CURRENT_DIR = Path.cwd()
PROJECT_ROOT = CURRENT_DIR if (CURRENT_DIR / "data").exists() else CURRENT_DIR.parent
DATA_DIR = PROJECT_ROOT / "data" / "sample"

print(f"Project root resolved to : {PROJECT_ROOT}")
print(f"Data directory           : {DATA_DIR}")
print(f"instruments.json exists  : {(DATA_DIR / 'instruments.json').exists()}")
print(f"prices.csv exists        : {(DATA_DIR / 'prices.csv').exists()}")

# 1.1 Dictionaries: Key-Value mappings (O(1) access)
sample_instrument = {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "currency": "USD",
    "is_active": True
}

print("Dictionary keys   :", list(sample_instrument.keys()))
print("Access by key     :", sample_instrument["name"])
print("Safe get with def :", sample_instrument.get("exchange", "UNKNOWN"))

# 1.2 Lists of Dictionaries: Tabular data representation
mock_rows = [
    {"date": "2026-09-01", "ticker": "AAPL", "close": "250.00"},
    {"date": "2026-09-01", "ticker": "SP500", "close": "6600.00"},
    {"date": "2026-09-02", "ticker": "AAPL", "close": "251.30"},
    {"date": "2026-09-02", "ticker": "SP500", "close": "6612.00"},
]

# Filtering via imperative loop (Beginner pattern):
aapl_rows_loop = []
for row in mock_rows:
    if row["ticker"] == "AAPL":
        aapl_rows_loop.append(row)

# Filtering via List Comprehension (Pythonic pattern):
aapl_rows_comp = [row for row in mock_rows if row["ticker"] == "AAPL"]

print(f"Loop filter count : {len(aapl_rows_loop)}")
print(f"Comp filter count : {len(aapl_rows_comp)}")
assert aapl_rows_loop == aapl_rows_comp, "Both patterns must yield identical results!"

def load_instruments(filepath=DATA_DIR / "instruments.json"):
    """Load and parse JSON metadata file into a Python dictionary."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)

instruments = load_instruments()
print("Type of loaded JSON:", type(instruments))
print("Top-level keys     :", list(instruments.keys()))

# Extracting and inspecting the two business objects
instrument = instruments["instrument"]
benchmark = instruments["benchmark"]

print("--- Primary Instrument ---")
print(f"Ticker   : {instrument['ticker']}")
print(f"Name     : {instrument['name']}")
print(f"Currency : {instrument['currency']}")
print(f"Market   : {instrument['market']}")

print("\n--- Benchmark Index ---")
print(f"Ticker   : {benchmark['ticker']}")
print(f"Name     : {benchmark['name']}")
print(f"Currency : {benchmark['currency']}")
print(f"Market   : {benchmark['market']}")

def load_prices(filepath=DATA_DIR / "prices.csv"):
    """Load market observations from CSV into a list of dictionaries."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

prices = load_prices()
print(f"Total records loaded : {len(prices)}")
print(f"Type of prices       : {type(prices)}")
print(f"Type of each row     : {type(prices[0])}")
print("\nFirst observation sample:")
for key, val in prices[0].items():
    print(f"  {key:8s} -> {val} (type: {type(val).__name__})")

raw_close = prices[0]["close"]

# 1. String concatenation trap:
print(f"String concatenation : raw_close + '10' = {raw_close + '10'}  <-- INCORRECT!")

# 2. Explicit conversion to float:
converted_close = float(raw_close)
print(f"Numerical addition   : converted_close + 10 = {converted_close + 10.0:.2f}  <-- CORRECT!")

def filter_prices(prices, ticker):
    """Filter observation dictionaries matching a specific ticker."""
    return [row for row in prices if row["ticker"] == ticker]

instrument_prices = filter_prices(prices, instrument["ticker"])
benchmark_prices = filter_prices(prices, benchmark["ticker"])

print(f"Instrument observations ({instrument['ticker']}) : {len(instrument_prices)}")
print(f"Benchmark observations  ({benchmark['ticker']})  : {len(benchmark_prices)}")

# TD02 CORE Requirement: 21 observations for each series
assert len(instrument_prices) == 21, "Expected 21 observations for AAPL"
assert len(benchmark_prices) == 21, "Expected 21 observations for SP500"

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

def display_market_summary(asset, prices, show_currency=True):
    """
    Display a standardized market summary for any instrument or benchmark.
    
    Args:
        asset (dict): Metadata dictionary (containing 'ticker', 'name', 'currency').
        prices (list): Filtered observation dictionaries.
        show_currency (bool): Whether to append the currency code to prices.
    """
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)
    currency_suffix = f" {asset.get('currency', '')}" if show_currency else ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
    print(f"First close  : {first_close:.2f}{currency_suffix}")
    print(f"Last close   : {last_close:.2f}{currency_suffix}")

# Test display
print("=== Test Display ===\n")
display_market_summary(instrument, instrument_prices, show_currency=True)
print()
display_market_summary(benchmark, benchmark_prices, show_currency=False)

def run_td02_market_snapshot():
    """Simulate the complete main() workflow for TD02."""
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print("Period   : 1 month")
    print("Interval : Daily")
    print()
    print("Instrument")
    display_market_summary(instrument, instrument_prices, show_currency=True)
    print()
    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)

# Execute full simulation
run_td02_market_snapshot()

