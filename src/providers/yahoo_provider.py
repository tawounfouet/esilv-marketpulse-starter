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
