print("hello world")
print("TD 04- Python Basics")

import json
import csv
from pathlib import Path

DATA_DIR = Path("/workspaces/esilv-marketpulse-g06-t03/data/sample")


def load_instruments(filepath):
    """Charge les métadonnées JSON."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        return json.load(file)


def load_prices(filepath):
    """Charge les observations du CSV."""
    with open(filepath, mode="r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    """Sélectionne les observations du ticker et les trie par date."""
    selected = [row for row in prices if row["ticker"] == ticker]
    return sorted(selected, key=lambda row: row["date"])


def display_market_summary(asset, observations, show_currency=True):
    """Affiche les cours et le rendement sur la période."""
    if not observations:
        print(f"Aucune donnée pour {asset['ticker']}")
        return

    first = observations[0]
    last = observations[-1]

    start_price = float(first["close"])
    end_price = float(last["close"])

    currency = f" {asset['currency']}" if show_currency else ""

    print(f"Ticker   : {asset['ticker']}")
    print(f"Nom      : {asset['name']}")
    print(f"Période  : {first['date']} -> {last['date']}")
    print(f"Premier  : {start_price:.2f}{currency}")
    print(f"Dernier  : {end_price:.2f}{currency}")

    if start_price == 0:
        print("Rendement : impossible à calculer (cours initial nul)")
    else:
        total_return = (end_price / start_price - 1) * 100
        print(f"Rendement : {total_return:+.2f}%")


def run_td04_market_snapshot():
    """Charge les données et affiche la synthèse MarketPulse."""
    instruments = load_instruments(DATA_DIR / "instruments.json")
    prices = load_prices(DATA_DIR / "prices.csv")

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print("=== MarketPulse ===")
    print(f"\nTotal records loaded : {len(prices)}")

    print("\nMarket configuration")
    print("Period   : 1 month")
    print("Interval : Daily")

    print("\nInstrument")
    display_market_summary(
        instrument, instrument_prices, show_currency=True
    )

    print("\nBenchmark")
    display_market_summary(
        benchmark, benchmark_prices, show_currency=False
    )


if __name__ == "__main__":
    run_td04_market_snapshot()