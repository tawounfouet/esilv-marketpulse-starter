# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Source:
data/sample/bloomberg_reference_sample.json

Reference:
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md

Live connectivity:
not demonstrated

The sample declares itself as `"access_mode": "approved_sample"` and
`"is_live_bloomberg_output": false`. Its values are illustrative teaching values
reused from `data/sample/prices.csv`, not certified Bloomberg historical observations.

This document must not be presented as proof of LIVE Bloomberg connectivity.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

Both pairs were verified in the sample (`canonical_ticker` / `provider_identifier`
at series level).

provider identifier != canonical ticker

The analytical layer must only receive `AAPL` and `SP500`.

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | Teaching wrapper key. ISO 8601 string `YYYY-MM-DD` |
| ticker | application mapping from series-level `canonical_ticker` | Not present in observations. Must be `AAPL` or `SP500`, never `provider_identifier` |
| open | `open_value` | Teaching wrapper key. Numeric |
| high | `high_value` | Teaching wrapper key. Numeric |
| low | `low_value` | Teaching wrapper key. Numeric |
| close | `close_value` | Teaching wrapper key. Numeric |
| volume | `volume_value` | Teaching wrapper key. Integer. Always `0` for SPX Index |

**Important:**

teaching wrapper key
!=
Bloomberg LIVE field mnemonic

`observation_date`, `open_value`, `high_value`, `low_value`, `close_value` and
`volume_value` are teaching keys defined for the fallback fixture. No LIVE
Bloomberg field name was observed or is claimed in this document.

## TD10 handoff

- Access mode: APPROVED_SAMPLE (live connectivity not demonstrated)
- Instrument identifier: `AAPL US Equity` -> canonical `AAPL`
- Benchmark identifier: `SPX Index` -> canonical `SP500`
- Date representation: ISO 8601 string `YYYY-MM-DD`, daily trading days only
  (2026-09-01 to 2026-09-30, 21 observations per series; weekends and
  2026-09-07, US Labor Day, are absent)
- Input structure: top-level object with metadata keys and a `series` list
  (2 elements). Each series has `role`, `canonical_ticker`,
  `provider_identifier` and an `observations` list. Each observation has
  `observation_date`, `open_value`, `high_value`, `low_value`, `close_value`,
  `volume_value`
- Missing fields: none, no `null` values and no absent keys in either series
- Special normalization notes:
  - `ticker` must be injected from series-level `canonical_ticker` into every
    canonical row
  - `provider_identifier` must not reach the analytical layer
  - `volume_value = 0` for SPX Index is a real value (an index has no traded
    volume), not missing data; keep it as `0`
  - Instrument and benchmark share the same dates, so `align_series()` should
    keep all 21 dates
- Expected canonical reference:
  data/sample/bloomberg_reference_expected.json
  - Expected output shape: a single flat `rows` list of 42 canonical rows
  (21 AAPL rows followed by 21 SP500 rows), each with exactly
  `date`, `ticker`, `open`, `high`, `low`, `close`, `volume`.
  Values are copied unchanged from the sample; only keys are renamed and
  `ticker` is injected from `canonical_ticker`.