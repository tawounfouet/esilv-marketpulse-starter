# TD05 - Remote Branch + Pull Request

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Several developers now contribute to the same MarketPulse repository."
```

## Context

The team fork already exists from TD01.

TD03 introduced local commits.

TD04 introduced local feature branches and merge.

TD05 now adds the remote collaboration layer:

```text
shared team baseline
        |
        v
local feature branch
        |
        v
commit
        |
        v
push to origin
        |
        v
remote branch
        |
        v
Pull Request
        |
        v
ready for TD06 review
```

The objective is no longer to learn how to fork.

The objective is to move a real branch from a student's local environment into the shared team repository and open a clear Pull Request.

Formal code review is the focus of TD06.

## Important repository model

The course uses:

```text
1 team
=
1 shared fork
```

not:

```text
1 student
=
1 fork
```

Instructor repository:

```text
tawounfouet/esilv-marketpulse
```

Team repository:

```text
<team-owner>/esilv-marketpulse-gXX-tYY
```

Example:

```text
alice-martin/esilv-marketpulse-g03-t02
```

All students contribute to that same team repository.

Do not create another fork for TD05.

## Learning objectives

At the end of TD05, you should be able to:

- distinguish a local branch from a remote branch;
- verify that `origin` points to the team repository;
- start from the shared team baseline;
- create one feature branch;
- implement and commit one small coherent change;
- push the branch to `origin`;
- understand what `git push -u` establishes;
- open a Pull Request inside the team repository;
- identify source and target branches;
- inspect the `Files changed` view;
- write a clear PR title and description;
- leave the Pull Request open for TD06 review.

## CORE definition of done

TD05 is complete when each student can confirm:

```text
[ ] Team Baseline Gate passed
[ ] origin points to the team repository
[ ] my local main matches origin/main before feature work
[ ] I created one feature branch
[ ] I created at least one meaningful commit
[ ] I pushed my branch to origin
[ ] the remote branch exists
[ ] I opened one Pull Request
[ ] the PR targets team main
[ ] the PR source is my feature branch
[ ] the PR title is meaningful
[ ] the PR description explains change + reason + validation
[ ] Files changed contains only intended work
[ ] MarketPulse still runs
[ ] the PR remains open for TD06
```

A second commit on the same PR is not required.

Extra remote-branch commands are not required.

## Prerequisites

Before starting:

```text
[ ] TD01-TD04 completed
[ ] Checkpoint A captured or ready
[ ] team repository accessible
[ ] all team members are collaborators
[ ] local commits understood
[ ] branches understood
[ ] local merge understood
[ ] python src/main.py works
```

## Team Baseline Gate

TD03 and TD04 may have produced different local `main` histories.

TD05 feature work starts only after the team has one shared baseline.

### Baseline model

```text
local learning histories
        |
        v
Checkpoint A capture
        |
        v
preserve local history
        |
        v
select one validated main
        |
        v
publish origin/main
        |
        v
align every student
        |
        v
TD05 feature branches
```

### 1. Capture Checkpoint A first

If Checkpoint A evidence is still needed, capture it before destructive alignment.

Your TD03-TD04 local history may be needed for:

```text
02_git_status_log.png
03_branch_merge.png
```

### 2. Make the local working tree safe

Each student runs:

```bash
git switch main
git status
```

Do not continue with uncommitted work.

### 3. Preserve the local learning history

Create:

```bash
git branch archive/td04-local
```

This is a local safety branch.

Do not push it unless the instructor explicitly asks you to.

### 4. Select and validate the team baseline

The instructor or designated integrator selects one `main` that satisfies:

```text
[ ] TEAM.md is correct
[ ] required starter files are present
[ ] no temporary conflict-demo file remains
[ ] working tree is clean
[ ] python src/main.py works
```

### 5. Verify origin

On the selected baseline:

```bash
git remote get-url origin
```

It must point to:

```text
<team-owner>/esilv-marketpulse-gXX-tYY
```

Stop if it points elsewhere.

### 6. Publish the baseline

Only the designated integrator publishes it:

```bash
git switch main
git push origin main
```

Now:

```text
origin/main
=
official TD05 starting point
```

### 7. Align every other student

Under instructor guidance:

```bash
git switch main
git status
git fetch origin
git reset --hard origin/main
```

This controlled `reset --hard` is allowed here only because:

```text
working tree checked clean
+
archive/td04-local created
+
instructor-controlled synchronization
```

A fresh Codespace or fresh clone after baseline publication is an acceptable alternative.

Do not use `git reset --hard` casually.

### 8. Verify common HEAD

Each student runs:

```bash
git status
git rev-parse HEAD
git rev-parse origin/main
python src/main.py
```

Required state:

```text
HEAD
=
origin/main
```

The Team Baseline Gate is now complete.

This is an operational synchronization step, not an advanced merge/rebase lesson.

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for GitHub variation, troubleshooting and validation.

| Time | Activity |
|---|---|
| 00-15 min | Team Baseline Gate |
| 15-23 min | Local vs remote + verify origin |
| 23-35 min | Create coordinated feature branch |
| 35-50 min | Implement, validate and commit |
| 50-60 min | Push branch |
| 60-74 min | Open Pull Request |
| 74-80 min | Inspect Files changed + leave PR open |
| 80-90 min | Buffer / troubleshooting / optional |

If the instructor has prepared the shared baseline before the timed activity, the saved time becomes buffer.

# CORE

# Part 1 - Local branch vs remote branch

A local branch exists in your working Git environment.

A remote branch exists in the GitHub team repository after push.

```text
LOCAL
feature branch
      |
      | git push
      v
REMOTE
origin/feature branch
```

Run:

```bash
git remote -v
git remote get-url origin
```

For the CORE:

```text
origin
=
team repository
```

The instructor repository may conceptually be called `upstream`, but configuring or synchronizing an `upstream` remote is not required in TD05.

# Part 2 - Coordinate one small contribution per student

Before creating branches, agree on distinct small tasks inside the team.

The goal is to avoid several students independently implementing the exact same change.

Possible contribution examples:

```text
Student A -> display provider label
Student B -> display market metadata
Student C -> improve execution documentation
Student D -> improve one clear terminal label or metadata field
```

The instructor may assign different tasks.

Each task must be:

```text
small
+
coherent
+
individually explainable
+
compatible with the current MarketPulse scope
```

Do not calculate returns yet.

Do not start a large refactor.

# Part 3 - Create the feature branch

Start from synchronized `main`:

```bash
git switch main
git status
git rev-parse HEAD
git rev-parse origin/main
```

Create a descriptive branch.

Example:

```bash
git switch -c feature/display-market-metadata
```

Verify:

```bash
git branch
```

Good branch names describe the work.

Avoid names based on the student name or vague words such as `test`, `work` or `final`.

# Part 4 - Implement and validate the change

Implement only the coordinated task assigned to your branch.

If the task is market metadata, existing values are available in:

```text
data/sample/instruments.json
```

Useful fields include:

```text
ticker
name
currency
market
```

Inspect your work:

```bash
git status
git diff
```

Run:

```bash
python src/main.py
```

The application must remain functional before the commit.

# Part 5 - Commit the feature

Stage only the intended files.

Example:

```bash
git add src/main.py
```

Inspect:

```bash
git diff --staged
```

Commit with a message matching the real change.

Example:

```bash
git commit -m "feat: display market metadata"
```

Verify:

```bash
git status
git log --oneline -5
```

# Part 6 - Push the branch

Push the current feature branch to the team repository.

Example:

```bash
git push -u origin feature/display-market-metadata
```

The `-u` option establishes tracking between the local branch and its remote counterpart.

After the first push, later pushes from the same tracked branch can usually use:

```bash
git push
```

Verify the branch exists on GitHub.

You should now be able to distinguish:

```text
feature/display-market-metadata
=
local branch

origin/feature/display-market-metadata
=
remote branch
```

# Part 7 - Open the Pull Request

Open the team repository on GitHub.

Create a Pull Request with:

```text
source
=
your pushed feature branch

target
=
team main
```

Do not target:

```text
tawounfouet/esilv-marketpulse
```

The TD05 Pull Request belongs inside the team repository.

## PR title

Use a clear title.

Example:

```text
feat: display market metadata
```

Avoid:

```text
PR
changes
work
test
final
```

## PR description

A useful description answers:

```text
What changed?
Why?
How was it validated?
```

Example structure:

```markdown
## What changed

- display market metadata for the instrument and benchmark.

## Why

The terminal summary should provide clearer context about each market series.

## Validation

- ran `python src/main.py`;
- inspected the terminal output;
- verified no unrelated change is included.
```

Adapt the description to your actual branch.

# Part 8 - Verify source, target and Files changed

Before considering the PR ready for review, inspect:

```text
author
source branch
target branch
commits
Files changed
```

Required interpretation:

```text
source branch
=
proposed work

target branch
=
team main
```

Open the GitHub `Files changed` tab.

Confirm:

```text
[ ] only intended files changed
[ ] no temporary debug output
[ ] no secret
[ ] no unrelated exercise file
[ ] the change matches the PR description
```

If unrelated changes appear, investigate before TD06 review.

# Part 9 - Individual traceability

The Pull Request is part of your individual Git trace.

It makes visible:

```text
author
branch
commits
changed files
discussion
review status
merge status
```

Do not create a PR from another student's account to simulate contribution.

Each student should be able to explain their own branch and PR.

# Part 10 - Leave the Pull Request open

Do not merge the PR during the normal TD05 flow.

TD06 uses these real Pull Requests for review.

Required TD05 end state:

```text
feature branch pushed
+
Pull Request open
+
ready for another student to review
```

The instructor may intervene only if a PR is unusable or incorrectly targets the wrong repository.

# Part 11 - CORE validation

Before finishing TD05, each student should confirm:

```text
[ ] origin is the team repository
[ ] I started from the shared origin/main baseline
[ ] I created my own feature branch
[ ] my commit is understandable
[ ] my feature branch exists on GitHub
[ ] I opened a Pull Request
[ ] source branch is correct
[ ] target branch is team main
[ ] Files changed contains intended work only
[ ] MarketPulse runs
[ ] the Pull Request remains open for TD06
```

If these checks pass, TD05 CORE is complete.

# Checkpoint relation

Checkpoint B is performed after TD08.

One required evidence file is:

```text
01_pull_request.png
```

The canonical evidence contract is:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

Do not submit Checkpoint B yet.

TD05 establishes the workflow that later evidence must demonstrate.

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied and the PR is safely open.

## Optional 1 - Add a justified second commit to the same PR

A Pull Request follows its source branch.

If a real improvement is needed:

```bash
git status
git diff
git add <file>
git commit -m "<meaningful message>"
git push
```

Refresh the existing PR.

Do not open a second PR for the same branch.

Do not manufacture a second commit only to demonstrate this behaviour.

## Optional 2 - Inspect remote tracking

Run:

```bash
git branch -vv
```

Identify the remote branch tracked by your local feature branch.

## Optional 3 - Inspect remote branches

Run:

```bash
git branch -r
```

Then optionally:

```bash
git branch -a
```

These commands are useful references, not CORE requirements.

## Optional 4 - Compare local diff with Files changed

Run:

```bash
git diff main..HEAD
```

Compare the result with the GitHub `Files changed` view.

## Optional 5 - Inspect feature-only commits

Run:

```bash
git log --oneline main..HEAD
```

Identify which commits belong to your feature branch but not to `main`.

# ADVANCED

No `READY_TO_TEACH` advanced activity is attached directly to TD05 at this time.

Complete the CORE and OPTIONAL work only.

Instructor deep dives may enrich explanations, but they are not student deliverables and are not checkpoint evidence.

# TROUBLESHOOTING

## Push rejected

Check:

```bash
git status
git branch
git remote get-url origin
```

Verify:

- you are on the expected feature branch;
- `origin` is the team repository;
- you have collaborator access.

## Permission denied

Verify that:

- you are authenticated with your own GitHub account;
- the team fork owner added you as collaborator;
- you accepted the invitation.

Do not share another student's credentials.

## Wrong origin

Run:

```bash
git remote get-url origin
```

Stop before pushing if the repository is not the team repository.

Ask the instructor for help.

## PR targets the instructor repository

Do not merge it.

Correct the target if possible or ask the instructor before recreating the PR.

## PR contains unexpected files

Inspect:

```bash
git status
git log --oneline
git diff main..HEAD
```

Then compare with GitHub `Files changed`.

## Local main differs from origin/main before branch creation

Do not start feature work.

Return to the Team Baseline Gate.

The TD05 branch must start from the common baseline.

# Final readiness check

Each student should be able to explain:

```text
local branch
remote branch
origin
git push
tracking branch
Pull Request
source branch
target branch
Files changed
PR title
PR description
```

Each student should also confirm:

```text
[ ] I pushed an identifiable branch
[ ] I opened an attributable Pull Request
[ ] the PR targets team main
[ ] the PR contains coherent work
[ ] the PR remains open for review
[ ] MarketPulse still runs
```

# What comes next?

TD06 introduces review before integration:

```text
open TD05 Pull Request
        |
        v
another student reviews
        |
        v
correction only if justified
        |
        v
approval
        |
        v
merge
        |
        v
team main synchronized
```

Do not merge the TD05 PR before the TD06 review workflow unless the instructor explicitly asks you to.
