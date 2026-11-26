# TD10 - Bloomberg Provider

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"MarketPulse must support Bloomberg without rewriting the whole application."
```

## Context

TD09 produced the mapping contract:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

TD10 turns that mapping into:

```text
src/providers/bloomberg_provider.py
```

The objective is not to build a generic provider framework.

The objective is to prove that the Bloomberg stage can feed the same canonical rows and the same analytics already used by CSV and Yahoo.

Target architecture:

```text
Bloomberg-stage input
        |
        v
bloomberg_provider.py
        |
        v
canonical rows
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
MarketPulse terminal output
```

## Authorized access modes

TD10 preserves the TD09 access mode:

```text
LIVE
or
APPROVED_SAMPLE
```

### LIVE

Use only the instructor-approved Bloomberg access mechanism documented during TD09.

The exact connection implementation depends on the classroom environment.

### APPROVED_SAMPLE

Use:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

APPROVED_SAMPLE validates the provider boundary and normalization contract.

It does not prove live Bloomberg connectivity.

## Learning objectives

At the end of TD10, you should be able to:

- create a Bloomberg-specific provider boundary;
- reuse the TD09 mapping instead of inventing fields;
- preserve canonical AAPL and SP500 tickers;
- normalize approved Bloomberg-stage input to canonical rows;
- obtain instrument and benchmark rows;
- reuse TD07 alignment unchanged;
- reuse TD07 analytics unchanged;
- create the shared `build_market_snapshot(...)` application boundary in `src/main.py`;
- make the terminal path consume that shared snapshot;
- keep `src/main.py` import-safe for TD11;
- make LIVE vs APPROVED_SAMPLE visible;
- validate the terminal path;
- complete the established Git workflow.

## CORE definition of done

TD10 is complete when the team can confirm:

```text
[ ] docs/BLOOMBERG_FIELD_MAPPING.md is the mapping source
[ ] src/providers/bloomberg_provider.py exists
[ ] AAPL maps to AAPL US Equity
[ ] SP500 maps to SPX Index
[ ] one authorized access mode is used: LIVE or APPROVED_SAMPLE
[ ] Bloomberg-stage input is normalized to canonical rows
[ ] canonical instrument ticker remains AAPL
[ ] canonical benchmark ticker remains SP500
[ ] instrument rows are not empty
[ ] benchmark rows are not empty
[ ] align_series() is reused
[ ] analytics.py has no Bloomberg-specific calculation
[ ] period return is reused
[ ] base 100 is reused
[ ] relative performance is reused
[ ] build_market_snapshot(...) exists in src/main.py
[ ] build_market_snapshot(...) returns the shared application result
[ ] main() consumes the shared snapshot
[ ] src/main.py keeps if __name__ == "__main__": main()
[ ] terminal output shows the actual access mode honestly
[ ] python src/main.py works
[ ] no credential is committed
[ ] the change follows the standard branch / PR / review workflow
```

Daily returns are not required.

A generic provider selector is not required.

YAML parsing is not required.

## Prerequisites

Before starting:

```text
[ ] TD01-TD09 completed
[ ] docs/BLOOMBERG_FIELD_MAPPING.md exists and was reviewed
[ ] TD09 access mode is documented
[ ] AAPL US Equity mapping is documented
[ ] SPX Index mapping is documented
[ ] src/analytics.py exists
[ ] Yahoo provider path is understood
[ ] team main is synchronized
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

Reference materials:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md
```

For LIVE mode, the instructor supplies or demonstrates only the environment-specific raw acquisition body.

For APPROVED_SAMPLE mode, the repository fallback assets are sufficient.

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for review, environment variation and troubleshooting.

| Time | Activity |
|---|---|
| 00-08 min | Review TD09 mapping + access mode |
| 08-18 min | Create Bloomberg provider boundary |
| 18-38 min | Implement raw input path + normalization |
| 38-52 min | Obtain AAPL + SP500 canonical rows |
| 52-65 min | Reuse alignment + analytics |
| 65-74 min | Build shared snapshot + integrate terminal output + mode label |
| 74-80 min | CORE validation + standard Git handoff |
| 80-90 min | Review / troubleshooting / OPTIONAL |

## Repository evolution

TD10 extends the CORE structure to:

```text
src/
├── main.py
├── analytics.py
└── providers/
    ├── __init__.py
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

Responsibility split:

```text
bloomberg_provider.py
=
Bloomberg identifier handling
+
authorized raw input boundary
+
Bloomberg-stage normalization

analytics.py
=
provider-neutral alignment
+
period return
+
base 100
+
relative performance

main.py
=
orchestration
+
terminal output
```

# CORE

# Part 1 - Review TD09 before coding

Open:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

Verify:

```text
[ ] Access mode is LIVE or APPROVED_SAMPLE
[ ] AAPL -> AAPL US Equity
[ ] SP500 -> SPX Index
[ ] input structure is documented
[ ] mapped fields are traceable
[ ] missing fields are documented honestly
[ ] TD10 handoff notes are present
```

Do not replace the TD09 mapping with assumptions from the internet.

# Part 2 - Create the feature branch

Use the established workflow:

```bash
git switch main
git pull
git status
git switch -c feature/bloomberg-provider
```

TD10 does not reteach Git theory.

# Part 3 - Create the provider module

Create:

```text
src/providers/bloomberg_provider.py
```

Keep the identifier mapping close to the provider boundary:

```python
BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}
```

The rest of MarketPulse continues to use:

```text
AAPL
SP500
```

# Part 4 - Separate raw input from normalization

The provider has two responsibilities.

## 4.1 Raw input boundary

Conceptual LIVE signature:

```python
def fetch_raw_bloomberg_history(
    identifier,
    start_date,
    end_date,
):
    ...
```

Only the instructor-approved classroom mechanism belongs inside this boundary.

Do not invent a Bloomberg package or connector.

In APPROVED_SAMPLE mode, raw input comes from:

```text
data/sample/bloomberg_reference_sample.json
```

Use the scaffold in:

```text
docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md
```

## 4.2 Normalization boundary

Create a function that transforms the authorized input into canonical rows.

Conceptual contract:

```python
def normalize_bloomberg_history(
    raw_data,
    canonical_ticker,
):
    ...
```

Output fields:

```text
date
ticker
open
high
low
close
volume
```

Field sources must come from TD09 mapping.

# Part 5 - APPROVED_SAMPLE normalization

When the session mode is APPROVED_SAMPLE, the input uses teaching wrapper keys:

```text
observation_date
open_value
high_value
low_value
close_value
volume_value
```

Map them to:

```text
date
open
high
low
close
volume
```

and assign the canonical ticker from the approved series metadata.

Example shape:

```python
{
    "date": observation["observation_date"],
    "ticker": canonical_ticker,
    "open": float(observation["open_value"]),
    "high": float(observation["high_value"]),
    "low": float(observation["low_value"]),
    "close": float(observation["close_value"]),
    "volume": int(observation["volume_value"]),
}
```

These wrapper keys are not Bloomberg field mnemonics.

Do not reuse them as LIVE field names unless the actual environment independently returns the same names.

# Part 6 - LIVE normalization

When the session mode is LIVE, use only fields actually documented in:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

The instructor-approved raw acquisition returns the actual classroom response.

Your normalization code translates that observed structure into the same canonical row contract.

If one expected field is unavailable, use only the instructor-approved convention documented in TD09.

Do not fabricate a value or field name.

# Part 7 - Obtain instrument and benchmark rows

The common mappings remain:

```text
AAPL
  |
  v
AAPL US Equity

SP500
  |
  v
SPX Index
```

Obtain canonical rows for both.

Required result:

```text
instrument rows
ticker = AAPL

benchmark rows
ticker = SP500
```

Both lists must be non-empty in the selected authorized mode.

# Part 8 - Validate canonical structure

Inspect one row from each series.

Both must expose:

```text
date
ticker
open
high
low
close
volume
```

Check:

```text
[ ] close is numeric
[ ] date is available
[ ] AAPL row uses ticker AAPL
[ ] benchmark row uses ticker SP500
```

In APPROVED_SAMPLE mode, compare the normalized rows with:

```text
data/sample/bloomberg_reference_expected.json
```

The reference provides an exact expected result for the fallback fixture.

# Part 9 - Reuse alignment unchanged

Use:

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

Do not implement:

```text
align_bloomberg_series()
```

unless the instructor explicitly identifies a real provider exception.

# Part 10 - Reuse analytics unchanged

Reuse the TD07 CORE functions:

```text
calculate_period_return()
calculate_base_100()
calculate_relative_performance()
```

Do not create:

```text
calculate_bloomberg_period_return()
calculate_bloomberg_base_100()
```

The architectural proof is:

```text
CSV -----------+
               |
Yahoo ---------+--> canonical rows --> same analytics.py
               |
Bloomberg -----+
```

# Part 11 - Build the shared snapshot and integrate the terminal path

TD10 must leave a concrete application boundary ready for TD11.

Use the frozen contract:

```text
docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
```

In `src/main.py`, create:

```python
def build_market_snapshot(...):
    ...
```

This function must reuse the provider path and shared analytics that already exist.

It must return the application result needed by both terminal and dashboard presentation.

At minimum, the snapshot contains:

```text
provider
lookback
interval
instrument
benchmark
instrument_return
benchmark_return
relative_performance
instrument_base_100
benchmark_base_100
```

Do not duplicate formulas inside the snapshot builder.

The intended flow is:

```text
provider rows
      |
      v
analytics.py
      |
      v
build_market_snapshot(...)
      |
      v
main()
      |
      v
terminal output
```

Keep `src/main.py` import-safe:

```python
def main():
    snapshot = build_market_snapshot(...)
    ...


if __name__ == "__main__":
    main()
```

This is required because TD11 imports `build_market_snapshot(...)` from `src/main.py`.

The terminal output must show the actual mode.

Example LIVE output:

```text
Provider
Bloomberg

Access mode
LIVE
```

Example fallback output:

```text
Provider
Bloomberg stage

Access mode
APPROVED_SAMPLE
```

Do not display APPROVED_SAMPLE as live Bloomberg retrieval.

Keep the common business context visible:

```text
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Period     : 1 month
Interval   : Daily
```

and reuse the calculated:

```text
instrument return
benchmark return
relative performance
base-100 series
```

TD10 is therefore the producing side of the TD10 -> TD11 snapshot handoff.

TD11 only adds presentation on top of this result.

# Part 12 - CORE validation

Run:

```bash
python src/main.py
```

Verify:

```text
[ ] access mode is visible
[ ] AAPL path works
[ ] SP500 path works
[ ] canonical rows have the expected fields
[ ] common dates exist
[ ] align_series() is reused
[ ] analytics.py contains no Bloomberg identifier
[ ] period return is calculated by shared analytics
[ ] base 100 is calculated by shared analytics
[ ] relative performance is calculated by shared analytics
[ ] build_market_snapshot(...) returns the required shared result
[ ] main() consumes build_market_snapshot(...)
[ ] importing src/main.py does not execute the terminal program
[ ] no credential appears in terminal output
```

If using APPROVED_SAMPLE:

```text
[ ] normalized fallback rows match the expected canonical reference
[ ] output does not claim LIVE connectivity
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

Typical required files:

```text
src/main.py
src/providers/bloomberg_provider.py
```

Only update the mapping document if the approved classroom observation changed.

Suggested commit and PR title:

```text
feat: add Bloomberg provider boundary
```

Reviewer checklist:

```text
[ ] TD09 mapping is respected
[ ] access mode is honest
[ ] provider identifiers stay in provider boundary
[ ] canonical tickers remain AAPL and SP500
[ ] normalized rows use canonical keys
[ ] analytics.py has no Bloomberg-specific formula
[ ] no credential is committed
[ ] APPROVED_SAMPLE is not labelled LIVE
```

# Checkpoint relation

Checkpoint C is performed after TD12.

TD10 prepares:

```text
01_final_market_data.png
```

but no Checkpoint C package is submitted yet.

If TD10 uses APPROVED_SAMPLE, do not present that execution as proof of live Bloomberg connectivity.

The final authorized provider evidence policy remains defined in:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied.

## Optional 1 - Human-readable settings update

You may update:

```text
config/settings.yml
```

to document:

```text
provider = bloomberg
lookback = 1mo
interval = 1d
```

The file remains a human-readable contract.

Do not add PyYAML for TD10 CORE.

## Optional 2 - Generic provider selection

Experiment with a small selector for:

```text
csv
yahoo
bloomberg
```

Do not build a plugin framework.

## Optional 3 - Additional provider metadata

Experiment with metadata such as:

```text
provider
access_mode
instrument_source
benchmark_source
```

Do not expose credentials or workstation details.

## Optional 4 - Extended error handling

Improve messages for:

```text
empty input
missing field
unsupported identifier
unavailable LIVE environment
```

Do not build retry or backoff infrastructure.

## Optional 5 - Additional Bloomberg-stage diagnostics

Compare one canonical row from:

```text
CSV
Yahoo
Bloomberg stage
```

and explain why the analytics layer can reuse them.

# ADVANCED

No `READY_TO_TEACH` advanced activity is active in TD10 at this time.

The planned advanced path:

```text
ADV-BBG-01 - Bloomberg Reference Data
```

currently has status:

```text
PENDING_EXTERNAL
```

It requires a validated Bloomberg LIVE environment.

Do not treat APPROVED_SAMPLE as LIVE evidence and do not attempt this activity until the delivery gate has passed.

# TROUBLESHOOTING

## LIVE access fails

Do not redesign the application.

With instructor approval, switch to:

```text
APPROVED_SAMPLE
```

and document the mode change.

## APPROVED_SAMPLE normalization differs from expected reference

Compare:

```text
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

Verify wrapper-key mapping and canonical ticker assignment.

## Provider returns rows but analytics fail

Inspect:

```text
date
ticker
close
common dates
```

The issue should be diagnosed at the contract boundary before analytics are modified.

## Analytics require Bloomberg identifiers

Stop.

Provider-specific identifiers must disappear before rows reach `analytics.py`.

## Credentials appear in code or output

Stop.

Remove the sensitive material and notify the instructor if it entered Git history.

# Final readiness check

Each student should be able to explain:

```text
[ ] TD09 mapping contract
[ ] Bloomberg provider boundary
[ ] LIVE vs APPROVED_SAMPLE
[ ] raw input vs normalization
[ ] AAPL vs AAPL US Equity
[ ] SP500 vs SPX Index
[ ] canonical row structure
[ ] why align_series() is reused
[ ] why analytics.py remains provider-neutral
[ ] why fallback execution is not live evidence
```

The team should confirm:

```text
[ ] bloomberg_provider.py exists
[ ] AAPL and SP500 canonical rows are produced
[ ] existing analytics are reused unchanged
[ ] build_market_snapshot(...) exists and is reusable
[ ] main() consumes the shared snapshot
[ ] actual access mode is visible
[ ] python src/main.py works
[ ] provider change was reviewed
[ ] no credentials were committed
```

# What comes next?

TD10 now provides:

```text
provider-specific input
        |
        v
canonical rows
        |
        v
shared analytics
```

TD10 now leaves the frozen application snapshot contract implemented in `src/main.py`:

```text
docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
```

The shared boundary produced by TD10 is:

```python
build_market_snapshot(...)
```

TD11 consumes this existing boundary.

The contract keeps one calculation path for both presentations:

```text
providers
   |
   v
analytics
   |
   v
snapshot
   |
   +----------+
   |          |
   v          v
terminal     Dash
```

TD11 will consume this contract rather than creating a second provider or analytics path.
