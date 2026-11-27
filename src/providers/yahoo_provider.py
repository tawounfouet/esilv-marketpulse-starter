"""MarketPulse Yahoo Finance provider (TD08).

Retrieves remote daily market data with yfinance and normalizes it
to the MarketPulse canonical observation contract:

    {"date": "YYYY-MM-DD", "ticker": str, "open": float, "high": float,
     "low": float, "close": float, "volume": int}
"""

import math

import yfinance as yf


PROVIDER_LABEL = "Yahoo Finance (remote)"

# MarketPulse canonical ticker -> Yahoo Finance symbol
YAHOO_SYMBOL_MAPPING = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def get_yahoo_symbol(canonical_ticker):
    if canonical_ticker not in YAHOO_SYMBOL_MAPPING:
        raise KeyError(f"No Yahoo Finance symbol mapped for {canonical_ticker}.")
    return YAHOO_SYMBOL_MAPPING[canonical_ticker]


def to_volume(value):
    """Volume must be an int; indices may return 0 or a missing value."""
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return 0
    return int(value)


def fetch_yahoo_prices(symbol, canonical_ticker, period="1mo", interval="1d"):
    """Retrieve Yahoo Finance history and return canonical observation rows."""
    history = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
    )

    if history.empty:
        raise ValueError(
            f"No Yahoo Finance data returned for symbol {symbol} "
            f"(period={period}, interval={interval})."
        )

    rows = []
    for timestamp, row in history.iterrows():
        rows.append({
            "date": timestamp.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": to_volume(row["Volume"]),
        })

    return rows


def fetch_canonical_prices(canonical_ticker, period="1mo", interval="1d"):
    """Fetch one MarketPulse ticker from Yahoo using the symbol mapping."""
    symbol = get_yahoo_symbol(canonical_ticker)
    return fetch_yahoo_prices(symbol, canonical_ticker, period, interval)


def print_remote_summary(title, canonical_ticker, prices):
    print(title)
    print(f"{canonical_ticker} (Yahoo symbol: {get_yahoo_symbol(canonical_ticker)})")
    print(f"Observations : {len(prices)}")
    print(f"First date   : {prices[0]['date']}")
    print(f"Last date    : {prices[-1]['date']}")
    print(f"First close  : {prices[0]['close']:.2f}")
    print(f"Last close   : {prices[-1]['close']:.2f}")


def main():
    period = "1mo"
    interval = "1d"

    instrument_prices = fetch_canonical_prices("AAPL", period, interval)
    benchmark_prices = fetch_canonical_prices("SP500", period, interval)

    print("=== MarketPulse - Yahoo Finance stage ===")
    print(f"Data source: {PROVIDER_LABEL}")
    print("Lookback   : 1 month")
    print("Interval   : Daily")
    print()
    print_remote_summary("Instrument", "AAPL", instrument_prices)
    print()
    print_remote_summary("Benchmark", "SP500", benchmark_prices)
    print()
    print("Canonical row sample:")
    print(instrument_prices[0])


if __name__ == "__main__":
    main()
