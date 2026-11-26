# TD07 - Data Normalization + Comparison

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"All market-data sources must feed a common comparison model."
```

## Context

The collaborative Git workflow is now established.

TD07 introduces the first reusable analytics layer in MarketPulse.

The problem is simple:

```text
AAPL price
about 250 USD

S&P 500 level
about 6600 points
```

Raw levels are on different scales.

To answer:

> Is the selected instrument outperforming or underperforming its benchmark over the same period?

MarketPulse needs:

```text
canonical numeric rows
+
common dates
+
period return
+
base 100
+
relative performance
```

The comparison logic must also be reusable by later providers.

That is why TD07 introduces:

```text
src/analytics.py
```

## Learning objectives

At the end of TD07, you should be able to:

- distinguish local CSV acquisition from reusable analytics;
- convert CSV numeric fields to useful Python types;
- preserve the canonical MarketPulse row structure;
- align instrument and benchmark observations by common date;
- calculate a period return;
- calculate a base-100 series;
- calculate relative performance;
- use percentage points correctly;
- place provider-neutral comparison logic in `src/analytics.py`;
- reuse the established Git workflow without relearning it.

## CORE definition of done

TD07 is complete when the team can confirm:

```text
[ ] src/analytics.py exists
[ ] analytics.py contains no provider-specific identifier
[ ] CSV close values are numeric before analytics
[ ] instrument and benchmark are aligned on common dates
[ ] calculate_period_return() works
[ ] calculate_base_100() starts at 100
[ ] calculate_relative_performance() uses instrument minus benchmark
[ ] src/main.py reuses analytics.py
[ ] python src/main.py works
[ ] no return percentage is hard-coded
[ ] the TD07 change follows the established branch / PR workflow
```

Daily returns are OPTIONAL.

They are not required to complete TD07 or the final CORE dashboard.

## Prerequisites

Before starting:

```text
[ ] TD01-TD06 completed
[ ] team main is synchronized
[ ] python src/main.py works
[ ] instrument and benchmark are loaded
[ ] branch / PR / review workflow is understood
```

Update local main:

```bash
git switch main
git pull
git status
python src/main.py
```

Start from a clean working tree.

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for review, troubleshooting and optional analytics.

| Time | Activity |
|---|---|
| 00-08 min | Comparison problem and canonical rows |
| 08-20 min | Normalize local CSV numeric fields |
| 20-35 min | Create analytics.py and align common dates |
| 35-48 min | Period return + relative performance |
| 48-62 min | Base-100 series |
| 62-72 min | Integrate analytics into main.py |
| 72-80 min | Validate + standard Git handoff |
| 80-90 min | Buffer / review / OPTIONAL |

## Repository evolution

TD07 changes the CORE structure from:

```text
src/
└── main.py
```

to:

```text
src/
├── main.py
└── analytics.py
```

Responsibility split:

```text
src/main.py
=
local CSV orchestration
+
terminal output

src/analytics.py
=
provider-neutral comparison logic
```

The analytics module must not contain identifiers such as:

```text
AAPL
SP500
^GSPC
AAPL US Equity
SPX Index
```

Those belong outside reusable analytics.

# CORE

# Part 1 - Understand the comparison problem

Raw price levels answer:

```text
"What is the value?"
```

Performance answers:

```text
"How much did the value change?"
```

The comparison contract is:

```text
same lookback
+
same interval
+
common observation dates
```

For the common course path:

```text
Lookback : 1 month
Interval : Daily
```

Do not compare different periods or different frequencies.

# Part 2 - Create the TD07 feature branch

Use the workflow learned in TD05 and TD06.

Start from current team `main`:

```bash
git switch main
git pull
git status
```

Create:

```bash
git switch -c feature/market-comparison
```

TD07 does not reteach Git theory.

Use `CONTRIBUTING.md` when you need the standard workflow reminder.

# Part 3 - Normalize local CSV rows

The CSV reader returns text.

A raw row is conceptually:

```python
{
    "date": "2026-09-01",
    "ticker": "AAPL",
    "open": "249.20",
    "high": "251.50",
    "low": "248.00",
    "close": "250.00",
    "volume": "38000000",
}
```

The canonical MarketPulse row fields remain:

```text
date
ticker
open
high
low
close
volume
```

For analytics, numeric fields must be numeric.

A simple local CSV normalization helper may be kept in `src/main.py`:

```python
def normalize_price_row(row):
    return {
        "date": row["date"],
        "ticker": row["ticker"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "volume": int(row["volume"]),
    }
```

Then:

```python
normalized_prices = [
    normalize_price_row(row)
    for row in prices
]
```

Why keep this outside `analytics.py`?

Because `analytics.py` should receive comparison-ready canonical rows.

Later providers will be responsible for producing that same row shape.

## Validate types

Temporarily inspect:

```python
print(type(normalized_prices[0]["close"]))
print(type(normalized_prices[0]["volume"]))
```

Expected:

```text
float
int
```

Remove temporary debug output afterward.

# Part 4 - Create src/analytics.py

Create:

```text
src/analytics.py
```

TD07 CORE introduces these reusable functions:

```python
index_by_date(...)
align_series(...)
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

Keep each function small.

# Part 5 - Index rows by date

In `src/analytics.py`:

```python
def index_by_date(prices):
    return {
        row["date"]: row
        for row in prices
    }
```

This converts:

```text
list of rows
```

into:

```text
date
  |
  v
row
```

for simple alignment.

# Part 6 - Align instrument and benchmark

Implement:

```python
def align_series(instrument_prices, benchmark_prices):
    instrument_by_date = index_by_date(instrument_prices)
    benchmark_by_date = index_by_date(benchmark_prices)

    common_dates = sorted(
        set(instrument_by_date)
        & set(benchmark_by_date)
    )

    aligned_instrument = [
        instrument_by_date[date]
        for date in common_dates
    ]

    aligned_benchmark = [
        benchmark_by_date[date]
        for date in common_dates
    ]

    return aligned_instrument, aligned_benchmark
```

Use it after filtering:

```python
aligned_instrument, aligned_benchmark = align_series(
    instrument_prices,
    benchmark_prices,
)
```

With the starter sample, both aligned series should contain:

```text
21 observations
```

with:

```text
first common date : 2026-09-01
last common date  : 2026-09-30
```

The important invariant is:

```text
len(aligned_instrument)
=
len(aligned_benchmark)
```

and corresponding rows refer to the same dates.

# Part 7 - Calculate period return

Use the aligned rows.

Formula:

```text
(last close / first close - 1) * 100
```

Implement in `src/analytics.py`:

```python
def calculate_period_return(prices):
    first_close = prices[0]["close"]
    last_close = prices[-1]["close"]

    return (last_close / first_close - 1) * 100
```

Then:

```python
instrument_return = calculate_period_return(
    aligned_instrument
)

benchmark_return = calculate_period_return(
    aligned_benchmark
)
```

Interpretation:

```text
positive
=
ending close above starting close

negative
=
ending close below starting close
```

# Part 8 - Calculate relative performance

Relative performance is:

```text
instrument period return
-
benchmark period return
```

Implement:

```python
def calculate_relative_performance(
    instrument_return,
    benchmark_return,
):
    return instrument_return - benchmark_return
```

Example:

```text
Instrument return : +6.48%
Benchmark return  : +2.15%

Relative performance
=
+4.33 percentage points
```

Use:

```text
percentage points
```

for this simple difference between percentage returns.

Do not reverse the subtraction.

# Part 9 - Build base 100

Base 100 puts differently scaled series on a common starting point.

Formula:

```text
current close / first close * 100
```

Implement:

```python
def calculate_base_100(prices):
    first_close = prices[0]["close"]
    result = []

    for row in prices:
        result.append({
            "date": row["date"],
            "ticker": row["ticker"],
            "value": row["close"] / first_close * 100,
        })

    return result
```

For both series:

```text
first base-100 value
=
100.00
```

The last value should be consistent with the period return.

Conceptually:

```text
period return = +6.48%

final base 100
about
106.48
```

Do not overwrite the original close values.

# Part 10 - Integrate analytics into main.py

Import the reusable functions:

```python
from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
```

Keep the flow understandable:

```text
load local CSV / JSON
        |
        v
normalize CSV rows
        |
        v
filter instrument + benchmark
        |
        v
align_series()
        |
        v
calculate_period_return()
calculate_base_100()
calculate_relative_performance()
        |
        v
display terminal summary
```

Target output shape:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Period return : 6.48%

Benchmark
SP500 - S&P 500
Period return : 2.15%

Relative performance
AAPL vs SP500 : +4.33 percentage points

Base 100
AAPL  : 100.00 -> 106.48
SP500 : 100.00 -> 102.15
```

Use calculated values.

Do not hard-code percentages.

# Part 11 - CORE validation

Run:

```bash
python src/main.py
```

Then verify:

```text
[ ] aligned series are not empty
[ ] aligned series have the same number of rows
[ ] corresponding rows use common dates
[ ] close values are numeric
[ ] period returns are calculated from aligned rows
[ ] relative performance = instrument - benchmark
[ ] first instrument base-100 value = 100
[ ] first benchmark base-100 value = 100
[ ] analytics.py contains no provider-specific identifier
[ ] main.py orchestrates instead of duplicating analytics
```

# Part 12 - Standard Git handoff

The Git workflow is already known.

Use the process defined in `CONTRIBUTING.md`:

```text
feature branch
+
inspect diff
+
commit
+
push
+
Pull Request
+
review
+
merge
```

Suggested commit:

```text
feat: add reusable market comparison analytics
```

Suggested PR title:

```text
feat: add reusable market comparison analytics
```

The PR should include at least:

```text
src/analytics.py
src/main.py
```

Before TD08 begins, the reviewed TD07 analytics must be available from team `main`.

This is a dependency handoff, not another Git lesson.

# Checkpoint relation

Checkpoint B is performed after TD08.

TD07 prepares the comparison behaviour later visible in:

```text
04_instrument_benchmark.png
```

The canonical evidence contract is:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

Do not submit Checkpoint B yet.

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied.

## Optional 1 - Daily returns

Daily return compares a close with the previous close:

```text
(current close / previous close - 1) * 100
```

Possible function:

```python
def calculate_daily_returns(prices):
    returns = []

    for index in range(1, len(prices)):
        previous = prices[index - 1]
        current = prices[index]

        value = (
            current["close"] / previous["close"] - 1
        ) * 100

        returns.append({
            "date": current["date"],
            "ticker": current["ticker"],
            "return": value,
        })

    return returns
```

For 21 price observations:

```text
20 daily returns
```

This function is optional and later dashboard completion does not depend on it.

## Optional 2 - Best and worst daily return

Only if Optional 1 was completed:

```text
best daily return
worst daily return
```

Keep this outside required MarketPulse analytics.

## Optional 3 - Aligned comparison rows

Build a derived structure such as:

```python
{
    "date": "...",
    "instrument_close": ...,
    "benchmark_close": ...,
}
```

for common dates.

## Optional 4 - Small comparison table

Display a few base-100 rows:

```text
date        AAPL      SP500
2026-...   100.00    100.00
...
```

Do not turn the terminal output into a full dashboard.

# ADVANCED

No `READY_TO_TEACH` advanced activity is attached directly to TD07 at this time.

Daily returns and the other extensions above remain OPTIONAL because they are lightweight continuations of the same analytics model.

Complete the CORE and OPTIONAL work only.

# TROUBLESHOOTING

## TypeError during calculations

Inspect:

```python
print(type(row["close"]))
```

If `close` is still text, local CSV normalization was not applied.

## No common dates

Inspect:

```python
print(sorted(index_by_date(instrument_prices)))
print(sorted(index_by_date(benchmark_prices)))
```

Do not calculate performance on unrelated windows.

## Different aligned lengths

The two lists returned by `align_series()` must be built from the same `common_dates`.

## Base 100 does not start at 100

Verify:

```text
first close / first close * 100
=
100
```

## Relative-performance sign is wrong

Use:

```text
instrument return
-
benchmark return
```

## Import error for analytics

Verify:

```text
src/main.py
src/analytics.py
```

and run from the repository root:

```bash
python src/main.py
```

# Final readiness check

Each student should be able to explain:

```text
[ ] canonical row
[ ] numeric normalization
[ ] common-date alignment
[ ] period return
[ ] base 100
[ ] relative performance
[ ] percentage points
[ ] why analytics.py is provider-neutral
[ ] why provider identifiers do not belong in analytics.py
```

The team should confirm:

```text
[ ] src/analytics.py exists
[ ] TD07 analytics are merged before TD08
[ ] python src/main.py works
[ ] daily returns were not required
```

# What comes next?

TD08 introduces Yahoo Finance.

The dependency is now explicit:

```text
TD07
canonical numeric rows
+
align_series()
+
period return
+
base 100
+
relative performance
        |
        v
TD08
Yahoo provider
        |
        v
same analytics.py
```

The next test is architectural:

> Can Yahoo Finance feed the same comparison functions without changing the analytics layer?
