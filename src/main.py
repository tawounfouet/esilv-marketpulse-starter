"""Run the MarketPulse comparison with Yahoo Finance data."""

import json
from pathlib import Path

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.yahoo_provider import (
    PROVIDER_LABEL,
    fetch_canonical_prices,
    get_yahoo_symbol,
)


DATA_DIR = Path("data/sample")
LOOKBACK = "1mo"
INTERVAL = "1d"
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    """Load the canonical instrument and benchmark descriptions."""
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def main():
    instruments = load_instruments()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    # Both series use the same remote period and interval.
    instrument_prices = fetch_canonical_prices(
        instrument["ticker"], LOOKBACK, INTERVAL
    )
    benchmark_prices = fetch_canonical_prices(
        benchmark["ticker"], LOOKBACK, INTERVAL
    )

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices, benchmark_prices
    )
    if not aligned_instrument:
        raise ValueError("No common observation dates for instrument and benchmark.")

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)
    relative_performance = calculate_relative_performance(
        instrument_return, benchmark_return
    )
    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    print("=== MarketPulse ===")
    print(f"Provider  : {PROVIDER_LABEL} via yfinance")
    print(f"Lookback  : {LOOKBACK_LABEL}")
    print(f"Interval  : {INTERVAL_LABEL}")
    print()

    print("Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Yahoo symbol : {get_yahoo_symbol(instrument['ticker'])}")
    print(f"Observations : {len(instrument_prices)}")
    print(f"Date range   : {instrument_prices[0]['date']} to {instrument_prices[-1]['date']}")
    print(f"Last close   : {instrument_prices[-1]['close']:.2f} {instrument['currency']}")
    print()

    print("Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Yahoo symbol : {get_yahoo_symbol(benchmark['ticker'])}")
    print(f"Observations : {len(benchmark_prices)}")
    print(f"Date range   : {benchmark_prices[0]['date']} to {benchmark_prices[-1]['date']}")
    print(f"Last close   : {benchmark_prices[-1]['close']:.2f} {benchmark['currency']}")
    print()

    print("Comparison on common dates")
    print(f"Aligned sessions : {len(aligned_instrument)}")
    print(f"Common date range: {aligned_instrument[0]['date']} to {aligned_instrument[-1]['date']}")
    print(f"{instrument['ticker']} period return : {instrument_return:+.2f}%")
    print(f"{benchmark['ticker']} period return : {benchmark_return:+.2f}%")
    print(
        f"Relative performance : {relative_performance:+.2f} "
        "percentage points"
    )
    print()

    print("Base 100")
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
