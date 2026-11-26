import yfinance as yf

# Mapping between MarketPulse canonical tickers and Yahoo Finance symbols
YAHOO_SYMBOL_MAPPING = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(
    symbol,
    canonical_ticker,
    period="1mo",
    interval="1d",
):
    """
    Retrieve historical market prices from Yahoo Finance and normalize to canonical format.
    
    Args:
        symbol (str): Yahoo Finance symbol (e.g., 'AAPL' or '^GSPC').
        canonical_ticker (str): Internal canonical ticker (e.g., 'AAPL' or 'SP500').
        period (str): Historical lookback window (default: '1mo').
        interval (str): Price frequency (default: '1d').
        
    Returns:
        list: Canonical observation dictionaries dict(date, ticker, open, high, low, close, volume).
    """
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
            "volume": int(row["Volume"]),
        })

    return rows

def test_fetch_yahoo_prices():

    for canonical_ticker, symbol in YAHOO_SYMBOL_MAPPING.items():

        rows = fetch_yahoo_prices(
            symbol,
            canonical_ticker,
            period="1mo",
            interval="1d"
        )

        # Vérification que des données ont été récupérées
        assert len(rows) > 0, "No data returned"

        for row in rows:

            # Vérification du ticker
            assert row["ticker"] == canonical_ticker

            # Vérification des types
            assert isinstance(row["date"], str)
            assert isinstance(row["open"], float)
            assert isinstance(row["high"], float)
            assert isinstance(row["low"], float)
            assert isinstance(row["close"], float)
            assert isinstance(row["volume"], int)

            # Vérification de la cohérence des prix
            assert row["high"] >= row["low"]
            assert row["high"] >= row["open"]
            assert row["high"] >= row["close"]
            assert row["low"] <= row["open"]
            assert row["low"] <= row["close"]
            assert row["volume"] >= 0

        print(f"Test passed for {canonical_ticker}")
        print(f"Number of observations: {len(rows)}")
        print(f"First observation: {rows[0]}")
        print()


if __name__ == "__main__":
    test_fetch_yahoo_prices()