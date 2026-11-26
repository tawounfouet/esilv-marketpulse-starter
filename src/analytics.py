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

import pytest


def obs(ticker, *rows):
    return [{"date": d, "ticker": ticker, "close": c} for d, c in rows]


ASSET = obs("AAPL", ("2026-01-01", 100.0), ("2026-01-02", 110.0), ("2026-01-03", 120.0))
BENCH = obs("SPY", ("2026-01-02", 210.0), ("2026-01-01", 200.0), ("2026-01-04", 220.0))


def test_index_by_date():
    assert index_by_date(ASSET) == {r["date"]: r for r in ASSET}
    assert index_by_date([]) == {}


def test_index_by_date_doublon_garde_le_dernier():
    rows = obs("X", ("2026-01-01", 1.0), ("2026-01-01", 2.0))
    assert index_by_date(rows) == {"2026-01-01": rows[1]}


def test_align_series():
    a, b = align_series(ASSET, BENCH)
    assert a == [ASSET[0], ASSET[1]]
    assert b == [BENCH[1], BENCH[0]]


def test_align_series_sans_date_commune():
    assert align_series([], []) == ([], [])
    assert align_series(ASSET[2:], BENCH[2:]) == ([], [])


@pytest.mark.parametrize("closes, attendu", [
    ([100.0, 120.0], 20.0),
    ([100.0, 80.0], -20.0),
    ([100.0, 150.0, 100.0], 0.0),
    ([100.0], 0.0),
    (["100", "110"], 10.0),
    ([100.0, 0.0], -100.0),
])
def test_period_return(closes, attendu):
    prices = [{"close": c} for c in closes]
    assert calculate_period_return(prices) == pytest.approx(attendu)


def test_base_100():
    avant = [r.copy() for r in ASSET]
    result = calculate_base_100(ASSET)
    assert [r["date"] for r in result] == [r["date"] for r in ASSET]
    assert [r["ticker"] for r in result] == ["AAPL"] * 3
    assert [r["value"] for r in result] == pytest.approx([100.0, 110.0, 120.0])
    assert ASSET == avant


@pytest.mark.parametrize("func", [calculate_period_return, calculate_base_100])
def test_serie_vide(func):
    with pytest.raises(ValueError, match="empty series"):
        func([])


@pytest.mark.parametrize("func", [calculate_period_return, calculate_base_100])
def test_prix_initial_zero(func):
    with pytest.raises(ZeroDivisionError, match="Initial price"):
        func(obs("X", ("2026-01-01", 0.0), ("2026-01-02", 10.0)))


@pytest.mark.parametrize("actif, indice, attendu", [
    (10.0, 5.0, 5.0),
    (5.0, 10.0, -5.0),
    (7.0, 7.0, 0.0),
    (-2.0, -8.0, 6.0),
])
def test_relative_performance(actif, indice, attendu):
    assert calculate_relative_performance(actif, indice) == pytest.approx(attendu)


if __name__ == "__main__":
    raise SystemExit(pytest.main(["-v", __file__]))