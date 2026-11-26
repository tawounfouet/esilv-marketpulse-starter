# Checkpoint B

## Student

- Name: Arthur Vanlaeres
- GitHub: @arthurvlrs05-rgb

## Contribution

- Branch: `arthur-vanlaeres`
- Work: connected Yahoo Finance acquisition to the TD07 analytics in `src/main.py`.
- Reused Hamza Asadullah's analytics implementation from PR #5 and preserved the original authorship in the Git history.
- Reused Hugo Dussart's Yahoo Finance provider from PR #6 without rewriting it.
- Pull Request: https://github.com/hasaddd20/esilv-marketpulse-g06-t03/pull/7 (open, targeting `main`).
- Reviewed Pull Request: pending a meaningful review by the student.

## Work completed

MarketPulse retrieves AAPL and the S&P 500 from Yahoo Finance for the same one-month daily window, aligns observations by date, and calculates period returns, base-100 values, and relative performance through the shared analytics module.

## Validation

The application was run against Yahoo Finance. Both symbols returned 23 observations over 2026-10-26 to 2026-11-25. A separate live-data check confirmed numeric canonical fields, matching aligned dates, 100.00 starting base values, return/base-100 consistency, and instrument-minus-benchmark relative performance.

## Evidence status

The required screenshots are not included yet. GitHub and terminal screenshots must be captured from the real user session, and the code-review screenshot must show a meaningful review submitted by the student. No screenshot or provider result has been fabricated.
