# Checkpoints and Evidence

## Canonical status

This document is the single source of truth for MarketPulse checkpoint evidence.

It defines:

- checkpoint timing;
- required and optional filenames;
- screenshot meaning;
- individual evidence rules;
- live validation principles;
- assessment guidance;
- security rules.

Student-facing labs may repeat a short capture checklist for convenience, but they do not redefine the evidence contract.

If another repository document conflicts with this file, this file controls the checkpoint evidence requirements.

## 1. Purpose

The goal is not to grade every lab independently.

Student progress is validated through three structured checkpoints.

The evidence model combines:

```text
ARTEFACT
+
GIT TRACE
+
SCREENSHOTS
+
EXECUTION
+
EXPLANATION
```

Screenshots alone are never sufficient proof of understanding.

## 2. Global evidence rules

All students must use the same evidence naming convention.

Rules:

```text
format          : PNG
naming          : lowercase_snake_case
numbering       : 01_, 02_, 03_...
spaces          : forbidden
accents         : forbidden
free naming     : forbidden
```

Each student stores evidence under their own GitHub username.

Example:

```text
evidence/
└── checkpoint-b/
    └── alice-martin/
        ├── README.md
        ├── 01_pull_request.png
        ├── 02_code_review.png
        ├── 03_yahoo_market_data.png
        └── 04_instrument_benchmark.png
```

The exact screenshot filenames defined in this document are part of the submission contract.

### Evidence completion status

A checkpoint evidence package may temporarily be in one of these states:

```text
READY
=
all locally controllable evidence is present

PENDING_EXTERNAL
=
one required proof depends on a documented external service or platform condition that is currently unavailable

COMPLETE
=
all required evidence has been captured from real project state
```

`PENDING_EXTERNAL` is not a substitute for missing student work.

It may be used only when the blocked proof depends on an external condition such as:

```text
Yahoo service availability
GitHub platform availability
clean-environment package installation
authorized provider environment
```

A pending external proof must be completed during an instructor-approved recovery window before final grading.

Do not replace a pending proof with:

```text
fabricated output
old unrelated screenshot
local CSV presented as remote data
controlled test double presented as live provider evidence
```

## 3. Checkpoint A - Foundations

Recommended timing:

```text
after TD04
```

Suggested weight inside the TD grade:

```text
25%
```

### Skills validated

- access to the team repository;
- Linux navigation;
- Python starter execution;
- CSV / JSON inspection;
- basic Git workflow;
- commits;
- branches;
- simple merge.

### Required screenshots

Exactly these three screenshots are required:

```text
01_terminal_python.png
02_git_status_log.png
03_branch_merge.png
```

#### 01_terminal_python.png

The screenshot should show the student working from the project repository and include evidence such as:

```bash
pwd
ls
python src/main.py
```

It should demonstrate that the student can navigate the Linux environment and execute MarketPulse.

#### 02_git_status_log.png

The screenshot should show:

```bash
git status
git log --oneline
```

The objective is to verify repository state and visible Git history.

#### 03_branch_merge.png

The screenshot should show branch usage and visible merge evidence.

Capture this evidence after the TD04 merge succeeds and before deleting the merged feature branch.

Recommended commands:

```bash
git branch
git branch --merged
git log --oneline --graph --decorate --all
```

A fast-forward merge is valid.

In that case, the graph may remain linear. The evidence is still valid when the merged feature branch is visible and `git branch --merged` confirms that it is integrated into the current `main`.

Do not force a merge commit only to make the screenshot look more complex.

After the evidence is captured, the local merged feature branch may be deleted.

### Live micro-validation

The instructor may ask for a small modification such as:

```text
create a branch
change displayed information
show git diff
commit the change
run MarketPulse
```

## 4. Checkpoint B - Collaboration and Data

Recommended timing:

```text
after TD08
```

Suggested weight inside the TD grade:

```text
30%
```

### Skills validated

- feature branch;
- push;
- Pull Request;
- useful review;
- identifiable individual contribution;
- CSV / JSON data handling;
- instrument and benchmark handling;
- common data model;
- Yahoo Finance integration;
- correct handling of the common CORE pair AAPL + S&P 500;
- same lookback and interval for instrument and benchmark.

### Required screenshots

Exactly these four screenshots are required:

```text
01_pull_request.png
02_code_review.png
03_yahoo_market_data.png
04_instrument_benchmark.png
```

#### 01_pull_request.png

The screenshot should make visible:

- Pull Request title;
- author;
- source branch;
- target branch;
- relevant status.

The Pull Request must correspond to identifiable work by the student.

#### 02_code_review.png

The screenshot should show a meaningful review performed by the student on another team member's Pull Request.

A reaction alone is not sufficient.

#### 03_yahoo_market_data.png

The screenshot should show MarketPulse retrieving or displaying remote market data through the Yahoo Finance stage of the project.

The evidence should make the selected instrument or market pair understandable.

This file requires a real successful remote Yahoo retrieval.

If Yahoo is unavailable during the scheduled checkpoint:

```text
checkpoint B
=
PENDING_EXTERNAL
```

for this evidence item only.

The student should still submit and explain the other Checkpoint B evidence that is already available.

The missing Yahoo screenshot is then captured during an instructor-approved recovery window after a successful remote retrieval.

Do not substitute:

```text
local CSV output
controlled provider-double output
an old unrelated screenshot
fabricated remote values
```

for `03_yahoo_market_data.png`.

#### 04_instrument_benchmark.png

The screenshot should show that MarketPulse handles both:

```text
Instrument
+
Benchmark
```

over the same common contract:

```text
Lookback : 1 month
Interval : Daily
```

Example:

```text
AAPL
+
S&P 500
```

If the teaching instructions allow another pair, the screenshot should show the team's selected instrument and its coherent benchmark.

### Example oral questions

The instructor may ask:

- Where is Yahoo Finance called?
- What data is returned?
- Where is the benchmark handled?
- Why must instrument and benchmark use the same period and interval?
- Why should processing not depend directly on one provider?

Changing the selected ticker or market pair is not a mandatory Checkpoint B skill.

If the instructor wants an extension question, they may optionally ask whether the student can explain what would need to change for another coherent instrument and benchmark pair.

## 5. Checkpoint C - Integration and Release

Recommended timing:

```text
after TD12
```

Suggested weight inside the TD grade:

```text
45%
```

### Skills validated

- multi-source MarketPulse integration;
- Bloomberg data access when the teaching environment permits;
- instrument and benchmark comparison;
- period returns;
- relative performance;
- base-100 comparison;
- Dash interface;
- Git collaborative workflow;
- clear contribution history;
- reproducible project execution;
- ability to explain and modify the submitted work.

### Required screenshots

Exactly these four screenshots are required:

```text
01_final_market_data.png
02_dash_dashboard.png
03_final_pull_request.png
04_reproducible_run.png
```

One optional advanced screenshot may also be submitted:

```text
05_advanced_deployment.png
```

#### 01_final_market_data.png

The screenshot should show the final authorised market-data provider or provider mode in operation.

When Bloomberg LIVE access is available and selected, Bloomberg LIVE may be shown.

When the authorized final path is:

```text
Bloomberg stage - APPROVED_SAMPLE
```

that exact mode must remain visible.

APPROVED_SAMPLE is valid final provider-stage evidence when it is the authorized teaching fallback, but it is not evidence of LIVE Bloomberg connectivity.

The generic filename is intentional so that the teaching team can accept the actual authorized final provider or mode without manufacturing provider claims.

#### 02_dash_dashboard.png

The screenshot should show the final MarketPulse dashboard.

At minimum, the visible dashboard should make it possible to identify:

```text
Instrument
Benchmark
Lookback
Interval
Instrument return
Benchmark return
Relative performance
Base-100 comparison chart
```

The objective is to show a real comparative market view, not only that Dash starts successfully.

#### 03_final_pull_request.png

The screenshot should show a final or late-stage Pull Request from the TD09-TD12 stage that demonstrates the collaborative workflow:

```text
feature branch
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

The Pull Request must be attributable to the student whose evidence directory contains the screenshot.

It does not have to be the single team-level final integration or release Pull Request.

A team may legitimately have one final integration Pull Request authored by one integration lead. Other students may use another meaningful late-stage Pull Request from TD09, TD10, TD11 or TD12, provided that it demonstrates their own identifiable contribution.

Do not create artificial duplicate final Pull Requests only to satisfy the screenshot requirement.

#### 04_reproducible_run.png

The screenshot should demonstrate that MarketPulse can be started from a clean or freshly prepared environment by following the repository documentation.

For the frozen CORE, the evidence should make the clean-run sequence understandable, including the relevant commands:

```bash
git clone ...
cd esilv-marketpulse-gXX-tYY
python -m pip install -r requirements.txt
python src/main.py
python src/dashboard.py
```

The screenshot does not need to fit every command on one terminal screen, but the submitted evidence and checkpoint README together must identify the clean environment and the successful final runtime path.

If the package index, GitHub, or another required external dependency is unavailable during the scheduled capture, this evidence item may be marked:

```text
PENDING_EXTERNAL
```

and completed during an instructor-approved recovery window.

A failed dependency installation must not be presented as a successful reproducible run.

A proprietary LIVE provider does not have to work outside its authorized environment. The reproducibility evidence may use the documented authorized fallback mode when that is the supported clean-run path.

#### 05_advanced_deployment.png

Status:

```text
OPTIONAL
```

This screenshot may demonstrate an optional advanced extension such as:

- SSH;
- remote Linux execution;
- VPS deployment;
- systemd;
- Docker;
- GitHub Actions.

It is not required for the common core and must not penalise students who do not complete the advanced track.

### ADVANCED assessment isolation

Repository taxonomy:

```text
CORE
OPTIONAL
ADVANCED
INSTRUCTOR
```

Checkpoint rule:

```text
ADVANCED work is never required
for Checkpoint A, B or C.
```

A student who completes the required CORE evidence must not lose common checkpoint credit because they did not complete an ADVANCED activity.

A `PENDING_EXTERNAL` advanced support is not available evidence until its delivery gate has passed.

Instructor-only material is never student evidence.

### Suggested final validation

A short technical demonstration may include:

```text
5 to 8 minutes per team
+
targeted individual questions
```

## 6. Official evidence matrix

| Checkpoint | Filename | Status |
|---|---|---|
| A | `01_terminal_python.png` | Required |
| A | `02_git_status_log.png` | Required |
| A | `03_branch_merge.png` | Required |
| B | `01_pull_request.png` | Required |
| B | `02_code_review.png` | Required |
| B | `03_yahoo_market_data.png` | Required |
| B | `04_instrument_benchmark.png` | Required |
| C | `01_final_market_data.png` | Required |
| C | `02_dash_dashboard.png` | Required |
| C | `03_final_pull_request.png` | Required |
| C | `04_reproducible_run.png` | Required |
| C | `05_advanced_deployment.png` | Optional |

Do not rename these files.

## 7. Evidence directory

Use:

```text
evidence/
|
+-- checkpoint-a/
|   +-- github-user-a/
|   +-- github-user-b/
|   +-- github-user-c/
|
+-- checkpoint-b/
|   +-- github-user-a/
|   +-- github-user-b/
|   +-- github-user-c/
|
+-- checkpoint-c/
    +-- github-user-a/
    +-- github-user-b/
    +-- github-user-c/
```

The individual directory name must match the student's GitHub username.

## 8. Individual checkpoint README

Each student checkpoint directory must also contain:

```text
README.md
```

Example:

```markdown
# Checkpoint B

## Student

- Name: Alice Martin
- GitHub: @alice-martin

## Contribution

- Branch: feature/yahoo-provider
- Main commits:
  - abc123
  - def456
- Pull Request: #18
- Reviewed Pull Request: #19

## Work completed

Implemented the Yahoo Finance provider and connected
the instrument and benchmark market data.

## Main difficulty

Handling missing observations between two market series.

## Evidence

- 01_pull_request.png
- 02_code_review.png
- 03_yahoo_market_data.png
- 04_instrument_benchmark.png
```

The filenames listed in the README must exactly match the files in the directory.

## 9. Individual evidence rule

Each student provides their own evidence.

A team should not copy the same personal-contribution screenshot into every student's directory when the screenshot is intended to prove individual work.

Shared application behaviour may naturally look similar across team members, but Git contribution evidence must remain attributable to the individual student.

For Checkpoint C, individual traceability does not mean that every student must author the same type of final release Pull Request.

The requirement is an attributable late-stage contribution, not an artificial duplication of team integration work.

## 10. Team vs individual validation

For collaborative tasks, a possible interpretation is:

```text
70% individual evidence and understanding
30% collective project result
```

The teaching team may adjust this weighting if needed.

## 11. Assessment dimensions

An indicative rubric may consider:

| Dimension | Indicative share |
|---|---:|
| Technical functionality | 30% |
| Git workflow and contribution | 25% |
| Understanding and explanation | 20% |
| Autonomy | 10% |
| Code organisation and clarity | 10% |
| Collaboration and review | 5% |

These percentages are guidance for checkpoint evaluation and may be adapted by the teaching team.

## 12. AI-assisted work

The objective is not to detect whether a tool helped produce code.

Students remain responsible for submitted work.

They must be able to:

- explain it;
- run it;
- modify it;
- debug it;
- identify where their contribution fits.

A live modification is stronger evidence than authorship speculation.

## 13. Security

Screenshots and evidence must never expose:

- passwords;
- API keys;
- GitHub tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials;
- payment information.

Before committing a screenshot, inspect it carefully.

## 14. Important distinction

```text
Presence
!=
work
!=
competence
```

Validation is based on demonstrated work and understanding.
