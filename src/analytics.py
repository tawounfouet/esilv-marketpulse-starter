def index_by_date(prices):
    """
    Index a list of canonical observation dictionaries by date ('YYYY-MM-DD').
    
    Args:
        prices (list): List of canonical observation dictionaries.
        
    Returns:
        dict: Mapping of {date: observation_dict}.
    """
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    """
    Align two price series on the sorted intersection of their common dates.
    
    Args:
        instrument_prices (list): Observations of the primary asset.
        benchmark_prices (list): Observations of the benchmark index.
        
    Returns:
        tuple: (aligned_instrument_prices, aligned_benchmark_prices)
    """
    instrument_by_date = index_by_date(instrument_prices)
    benchmark_by_date = index_by_date(benchmark_prices)

    common_dates = sorted(set(instrument_by_date.keys()) & set(benchmark_by_date.keys()))

    aligned_instrument = [instrument_by_date[date] for date in common_dates]
    aligned_benchmark = [benchmark_by_date[date] for date in common_dates]

    return aligned_instrument, aligned_benchmark


def calculate_period_return(prices):
    """
    Calculate total arithmetic return over the observed period:
    Formula: ((last_close / first_close) - 1.0) * 100.0
    
    Args:
        prices (list): Chronologically sorted list of observations.
        
    Returns:
        float: Percentage return (e.g., 6.48 for +6.48%).
    """
    if not prices:
        raise ValueError("Cannot compute return on an empty series.")
    
    first_close = float(prices[0]["close"])
    last_close = float(prices[-1]["close"])

    if first_close == 0.0:
        raise ZeroDivisionError("Initial price cannot be zero.")

    return ((last_close / first_close) - 1.0) * 100.0


def calculate_base_100(prices):
    """
    Normalize a price series to Base 100 (where day zero equals 100.0).
    Formula: (current_close / first_close) * 100.0
    
    Args:
        prices (list): List of canonical observations.
        
    Returns:
        list: List of dictionaries [{'date': ..., 'ticker': ..., 'value': float}, ...].
    """
    if not prices:
        raise ValueError("Cannot calculate Base 100 on an empty series.")

    first_close = float(prices[0]["close"])
    if first_close == 0.0:
        raise ZeroDivisionError("Initial price cannot be zero.")

    result = []
    for row in prices:
        result.append({
            "date": row["date"],
            "ticker": row["ticker"],
            "value": (float(row["close"]) / first_close) * 100.0,
        })
    return result


def calculate_relative_performance(instrument_return, benchmark_return):
    """
    Calculate relative outperformance or underperformance in percentage points.
    Formula: instrument_return - benchmark_return
    
    Args:
        instrument_return (float): Asset return in %.
        benchmark_return (float): Benchmark return in %.
        
    Returns:
        float: Difference in percentage points (pts).
    """
    return instrument_return - benchmark_return

