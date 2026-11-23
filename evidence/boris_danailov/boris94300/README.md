# Checkpoint A

## Student

- Name: Boris Danailov
- GitHub: @boris94300

## Contribution

- Branches: `boris-danailov`, `feature/display-observation-dates`
- Main commits:
  - f208b28 - refactor: reuse market summary display for instrument and benchmark
  - dfa728c - docs: complete TEAM.md for group G05 team T02
  - 999f9a6 - feat: display first and last observation dates

## Work completed

- TD02: added `get_first_close()` and `get_last_close()` with explicit
  `float` conversion, and one reusable `display_market_summary()` used for
  both AAPL and the S&P 500 benchmark (21 observations each).
- TD03: inspected the TD02 changes with `git status` / `git diff`, staged
  them deliberately and recorded them in two separate commits.
- TD04: created `feature/display-observation-dates`, added
  `get_first_date()` and `get_last_date()` to the summary, then merged the
  branch into `main` (fast-forward).

## Main difficulty

Keeping my branch aligned with the team's `origin/main`, which had moved
forward with other members' Pull Requests before my TD04 work.

## Evidence

- 01_terminal_python.png
- 02_git_status_log.png
- 03_branch_merge.png
