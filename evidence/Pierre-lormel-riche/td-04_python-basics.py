from module import load_instruments
from module import load_prices
from module import filter_prices
from module import get_first_close
from module import get_last_close


def display_market_summary(asset, prices, show_currency=True):
    """Display the same summary for the instrument or the benchmark."""
    currency = f" {asset['currency']}" if show_currency else ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
    print(f"First close  : {get_first_close(prices):.2f}{currency}")
    print(f"Last close   : {get_last_close(prices):.2f}{currency}")


instruments = load_instruments()
prices = load_prices()

instrument = instruments["instrument"]
benchmark = instruments["benchmark"]

instrument_prices = filter_prices(prices, instrument["ticker"])
benchmark_prices = filter_prices(prices, benchmark["ticker"])

print("=== TD-04 Python basics ===")
print()
print("Instrument")
display_market_summary(instrument, instrument_prices)
print()
print("Benchmark")
display_market_summary(benchmark, benchmark_prices, show_currency=False)
