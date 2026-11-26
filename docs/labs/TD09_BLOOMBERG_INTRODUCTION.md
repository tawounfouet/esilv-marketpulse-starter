# TD09 - Bloomberg Introduction

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"The trading desk now has access to a professional market-data environment."
```

## Context

MarketPulse already supports:

```text
CSV / JSON
+
Yahoo Finance
```

and the analytical layer is stable:

```text
canonical rows
      |
      v
align_series()
      |
      v
period return
base 100
relative performance
```

TD09 introduces the Bloomberg stage.

The objective is not to build the Bloomberg provider yet.

The objective is to establish an accurate mapping contract for TD10:

```text
canonical ticker
+
Bloomberg identifier
+
observed or approved input fields
+
MarketPulse canonical fields
+
honest access mode
```

The main deliverable is:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

## Authorized access modes

TD09 supports exactly two teaching modes:

```text
LIVE
or
APPROVED_SAMPLE
```

### LIVE

Use LIVE when the instructor-approved Bloomberg environment successfully returns data during class.

The mapping document must record the actual access method and actual observed field names.

### APPROVED_SAMPLE

Use APPROVED_SAMPLE when the live environment is unavailable or unsuitable for the scheduled lab.

Use only:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

The fallback fixture uses teaching wrapper keys.

Those keys are not Bloomberg field mnemonics.

APPROVED_SAMPLE does not prove live Bloomberg connectivity.

## Learning objectives

At the end of TD09, you should be able to:

- explain Bloomberg's role in MarketPulse;
- distinguish canonical tickers from provider identifiers;
- explain `AAPL -> AAPL US Equity`;
- explain `SP500 -> SPX Index`;
- distinguish LIVE from APPROVED_SAMPLE mode;
- inspect one approved Bloomberg-stage input;
- identify the fields available in that input;
- map those fields to the MarketPulse canonical row contract;
- preserve canonical tickers;
- document the access mode honestly;
- prepare a mapping contract usable by TD10.

## CORE definition of done

TD09 is complete when the team can confirm:

```text
[ ] one access mode is explicitly documented: LIVE or APPROVED_SAMPLE
[ ] AAPL -> AAPL US Equity is documented
[ ] SP500 -> SPX Index is documented
[ ] one instrument input was inspected
[ ] one benchmark input was inspected
[ ] docs/BLOOMBERG_FIELD_MAPPING.md exists
[ ] the mapping document identifies the source of each mapped field
[ ] canonical ticker AAPL is preserved
[ ] canonical ticker SP500 is preserved
[ ] unverified Bloomberg field names were not invented
[ ] no credential or sensitive session information is committed
[ ] the mapping document was reviewed before merge
```

Live Bloomberg connectivity is not required for CORE completion.

Provider implementation is not required in TD09.

## Prerequisites

Before starting:

```text
[ ] TD01-TD08 completed
[ ] Checkpoint B completed or ready
[ ] team main is synchronized
[ ] canonical row contract is understood
[ ] Yahoo provider boundary is understood
[ ] TD07 analytics are understood
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

Before TD09 begins, the instructor should choose one session mode:

```text
LIVE
or
APPROVED_SAMPLE
```

Reference:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
```

If LIVE fails during class, the instructor may switch the session to APPROVED_SAMPLE.

The change of mode must be documented honestly.

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for review, environment variation and troubleshooting.

| Time | Activity |
|---|---|
| 00-08 min | Bloomberg role + session mode |
| 08-20 min | Canonical vs Bloomberg identifiers |
| 20-35 min | Inspect approved instrument input |
| 35-47 min | Inspect approved benchmark input |
| 47-62 min | Map input fields to canonical fields |
| 62-72 min | Create mapping document |
| 72-80 min | Validate + standard Git handoff |
| 80-90 min | Review / troubleshooting / OPTIONAL |

# CORE

# Part 1 - Position Bloomberg in the provider progression

MarketPulse now has three provider stages:

```text
CSV
  |
  v
local teaching data

Yahoo
  |
  v
accessible remote data

Bloomberg
  |
  v
professional market-data stage
```

The provider changes.

The business model does not:

```text
1 instrument
+
1 benchmark
+
1 month
+
Daily
+
canonical rows
+
shared analytics
```

The Bloomberg-specific work must stop at the provider boundary.

# Part 2 - Understand the identifier mapping

The common MarketPulse pair remains:

```text
Instrument canonical ticker : AAPL
Benchmark canonical ticker  : SP500
```

Provider identifiers:

```text
AAPL
  |
  +-- Yahoo      : AAPL
  +-- Bloomberg  : AAPL US Equity

SP500
  |
  +-- Yahoo      : ^GSPC
  +-- Bloomberg  : SPX Index
```

The analytical layer should continue to receive:

```text
AAPL
SP500
```

not provider-specific identifiers.

# Part 3 - Create the TD09 documentation branch

Use the established Git workflow:

```bash
git switch main
git pull
git status
git switch -c docs/bloomberg-mapping
```

TD09's main contribution is documentation.

Do not start implementing `bloomberg_provider.py` yet.

# Part 4 - Record the access mode first

Create:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

Start the document with:

```markdown
# Bloomberg Field Mapping

## Access mode

LIVE
```

or:

```markdown
# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE
```

Do not leave the mode ambiguous.

## If LIVE

Also record:

```text
actual classroom access method
actual identifiers used
actual observed response structure
```

## If APPROVED_SAMPLE

Record:

```text
Source:
data/sample/bloomberg_reference_sample.json

Reference:
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md

Live connectivity:
not demonstrated
```

# Part 5 - Inspect the instrument input

Use:

```text
AAPL US Equity
```

## LIVE mode

Use only the instructor-approved access mechanism.

Inspect the returned response and record:

```text
identifier
date representation
available fields
data structure
missing values if any
```

Do not guess missing field names.

## APPROVED_SAMPLE mode

Inspect:

```text
data/sample/bloomberg_reference_sample.json
```

Find the series with:

```text
provider_identifier = AAPL US Equity
canonical_ticker    = AAPL
```

The fallback keys are:

```text
observation_date
open_value
high_value
low_value
close_value
volume_value
```

These are teaching wrapper keys.

Do not call them Bloomberg field mnemonics.

# Part 6 - Inspect the benchmark input

Repeat the same process for:

```text
SPX Index
```

The canonical benchmark must remain:

```text
SP500
```

In APPROVED_SAMPLE mode, verify:

```text
provider_identifier = SPX Index
canonical_ticker    = SP500
```

The important distinction is:

```text
provider identifier
!=
canonical ticker
```

# Part 7 - Map input fields to the canonical model

MarketPulse expects:

```text
date
ticker
open
high
low
close
volume
```

Create a mapping table in:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

Use this structure:

```markdown
## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | ... | ... |
| ticker | application mapping | AAPL or SP500 |
| open | ... | ... |
| high | ... | ... |
| low | ... | ... |
| close | ... | ... |
| volume | ... | ... |
```

### LIVE mode rule

Use only field names actually observed in the instructor-approved environment.

If a field is unavailable:

```text
record unavailable
```

Do not invent a name.

### APPROVED_SAMPLE mode rule

Use the teaching wrapper mapping defined in:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
```

For example:

```text
observation_date -> date
close_value      -> close
```

Also state explicitly:

```text
teaching wrapper key
!=
Bloomberg LIVE field mnemonic
```

# Part 8 - Preserve canonical tickers

The target canonical rows must use:

```text
AAPL
SP500
```

Conceptually:

```python
{
    "date": "...",
    "ticker": "SP500",
    "open": ...,
    "high": ...,
    "low": ...,
    "close": ...,
    "volume": ...,
}
```

TD09 does not implement this normalization yet.

It documents enough information for TD10 to implement it correctly.

# Part 9 - Add observations for TD10

The mapping document should include a short TD10 handoff section:

```markdown
## TD10 handoff

- Access mode:
- Instrument identifier:
- Benchmark identifier:
- Date representation:
- Input structure:
- Missing fields:
- Special normalization notes:
```

For APPROVED_SAMPLE mode, also include:

```text
Expected canonical reference:
data/sample/bloomberg_reference_expected.json
```

# Part 10 - Validate the mapping document

Before committing, verify:

```text
[ ] access mode is explicit
[ ] instrument mapping is documented
[ ] benchmark mapping is documented
[ ] field source is identifiable
[ ] canonical tickers remain AAPL and SP500
[ ] LIVE fields are observed rather than invented
[ ] APPROVED_SAMPLE wrapper keys are labelled as teaching keys
[ ] missing fields are documented honestly
[ ] no credential appears
[ ] TD10 handoff is present
```

# Part 11 - Standard Git handoff

Inspect:

```bash
git status
git diff
```

Stage:

```bash
git add docs/BLOOMBERG_FIELD_MAPPING.md
```

Commit:

```bash
git commit -m "docs: map Bloomberg stage to MarketPulse"
```

Push and open a Pull Request toward team `main`.

Suggested PR title:

```text
docs: map Bloomberg stage to MarketPulse
```

Reviewer checklist:

```text
[ ] access mode is honest
[ ] AAPL mapping is correct
[ ] SP500 mapping is correct
[ ] field mapping is traceable to observed LIVE data or approved sample
[ ] no invented LIVE field name
[ ] no credential
[ ] TD10 handoff is usable
```

Merge after review.

# Checkpoint relation

Checkpoint C is performed after TD12.

TD09 prepares the final provider integration but does not require a Checkpoint C screenshot yet.

A sample-based TD09 session must not be presented later as proof of LIVE Bloomberg connectivity.

The canonical evidence contract remains:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied.

## Optional 1 - Extended LIVE exploration

If LIVE mode is stable and instructor time allows, inspect additional returned metadata or a slightly wider historical sample.

Do not expand the required mapping contract.

## Optional 2 - Additional identifiers

Inspect another instructor-approved Bloomberg identifier.

Do not change the common CORE pair.

## Optional 3 - Compare provider identifiers

Build a small comparison table:

```text
Canonical
CSV
Yahoo
Bloomberg
```

for AAPL and SP500.

## Optional 4 - Draw the provider boundary

Draw:

```text
Bloomberg-stage input
        |
        v
TD10 provider normalization
        |
        v
canonical rows
        |
        v
analytics.py
```

Explain where provider-specific identifiers disappear.

# ADVANCED

No `READY_TO_TEACH` advanced activity is attached directly to TD09 at this time.

The Bloomberg reference-data path is intentionally not active here because its prerequisites include:

```text
TD09-TD10 CORE complete
+
validated Bloomberg LIVE environment
```

Instructor deep dives may be used during TD09, but they are not student deliverables.

# TROUBLESHOOTING

## LIVE Bloomberg access unavailable

Switch to APPROVED_SAMPLE only with instructor approval.

Use:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
data/sample/bloomberg_reference_sample.json
```

Document:

```text
Access mode: APPROVED_SAMPLE
Live connectivity: not demonstrated
```

## LIVE fields differ from expectation

Record what is actually returned.

Do not modify the observed names to match an assumption.

## APPROVED_SAMPLE wrapper keys look unfamiliar

That is expected.

They are teaching wrapper keys designed for the fallback fixture.

Use the instructor reference mapping.

Do not call them Bloomberg mnemonics.

## Identifier not recognized in LIVE mode

Verify with the instructor.

Do not try random identifiers until one works.

## Sensitive information appears

Do not commit it.

Remove it from the document or screenshot and notify the instructor if it has already entered Git history.

# Final readiness check

Each student should be able to explain:

```text
[ ] Bloomberg role in MarketPulse
[ ] LIVE vs APPROVED_SAMPLE
[ ] canonical ticker vs provider identifier
[ ] AAPL vs AAPL US Equity
[ ] SP500 vs SPX Index
[ ] observed LIVE field vs teaching wrapper key
[ ] why unverified fields must not be invented
[ ] why analytics.py remains provider-neutral
[ ] what TD10 must implement from the mapping
```

The team should confirm:

```text
[ ] docs/BLOOMBERG_FIELD_MAPPING.md exists
[ ] access mode is explicit
[ ] mapping was reviewed
[ ] no credentials were committed
[ ] TD10 handoff is complete
```

# What comes next?

TD09 ends with a mapping contract.

TD10 turns that contract into:

```text
src/providers/bloomberg_provider.py
```

The intended transition is:

```text
TD09
identifier + field mapping
        |
        v
TD10
provider normalization
        |
        v
canonical rows
        |
        v
existing analytics.py
```
