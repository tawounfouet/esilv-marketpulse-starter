from pathlib import Path
import json

# Robust path resolution to the approved reference sample
CANDIDATE_PATHS = [
    Path("data/sample/bloomberg_reference_sample.json"),
    Path("../data/sample/bloomberg_reference_sample.json"),
    Path("../../data/sample/bloomberg_reference_sample.json"),
]


def get_reference_sample_path():
    for p in CANDIDATE_PATHS:
        if p.exists():
            return p
    return CANDIDATE_PATHS[0]


BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}

def load_bloomberg_reference_sample(path=None):
    """Load the approved sample JSON payload."""
    target_path = Path(path) if path else get_reference_sample_path()
    with open(target_path, encoding="utf-8") as file:
        return json.load(file)


def find_reference_series(payload, provider_identifier):
    """Find the series matching a specific Bloomberg identifier."""
    for series in payload.get("series", []):
        if series.get("provider_identifier") == provider_identifier:
            return series

    raise ValueError(
        f"Approved Bloomberg series not found for identifier: {provider_identifier}"
    )


def normalize_reference_series(series):
    """
    Normalize an approved reference series into canonical MarketPulse rows.
    
    Args:
        series (dict): Dictionary with 'canonical_ticker' and 'observations'.
        
    Returns:
        list: Canonical MarketPulse observations.
    """
    canonical_ticker = series["canonical_ticker"]
    rows = []

    for obs in series["observations"]:
        rows.append({
            "date": obs["observation_date"],
            "ticker": canonical_ticker,
            "open": float(obs["open_value"]),
            "high": float(obs["high_value"]),
            "low": float(obs["low_value"]),
            "close": float(obs["close_value"]),
            "volume": int(obs["volume_value"]),
        })

    return rows


def fetch_approved_sample_prices(provider_identifier, sample_path=None):
    """
    Extract and normalize prices for an identifier in APPROVED_SAMPLE mode.
    """
    payload = load_bloomberg_reference_sample(sample_path)
    series = find_reference_series(payload, provider_identifier)
    return normalize_reference_series(series)


def fetch_raw_bloomberg_history(identifier, start_date=None, end_date=None):
    """Hook for live dealing-room acquisition."""
    raise NotImplementedError(
        "Live Bloomberg connection requires the physical trading room terminal environment."
    )


def fetch_bloomberg_prices(ticker, mode="APPROVED_SAMPLE"):
    """
    Main entry point for Bloomberg prices acquisition.
    """
    if ticker not in BLOOMBERG_IDENTIFIERS:
        raise KeyError(f"Unknown canonical ticker for Bloomberg provider: {ticker}")
        
    provider_id = BLOOMBERG_IDENTIFIERS[ticker]

    if mode == "APPROVED_SAMPLE":
        return fetch_approved_sample_prices(provider_id)
    elif mode == "LIVE":
        _raw = fetch_raw_bloomberg_history(provider_id)
        raise NotImplementedError("Live mode not currently active.")
    else:
        raise ValueError(f"Unrecognized Bloomberg mode: {mode}")
