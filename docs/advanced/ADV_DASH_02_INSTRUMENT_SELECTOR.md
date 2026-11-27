# ADV-DASH-02 - Instrument Selector

Status:

```text
PENDING_EXTERNAL
```

Mode:

```text
MINI_LAB
```

Estimated duration:

```text
30-45 minutes
```

## 1. Objective

Allow a user to select another supported instrument without duplicating provider or analytics logic in the Dash layer.

## 2. Prerequisites

```text
TD11 CORE complete
ADV-DASH-01 complete
Dash installed
application layer supports parameterized instrument selection
```

This activity is not required for Checkpoint C.

## 3. Architecture requirement

Required direction:

```text
dropdown
   |
   v
callback
   |
   v
parameterized application function
   |
   v
snapshot
   |
   v
figure / metrics
```

Forbidden direction:

```text
dropdown
-> if AAPL call Yahoo directly
-> if MSFT call another provider directly
-> recompute analytics in dashboard.py
```

## 4. Define supported choices

Example:

```python
SUPPORTED_INSTRUMENTS = [
    {"label": "Apple", "value": "AAPL"},
    {"label": "Microsoft", "value": "MSFT"},
]
```

The benchmark remains the course benchmark unless the application layer explicitly supports a coherent alternative.

## 5. Add the selector

```python
dcc.Dropdown(
    id="instrument-selector",
    options=SUPPORTED_INSTRUMENTS,
    value="AAPL",
    clearable=False,
)
```

## 6. Rebuild through the application boundary

Illustrative callback shape:

```python
@app.callback(
    Output("comparison-graph", "figure"),
    Input("instrument-selector", "value"),
)
def update_instrument(selected_ticker):
    snapshot = build_market_snapshot(
        instrument_ticker=selected_ticker,
        ...
    )

    return build_comparison_figure(snapshot)
```

The exact parameter names must match the actual team application.

Do not invent a second snapshot contract inside the dashboard.

## 7. Definition of done

```text
[ ] at least two supported instruments are selectable
[ ] callback uses application-layer parameters
[ ] benchmark remains coherent
[ ] provider-specific symbols stay inside providers
[ ] analytics remain in analytics.py
[ ] selected instrument is visible
[ ] figure updates successfully
```

## 8. Testing checklist

For each supported instrument:

```text
[ ] provider path succeeds
[ ] canonical ticker is correct
[ ] common dates exist
[ ] returns are coherent
[ ] base-100 chart starts at 100
[ ] no provider logic appears in dashboard.py
```

## 9. Cleanup

If multi-instrument support is experimental, keep it on a feature branch.

Do not merge hard-coded duplicated business paths into team main.

## 10. Qualification status

The architectural support is complete.

Real callback execution requires Dash and an application state that genuinely supports parameterized instruments.

This runner cannot prove that final student-stage environment.

Therefore:

```text
support design
=
COMPLETE

real instrument-selector execution
=
EXTERNAL VERIFY
```

Promotion to unconditional READY_TO_TEACH requires a real Dash validation after ADV-DASH-01.
