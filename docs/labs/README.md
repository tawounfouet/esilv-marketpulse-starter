# MarketPulse Lab Index

## Purpose

This directory contains the student-facing practical lab sequence for MarketPulse.

Each TD is designed as a 1 hour 30 minute unit.

The common sequence contains 12 TD units for a total of 18 hours.

## Sequence

| TD | Topic | Main MarketPulse outcome |
|---|---|---|
| TD01 | Bootstrap + Linux | Team repository and working environment |
| TD02 | Python + CSV / JSON | Local instrument and benchmark data |
| TD03 | Git Local Workflow | Versioned MarketPulse changes |
| TD04 | Branches + Merge | Feature branches and merge |
| TD05 | Remote Branch + Pull Request | Collaborative contribution |
| TD06 | Code Review | Reviewed integration |
| TD07 | Data Normalization + Comparison | Comparison-ready data |
| TD08 | Yahoo Finance | Remote daily market data |
| TD09 | Bloomberg Introduction | First professional market-data access |
| TD10 | Bloomberg Provider | Multi-provider MarketPulse |
| TD11 | Dash Dashboard | Comparative market dashboard |
| TD12 | Integration + Release | Reproducible final release |

## Pedagogical waves

```text
Wave 1 - TD01-TD02 - 3 hours
Wave 2 - TD03-TD06 - 6 hours
Wave 3 - TD07-TD08 - 3 hours
Wave 4 - TD09-TD12 - 6 hours
```

## Checkpoint phases

```text
Checkpoint Phase A - TD01-TD04
    |
    v
Checkpoint A

Checkpoint Phase B - TD05-TD08
    |
    v
Checkpoint B

Checkpoint Phase C - TD09-TD12
    |
    v
Checkpoint C
```

Pedagogical waves and checkpoint phases are intentionally different groupings.

The official evidence contract is documented in:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

## Teaching taxonomy

Every lab now uses the same student-facing structure:

```text
CORE
OPTIONAL
ADVANCED
```

Interpretation:

```text
CORE
=
mandatory common work
+
checkpoint-aligned
+
part of the 18-hour path

OPTIONAL
=
lightweight extension
+
normally 5 to 20 minutes
+
no checkpoint requirement

ADVANCED
=
materially deeper practice
+
separate support under docs/advanced/
+
never required for a checkpoint
```

Instructor-only conceptual depth remains under:

```text
docs/instructor/
```

and is not student evidence.

A student who completes the CORE without ADVANCED work must remain eligible for full common checkpoint assessment.

## Advanced track portal

The canonical navigation and selection guide for advanced material is:

```text
docs/advanced/README.md
```

Use the portal for:

```text
domain paths
durations
prerequisites
delivery modes
infrastructure gates
diagnostic-driven selection
self-study guidance
```

This file remains the source of truth for which advanced supports are currently activated from each TD.

## Current ADVANCED availability

Only supports with status:

```text
READY_TO_TEACH
```

are activated as student-facing links.

| TD | Active READY_TO_TEACH ADVANCED support | Other status |
|---|---|---|
| TD01 | ADV-LNX-01, ADV-LNX-02, ADV-LNX-03 | - |
| TD02 | ADV-LNX-04 | - |
| TD03 | ADV-GIT-02 | - |
| TD04 | ADV-GIT-01 | - |
| TD05 | None | No active advanced support |
| TD06 | None | No active advanced support |
| TD07 | None | No active advanced support |
| TD08 | None | No active advanced support |
| TD09 | None | Bloomberg advanced path not yet active |
| TD10 | None | ADV-BBG-01 is PENDING_EXTERNAL |
| TD11 | None | ADV-DASH-01 and ADV-DASH-02 are PENDING_EXTERNAL |
| TD12 | ADV-GIT-04 | ADV-RMT-01 and ADV-RMT-03 are PENDING_EXTERNAL |

Current totals:

```text
READY_TO_TEACH active links
=
7

PENDING_EXTERNAL supports
=
5
```

PENDING_EXTERNAL means the support exists but still requires a real external teaching environment before activation.

## Files

The TD files follow this naming convention:

```text
TD01_BOOTSTRAP_LINUX.md
TD02_PYTHON_CSV_JSON.md
TD03_GIT_LOCAL_WORKFLOW.md
TD04_BRANCHES_AND_MERGE.md
TD05_FORK_AND_PULL_REQUEST.md
TD06_CODE_REVIEW.md
TD07_DATA_NORMALIZATION_AND_COMPARISON.md
TD08_YAHOO_FINANCE.md
TD09_BLOOMBERG_INTRODUCTION.md
TD10_BLOOMBERG_PROVIDER.md
TD11_DASH_DASHBOARD.md
TD12_INTEGRATION_AND_RELEASE.md
```

## Important

Students should work through the TDs in order.

Later TDs assume that the repository and Git workflow established earlier are already operational.
