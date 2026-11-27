# TD02 - Python + CSV / JSON

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"The trading desk still sends local CSV and JSON market files."
```

## Context

TD01 made the MarketPulse starter operational.

TD02 now turns the starter into a small Python data-processing exercise.

The trading desk currently provides:

- instrument metadata in JSON;
- daily market prices in CSV.

MarketPulse must load both files, distinguish the primary instrument from its benchmark, filter the correct observations and display a reusable summary.

The common starter still uses:

```text
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Lookback   : 1 month
Interval   : Daily
Provider   : CSV
```

Do not calculate returns yet.

Period return, base 100 and relative performance are introduced later.

## Learning objectives

At the end of TD02, you should be able to:

- recognize Python lists and dictionaries;
- read JSON with `json.load()`;
- read CSV with `csv.DictReader`;
- explain why CSV numeric fields initially arrive as text;
- convert numeric text to Python numbers;
- filter observations by ticker;
- use simple loops and conditions;
- create small reusable functions;
- display the same summary logic for instrument and benchmark.

## CORE definition of done

TD02 is complete when MarketPulse:

```text
[ ] still runs with python src/main.py
[ ] loads instruments.json
[ ] loads prices.csv
[ ] separates AAPL and SP500 rows
[ ] has 21 observations for each series
[ ] displays the first close for each series
[ ] displays the last close for each series
[ ] converts close values to numeric form before numerical use
[ ] uses reusable summary logic
[ ] has meaningful Python changes ready for TD03 Git work
```

No return calculation is required.

Optional exercises are not required to complete TD02.

## Prerequisites

Before starting:

```text
[ ] TD01 completed
[ ] team repository accessible
[ ] TEAM.md completed
[ ] Linux terminal available
[ ] python src/main.py works
```

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for questions, debugging and validation.

| Time | Activity |
|---|---|
| 00-08 min | Review the starter |
| 08-20 min | JSON and dictionaries |
| 20-35 min | CSV and list-of-dictionaries |
| 35-48 min | Numeric conversion and filtering |
| 48-63 min | First and last close helpers |
| 63-75 min | Reusable market summary |
| 75-80 min | Final run and CORE validation |
| 80-90 min | Buffer and optional exercises |

# CORE

# Part 1 - Review the starter

Open:

```text
src/main.py
```

Run:

```bash
python src/main.py
```

Identify:

```text
import csv
import json
Path
DATA_DIR
load_instruments()
load_prices()
filter_prices()
main()
```

Be able to answer:

1. Which function reads JSON?
2. Which function reads CSV?
3. Which function selects one ticker?
4. Which function coordinates execution?
5. Where are the input files stored?

Do not refactor the project architecture in TD02.

# Part 2 - Understand JSON and dictionaries

Inspect:

```bash
cat data/sample/instruments.json
```

The top-level objects are:

```text
instrument
benchmark
```

The current loader is conceptually:

```python
with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
    instruments = json.load(file)
```

Temporarily inspect the result:

```python
print(type(instruments))
print(instruments.keys())
```

Then inspect nested dictionaries:

```python
instrument = instruments["instrument"]
benchmark = instruments["benchmark"]

print(instrument["ticker"])
print(instrument["name"])
print(instrument["currency"])

print(benchmark["ticker"])
print(benchmark["name"])
```

You should understand:

```text
instruments
=
dictionary containing two business objects

instrument
=
dictionary describing the primary instrument

benchmark
=
dictionary describing the comparison benchmark
```

Remove temporary inspection prints when they are no longer useful.

# Part 3 - Understand CSV and lists of dictionaries

Inspect:

```bash
head data/sample/prices.csv
```

The columns are:

```text
date
ticker
open
high
low
close
volume
```

The current loader uses:

```python
def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))
```

Temporarily inspect:

```python
prices = load_prices()

print(type(prices))
print(type(prices[0]))
print(prices[0])
```

You should observe:

```text
prices
=
list

prices[0]
=
dictionary
```

## CSV values are text

Inspect:

```python
print(prices[0]["close"])
print(type(prices[0]["close"]))
```

Convert when a numerical value is needed:

```python
close = float(prices[0]["close"])
```

Key rule:

```text
CSV text
    |
    v
explicit numeric conversion
    |
    v
safe numerical use
```

Do not perform arithmetic on price strings.

# Part 4 - Filter instrument and benchmark rows

MarketPulse stores both series in the same CSV.

The starter helper is:

```python
def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]
```

Use it for both business objects:

```python
instrument_prices = filter_prices(
    prices,
    instrument["ticker"],
)

benchmark_prices = filter_prices(
    prices,
    benchmark["ticker"],
)
```

Check:

```python
print(len(instrument_prices))
print(len(benchmark_prices))
```

Expected result:

```text
21
21
```

## Understand the list comprehension

Equivalent logic is:

```python
result = []

for row in prices:
    if row["ticker"] == ticker:
        result.append(row)
```

You do not need to keep both implementations.

The important concept is:

```text
loop
+
condition
+
append
=
filtering
```

# Part 5 - Create first and last close helpers

Create:

```python
def get_first_close(prices):
    ...
```

The function should:

1. access the first observation;
2. read `close`;
3. convert it to `float`;
4. return the number.

Expected values:

```text
AAPL  -> 250.00
SP500 -> 6600.00
```

Then create:

```python
def get_last_close(prices):
    ...
```

Expected values:

```text
AAPL  -> 266.20
SP500 -> 6742.00
```

Keep the functions small and readable.

A complex error model is not required in TD02.

# Part 6 - Build one reusable market summary

Do not duplicate one display implementation for AAPL and another for SP500.

Create one reusable function.

Suggested signature:

```python
def display_market_summary(asset, prices, show_currency=True):
    ...
```

It should display:

```text
ticker
name
number of observations
first close
last close
```

Example instrument output:

```text
AAPL - Apple Inc.
Observations : 21
First close  : 250.00 USD
Last close   : 266.20 USD
```

Example benchmark output:

```text
SP500 - S&P 500
Observations : 21
First close  : 6600.00
Last close   : 6742.00
```

The main idea is:

```text
same operation
+
different data
=
reusable function
```

# Part 7 - Keep main() readable

A clear flow is:

```text
load metadata
      |
      v
load prices
      |
      v
select instrument + benchmark
      |
      v
filter both series
      |
      v
display configuration
      |
      v
display both summaries
```

Do not move all implementation logic directly into `main()`.

Use small functions when they make responsibilities clearer.

# Part 8 - Validate the final output

Run:

```bash
python src/main.py
```

Target output:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close  : 250.00 USD
Last close   : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close  : 6600.00
Last close   : 6742.00
```

Small formatting differences are acceptable.

Required behaviour:

```text
[ ] instrument identified
[ ] benchmark identified
[ ] both series filtered
[ ] 21 observations for AAPL
[ ] 21 observations for SP500
[ ] first close displayed
[ ] last close displayed
[ ] numerical conversion performed
[ ] reusable summary logic used
```

# Part 9 - Python concepts recap

You should now recognize:

```text
list
dictionary
function
condition
loop
type conversion
```

Examples:

```python
prices[0]

instrument["ticker"]

def get_last_close(prices):
    ...

if row["ticker"] == ticker:
    ...

for row in prices:
    ...

float(row["close"])
```

# Part 10 - CORE handoff to TD03

Do not turn TD02 into a Git lesson.

Formal local Git workflow begins in TD03.

At the end of TD02:

1. make sure the Python changes work;
2. do not create a Pull Request;
3. do not create an unnecessary feature branch;
4. unless the instructor explicitly asks otherwise, leave the useful TD02 changes available in your working tree for TD03.

TD03 will begin from those real changes.

The intended transition is:

```text
TD02
working Python change
      |
      v
TD03
git status
git diff
git add
git commit
git log
```

This gives Git a real purpose.

The first meaningful TD03 commit may represent the working Python changes produced during TD02.

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied.

## Optional 1 - First and last date

Create:

```python
def get_first_date(prices):
    ...
```

and:

```python
def get_last_date(prices):
    ...
```

Expected common sample range:

```text
2026-09-01
2026-09-30
```

## Optional 2 - Positive-volume observations

For the instrument only, count rows where:

```python
int(row["volume"]) > 0
```

Do not make benchmark volume part of the CORE comparison requirement.

## Optional 3 - Minimum and maximum close

Create small functions that return:

```text
minimum close
maximum close
```

Do not use pandas.

## Optional 4 - List slicing

Inspect:

```python
prices[:3]
```

Iterate through the first three rows.

## Optional 5 - Output formatting

Experiment with:

```python
f"{value:.2f}"
```

Formatting polish must not replace the CORE requirements.

# ADVANCED

Complete advanced work only after TD02 CORE is complete.

Advanced work is not required for Checkpoint A.

## ADV-LNX-04 - Environment Variables

Status:

```text
READY_TO_TEACH
```

Prerequisites:

```text
TD02 CORE complete
basic Python imports
```

Estimated duration:

```text
30 minutes
```

Support:

[ADV-LNX-04 - Environment Variables](../advanced/ADV_LNX_04_ENVIRONMENT_VARIABLES.md)

# TROUBLESHOOTING

## IndexError

If:

```python
prices[0]
```

or:

```python
prices[-1]
```

fails, verify that filtering returned observations.

## KeyError

Inspect available keys:

```python
print(row.keys())
print(instrument.keys())
```

Check spelling and capitalization.

## ValueError during float conversion

Inspect the value before converting:

```python
print(row["close"])
```

Confirm that the field contains numeric text.

## FileNotFoundError

From the repository root:

```bash
pwd
ls
ls data/sample
```

Then retry:

```bash
python src/main.py
```

# Final readiness check

Each student should be able to explain:

```text
[ ] what a Python list is
[ ] what a Python dictionary is
[ ] what csv.DictReader returns
[ ] why CSV numeric values need conversion
[ ] how MarketPulse filters by ticker
[ ] why one reusable summary function is useful
[ ] where instrument metadata is stored
[ ] where price observations are stored
```

The team should confirm:

```text
[ ] MarketPulse runs
[ ] AAPL has 21 observations
[ ] SP500 has 21 observations
[ ] first and last closes are displayed
[ ] no external Python library was required
[ ] no return calculation was added
```

# Checkpoint relation

No screenshot package is submitted after TD02.

TD01 and TD02 contribute to:

```text
Checkpoint A - Foundations
```

Checkpoint A is validated after TD04.
# Checkpoint relation and Evidence Artefacts

The single source of truth for all checkpoint evidence requirements is:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

No screenshot package is submitted after TD02.

TD01 and TD02 together establish the execution skills validated by:

```text
Checkpoint A - Foundations (25% weight)
```

Checkpoint A is officially assessed after TD04.

### Checkpoint A Artefact: `01_terminal_python.png`

The first required Checkpoint A screenshot can be captured from the working TD02 state:

| Attribute | Specification |
|---|---|
| **Checkpoint** | Checkpoint A — Foundations |
| **Filename** | `01_terminal_python.png` |
| **Target Directory** | `evidence/checkpoint-a/<github-username>/` |
| **Status** | Required for Checkpoint A |
| **Format** | PNG (lowercase_snake_case, strictly no spaces) |

#### Terminal execution to display:
```bash
pwd
ls
python src/main.py
```

#### Verification objective:
Shows that the student can navigate the Linux project repository and run MarketPulse with local CSV/JSON loading, displaying the 21 observations and first/last close values for both `AAPL` and `SP500`.

> **Note:** Each student must capture their own screenshot in their own named directory (`evidence/checkpoint-a/<github-username>/`). Submissions are graded after TD04.

# What comes next?

Pedagogical Wave 1 is now complete:

```text
Wave 1 - Foundations - 3 hours

TD01 - Bootstrap + Linux
TD02 - Python + CSV / JSON
```

TD03 introduces the local Git workflow.

It starts from the meaningful Python changes produced here:

```text
working tree
    |
    v
git status
    |
    v
git diff
    |
    v
git add
    |
    v
git commit
    |
    v
git log
```
