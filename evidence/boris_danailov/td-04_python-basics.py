from module import filter_prices, get_first_close, get_last_close, load_instruments, load_prices


def display_market_summary(asset, prices, show_currency=True):
    unit = " " + asset["currency"] if show_currency else ""
    print(asset["ticker"], "-", asset["name"])
    print("Observations:", len(prices))
    print(f"First close: {get_first_close(prices):.2f}{unit}")
    print(f"Last close: {get_last_close(prices):.2f}{unit}")


instruments = load_instruments()
prices = load_prices()

aapl = instruments["instrument"]
sp500 = instruments["benchmark"]

aapl_prices = filter_prices(prices, aapl["ticker"])
sp500_prices = filter_prices(prices, sp500["ticker"])

print("=== MarketPulse - TD04 ===")
print()
print("Instrument")
display_market_summary(aapl, aapl_prices)
print()
print("Benchmark")
display_market_summary(sp500, sp500_prices, show_currency=False)
