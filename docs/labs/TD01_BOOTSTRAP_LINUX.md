# TD01 - Bootstrap + Linux

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"We need a common environment before we can work on MarketPulse."
```

## Context

You are joining a trading desk.

During the module, your team will progressively build MarketPulse, a Python application that compares a financial instrument with its market benchmark.

The common starter uses:

```text
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Lookback   : 1 month
Interval   : Daily
Provider   : CSV
```

Today, the goal is not to modify the financial logic.

The goal is to make sure that every team can access, inspect and run the project from a Linux environment.

## Learning objectives

At the end of TD01, you should be able to:

- identify the MarketPulse project;
- access an identified team repository;
- use a Linux terminal;
- understand your current directory;
- list and inspect project files;
- verify Python and Git availability;
- execute the MarketPulse starter;
- identify the CSV and JSON input files.

## CORE definition of done

TD01 is complete when your team can confirm:

```text
[ ] one team repository exists
[ ] repository name follows esilv-marketpulse-gXX-tYY
[ ] TEAM.md is completed
[ ] all team members can access the repository
[ ] one working development environment is available
[ ] one working Linux terminal is available
[ ] Python is available
[ ] Git is available
[ ] MarketPulse runs with python src/main.py
[ ] CSV and JSON starter files were inspected
```

Optional exploration is not required to complete TD01.

## Before starting

Instructor repository:

```text
tawounfouet/esilv-marketpulse-starter
```

Team repository naming convention:

```text
esilv-marketpulse-gXX-tYY
```

Example:

```text
esilv-marketpulse-g03-t02
```

Recommended team size:

```text
3 to 4 students
```

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are kept as buffer for environment variation, questions and validation.

| Time | Activity |
|---|---|
| 00-08 min | MarketPulse context |
| 08-22 min | Team repository and collaborators |
| 22-32 min | TEAM.md |
| 32-42 min | Development environment and terminal |
| 42-58 min | Linux navigation |
| 58-68 min | Inspect CSV and JSON |
| 68-78 min | Verify Python/Git and run MarketPulse |
| 78-80 min | CORE definition of done |
| 80-90 min | Buffer, support and optional exploration |

## Environment timebox rule

Do not let one environment problem consume the session.

```text
Individual blocker for approximately 10 minutes
        |
        v
pair temporarily with a teammate
        |
        v
continue the TD
        |
        v
resolve the individual issue with instructor support
```

Do not install VirtualBox, WSL, Docker or another large local environment during the common TD unless the instructor explicitly asks you to.

# CORE

# Part 1 - Understand MarketPulse

## 1.1 Business question

MarketPulse progressively answers:

> How is a financial instrument performing compared with its market benchmark?

The project will later evolve through:

```text
CSV / JSON
    |
    v
Yahoo Finance
    |
    v
Bloomberg
    |
    v
Performance comparison
    |
    v
Dash
```

Do not implement these later stages today.

## 1.2 Identify the starter

The starter contains:

```text
esilv-marketpulse-starter/
├── README.md
├── TEAM_TEMPLATE.md
├── CONTRIBUTING.md
├── config/
├── data/
├── docs/
├── evidence/
└── src/
```

For TD01, focus on:

```text
README.md
TEAM_TEMPLATE.md
data/sample/instruments.json
data/sample/prices.csv
src/main.py
```

# Part 2 - Prepare the team repository

## 2.1 Form the team

Confirm:

```text
TD Group         : GXX
MarketPulse Team : TXX
```

Example:

```text
TD Group         : G03
MarketPulse Team : T02
```

## 2.2 Create one team fork

One team member creates the fork from:

```text
tawounfouet/esilv-marketpulse-starter
```

Only one team fork is required.

Do not create one fork per student.

## 2.3 Rename the fork

Use:

```text
esilv-marketpulse-gXX-tYY
```

Example:

```text
esilv-marketpulse-g03-t02
```

Do not add student names or initials to the repository name.

## 2.4 Add collaborators

The fork owner adds the other team members as collaborators.

Every student must confirm access using their own GitHub account.

# Part 3 - Create TEAM.md

Create:

```text
TEAM.md
```

from:

```text
TEAM_TEMPLATE.md
```

Complete at least:

- TD group;
- MarketPulse team number;
- GitHub username of each member (without publishing legal names);
- GitHub username of each member;
- team repository name.

Do not add:

- student identification numbers;
- personal email addresses;
- phone numbers;
- passwords;
- tokens.

Every team member should be able to answer:

```text
What is our TD group?
What is our MarketPulse team?
What is our repository name?
Who are the repository collaborators?
```

# Part 4 - Open the common development environment

Use the development environment indicated by the instructor.

For the common course path, GitHub Codespaces may be used to provide:

```text
Linux terminal
+
Python
+
Git
+
repository workspace
```

Codespaces is a means to obtain a common environment.

It is not a separate competency being assessed in TD01.

Open a terminal before continuing.

# Part 5 - Linux navigation

## 5.1 Identify the current directory

Run:

```bash
pwd
```

The displayed path tells you where the shell is currently working.

## 5.2 List repository files

Run:

```bash
ls
ls -la
```

Identify at least:

```text
README.md
config
data
docs
evidence
src
```

## 5.3 Navigate to the sample data

Run:

```bash
cd data
pwd
ls

cd sample
pwd
ls
```

You should find:

```text
instruments.json
prices.csv
```

Return to the repository root:

```bash
cd ../..
pwd
```

# Part 6 - Inspect the starter data

## 6.1 JSON metadata

Run:

```bash
cat data/sample/instruments.json
```

Identify:

```text
instrument
benchmark
ticker
name
currency
market
```

You should be able to answer:

1. What is the instrument?
2. What is the benchmark?
3. Where are their names and tickers stored?

## 6.2 CSV observations

Run:

```bash
head data/sample/prices.csv
```

Identify:

```text
date
ticker
open
high
low
close
volume
```

Search for both series:

```bash
grep AAPL data/sample/prices.csv
grep SP500 data/sample/prices.csv
```

You should understand that the CSV contains observations for both the instrument and the benchmark.

# Part 7 - Verify the runtime

## 7.1 Check Python

Run:

```bash
python --version
```

If the instructor-provided environment uses a different command, follow the instructor instruction.

## 7.2 Check Git

Run:

```bash
git --version
```

Formal Git workflow begins later.

Do not create branches or commits in TD01 unless the instructor asks you to.

## 7.3 Run MarketPulse

From the repository root:

```bash
python src/main.py
```

Expected output:

```text
=== MarketPulse ===

Instrument
AAPL - Apple Inc.
Last price: 266.20 USD

Benchmark
SP500 - S&P 500
Last level: 6742.00

Period: 1 month
Interval: Daily

Observations
AAPL: 21
SP500: 21
```

Be able to identify:

```text
program          : src/main.py
market metadata  : data/sample/instruments.json
daily prices     : data/sample/prices.csv
instrument       : AAPL
benchmark        : SP500 / S&P 500
```

# Part 8 - CORE validation

Before finishing the required work, each student should confirm:

```text
[ ] I can access the team repository
[ ] I know the team repository name
[ ] I can open the common development environment
[ ] I can use pwd
[ ] I can use ls
[ ] I can use cd
[ ] I can use cat
[ ] I can use head
[ ] I can use grep
[ ] I can identify the JSON metadata file
[ ] I can identify the CSV price file
[ ] I can check the Python version
[ ] I can check the Git version
[ ] I can run python src/main.py
[ ] I can identify instrument and benchmark
```

The team should confirm:

```text
[ ] TEAM.md is completed
[ ] all members have repository access
[ ] repository naming is correct
```

If all checks pass, TD01 CORE is complete.

# OPTIONAL

Complete these tasks only after the CORE definition of done is satisfied.

## Optional 1 - Count observations

Run:

```bash
grep -c AAPL data/sample/prices.csv
grep -c SP500 data/sample/prices.csv
```

Expected result:

```text
21
21
```

Question:

> Why is having two aligned series useful for future comparison work?

## Optional 2 - Explore Linux output

Try:

```bash
ls -lh
head -n 5 data/sample/prices.csv
tail -n 5 data/sample/prices.csv
```

Explain what changes between these commands.

## Optional 3 - Count and search repository files

Try:

```bash
find . -type f
grep -R "AAPL" .
```

Do not spend time interpreting every result.

The goal is only to discover that Linux commands can inspect an entire project tree.

## Optional 4 - Inspect Git without changing anything

Try:

```bash
git status
git log --oneline
```

Do not create branches or commits.

Formal Git work starts in TD03.

# ADVANCED

Complete advanced work only after TD01 CORE is complete.

Advanced work is not required for Checkpoint A.

## ADV-LNX-01 - File Operations

Status:

```text
READY_TO_TEACH
```

Prerequisites:

```text
TD01 CORE complete
comfortable with pwd / ls / cd
```

Estimated duration:

```text
30 minutes
```

Support:

[ADV-LNX-01 - File Operations](../advanced/ADV_LNX_01_FILE_OPERATIONS.md)

## ADV-LNX-02 - Permissions and chmod

Status:

```text
READY_TO_TEACH
```

Prerequisites:

```text
TD01 CORE complete
basic file operations
```

Estimated duration:

```text
30-45 minutes
```

Support:

[ADV-LNX-02 - Permissions and chmod](../advanced/ADV_LNX_02_PERMISSIONS_CHMOD.md)

## ADV-LNX-03 - Pipes and Text Processing

Status:

```text
READY_TO_TEACH
```

Prerequisites:

```text
TD01 CORE complete
local MarketPulse files available
```

Estimated duration:

```text
60-90 minutes
```

Support:

[ADV-LNX-03 - Pipes and Text Processing](../advanced/ADV_LNX_03_PIPES_TEXT_PROCESSING.md)

# TROUBLESHOOTING

## Python command not found

Ask the instructor which Python command is expected in the common environment.

Do not spend the session installing a different Python distribution.

## Repository not accessible

Check:

- that you are signed into the expected GitHub account;
- that the fork owner added you as collaborator;
- that you accepted the collaboration invitation.

## Codespace or environment issue

Apply the timebox rule:

```text
approximately 10 minutes blocked
        |
        v
pair with a teammate
        |
        v
continue learning
```

The individual environment can be diagnosed with instructor support while the student remains active in the lab.

## MarketPulse does not run

From the repository root, check:

```bash
pwd
ls
ls src
ls data/sample
```

Then retry:

```bash
python src/main.py
```

# Checkpoint relation and Evidence Artefacts

The single source of truth for all evidence requirements is:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

Checkpoint A is formally validated after TD04. No screenshot submission is required at the end of TD01.

However, TD01 establishes the working environment and terminal mastery required for the first Checkpoint A evidence artefact:

```text
evidence/checkpoint-a/<github-username>/01_terminal_python.png
```

### Checkpoint A Artefact: `01_terminal_python.png`

| Attribute | Specification |
|---|---|
| **Checkpoint** | Checkpoint A - Foundations (suggested weight only, pending teaching-team approval) |
| **Filename** | `01_terminal_python.png` |
| **Target Directory** | `evidence/checkpoint-a/<github-username>/` |
| **Status** | Required for Checkpoint A |
| **Format** | PNG (lowercase_snake_case, no spaces, no accents) |

#### What the screenshot must display:
```bash
pwd
ls
python src/main.py
```

#### Verification objective:
Demonstrates that the student can open a Linux terminal, navigate to the team repository root (`pwd`), list project contents (`ls`), and execute MarketPulse (`python src/main.py`) with clean starter output.

> **Tip:** You may prepare and save this screenshot now in your individual evidence folder so that it is ready for Checkpoint A.

# What comes next?

Pedagogical Wave 1 is not finished yet.

TD02 completes Wave 1 with Python and local data manipulation.

In TD02, MarketPulse becomes a real Python exercise using:

```text
CSV
+
JSON
+
Instrument
+
Benchmark
```

No checkpoint evidence is submitted at the end of TD01.

Checkpoint A is performed after TD04.
