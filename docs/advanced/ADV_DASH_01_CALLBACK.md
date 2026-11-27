# ADV-DASH-01 - Dash Callback

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

Extend the static TD11 dashboard with one meaningful Dash callback while preserving the MarketPulse application boundary.

## 2. Prerequisites

```text
TD11 CORE complete
python src/dashboard.py works
Dash installed in the teaching environment
build_market_snapshot(...) is reusable
```

This activity is not required for Checkpoint C.

## 3. Architecture guardrail

Do not build:

```text
callback
-> provider-specific request
-> duplicate analytics
```

Use:

```text
callback
-> application function
-> snapshot
-> presentation
```

## 4. Add one interaction

A simple training interaction can refresh a text summary from a selected display mode.

Example UI:

```python
dcc.Dropdown(
    id="metric-view",
    options=[
        {"label": "Relative performance", "value": "relative"},
        {"label": "Instrument return", "value": "instrument"},
        {"label": "Benchmark return", "value": "benchmark"},
    ],
    value="relative",
)

html.Div(id="metric-output")
```

## 5. Add the callback

Example:

```python
from dash import Input, Output

@app.callback(
    Output("metric-output", "children"),
    Input("metric-view", "value"),
)
def render_metric(metric_view):
    snapshot = build_market_snapshot(...)

    values = {
        "relative": snapshot["relative_performance"],
        "instrument": snapshot["instrument_return"],
        "benchmark": snapshot["benchmark_return"],
    }

    return f"{metric_view}: {values[metric_view]:.2f}%"
```

The exact `build_market_snapshot(...)` arguments must match the team's current application contract.

## 6. Better variant

If the existing TD11 module already creates one snapshot at startup and the interaction only changes presentation, reuse that snapshot instead of reacquiring provider data.

Rule:

```text
presentation-only interaction
=
do not reacquire data unnecessarily
```

## 7. Definition of done

```text
[ ] one real Input exists
[ ] one real Output exists
[ ] callback changes visible content
[ ] callback contains no provider-specific function
[ ] callback contains no duplicated return/base-100 formula
[ ] TD11 static dashboard remains understandable
```

## 8. Testing checklist

Run:

```bash
python src/dashboard.py
```

Then verify in the browser:

```text
[ ] page loads
[ ] dropdown is visible
[ ] changing selection updates output
[ ] no callback exception appears
[ ] terminal business values and callback values remain consistent
```

## 9. Cleanup

If the advanced interaction is not intended to stay in the team project:

```text
restore the TD11 static version
or
keep the advanced work on a dedicated feature branch
```

Do not leave a broken callback on shared main.

## 10. Qualification status

The callback architecture and code contract are specified.

This runner does not have the Dash package installed.

Therefore:

```text
support design
=
COMPLETE

real Dash callback execution
=
EXTERNAL VERIFY
```

Promotion to unconditional READY_TO_TEACH requires a real Dash run in the teaching environment.
