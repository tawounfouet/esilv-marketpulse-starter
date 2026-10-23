# 🗃️ MarketPulse — Data Catalog & Asset Registry

Welcome to the **Data Catalog** of the **MarketPulse** platform.

This directory houses the local datasets, reference fixtures, and schema contracts utilized across the 12 practical labs (TD01 to TD12) and 5 feature modules.

---

## 🏛️ Data Architecture & Governance Principles

1. **Provider-Agnostic Canonical Layer**:
   MarketPulse enforces a strict boundary between raw provider data formats and internal business calculations. Regardless of whether data originates from local CSV/JSON files, the remote Yahoo Finance API, or a Bloomberg Terminal, all inputs are parsed and normalized into a uniform **Canonical Observation Contract**.

2. **Reproducibility & Offline Determinism**:
   The fixtures in `data/sample/` provide deterministic offline datasets. This ensures that every student, continuous integration pipeline, or dry-run environment can execute tests, build market snapshots, and run the dashboard without requiring live external market API connectivity.

3. **Immutability of Seed Assets**:
   Files in `data/sample/` are considered immutable reference seeds. Runtime caching, temporary exports, or student test outputs must never overwrite these files.

---

## 📂 Directory Layout

```text
data/
└── sample/
    ├── instruments.json                 # Instrument and benchmark metadata
    ├── prices.csv                       # Historical daily OHLCV prices (AAPL & SP500)
    ├── bloomberg_reference_sample.json  # Instructor-approved Bloomberg API payload fixture
    └── bloomberg_reference_expected.json# Expected canonical transformation benchmark
```

---

## 📋 Catalog of Registered Datasets

### 1. `instruments.json` — Asset & Benchmark Metadata

* **Path**: [`data/sample/instruments.json`](sample/instruments.json)
* **Format**: JSON (`UTF-8`)
* **Role**: Defines the operational scope and configuration contract for MarketPulse (TD01, TD02, TD10, TD12).
* **Cardinality**: 2 business entities (`instrument` and `benchmark`).

#### Schema Definition:

| Entity | Attribute | Type | Description | Allowed / Example Values |
|---|---|---|---|---|
| `instrument` | `ticker` | `string` | Canonical application ticker of the primary asset | `"AAPL"` |
| `instrument` | `name` | `string` | Human-readable company or asset name | `"Apple Inc."` |
| `instrument` | `currency` | `string` | ISO 4217 three-letter currency code | `"USD"` |
| `instrument` | `market` | `string` | Exchange or primary listing market | `"NASDAQ"` |
| `benchmark` | `ticker` | `string` | Canonical application ticker of the reference index | `"SP500"` |
| `benchmark` | `name` | `string` | Full index title | `"S&P 500"` |
| `benchmark` | `currency` | `string` | ISO 4217 three-letter currency code | `"USD"` |
| `benchmark` | `market` | `string` | Geographical market scope | `"US"` |

#### Sample Record:
```json
{
  "instrument": {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "currency": "USD",
    "market": "NASDAQ"
  },
  "benchmark": {
    "ticker": "SP500",
    "name": "S&P 500",
    "currency": "USD",
    "market": "US"
  }
}
```

---

### 2. `prices.csv` — Historical Market Observations

* **Path**: [`data/sample/prices.csv`](sample/prices.csv)
* **Format**: Comma-Separated Values (CSV, header row, RFC 4180)
* **Role**: Primary time-series seed data used for bootstrapping MarketPulse (TD01 to TD07).
* **Temporal Window (Lookback)**: 1 month (`2026-09-01` to `2026-09-30`).
* **Frequency (Interval)**: Daily trading sessions.
* **Cardinality**: 42 rows (21 observations for `AAPL`, 21 observations for `SP500`).

#### Schema Definition:

| Column | Raw Type | Parsed Type | Constraint | Description |
|---|---|---|---|---|
| `date` | `string` | `string` | `YYYY-MM-DD` | Calendar date of the trading session |
| `ticker` | `string` | `string` | Canonical ticker | Instrument symbol (`AAPL` or `SP500`) |
| `open` | `string` | `float` | $\ge 0.0$ | Opening session price |
| `high` | `string` | `float` | $\ge \max(\text{open}, \text{low}, \text{close})$ | Highest traded price during session |
| `low` | `string` | `float` | $\le \min(\text{open}, \text{high}, \text{close})$ | Lowest traded price during session |
| `close` | `string` | `float` | $\ge 0.0$ | Official closing session price |
| `volume` | `string` | `int` | $\ge 0$ | Total traded share volume (0 for indices) |

> ⚠️ **Data Engineering Warning (Type Casting)**:
> In Python, `csv.DictReader` parses all values as text (`str`). Any mathematical calculation requires explicit numeric casting:
> ```python
> close_price = float(row["close"])
> trade_volume = int(row["volume"])
> ```

#### Sample Records:
```csv
date,ticker,open,high,low,close,volume
2026-09-01,AAPL,249.20,251.50,248.00,250.00,38000000
2026-09-01,SP500,6592.00,6615.00,6580.00,6600.00,0
2026-09-02,AAPL,250.80,252.80,249.60,251.30,39500000
2026-09-02,SP500,6607.00,6627.00,6595.00,6612.00,0
```

---

### 3. `bloomberg_reference_sample.json` — Approved Bloomberg Fixture

* **Path**: [`data/sample/bloomberg_reference_sample.json`](sample/bloomberg_reference_sample.json)
* **Format**: JSON (`UTF-8`)
* **Role**: Certified teaching fixture simulating raw Bloomberg Terminal output for TD10 (`src/providers/bloomberg_provider.py`).
* **Access Mode**: `APPROVED_SAMPLE` (allows students to develop and test Bloomberg adapter transformations without terminal hardware).
* **Provider Identifiers**:
  - `AAPL US Equity` $\rightarrow$ Canonical `AAPL`
  - `SPX Index` $\rightarrow$ Canonical `SP500`

#### Schema Definition:

```json
{
  "sample_kind": "instructor_approved_fallback_fixture",
  "provider_stage": "bloomberg",
  "access_mode": "approved_sample",
  "is_live_bloomberg_output": false,
  "series": [
    {
      "role": "instrument",
      "canonical_ticker": "AAPL",
      "provider_identifier": "AAPL US Equity",
      "observations": [
        {
          "observation_date": "YYYY-MM-DD",
          "open_value": float,
          "high_value": float,
          "low_value": float,
          "close_value": float,
          "volume_value": int
        }
      ]
    }
  ]
}
```

---

### 4. `bloomberg_reference_expected.json` — Validation Benchmark

* **Path**: [`data/sample/bloomberg_reference_expected.json`](sample/bloomberg_reference_expected.json)
* **Format**: JSON (`UTF-8`)
* **Role**: Golden regression target. Contains the exact expected canonical list of dictionaries that `fetch_bloomberg_prices()` must produce when parsing `bloomberg_reference_sample.json`.
* **Cardinality**: 42 canonical observation rows.

---

## 📐 The MarketPulse Canonical Data Contract

All provider adapters (`csv`, `yfinance`, `bloomberg`) must normalize raw feeds into this exact Python dictionary contract:

```python
{
    "date": "YYYY-MM-DD",  # str (ISO-8601 calendar date)
    "ticker": "AAPL",      # str (Canonical application ticker)
    "open": 249.20,        # float (Opening price)
    "high": 251.50,        # float (Session high)
    "low": 248.00,         # float (Session low)
    "close": 250.00,       # float (Official closing price)
    "volume": 38000000     # int (Traded volume or 0 for indices)
}
```

---

## 🔄 End-to-End Data Lineage

```mermaid
graph TD
    subgraph Data Sources
        CSV[prices.csv]
        JSON_META[instruments.json]
        BBG_SAMPLE[bloomberg_reference_sample.json]
        YF_API[Remote Yahoo Finance API]
        BBG_LIVE[Live Bloomberg Terminal]
    end

    subgraph Provider Adapters (src/providers/)
        CSV_LOADER[Local File Parser]
        YF_ADAPTER[yahoo_provider.py]
        BBG_ADAPTER[bloomberg_provider.py]
    end

    subgraph Canonical Normalization
        CANONICAL[Canonical Observation Dictionaries]
    end

    subgraph Analytical Engine (src/analytics.py)
        ALIGN[align_series: Date Intersection]
        BASE100[calculate_base_100: Base 100 Indexation]
        RETURNS[calculate_period_return: Total Return]
        ALPHA[calculate_relative_performance: Alpha Spread]
    end

    subgraph Presentation & Consumers
        CLI[src/main.py: Terminal Snapshot Report]
        DASH[src/dashboard.py: Plotly Dash Dark Mode]
    end

    CSV --> CSV_LOADER
    JSON_META --> CSV_LOADER
    BBG_SAMPLE --> BBG_ADAPTER
    BBG_LIVE --> BBG_ADAPTER
    YF_API --> YF_ADAPTER

    CSV_LOADER --> CANONICAL
    YF_ADAPTER --> CANONICAL
    BBG_ADAPTER --> CANONICAL

    CANONICAL --> ALIGN
    ALIGN --> BASE100
    ALIGN --> RETURNS
    ALIGN --> ALPHA

    BASE100 --> CLI
    RETURNS --> CLI
    ALPHA --> CLI

    BASE100 --> DASH
    RETURNS --> DASH
    ALPHA --> DASH
```

### ASCII Representation:

```text
DATA SOURCES
  ┌───────────────────────────────┐     ┌────────────────────────┐     ┌───────────────────────────────┐
  │         Local Files           │     │   Remote Yahoo Finance │     │      Bloomberg Terminal       │
  │ • prices.csv                  │     │ • yfinance API         │     │ • bloomberg_reference_sample  │
  │ • instruments.json            │     │                        │     │ • Live blpapi session         │
  └───────────────┬───────────────┘     └───────────┬────────────┘     └───────────────┬───────────────┘
                  │                                 │                                  │
                  ▼                                 ▼                                  ▼
PROVIDER ADAPTERS (src/providers/)
  ┌───────────────────────────────┐     ┌────────────────────────┐     ┌───────────────────────────────┐
  │       Local CSV/JSON          │     │   yahoo_provider.py    │     │     bloomberg_provider.py     │
  │      (csv.DictReader)         │     │ (fetch_yahoo_prices)   │     │ (fetch_bloomberg_prices)      │
  └───────────────┬───────────────┘     └───────────┬────────────┘     └───────────────┬───────────────┘
                  │                                 │                                  │
                  └─────────────────────────┬───────┴──────────────────────────────────┘
                                            ▼
CANONICAL NORMALIZATION
  ┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │                           Canonical Observation Row Dictionaries                                   │
  │          {"date": str, "ticker": str, "open": float, "high": float, "low": float,                  │
  │           "close": float, "volume": int}                                                           │
  └─────────────────────────────────────────┬──────────────────────────────────────────────────────────┘
                                            │
                                            ▼
ANALYTICAL ENGINE (src/analytics.py)
  ┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ 1. align_series()                  ──> Date intersection on common trading days                    │
  │ 2. calculate_period_return()       ──> Arithmetic period returns (Instrument & Benchmark)           │
  │ 3. calculate_base_100()            ──> Normalized performance indexation (Base 100)                │
  │ 4. calculate_relative_performance()──> Alpha spread in percentage points (pp)                      │
  └─────────────────────────────────────────┬──────────────────────────────────────────────────────────┘
                                            │
                                            ▼
PRESENTATION & CONSUMERS
  ┌─────────────────────────────────────────┴──────────────────────────────────────────────────────────┐
  │                                                                                                    │
  ▼                                                                                                    ▼
CLI APPLICATION (src/main.py)                                       WEB DASHBOARD (src/dashboard.py)
┌─────────────────────────────────────────┐                         ┌──────────────────────────────────┐
│ build_market_snapshot()                 │                         │ Plotly Dash Interactive UI       │
│ • Formatted terminal KPI tables         │                         │ • Theme Switcher (Dark / Light)  │
│ • Multi-series observations count       │                         │ • Real-time Base 100 Chart       │
│ • Initial and latest closing prices     │                         │ • Dynamic KPI Summary Cards      │
└─────────────────────────────────────────┘                         └──────────────────────────────────┘
```

---

## 🐍 Practical Ingestion Recipes

### 1. Robust File Loading with `pathlib`
```python
from pathlib import Path
import csv
import json

# Dynamically resolve data directory from anywhere in the repository
PROJECT_ROOT = Path.cwd() if (Path.cwd() / "data").exists() else Path.cwd().parent
DATA_DIR = PROJECT_ROOT / "data" / "sample"

def load_metadata():
    with open(DATA_DIR / "instruments.json", mode="r", encoding="utf-8") as file:
        return json.load(file)

def load_prices():
    with open(DATA_DIR / "prices.csv", mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))
```

### 2. Validating Numerical Integrity
```python
def validate_canonical_row(row):
    assert "date" in row, "Missing date"
    assert "ticker" in row, "Missing ticker"
    assert float(row["close"]) >= 0.0, "Close price must be non-negative"
    assert float(row["high"]) >= float(row["low"]), "High must be >= Low"
```
