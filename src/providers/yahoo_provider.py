import yfinance as yf


def load_yahoo_prices(ticker, period="1mo", interval="1d"):
    symbol = "^GSPC" if ticker == "SP500" else ticker

    data = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False
    )

    data = data.dropna(subset=["Close"])

    if data.empty:
        raise ValueError(f"No data for {ticker}")

    prices = []

    for date, row in data.iterrows():
        prices.append({
            "date": date.strftime("%Y-%m-%d"),
            "ticker": ticker,
            "close": float(row["Close"])
        })

    return prices
