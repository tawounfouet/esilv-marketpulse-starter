from math import isclose

from src.analytics import (
    index_by_date,
    align_series,
    calculate_period_return,
    calculate_base_100,
    calculate_relative_performance,
)

# Fake price series
aapl = [
    {"date": "2026-11-01", "ticker": "AAPL", "close": 100},
    {"date": "2026-11-02", "ticker": "AAPL", "close": 110},
    {"date": "2026-11-03", "ticker": "AAPL", "close": 120},
]

sp500 = [
    {"date": "2026-11-01", "ticker": "SP500", "close": 200},
    {"date": "2026-11-02", "ticker": "SP500", "close": 205},
    {"date": "2026-11-03", "ticker": "SP500", "close": 210},
]

# Test 1: Period return
ra = calculate_period_return(aapl)
rb = calculate_period_return(sp500)

assert isclose(ra, 20.0)
assert isclose(rb, 5.0)

print("Test 1: Period return OK")

# Test 2: Base 100
base_100 = calculate_base_100(aapl)

assert isclose(base_100[0]["value"], 100.0)
assert isclose(base_100[1]["value"], 110.0)
assert isclose(base_100[2]["value"], 120.0)

print("Test 2: Base 100 OK")

# Test 3: Relative performance
relative = calculate_relative_performance(ra, rb)

assert isclose(relative, 15.0)

print("Test 3: Relative performance OK")

# Test 4: Alignment with missing dates
sp500_missing = [sp500[0], sp500[2]]

aligned_aapl, aligned_sp500 = align_series(
    aapl, sp500_missing
)

assert len(aligned_aapl) == 2
assert len(aligned_sp500) == 2

assert [r["date"] for r in aligned_aapl] == [
    "2026-11-01",
    "2026-11-03",
]

assert [r["date"] for r in aligned_aapl] == [
    r["date"] for r in aligned_sp500
]

print("Test 4: Series alignment OK")

# Test 5: Empty series
try:
    calculate_period_return([])
except ValueError:
    print("Test 5: Empty series OK")
else:
    raise AssertionError("Expected ValueError")

# Test 6: Date indexing
indexed = index_by_date(aapl)

assert indexed["2026-11-01"]["close"] == 100

print("Test 6: Date indexing OK")

print("All analytics tests passed!")
