# TD08 - Yahoo Finance

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Traders need more recent market data than local files."
```

## Context

TD07 introduced provider-neutral analytics in:

```text
src/analytics.py
```

TD08 changes the data source while preserving those analytics.

The target architecture is:

```text
Yahoo Finance
      |
      v
Yahoo provider
      |
      v
canonical MarketPulse rows
      |
      v
TD07 analytics.py
      |
      v
terminal comparison
```

The remote data is accessed through:

```text
yfinance
```

Important:

```text
yfinance is a community Python library.
It is not the official Yahoo Finance API.
```

TD08 is not a pandas course and not a provider-framework design exercise.

The goal is to build one simple adapter that produces the same canonical rows already consumed by MarketPulse analytics.

## Learning objectives

At the end of TD08, you should be able to:

- install and record one direct dependency;
- retrieve one remote Yahoo Finance series;
- distinguish canonical ticker from provider-specific symbol;
- create `src/providers/yahoo_provider.py`;
- normalize Yahoo output into the MarketPulse canonical row contract;
- preserve `SP500` as the benchmark ticker while mapping Yahoo to `^GSPC`;
- retrieve instrument and benchmark for a 1-month daily window;
- align the two remote series using TD07 logic;
- reuse TD07 analytics unchanged;
- run MarketPulse with remote data;
- prepare Checkpoint B evidence honestly.

## CORE definition of done

TD08 is complete when the team can confirm:

```text
[ ] yfinance is installed in the working environment
[ ] yfinance is recorded in requirements.txt
[ ] src/providers/__init__.py exists
[ ] src/providers/yahoo_provider.py exists
[ ] Yahoo AAPL data can be retrieved
[ ] provider output is normalized to canonical rows
[ ] canonical ticker AAPL remains AAPL
[ ] canonical ticker SP500 remains SP500
[ ] Yahoo-specific benchmark symbol is ^GSPC
[ ] instrument and benchmark use period=1mo
[ ] instrument and benchmark use interval=1d
[ ] TD07 align_series() is reused
[ ] TD07 analytics functions are reused without provider-specific changes
[ ] python src/main.py works
[ ] the TD08 change follows the standard branch / PR / review workflow
[ ] Checkpoint B can be captured after successful remote retrieval
```

The following are not required for CORE completion:

```text
invalid-symbol experiment
alternate market pair
generic provider selector
YAML provider parsing
advanced retry logic
extra provider-error drills
```

## Prerequisites

Before starting:

```text
[ ] TD01-TD07 completed
[ ] reviewed TD07 analytics are merged to team main
[ ] src/analytics.py exists
[ ] python src/main.py works with local CSV
[ ] branch / PR / review workflow is understood
[ ] internet access is available
```

Update local main:

```bash
git switch main
git pull
git status
python src/main.py
```

Start from a clean working tree.

## Instructor preparation

Before the session, the instructor should have:

```text
[ ] known-good yfinance retrieval snippet
[ ] expected canonical row example
[ ] AAPL -> AAPL mapping confirmed
[ ] SP500 -> ^GSPC mapping confirmed
[ ] temporary-outage fallback explanation ready
```

Reference:

```text
docs/09_YAHOO_FINANCE_INSTRUCTOR_REFERENCE.md
```

The reference is a teaching fallback, not a substitute for successful remote evidence.

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for review, remote-provider variation and Checkpoint B capture.

| Time | Activity |
|---|---|
| 00-08 min | Provider boundary + symbol mapping |
| 08-18 min | Install and record yfinance |
| 18-30 min | Retrieve AAPL and inspect returned structure |
| 30-48 min | Create Yahoo provider + normalize rows |
| 48-60 min | Retrieve AAPL + SP500 benchmark |
| 60-70 min | Reuse TD07 alignment + analytics |
| 70-78 min | Validate MarketPulse + standard Git handoff |
| 78-80 min | CORE definition of done |
| 80-90 min | Review / Checkpoint B / troubleshooting |

## Repository evolution

TD08 extends the CORE structure to:

```text
src/
├── main.py
├── analytics.py
└── providers/
    ├── __init__.py
    └── yahoo_provider.py
```

Responsibility split:

```text
src/providers/yahoo_provider.py
=
Yahoo acquisition
+
Yahoo symbol handling
+
Yahoo -> canonical row normalization

src/analytics.py
=
provider-neutral alignment
+
period return
+
base 100
+
relative performance

src/main.py
=
orchestration
+
terminal output
```

# CORE

# Part 1 - Understand canonical ticker vs provider symbol

The business identifiers stay stable:

```text
Instrument canonical ticker : AAPL
Benchmark canonical ticker  : SP500
```

Yahoo-specific symbols are:

```text
AAPL  -> AAPL
SP500 -> ^GSPC
```

The critical distinction is:

```text
SP500
=
MarketPulse canonical ticker

^GSPC
=
Yahoo provider symbol
```

Do not propagate `^GSPC` into `analytics.py`.

Provider identifiers belong at the provider boundary.

# Part 2 - Create the TD08 feature branch

Use the standard workflow already learned.

```bash
git switch main
git pull
git status
git switch -c feature/yahoo-provider
```

TD08 does not reteach Git theory.

Use `CONTRIBUTING.md` when you need the workflow reminder.

# Part 3 - Install and record yfinance

Check:

```bash
python -m pip show yfinance
```

If needed:

```bash
python -m pip install yfinance
```

Then add the direct dependency to:

```text
requirements.txt
```

Required entry:

```text
yfinance
```

Do not manually list every transitive dependency.

A teammate should later be able to install project dependencies with:

```bash
python -m pip install -r requirements.txt
```

# Part 4 - Retrieve AAPL first

Before writing the provider module, make one minimal retrieval.

```python
import yfinance as yf

history = yf.Ticker("AAPL").history(
    period="1mo",
    interval="1d",
    auto_adjust=False,
)

print(history.head())
```

You only need to identify:

```text
date index
Open
High
Low
Close
Volume
```

The returned structure is table-like and backed by pandas.

Do not turn TD08 into a pandas tutorial.

The goal is only to convert the rows into the existing MarketPulse contract.

# Part 5 - Create the Yahoo provider

Create:

```text
src/providers/__init__.py
src/providers/yahoo_provider.py
```

Use one provider function.

Suggested contract:

```python
fetch_yahoo_prices(
    symbol,
    canonical_ticker,
    period="1mo",
    interval="1d",
)
```

A teaching implementation is:

```python
import yfinance as yf


def fetch_yahoo_prices(
    symbol,
    canonical_ticker,
    period="1mo",
    interval="1d",
):
    history = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
    )

    if history.empty:
        raise ValueError(
            f"No Yahoo Finance data returned for {symbol}"
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
```

The exact internal syntax may evolve with the library.

The required contract is the returned canonical row structure.

# Part 6 - Validate one canonical Yahoo row

Retrieve:

```python
instrument_prices = fetch_yahoo_prices(
    symbol="AAPL",
    canonical_ticker="AAPL",
)
```

Inspect:

```python
print(instrument_prices[0])
```

Expected shape:

```python
{
    "date": "YYYY-MM-DD",
    "ticker": "AAPL",
    "open": 0.0,
    "high": 0.0,
    "low": 0.0,
    "close": 0.0,
    "volume": 0,
}
```

The numeric values above describe types and shape only.

Do not hard-code them.

Required types:

```text
date    -> str
ticker  -> str
open    -> float
high    -> float
low     -> float
close   -> float
volume  -> int
```

# Part 7 - Add the Yahoo symbol mapping

A minimal mapping is enough:

```python
YAHOO_SYMBOLS = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}
```

Keep the mapping near Yahoo acquisition logic or orchestration.

Do not place it in `analytics.py`.

The common business ticker remains:

```text
SP500
```

even though Yahoo receives:

```text
^GSPC
```

# Part 8 - Retrieve instrument and benchmark

Retrieve both series through the same provider function:

```python
instrument_prices = fetch_yahoo_prices(
    symbol=YAHOO_SYMBOLS["AAPL"],
    canonical_ticker="AAPL",
    period="1mo",
    interval="1d",
)

benchmark_prices = fetch_yahoo_prices(
    symbol=YAHOO_SYMBOLS["SP500"],
    canonical_ticker="SP500",
    period="1mo",
    interval="1d",
)
```

Do not duplicate provider implementation for instrument and benchmark.

Do not assume that both raw series always contain exactly the same dates.

# Part 9 - Reuse TD07 alignment

Import the existing TD07 function:

```python
from analytics import align_series
```

Then:

```python
aligned_instrument, aligned_benchmark = align_series(
    instrument_prices,
    benchmark_prices,
)
```

The alignment logic must not be rewritten for Yahoo.

Validate:

```text
[ ] aligned instrument is not empty
[ ] aligned benchmark is not empty
[ ] both aligned lists have the same length
[ ] corresponding rows use common dates
```

# Part 10 - Reuse TD07 analytics unchanged

Reuse:

```python
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

The architectural proof is:

```text
CSV
  |
  v
canonical rows
  |
  +------------------+
                     |
Yahoo                |
  |                  |
  v                  |
canonical rows       |
  |                  |
  +------------------+
          |
          v
same analytics.py
```

If `analytics.py` needs to check whether the provider is CSV or Yahoo, stop and inspect the design.

Provider-specific behaviour should remain outside the analytical layer.

# Part 11 - Integrate Yahoo into main.py

Keep the orchestration understandable.

Conceptually:

```text
select Yahoo provider path
        |
        v
fetch AAPL
        |
        v
fetch ^GSPC as canonical SP500
        |
        v
align_series()
        |
        v
period return
base 100
relative performance
        |
        v
terminal summary
```

The terminal output should identify the provider honestly.

Example:

```text
Provider
Yahoo Finance via yfinance

Market configuration
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Period     : 1 month
Interval   : Daily

Instrument return : ...
Benchmark return  : ...

Relative performance
AAPL vs SP500 : ... percentage points
```

The values depend on retrieval time.

Do not hard-code market values or expected percentages.

# Part 12 - CORE validation

Run:

```bash
python src/main.py
```

Then verify:

```text
[ ] provider is identified as Yahoo Finance via yfinance
[ ] AAPL remote data is not empty
[ ] SP500 benchmark remote data is not empty
[ ] Yahoo symbol ^GSPC is used only at provider boundary
[ ] canonical ticker remains SP500
[ ] rows use date/ticker/open/high/low/close/volume
[ ] period is 1 month
[ ] interval is daily
[ ] common dates exist
[ ] TD07 analytics are reused unchanged
[ ] first base-100 value is 100 for both aligned series
[ ] relative performance uses instrument minus benchmark
```

# Part 13 - Standard Git handoff

Use the established workflow:

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

Typical changed files:

```text
requirements.txt
src/main.py
src/providers/__init__.py
src/providers/yahoo_provider.py
```

Suggested commit and PR title:

```text
feat: add Yahoo Finance provider
```

Before merge, the reviewer should verify:

```text
[ ] yfinance is recorded in requirements.txt
[ ] provider code is separate from analytics
[ ] AAPL maps to AAPL
[ ] SP500 maps to ^GSPC
[ ] canonical ticker remains SP500
[ ] returned rows are canonical
[ ] analytics.py has no Yahoo-specific change
[ ] no market value is hard-coded
[ ] no unrelated file is included
```

# Part 14 - Checkpoint B

Checkpoint B closes Checkpoint Phase B after TD08.

Canonical evidence contract:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

For convenience, required files are:

```text
README.md
01_pull_request.png
02_code_review.png
03_yahoo_market_data.png
04_instrument_benchmark.png
```

Store them under:

```text
evidence/checkpoint-b/<github-username>/
```

Do not rename the files.

## Capture checklist

Before leaving TD08:

```text
[ ] my Pull Request is attributable to me
[ ] my review contains meaningful technical content
[ ] successful Yahoo remote retrieval is visible
[ ] AAPL and SP500 are both visible
[ ] lookback is 1 month
[ ] interval is Daily
[ ] no secret appears in the screenshots
```

Do not use static CSV output as Yahoo evidence.

Do not fabricate remote-provider evidence.

Screenshots do not replace execution and explanation.

# Part 15 - Temporary Yahoo outage procedure

Remote services are outside the repository's control.

If Yahoo retrieval fails during the session:

1. verify internet access;
2. verify the symbol;
3. compare your provider code with the instructor reference;
4. retry once after correcting any local issue;
5. use the local CSV path to continue validating `analytics.py`;
6. report the external failure to the instructor.

Do not rewrite analytics because Yahoo is temporarily unavailable.

Do not fabricate successful Yahoo output.

Checkpoint B file `03_yahoo_market_data.png` requires a successful remote retrieval.

If Yahoo remains externally unavailable after local code checks and one retry, follow the canonical recovery rule in:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

The Yahoo evidence item becomes:

```text
PENDING_EXTERNAL
```

until a successful remote retrieval can be captured during an instructor-approved recovery window.

Do not substitute CSV output, provider-double output or fabricated values for the missing Yahoo evidence.

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied.

## Optional 1 - Invalid-symbol experiment

Try a clearly invalid symbol in a temporary experiment.

Observe the provider response.

Restore the valid mapping afterward.

Do not make this experiment part of required Checkpoint B evidence.

## Optional 2 - Alternate instrument

Temporarily retrieve another widely traded instrument such as:

```text
MSFT
```

The common CORE pair remains:

```text
AAPL + S&P 500
```

Do not make alternate pair selection a mandatory TD08 task.

Checkpoint B also does not require changing the CORE market pair.

For mandatory validation, the common pair remains:

```text
AAPL + S&P 500
```

## Optional 3 - Provider selector

Experiment with:

```text
csv
or
yahoo
```

without changing analytical functions.

A generic provider framework is not required.

## Optional 4 - Configuration refactor

You may document provider mapping more formally.

Do not require YAML parsing.

Do not introduce PyYAML only for this exercise.

## Optional 5 - Additional provider-error handling

You may improve user-facing error messages.

Do not build:

```text
retry framework
backoff engine
provider abstraction framework
```

inside TD08.

# ADVANCED

No `READY_TO_TEACH` advanced activity is attached directly to TD08 at this time.

Provider selection and additional provider-error handling remain OPTIONAL experiments with explicit scope limits.

Advanced work is not required for Checkpoint B.

# TROUBLESHOOTING

## ModuleNotFoundError: yfinance

Run:

```bash
python -m pip install -r requirements.txt
```

or verify:

```bash
python -m pip show yfinance
```

## Empty Yahoo response

Check:

```text
internet access
symbol spelling
period=1mo
interval=1d
```

Test AAPL and `^GSPC` separately.

## Returned columns differ from expectation

Inspect:

```python
print(history.columns)
```

Use the structure actually returned by the library.

Do not invent provider fields.

## Import error for providers

Verify:

```text
src/
├── main.py
├── analytics.py
└── providers/
    ├── __init__.py
    └── yahoo_provider.py
```

Run from repository root:

```bash
python src/main.py
```

## No common dates

Use the existing `align_series()`.

Inspect the dates returned by both provider calls.

Do not compare rows only by list position.

## PR changes analytics.py for Yahoo-specific logic

Stop before merge.

Yahoo-specific symbols and acquisition behaviour belong in the provider boundary, not in `analytics.py`.

# Final readiness check

Each student should be able to explain:

```text
[ ] yfinance vs official Yahoo API
[ ] canonical ticker vs provider symbol
[ ] SP500 vs ^GSPC
[ ] provider normalization
[ ] canonical row structure
[ ] common-date alignment
[ ] why analytics.py stays provider-neutral
[ ] why requirements.txt matters
[ ] what to do during temporary provider failure
```

The team should confirm:

```text
[ ] Yahoo provider returns canonical rows
[ ] SP500 remains the canonical benchmark ticker
[ ] ^GSPC remains Yahoo-specific
[ ] TD07 analytics run unchanged
[ ] python src/main.py works with successful Yahoo retrieval
[ ] Checkpoint B can be completed honestly
```

# What comes next?

Pedagogical Wave 3 and Checkpoint Phase B are now complete:

```text
Wave 3 - TD07-TD08

TD07
provider-neutral analytics

TD08
Yahoo provider
        |
        v
same analytics contract
```

TD09 introduces the professional data environment.

The central design rule remains:

```text
provider-specific acquisition
        |
        v
canonical rows
        |
        v
provider-neutral analytics
```
