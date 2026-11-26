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
- Reviewed Pull Request: no submitted review by Arthur was found on the team's PRs. Arthur was requested to review PR #6, but GitHub shows no submitted review from Arthur. This evidence remains to be completed.

## Work completed

MarketPulse retrieves AAPL and the S&P 500 from Yahoo Finance for the same one-month daily window, aligns observations by date, and calculates period returns, base-100 values, and relative performance through the shared analytics module.

## Validation

The application was run twice in separate terminal sessions against live Yahoo Finance data. Both symbols returned 23 observations over 2026-10-26 to 2026-11-25, with last closes of 355.58 USD for AAPL and 7182.78 for SP500. The comparison displayed AAPL at +3.39%, SP500 at -6.43%, relative performance at +9.83 percentage points, and base-100 values of 100.00 to 103.39 for AAPL and 100.00 to 93.57 for SP500. A separate live-data check confirmed numeric canonical fields, matching aligned dates, 100.00 starting base values, return/base-100 consistency, and instrument-minus-benchmark relative performance.

## Evidence status

Evidence files:

- `01_pull_request.png`: real capture of the live GitHub PR #7 page. It shows the title, Open status, `arthur-vanlaeres` source branch, and `main` target branch.
- `02_code_review.png`: no submitted review by Arthur was found on PRs #1–#7. PR #6 had a review request for Arthur, but no review was submitted; this proof remains to be completed.
- `03_yahoo_market_data.png`: real terminal capture from the first live run, showing Yahoo Finance, AAPL and SP500 observations, date ranges, and last closes.
- `04_instrument_benchmark.png`: real terminal capture from the second live run, showing aligned dates, period returns, relative performance, and base-100 values.

No screenshot or provider result has been fabricated. No review comment or review was published for this evidence check.
