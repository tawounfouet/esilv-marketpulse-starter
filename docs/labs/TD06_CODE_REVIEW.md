# TD06 - Code Review

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Changes must be reviewed before integration."
```

## Context

TD05 ended with real Pull Requests left open in the shared team repository.

TD06 adds the review step before merge.

The collaborative workflow is now:

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
review by another student
      |
      +--> real issue found?
      |       |
      |       +--> yes -> correction -> push -> review again
      |       |
      |       +--> no  -> approval
      |
      v
merge
      |
      v
team main
```

A correction is required only when the review identifies a real issue.

Do not manufacture a defect or an unnecessary fix just to create another commit.

## Learning objectives

At the end of TD06, you should be able to:

- explain why code review exists;
- inspect another student's Pull Request;
- read the `Files changed` view;
- compare the PR description with the actual diff;
- write meaningful technical feedback;
- distinguish Comment, Request changes and Approve;
- request a correction only when justified;
- update the same PR when a real correction is required;
- approve a PR after actual inspection;
- merge after review;
- synchronize local `main` after merge.

## CORE definition of done

TD06 is complete when each student can confirm:

```text
[ ] I reviewed another student's Pull Request
[ ] I inspected Files changed
[ ] my review contains meaningful technical feedback
[ ] I can explain Comment vs Request changes vs Approve
[ ] I requested a correction only if a real issue existed
[ ] if my PR required a correction, I updated the same branch and PR
[ ] my own PR was reviewed by another student
[ ] my PR was merged only after review
[ ] I synchronized local main after merge
[ ] MarketPulse still runs
```

A review does not need to produce a correction to be valid.

## Prerequisites

Before starting:

```text
[ ] TD05 completed
[ ] I have an open Pull Request
[ ] another team member has an open Pull Request
[ ] my feature branch was pushed to origin
[ ] my PR targets team main
[ ] Files changed was checked in TD05
[ ] python src/main.py works
```

If a team is missing an open PR, fix that TD05 prerequisite before starting the main TD06 workflow.

Do not create meaningless code only to generate something to review.

## Important review rule

A meaningful review demonstrates inspection.

Weak examples:

```text
looks good
ok
nice
works
```

Better examples:

```text
The instrument metadata is displayed correctly.
I also checked the benchmark path and the same helper is reused.
```

```text
The output works for AAPL, but SP500 now prints the wrong label.
Please correct the benchmark label before merge.
```

```text
The implementation is coherent and python src/main.py still works.
I found no blocking issue, so I approve the PR.
```

Positive feedback can be meaningful when it states what was actually verified.

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for GitHub variation, merge recovery and optional review practice.

| Time | Activity |
|---|---|
| 00-10 min | Review purpose and outcomes |
| 10-25 min | Inspect another student's PR |
| 25-40 min | Write meaningful review |
| 40-55 min | Correction cycle only if justified |
| 55-65 min | Approve when ready |
| 65-75 min | Merge and synchronize main |
| 75-80 min | CORE validation |
| 80-90 min | Buffer / optional practice |

# CORE

# Part 1 - Understand the purpose of review

Code review contributes to:

```text
quality
+
shared understanding
+
error detection
+
consistency
+
knowledge transfer
```

The reviewer is not expected to redesign the feature.

The reviewer should determine whether the proposed change is:

- understandable;
- relevant;
- limited to its intended scope;
- technically coherent;
- safe to integrate at the current course level.

# Part 2 - Assign reviewers

Each student reviews another student's Pull Request.

Do not review your own PR.

For three students:

```text
A reviews B
B reviews C
C reviews A
```

For four students:

```text
A reviews B
B reviews C
C reviews D
D reviews A
```

The objective is distributed responsibility and individual traceability.

# Part 3 - Read the Pull Request before commenting

Open the assigned Pull Request.

Inspect:

```text
title
description
author
source branch
target branch
commits
Files changed
```

Before submitting a review, answer:

1. What change does the PR propose?
2. Which files changed?
3. Does the description match the diff?
4. Is the change limited to the expected scope?
5. Does the implementation remain understandable?

# Part 4 - Inspect Files changed

Open:

```text
Files changed
```

Check at least:

```text
[ ] expected files only
[ ] no temporary debug output
[ ] no accidental unrelated edits
[ ] no secret
[ ] output logic remains understandable
[ ] MarketPulse behaviour still matches the stated change
```

Possible MarketPulse review questions include:

```text
Does the feature work for both instrument and benchmark?

Does it reuse existing logic instead of duplicating large blocks?

Does it preserve the current lookback and interval?

Does it introduce a hard-coded market value?

Does python src/main.py still run?
```

Do not invent advanced architecture requirements that have not been taught yet.

# Part 5 - Write meaningful technical feedback

A useful review is:

```text
specific
+
technical
+
grounded in the diff
+
actionable when correction is needed
```

## Example without blocking issue

```text
I checked the market metadata output for both AAPL and SP500.
The existing display helper is reused and the PR only changes src/main.py.
No blocking issue found.
```

## Example with a real issue

```text
The instrument output is correct, but the benchmark still uses the instrument market label.
Please use the benchmark metadata in this branch before merge.
```

## Example validation request

```text
Please confirm python src/main.py still shows both AAPL and SP500 after this change.
```

A meaningful review may end in approval without requiring a code change.

# Part 6 - Choose the correct review outcome

Use the outcome that matches what you actually found.

## Comment

Use Comment when:

- asking a question;
- clarifying a detail;
- leaving non-blocking feedback.

## Request changes

Use Request changes only when the PR should not merge yet.

Examples:

- feature does not work;
- benchmark behaviour is broken;
- unintended files are included;
- required part of the change is missing;
- a clear technical defect is visible.

## Approve

Use Approve when:

- you inspected the diff;
- the PR matches its stated purpose;
- no blocking issue remains;
- the change is ready to integrate.

Do not request changes merely because the exercise mentions review.

Do not approve without inspecting the change.

# Part 7 - Correction cycle only when justified

If your reviewer identified a real issue on your own PR, stay on the same feature branch.

Verify:

```bash
git branch
git status
```

Apply only the justified correction.

Then inspect and validate:

```bash
git diff
python src/main.py
```

Stage and commit:

```bash
git add <changed-file>
git commit -m "fix: address review feedback"
git push
```

The existing Pull Request updates automatically because it follows the same branch.

```text
same feature branch
      |
      +-- initial commit
      |
      +-- justified fix commit
      |
      v
same Pull Request
```

If no real issue was found, skip this part.

Do not add a fake fix commit.

# Part 8 - Review again when a correction occurred

If the author pushed a correction, the reviewer reopens the PR and verifies the new diff.

Check:

```text
[ ] original issue addressed
[ ] no unrelated change introduced
[ ] feature still matches its scope
[ ] MarketPulse still behaves correctly
```

If the PR is ready, approve it.

If no correction was required in the first place, the original review may proceed directly to approval.

# Part 9 - Merge after review

Merge the approved Pull Request into:

```text
team main
```

Do not merge into the instructor repository.

After merge, verify on GitHub:

```text
PR status = Merged
```

The reviewed feature is now part of the shared team baseline.

# Part 10 - Synchronize local main

GitHub `main` changed during merge.

Each student should update their local copy.

Run:

```bash
git switch main
git status
git pull
```

Then verify:

```bash
git log --oneline -5
python src/main.py
```

You should be able to identify the integrated work in the local history.

Before later labs begin, the team should avoid leaving different outdated local `main` states.

# Part 11 - CORE validation

Each student should show or explain:

```text
reviewed PR
Files changed
meaningful feedback
review outcome
merge status
updated local main
```

Run:

```bash
git status
git log --oneline -5
python src/main.py
```

If a correction occurred, be able to explain why it was necessary.

If no correction occurred, be able to explain why approval was justified.

That distinction is part of the learning objective.

# Checkpoint relation

Checkpoint B is performed after TD08.

One required evidence file is:

```text
02_code_review.png
```

The canonical evidence contract is:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

The evidence must show meaningful review activity performed by the student.

A reaction alone is not sufficient.

Do not submit Checkpoint B yet.

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied.

## Optional 1 - Inspect review history

Inspect the PR conversation and review timeline.

Identify:

```text
author
reviewer
review outcome
merge status
```

## Optional 2 - Compare commits inside a corrected PR

Only if the PR actually required a correction, identify:

```text
initial implementation commit
review correction commit
```

Do not create a second commit solely for this exercise.

## Optional 3 - Inspect integrated Git history

Run:

```bash
git log --oneline --graph --decorate --all
```

Identify the reviewed integration.

## Optional 4 - Inspect one integrated commit

Run:

```bash
git show <commit-id>
```

Explain what changed.

## Optional 5 - Improve a weak review statement

Rewrite:

```text
Looks good.
```

into a statement that names what was actually inspected and why the PR is ready or not ready.

# ADVANCED

No `READY_TO_TEACH` advanced activity is attached directly to TD06 at this time.

Complete the CORE and OPTIONAL work only.

Instructor deep dives may enrich explanations, but they are not student deliverables and are not checkpoint evidence.

# TROUBLESHOOTING

## No open Pull Request to review

Return to the TD05 end state.

The normal solution is to recover or open a real coherent TD05 PR.

Do not invent random code merely to create review material.

## Cannot review or approve

Verify:

- you are signed into your own GitHub account;
- you have collaborator access;
- you are not reviewing your own PR.

## New correction commit does not appear in the PR

Check:

```bash
git branch
git status
git remote get-url origin
git push
```

Make sure you pushed to the source branch used by the PR.

## PR has no defect

This is valid.

Write meaningful feedback describing what you checked, then approve if the PR is ready.

Do not create a synthetic problem.

## Local main does not contain the merged feature

Run:

```bash
git switch main
git pull
git log --oneline -5
```

## Merge creates an unexpected result

Run:

```bash
python src/main.py
git status
git log --oneline --graph --decorate --all
```

Do not start TD07 work until the team understands the repository state.

# Final readiness check

Each student should confirm:

```text
[ ] I reviewed another student's Pull Request
[ ] I inspected Files changed
[ ] I left meaningful technical feedback
[ ] I understand Comment
[ ] I understand Request changes
[ ] I understand Approve
[ ] I know that correction is conditional on a real issue
[ ] I know how the same PR receives a correction commit if needed
[ ] my own PR was reviewed by another student
[ ] my PR was merged only after review
[ ] local main is synchronized
[ ] MarketPulse still runs
```

# What comes next?

Pedagogical Wave 2 is now complete:

```text
Wave 2 - Git and Collaboration - 6 hours

TD03 - Git Local Workflow
TD04 - Branches + Merge
TD05 - Remote Branch + Pull Request
TD06 - Code Review
```

Checkpoint B is not performed yet.

It closes Checkpoint Phase B after TD08.

The collaboration workflow is now established and should be reused rather than retaught in every later lab.

TD07 introduces the reusable comparison layer:

```text
canonical local data
        |
        v
alignment
        |
        v
period return
        |
        v
base 100
        |
        v
relative performance
```
