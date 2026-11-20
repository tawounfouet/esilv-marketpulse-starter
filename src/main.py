from pathlib import Path
import csv
import json
try:
    from src.analytics import (
        align_series,
        calculate_period_return,
        calculate_base_100,
        calculate_relative_performance,
    )
except ModuleNotFoundError as error:
    if error.name != "src":
        raise
    from analytics import (
        align_series,
        calculate_period_return,
        calculate_base_100,
        calculate_relative_performance,
    )

DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


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
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]

    print("=== MarketPulse ===")
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
    print("Observations")
    print(f"{instrument['ticker']}: {len(instrument_prices)}")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)}")
     
        # TD07 - Calculations
    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices
    )

    # Calculate the period return of each series
    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    # Compare instrument and benchmark performance
    relative_performance = calculate_relative_performance(
        instrument_return,
        benchmark_return
    )

    # Normalize both series to base 100
    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    # TD07 - Display
    print()
    print("=== Comparison (aligned) ===")

    print(f"Aligned sessions: {len(aligned_instrument)}")

    print(
        f"{instrument['ticker']} period return: "
        f"{instrument_return:+.2f}%"
    )

    print(
        f"{benchmark['ticker']} period return: "
        f"{benchmark_return:+.2f}%"
    )

    print(
        f"Relative performance: "
        f"{relative_performance:+.2f} percentage points"
    )

    print()
    print("=== Base 100 ===")

    print(
        f"{instrument['ticker']}: "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )

    print(
        f"{benchmark['ticker']}: "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()
