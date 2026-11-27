# 📓 MarketPulse — Learning Notebooks & Interactive Prototypes (Jupyter)

Welcome to the `notebooks/` directory of **MarketPulse**.

These Jupyter notebooks serve as the **interactive laboratory and prototyping environment** for the project. They allow students to experiment with, test, and validate each financial and technical component before refactoring it into a clean, modular production script inside `src/`.

---

## 🔰 Individual Onboarding & Preparatory Labs (All Students / TD02)

Before beginning the collaborative Git feature branches, all students have access to two preparatory notebooks:

| Notebook | Focus & Topics | Role & Target |
|---|---|---|
| [`00_python_fundamentals.ipynb`](00_python_fundamentals.ipynb) | **Reference Course & Quantitative Toolbox** : Advanced collections (`list`, `dict`, `set`), list/dict comprehensions, date intersection, pure functions, `pathlib` robust resolution, CSV text trap, and Pandas-to-canonical contract conversion. | Transverse learning guide mobilised across all TDs (01 to 12) |
| [`00_td02_sandbox.ipynb`](00_td02_sandbox.ipynb) | **Interactive Sandbox for TD02** : Practical step-by-step loading of `instruments.json` and `prices.csv`, observation filtering, and prototyping helpers (`get_first_close`, `get_last_close`, `display_market_summary`). | Interactive testing sandbox before updating [`src/main.py`](../src/main.py) |

---

## 👥 Collaborative Team Workflow (4-Student Group)

In this course, each team works on a **shared GitHub fork** (`<team-owner>/esilv-marketpulse-gXX-tYY`).
To ensure individual contribution traceability (commits, Pull Requests, Code Reviews) and prevent Git merge conflicts, the team organizes into **two cross-review pairs**:

* **Pair A (Data & Core Logic)**: **Student 1** ⇄ **Student 2**
* **Pair B (UI & Integration)**: **Student 3** ⇄ **Student 4**

Each student acts as the author of at least one feature and the official reviewer for their partner's feature.

---

## 🗺️ Feature Roadmap & Mapping to `src/` Modules

| Feature | Git Branch | Author | Reviewer | Source Notebook | Target File | Milestone & Evidence |
|---|---|---|---|---|---|---|
| **Feature 1** | `feature/analytics` | **Student 1** | **Student 2** | [`01_analytics.ipynb`](01_analytics.ipynb) | [`src/analytics.py`](../src/analytics.py) | **Checkpoint B**: [`01_pull_request.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md) (St.1), [`02_code_review.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md) (St.2) |
| **Feature 2** | `feature/yahoo-provider` | **Student 3** | **Student 4** | [`02_yahoo_provider.ipynb`](02_yahoo_provider.ipynb) | [`src/providers/yahoo_provider.py`](../src/providers/yahoo_provider.py) | **Checkpoint B**: [`01_pull_request.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md) (St.3), [`02_code_review.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md) (St.4), [`03_yahoo_market_data.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md) |
| **Feature 3** | `feature/bloomberg-provider` | **Student 1** | **Student 2** | [`03_bloomberg_provider.ipynb`](03_bloomberg_provider.ipynb) | [`src/providers/bloomberg_provider.py`](../src/providers/bloomberg_provider.py) | **Checkpoint C**: [`01_final_market_data.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md), [`03_final_pull_request.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md) |
| **Feature 4** | `feature/market-snapshot-cli` | **Student 2** | **Student 1** | [`04_market_snapshot_main.ipynb`](04_market_snapshot_main.ipynb) | [`src/main.py`](../src/main.py) | **Checkpoint C**: [`03_final_pull_request.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md), [`04_reproducible_run.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md) |
| **Feature 5** | `feature/dash-dashboard` | **Student 3** | **Student 4** | [`05_dashboard.ipynb`](05_dashboard.ipynb) | [`src/dashboard.py`](../src/dashboard.py) | **Checkpoint C**: [`02_dash_dashboard.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md), [`03_final_pull_request.png`](../docs/04_CHECKPOINTS_AND_EVIDENCE.md) |

> 🚀 **Student 4 Capstone Mission (TD12)**: Leads the final `feature/release-and-evidence` branch to validate clean-environment reproducibility, lock dependencies in [`requirements.txt`](../requirements.txt), update [`README.md`](../README.md), and coordinate team evidence collection. Reviewer: Student 3.

---

## 🔄 Standard Git Integration Protocol for Each Feature

For each feature, follow these 6 steps in your Linux terminal:

```bash
# 1. Always synchronize your local main before starting new work
git switch main
git pull origin main

# 2. Create and switch to the dedicated feature branch
git switch -c feature/<feature-name>

# 3. Extract pure functions into the designated src/ file (see guide in each notebook)

# 4. Verify locally from the Linux terminal
python3 -c "import src..." # or python3 src/main.py

# 5. Stage, commit with a conventional message, and push
git add src/
git commit -m "feat(<scope>): explicit summary message"
git push -u origin feature/<feature-name>

# 6. Open a Pull Request on GitHub targeting 'main' and assign your partner as Reviewer
```

---

## 🏗️ Frozen CORE Target Architecture in `src/`

Upon completing the 12 practical labs, your `src/` directory must reflect the official frozen architecture:

```text
src/
├── main.py                    # CLI entry point and build_market_snapshot() orchestrator
├── analytics.py               # Pure quantitative calculations (Base 100, period return)
├── dashboard.py               # Interactive Plotly Dash dashboard with Dark Mode
└── providers/
    ├── __init__.py            # Python package initializer
    ├── yahoo_provider.py      # Yahoo Finance adapter via yfinance
    └── bloomberg_provider.py  # Bloomberg adapter (APPROVED_SAMPLE / LIVE modes)
```
