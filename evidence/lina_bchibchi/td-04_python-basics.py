from modules import load_prices
from modules import load_instruments
from modules import filter_prices
from modules import display_market_summary

def run_td02_market_snapshot():
    instruments = load_instruments()
    prices = load_prices()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]
    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])
    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print("Period : 1 month")
    print("Interval : Daily")
    print()
    print("Instrument")
    display_market_summary(instrument, instrument_prices, show_currency=True)
    print()
    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)
#Execute full simulation

run_td02_market_snapshot()