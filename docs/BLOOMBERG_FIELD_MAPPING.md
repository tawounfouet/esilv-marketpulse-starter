# Bloomberg Field Mapping

## Access mode

**APPROVED_SAMPLE**

The repository documents `APPROVED_SAMPLE` as an authorized classroom mode. The inspected fixture identifies itself as an instructor-approved fallback fixture and sets `is_live_bloomberg_output` to `false`. No Bloomberg LIVE session or data was used. This mapping is not evidence of LIVE Bloomberg connectivity.

## Scope and provenance

This contract is based on the approved teaching fixture, its expected canonical result, and the canonical row contract in `data/README.md`:

- Input: `data/sample/bloomberg_reference_sample.json`
- Expected output: `data/sample/bloomberg_reference_expected.json`
- Canonical contract: `data/README.md`

The fixture provenance says its illustrative values were reused from `data/sample/prices.csv` and are not certified Bloomberg historical observations. Its field names are teaching wrapper keys, not Bloomberg field mnemonics.

**Repository note:** TD09 references `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md`, but that file is absent from the synchronized `main` branch and its available Git history. The mappings below are therefore traced directly to the two checked-in fixtures and `data/README.md`; they do not claim to reproduce any definition from the missing reference or any LIVE Bloomberg field.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier | Source |
|---|---|---|---|
| Instrument | `AAPL` | `AAPL US Equity` | `series[].canonical_ticker` and `series[].provider_identifier` in the sample fixture |
| Benchmark | `SP500` | `SPX Index` | `series[].canonical_ticker` and `series[].provider_identifier` in the sample fixture |

The Bloomberg identifier is provider-specific. The canonical ticker must remain `AAPL` or `SP500` when observations reach MarketPulse analytics.

## Inspected sample structure

The approved input contains two series, each with an `observations` array of daily records:

| Series | Canonical ticker | Provider identifier | Rows | Date range |
|---|---|---|---:|---|
| Instrument | `AAPL` | `AAPL US Equity` | 21 | 2026-09-01 to 2026-09-30 |
| Benchmark | `SP500` | `SPX Index` | 21 | 2026-09-01 to 2026-09-30 |

Both series use the same 21 unique sample dates. `observation_date` is an ISO calendar date string (`YYYY-MM-DD`). The records contain all six wrapper keys in the field mapping below; no key is absent and no observation value is `null`.

The four price values are JSON numbers. The AAPL fixture uses both integer and decimal JSON numbers; the SPX fixture uses integer JSON numbers. The canonical contract represents `open`, `high`, `low`, and `close` as floats, so TD10 should normalize these numeric values to `float`. `volume_value` is an integer in both series. In the sample, every SPX volume value is explicitly `0`; it is not a missing or `null` value. `data/README.md` defines canonical volume as an integer and allows `0` for indices.

## Field mapping

| MarketPulse field | APPROVED_SAMPLE source / mapping | Canonical type | Status / notes |
|---|---|---|---|
| `date` | `observation_date` | `str` (`YYYY-MM-DD`) | Teaching wrapper key; copy the ISO date string. |
| `ticker` | Application mapping from the series `canonical_ticker` metadata | `str` | Preserve `AAPL` for `AAPL US Equity` and `SP500` for `SPX Index`; do not use Bloomberg identifiers as tickers. |
| `open` | `open_value` | `float` | Teaching wrapper key; convert the JSON number to `float`. |
| `high` | `high_value` | `float` | Teaching wrapper key; convert the JSON number to `float`. |
| `low` | `low_value` | `float` | Teaching wrapper key; convert the JSON number to `float`. |
| `close` | `close_value` | `float` | Teaching wrapper key; convert the JSON number to `float`. |
| `volume` | `volume_value` | `int` | Teaching wrapper key; keep as integer. The SPX sample supplies explicit `0` values, consistent with the index convention in `data/README.md`. |

All source names above are wrapper keys from `APPROVED_SAMPLE`. No Bloomberg LIVE field mnemonic has been observed or inferred.

## Expected canonical reference

`data/sample/bloomberg_reference_expected.json` contains 42 canonical rows: 21 with ticker `AAPL` and 21 with ticker `SP500`. The sample transformation above matches those rows exactly, including dates, canonical tickers, numeric values, and integer volumes.

## TD10 handoff

- **Access mode:** `APPROVED_SAMPLE`
- **Instrument identifier:** `AAPL US Equity`; canonical ticker: `AAPL`
- **Benchmark identifier:** `SPX Index`; canonical ticker: `SP500`
- **Date representation:** ISO calendar date string, `YYYY-MM-DD`
- **Input structure:** top-level `series[]` metadata with per-series `observations[]`
- **Input fields:** `observation_date`, `open_value`, `high_value`, `low_value`, `close_value`, `volume_value`
- **Missing fields or values:** none in the inspected fixture; SPX `volume_value` is explicitly integer `0`
- **Normalization notes:** map wrapper keys to the canonical row names; convert OHLC JSON numbers to floats; retain volume as an integer; map provider identifiers to the canonical tickers before passing rows to analytics
- **Expected canonical reference:** `data/sample/bloomberg_reference_expected.json`
- **LIVE connectivity:** not demonstrated

The missing instructor reference file is a repository gap for reviewer follow-up. If LIVE access is introduced later, inspect the actual response and document only field names and missing-value behavior observed in that environment.
