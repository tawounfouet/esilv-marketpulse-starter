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

def load_instruments(filepath="/workspaces/esilv-marketpulse-g06-t02/evidence/Alexandra-NdoloDifom/data/sample/instruments.json"):
    """Load and parse JSON metadata file into a Python dictionary."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)

instruments = load_instruments()
print("Type of loaded JSON:", type(instruments))
print("Top-level keys     :", list(instruments.keys()))

def load_prices(filepath="/workspaces/esilv-marketpulse-g06-t02/evidence/Alexandra-NdoloDifom/data/sample/prices.csv"):
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

def filter_prices(prices, ticker):
    """Filter observation dictionaries matching a specific ticker."""
    return [row for row in prices if row["ticker"] == ticker]

instrument_prices = filter_prices(prices, instruments['ticker'])
benchmark_prices = filter_prices(prices, benchmark['ticker'])

print(f"Instrument observations ({instrument['ticker']}) : {len(instrument_prices)}")
print(f"Benchmark observations  ({benchmark['ticker']})  : {len(benchmark_prices)}")

# TD02 CORE Requirement: 21 observations for each series
assert len(instrument_prices) == 21, "Expected 21 observations for AAPL"
assert len(benchmark_prices) == 21, "Expected 21 observations for SP500"

def run_td02_market_snapshot():
    """Simulate the complete main() workflow for TD02."""
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument['ticker'])
    benchmark_prices = filter_prices(prices, benchmark['ticker'])

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