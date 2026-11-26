"""MarketPulse analytics: pure functions for comparison (TD07)."""


def index_by_date(prices):
    result = {}

    for price in prices:
        result[price["date"]] = price

    return result


def align_series(instrument_prices, benchmark_prices):

    instrument_by_date = index_by_date(instrument_prices)
    benchmark_by_date = index_by_date(benchmark_prices)

    common_dates = sorted(
        set(instrument_by_date) & set(benchmark_by_date)
    )

    aligned_instrument = []
    aligned_benchmark = []

    for date in common_dates:
        aligned_instrument.append(instrument_by_date[date])
        aligned_benchmark.append(benchmark_by_date[date])

    return aligned_instrument, aligned_benchmark


def calculate_period_return(prices):

    if not prices:
        raise ValueError("Price series cannot be empty")

    first_close = float(prices[0]["close"])
    last_close = float(prices[-1]["close"])

    if first_close == 0:
        raise ValueError("First close cannot be zero")

    period_return = ((last_close / first_close) - 1.0) * 100.0

    return period_return

def calculate_base_100(prices):

    if not prices:
        raise ValueError("Price series cannot be empty")

    first_close = float(prices[0]["close"])

    if first_close == 0:
        raise ValueError("First close cannot be zero")

    base_100 = []

    for price in prices:

        current_close = float(price["close"])

        value = (current_close / first_close) * 100.0

        base_100.append({
            "date": price["date"],
            "ticker": price["ticker"],
            "value": value
        })

    return base_100

def calculate_relative_performance(instrument_return, benchmark_return):

    relative_performance = instrument_return - benchmark_return

    return relative_performance