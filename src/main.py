from pathlib import Path
import csv
import json
from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.bloomberg_provider import fetch_bloomberg_prices

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

PROVIDER_LABEL = "Bloomberg stage"
ACCESS_MODE = "APPROVED_SAMPLE"

INSTRUMENT = "AAPL"
BENCHMARK = "SP500"
LOOKBACK = "1mo"
INTERVAL = "1d"


def build_market_snapshot(
    instrument=INSTRUMENT,
    benchmark=BENCHMARK,
    lookback=LOOKBACK,
    interval=INTERVAL,
):
    """Shared application result, consumed by the terminal (TD10) and Dash (TD11)."""
    # 1. Provider -> canonical rows
    instrument_prices = fetch_bloomberg_prices(instrument)   # ⚠️ check signature
    benchmark_prices = fetch_bloomberg_prices(benchmark)

    # 2. Shared alignment (unchanged)
    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    # 3. Shared analytics (unchanged, no formula here)
    instrument_return = calculate_period_return(aligned_instrument)   # ⚠️
    benchmark_return = calculate_period_return(aligned_benchmark)
    relative_performance = calculate_relative_performance(            # ⚠️
        instrument_return,
        benchmark_return,
    )

    return {
        "provider": PROVIDER_LABEL,
        "access_mode": ACCESS_MODE,
        "lookback": lookback,
        "interval": interval,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": relative_performance,
        "instrument_base_100": calculate_base_100(aligned_instrument),  # ⚠️
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }

def main():

    # instruments = load_instruments()
    # prices = load_prices()

    # instrument = instruments["instrument"]
    # benchmark = instruments["benchmark"]

    # instrument_prices = filter_prices(prices, instrument["ticker"])
    # benchmark_prices = filter_prices(prices, benchmark["ticker"])

    # instrument_latest = instrument_prices[-1]
    # benchmark_latest = benchmark_prices[-1]

    # print("=== MarketPulse ===")
    # print("Data source: Local CSV")  
    # print()
    # print("Instrument")
    # print(f"{instrument['ticker']} - {instrument['name']}")
    # print(f"Lastest closing price: {instrument_latest['close']} {instrument['currency']}")
    # print()
    # print("Benchmark")
    # print(f"{benchmark['ticker']} - {benchmark['name']}")
    # print(f"Last level: {benchmark_latest['close']}")
    # print(f"Benchmark: {benchmark['market']}")
    # print()
    
    # print(f"Period: {LOOKBACK_LABEL}")
    # print(f"Interval: {INTERVAL_LABEL}")
    # print()
    # print("Observations")
    # print(f"{instrument['ticker']}: {len(instrument_prices)}")
    # print(f"{benchmark['ticker']}: {len(benchmark_prices)}")


    snapshot = build_market_snapshot()

    print("MarketPulse")
    print("=" * 40)
    print()
    print("Provider")
    print(snapshot["provider"])
    print()
    print("Access mode")
    print(snapshot["access_mode"])
    print()
    print("Instrument : AAPL - Apple Inc.")
    print("Benchmark  : S&P 500")
    print("Period     : 1 month")
    print("Interval   : Daily")
    print()
    print(f"Instrument return    : {snapshot['instrument_return']:+.2f}%")
    print(f"Benchmark return     : {snapshot['benchmark_return']:+.2f}%")
    print(f"Relative performance : {snapshot['relative_performance']:+.2f} pts")
    print()
    print(f"Base-100 points      : {len(snapshot['instrument_base_100'])}")
    print()
    print("Note: APPROVED_SAMPLE fixture - live Bloomberg connectivity not demonstrated.")




if __name__ == "__main__":
    main() 
