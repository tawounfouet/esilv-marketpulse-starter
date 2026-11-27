# Student Onboarding

## Objective

At the end of onboarding, every student must be able to access the team repository, open a development environment and run the MarketPulse starter.

## 1. Create or verify your GitHub account

Each student must use their own GitHub account.

Do not share accounts.

Before continuing, verify that you can sign in to GitHub.

## 2. Form your MarketPulse team

Recommended team size:

```text
3 to 4 students
```

Your team receives two identifiers:

```text
TD Group: GXX
MarketPulse Team: TXX
```

Example:

```text
G03-T02
```

## 3. Fork the instructor repository

Only one member creates the initial team fork.

Source repository:

```text
tawounfouet/esilv-marketpulse-starter
```

The fork belongs to the team for the duration of the module.

The student who creates the fork is not automatically the team leader.

## 4. Rename the team repository

Use the following convention:

```text
esilv-marketpulse-gXX-tYY
```

Example:

```text
esilv-marketpulse-g03-t02
```

Do not include student initials in the repository name.

## 5. Add team collaborators

The fork owner adds the other team members as collaborators.

Each team member must then verify that they can access the repository with their own GitHub account.

## 6. Create TEAM.md

Copy:

```text
TEAM_TEMPLATE.md
```

to:

```text
TEAM.md
```

Complete:

- TD group;
- MarketPulse team number;
- full names;
- GitHub usernames;
- repository name.

Do not include personal email addresses or student identification numbers.

## 7. Open the development environment

Use the environment specified by the instructor.

For the common course path, GitHub Codespaces may be used to provide a Linux terminal and Python environment without local installation complexity.

## 8. Verify the terminal

Run:

```bash
pwd
ls
python --version
git --version
```

You should be able to identify:

- your current directory;
- the repository files;
- the Python version;
- the Git version.

## 9. Run MarketPulse

From the repository root:

```bash
python src/main.py
```

The starter should display:

```text
=== MarketPulse ===

Instrument
AAPL - Apple Inc.

Benchmark
SP500 - S&P 500

Period: 1 month
Interval: Daily
```

Exact values may evolve during the course.

## 10. Inspect the starter files

Use simple Linux commands:

```bash
ls
ls data/sample
cat data/sample/instruments.json
head data/sample/prices.csv
```

The goal is not to memorize commands. The goal is to become comfortable navigating and inspecting a project from a terminal.

## 11. Verify Git identity

Run:

```bash
git config user.name
git config user.email
```

Your commits must be attributable to your own GitHub identity.

Ask the instructor for help if the identity is incorrect.

## 12. Readiness checklist

Before onboarding is considered complete:

```text
[ ] GitHub login works
[ ] Team is identified
[ ] Team repository exists
[ ] Repository follows esilv-marketpulse-gXX-tYY naming
[ ] All members have access
[ ] TEAM.md is completed
[ ] Development environment opens
[ ] Linux terminal works
[ ] python --version works
[ ] git --version works
[ ] python src/main.py works
```

## 13. Troubleshooting rule

Do not spend the entire lab blocked by one workstation issue.

If an individual environment problem cannot be solved quickly, the instructor may temporarily ask you to pair with another team member while the issue is diagnosed.

The common lab should not be blocked by optional installation work.
