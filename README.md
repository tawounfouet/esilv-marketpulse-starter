# ESILV MarketPulse

<p align="center">
  <img
    src="https://www.itii-pdl.com/wp-content/uploads/2024/11/logo_esilv_couleur.jpg?ver=1733410620"
    alt="ESILV - De Vinci Higher Education"
    width="100"
  />
</p>

[![Course: MESIFI472326](https://img.shields.io/badge/course-MESIFI472326-1f6feb.svg)](docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md)
[![ESILV A4](https://img.shields.io/badge/ESILV-A4-111827.svg)](docs/00_MARKETPULSE_FUNCTIONAL_CONTRACT.md)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg)](https://www.python.org/)
[![Labs](https://img.shields.io/badge/labs-12-2ea44f.svg)](docs/labs/README.md)
[![TD](https://img.shields.io/badge/TD-18h-orange.svg)](docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md)
[![Status](https://img.shields.io/badge/status-baseline%20ready-success.svg)](docs/16_TEACHING_BASELINE_RELEASE.md)

**MarketPulse** is the progressive teaching project for the **ESILV A4 - Python, Git, Linux** module.

> Acquire market data from several provider stages, normalize it to one canonical contract, compare one instrument with its benchmark, then expose the same application result through the terminal and a Dash dashboard.

### ⚡ Languages and Tools

<p align="center">
  <a href="https://www.python.org/" target="_blank" rel="noreferrer" title="Python">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  </a>
  <a href="https://git-scm.com/" target="_blank" rel="noreferrer" title="Git">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="git" width="40" height="40"/>
  </a>
  <a href="https://github.com/" target="_blank" rel="noreferrer" title="GitHub">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" alt="github" width="40" height="40"/>
  </a>
  <a href="https://www.kernel.org/" target="_blank" rel="noreferrer" title="Linux">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/>
  </a>
  <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer" title="Bash">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bash/bash-original.svg" alt="bash" width="40" height="40"/>
  </a>
  <a href="https://finance.yahoo.com/" target="_blank" rel="noreferrer" title="Yahoo Finance / yfinance">
    <img src="https://logos-world.net/wp-content/uploads/2020/10/Yahoo-Emblem.png" alt="yahoo" width="40" height="40"/>
  </a>
  <a href="https://dash.plotly.com/" target="_blank" rel="noreferrer" title="Dash">
    <img src="https://img.shields.io/badge/Dash-008DE5?logo=plotly&amp;logoColor=white" alt="dash" height="40"/>
  </a>
  <a href="https://plotly.com/python/" target="_blank" rel="noreferrer" title="Plotly">
    <img src="https://cdn.simpleicons.org/plotly/3F4F75" alt="plotly" width="40" height="40"/>
  </a>
  <a href="https://www.bloomberg.com/professional/" target="_blank" rel="noreferrer" title="Bloomberg">
    <img src="https://img.shields.io/badge/Bloomberg-000000?logo=bloomberg&amp;logoColor=white" alt="bloomberg" height="40"/>
  </a>
</p>

## What students build

MarketPulse starts deliberately small and evolves across 12 practical labs.

The common business model is:

```text
1 Instrument
+
1 Benchmark
+
1 Provider
+
1 Historical Window
+
1 Interval
+
Performance Comparison
```

CORE defaults:

```text
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Lookback   : 1 month
Interval   : Daily
```

The provider progression is:

```text
CSV / JSON
    |
    v
Yahoo Finance
    |
    v
Bloomberg stage
    |
    v
Canonical Market Data
    |
    v
Shared Analytics
    |
    v
Application Snapshot
    |
    +----------------+
    |                |
    v                v
Terminal            Dash
```

## Core analytical contract

The required financial concepts stay intentionally small:

```text
period return
+
base-100 normalization
+
relative performance
```

Daily returns, volume analysis and richer quantitative indicators are optional extensions.

The central business question is:

> Is the selected instrument outperforming or underperforming its benchmark over the same period and frequency?

See [the functional contract](docs/00_MARKETPULSE_FUNCTIONAL_CONTRACT.md).

## Application architecture

The frozen 18-hour CORE Python structure is:

```text
src/
├── main.py
├── analytics.py
├── dashboard.py
└── providers/
    ├── __init__.py
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

Responsibilities:

```text
providers/
=
provider-specific acquisition
+
normalization to canonical rows

analytics.py
=
alignment
+
period return
+
base 100
+
relative performance

main.py
=
application orchestration
+
build_market_snapshot(...)
+
terminal presentation

dashboard.py
=
Dash presentation
+
snapshot consumption
```

The application result shared by terminal and Dash is defined in [the snapshot contract](docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md).

The design principle is:

```text
Acquire once
normalize once
calculate once
present many times
```

## Canonical runtime

Terminal:

```bash
python src/main.py
```

Dashboard, introduced in TD11:

```bash
python src/dashboard.py
```

These are the two canonical CORE runtime commands.

The instructor starter repository does not necessarily contain every later-stage student file on day one. Files appear progressively during the lab sequence.

## Installation

The starter TD01-TD02 path uses only the Python standard library.

Later labs add direct dependencies as required.

When `requirements.txt` contains the dependencies for the current stage:

```bash
python -m pip install -r requirements.txt
```

Typical later-stage dependencies include:

```text
yfinance
dash
plotly
```

The complete dependency model, including standard-library modules, transitive dependencies, Bloomberg environment rules and explicit CORE exclusions, is documented in:

[MarketPulse libraries and dependencies](docs/13_MARKETPULSE_LIBRARIES_AND_DEPENDENCIES.md)

Do not add packages that are not actually required by the implementation.

## Bloomberg teaching modes

The Bloomberg stage supports two authorized classroom modes:

```text
LIVE
or
APPROVED_SAMPLE
```

`LIVE` means the instructor-approved Bloomberg environment successfully returned data.

`APPROVED_SAMPLE` means the instructor fallback assets were used for mapping and normalization work.

Important:

```text
APPROVED_SAMPLE
!=
LIVE Bloomberg evidence
```

Instructor reference:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
```

## Student Git workflow

The collaboration model is:

```text
one team
=
one shared fork
```

Team repository naming:

```text
<owner>/esilv-marketpulse-gXX-tYY
```

Typical contribution flow:

```text
feature branch
      |
      v
commit
      |
      v
push
      |
      v
Pull Request
      |
      v
review
      |
      v
merge
```

Start with:

- [Student onboarding](docs/01_STUDENT_ONBOARDING.md)
- [Git team workflow](docs/03_GITHUB_TEAM_WORKFLOW.md)
- [Contributing guide](CONTRIBUTING.md)

Canonical instructor repository:

```text
tawounfouet/esilv-marketpulse
```

## 18-hour learning path

The 12 TDs are organized into four pedagogical waves:

```text
WAVE 1 - Foundations - 3h
TD01 Bootstrap + Linux
TD02 Python + CSV / JSON

WAVE 2 - Git and Collaboration - 6h
TD03 Git Local Workflow
TD04 Branches + Merge
TD05 Remote Branch + Pull Request
TD06 Code Review

WAVE 3 - Comparison + Yahoo Finance - 3h
TD07 Data Normalization + Comparison
TD08 Yahoo Finance

WAVE 4 - Professional Integration - 6h
TD09 Bloomberg Introduction
TD10 Bloomberg Provider
TD11 Dash Dashboard
TD12 Integration + Release
```


## Assessment checkpoints

The checkpoint phases are different from the four pedagogical waves:

```text
Checkpoint A
TD01-TD04
Foundations
25% of the TD grade

Checkpoint B
TD05-TD08
Collaboration and Data
30% of the TD grade

Checkpoint C
TD09-TD12
Integration and Release
45% of the TD grade
```

The canonical evidence specification is:

[Checkpoint and evidence contract](docs/04_CHECKPOINTS_AND_EVIDENCE.md)

Screenshots complement Git history, execution and explanation. They do not replace them.

## Starter data

The repository includes illustrative educational sample data for:

```text
AAPL
SP500
```

The values are teaching data.

They are not certified historical market observations.

This keeps the first labs deterministic and inspectable before remote providers are introduced.

## Repository evolution

The repository intentionally does not expose the complete final architecture on day one.

```text
TD01-TD06
src/main.py

TD07
+ src/analytics.py

TD08
+ src/providers/yahoo_provider.py

TD09
+ docs/BLOOMBERG_FIELD_MAPPING.md

TD10
+ src/providers/bloomberg_provider.py

TD11
+ src/dashboard.py

TD12
release validation only
```

Target structure:

[Target repository structure](docs/05_TARGET_REPOSITORY_STRUCTURE.md)



## Security

Never commit:

```text
passwords
API keys
access tokens
SSH private keys
Bloomberg credentials
cloud credentials
billing information
session secrets
```

Do not copy another student's credentials.

Do not fabricate provider evidence when an external service is unavailable.


The common CORE still does not require:

```text
tests/
Dockerfile
GitHub Actions
Kubernetes
complex packaging
advanced CI/CD
advanced quantitative finance
```

Current active ADVANCED work is indexed from:

```text
docs/advanced/README.md
```

The lab-to-advanced availability map is maintained in:

```text
docs/labs/README.md
```

Instructor deep dives are indexed from:

```text
docs/instructor/deep-dives/README.md
```

Some advanced supports may exist with status:

```text
PENDING_EXTERNAL
```

Such supports are not activated as student exercises until their real delivery gate passes.

This README intentionally does not display CI, security, release or license badges because those contracts are not present in the CORE repository.


---

**Course:** MESIFI472326 - Python, Git, Linux  
**School:** ESILV - A4  
**Use case:** MarketPulse - Multi-Source Financial Market Data Dashboard
