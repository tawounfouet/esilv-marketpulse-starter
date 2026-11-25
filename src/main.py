from pathlib import Path
import csv
import json
from analytics import (
    align_prices,
    period_return,
    base_100,
    relative_performance
)

from providers.yahoo_provider import load_yahoo_prices


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"

def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def main():
    instruments = load_instruments()


    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = load_yahoo_prices(instrument["ticker"])
    benchmark_prices = load_yahoo_prices(benchmark["ticker"])

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]

    print("=== MarketPulse ===")
    print("Provider: Yahoo Finance")
    print()
    print("Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Last price: {instrument_latest['close']} {instrument['currency']}")
    print()
    print("Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Last level: {benchmark_latest['close']}")
    print()
    print(f"Period: {LOOKBACK_LABEL}")
    print(f"Interval: {INTERVAL_LABEL}")
    print()
    print("\nObservations")
    print(f"\n{instrument['ticker']}: {len(instrument_prices)}")
    print(f"First date: {get_first_date(instrument_prices)}")
    print(f"Last date: {get_last_date(instrument_prices)}")
    print(f"\n{benchmark['ticker']}: {len(benchmark_prices)}")
    print(f"First date: {get_first_date(benchmark_prices)}")
    print(f"Last date: {get_last_date(benchmark_prices)}")
    dates, i, b = align_prices(instrument_prices, benchmark_prices)

    print("\n=== Performance Comparison ===")
    print(f"Common observations: {len(dates)}")
    print(f"Common period: {dates[0]} to {dates[-1]}")
    print(f"Instrument return: {period_return(i):.2%}")
    print(f"Benchmark return: {period_return(b):.2%}")
    print(f"Relative performance: {relative_performance(i, b)*100:.2f} pp")
    print(f"Instrument base 100: {base_100(i)[-1]:.2f}")
    print(f"Benchmark base 100: {base_100(b)[-1]:.2f}")


if __name__ == "__main__":
    main()
