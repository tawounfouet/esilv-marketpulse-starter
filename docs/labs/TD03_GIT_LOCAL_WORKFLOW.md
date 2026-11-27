# TD03 - Git Local Workflow

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"We need to keep a reliable history of changes."
```

## Context

TD02 produced meaningful Python changes in MarketPulse.

TD03 gives those changes a history.

The central question is:

> How can we know what changed, who changed it and when?

Git provides that history.

This TD focuses only on local Git:

```text
working tree
    |
    v
staging area
    |
    v
local commit history
```

Branches are introduced in TD04.

Remote push, Pull Requests and code review are introduced later.

## Learning objectives

At the end of TD03, you should be able to:

- explain working tree, staging area and commit;
- inspect repository state with `git status`;
- inspect unstaged changes with `git diff`;
- select changes with `git add`;
- inspect staged changes with `git diff --staged`;
- create a meaningful commit;
- read history with `git log`;
- inspect one commit with `git show`;
- identify your Git author identity;
- explain the change represented by your own commit.

## CORE definition of done

TD03 is complete when each student can confirm:

```text
[ ] my Git identity is correct
[ ] I inspected the real TD02 working changes
[ ] I used git status
[ ] I used git diff
[ ] I staged an intended change
[ ] I inspected git diff --staged
[ ] I created at least one meaningful local commit
[ ] I can find that commit in git log
[ ] I can inspect it with git show
[ ] I can explain the diff
[ ] MarketPulse still runs
```

No remote push is required.

No Pull Request is required.

## Prerequisites

Before starting:

```text
[ ] TD01 completed
[ ] TD02 completed
[ ] team repository accessible
[ ] meaningful TD02 Python changes are available
[ ] python src/main.py works
[ ] Git is available
```

## Important TD03 rule

During TD03, direct local commits on `main` may be used as a temporary pedagogical exception.

The objective is to learn the local Git lifecycle before branches are introduced.

From TD04 onward:

```text
feature work
    |
    v
branch
    |
    v
merge
```

From TD05 onward:

```text
branch
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

Do not generalize the TD03 exception into a permanent workflow.

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for questions, recovery and optional exploration.

| Time | Activity |
|---|---|
| 00-10 min | Git mental model and identity |
| 10-22 min | Inspect TD02 working changes |
| 22-35 min | Understand status and diff |
| 35-48 min | Stage intended changes |
| 48-62 min | Create the first meaningful commit |
| 62-72 min | Read history and inspect commit |
| 72-80 min | Run MarketPulse and CORE validation |
| 80-90 min | Buffer and optional exercises |

# CORE

# Part 1 - Understand the local Git model

A simplified model is:

```text
Working tree
     |
     | git add
     v
Staging area
     |
     | git commit
     v
Local history
```

## Working tree

The working tree contains the files you are currently editing.

A tracked file can be modified without being part of a commit yet.

## Staging area

The staging area contains the exact changes selected for the next commit.

This means:

```text
modified
!=
staged
```

## Commit

A commit records a selected project state with metadata such as:

```text
author
date
message
identifier
changed content
```

Saving a file in the editor does not create a commit.

# Part 2 - Verify Git identity

Run:

```bash
git --version
git config user.name
git config user.email
```

Your commits must be attributable to your own identity.

If the values are missing or clearly incorrect, ask the instructor before continuing.

Do not copy another student's Git identity.

# Part 3 - Inspect the real TD02 changes

TD03 should start from the useful Python work completed in TD02.

Run:

```bash
git status
```

Then:

```bash
git diff
```

Your output may show changes in:

```text
src/main.py
```

or another file legitimately modified during TD02.

Do not create an artificial change if meaningful TD02 work is already available.

## Questions

Be able to answer:

1. Which files are modified?
2. Which lines were added?
3. Which lines were removed?
4. Does the diff match the work you intended?
5. Is there temporary debugging output that should be removed before committing?

The required habit is:

```text
change
  |
  v
inspect
  |
  v
stage
  |
  v
inspect again
  |
  v
commit
```

# Part 4 - Understand git status and git diff

Run:

```bash
git status
git status --short
git diff
```

Use `git status` to understand repository state.

Use `git diff` to inspect unstaged changes.

Possible short-status markers may include:

```text
M
??
```

You do not need to memorize every Git status code today.

You should understand the difference between:

```text
tracked file modified
untracked file
staged change
```

# Part 5 - Stage the intended change

If the useful TD02 work is in:

```text
src/main.py
```

stage that file:

```bash
git add src/main.py
```

If another intended file is part of the same coherent change, stage it deliberately.

Do not use:

```bash
git add .
```

without first understanding what it would include.

After staging, run:

```bash
git status
git diff --staged
```

Compare:

```bash
git diff
```

with:

```bash
git diff --staged
```

You should be able to explain:

```text
git diff
=
unstaged changes

git diff --staged
=
changes selected for the next commit
```

# Part 6 - Create the first meaningful commit

Before committing, verify MarketPulse:

```bash
python src/main.py
```

The project should still run.

## Commit-message rule

Use a message that describes the actual change.

Examples:

```text
feat: improve MarketPulse market summary
refactor: reuse market summary display
docs: clarify starter execution
```

Avoid:

```text
update
changes
work
test
final
final2
```

Create the commit:

```bash
git commit -m "<meaningful message>"
```

The first meaningful TD03 commit may represent the Python work produced during TD02.

This is intentional.

Git is being introduced to version real work, not a fabricated exercise.

# Part 7 - Read the local history

Run:

```bash
git status
git log --oneline
```

Your new commit should appear near the top.

Identify:

```text
short commit identifier
commit message
```

Inspect the latest commit:

```bash
git show HEAD
```

or use its identifier:

```bash
git show <commit-id>
```

Be able to explain:

1. which files changed;
2. what the diff represents;
3. why the commit message is appropriate;
4. who is recorded as the author.

# Part 8 - Commit quality and traceability

A useful commit should be:

```text
small
+
coherent
+
understandable
+
explainable
```

Avoid mixing unrelated work when it can be separated clearly.

Each student should eventually be able to answer:

```text
Which commits are mine?
What did I change?
Why did I change it?
Can I explain the diff?
Can I reproduce the change?
```

Being listed in `TEAM.md` does not by itself prove technical contribution.

# Part 9 - Local vs remote Git

TD03 stops at local history:

```text
Working tree
      |
      v
Staging area
      |
      v
Local commit
```

Do not make remote collaboration part of today's required workflow.

The next stages are introduced later:

```text
TD04
branches + merge

TD05
push + Pull Request

TD06
code review
```

# Part 10 - CORE validation

Run:

```bash
git status
git log --oneline
python src/main.py
```

Then inspect your own commit:

```bash
git show HEAD
```

If several commits were created, inspect the commit that represents your own work.

You should be able to explain:

```text
working tree
staging area
commit
commit identifier
git status
git diff
git diff --staged
git add
git commit
git log
git show
```

If those concepts and commands are understood, TD03 CORE is complete.

# Checkpoint relation and Evidence Artefacts

The canonical source of truth for all checkpoint evidence requirements is:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

Checkpoint A is performed after TD04.

TD03 establishes the local Git workflow and history required for the second Checkpoint A evidence artefact:

```text
evidence/checkpoint-a/<github-username>/02_git_status_log.png
```

### Checkpoint A Artefact: `02_git_status_log.png`

| Attribute | Specification |
|---|---|
| **Checkpoint** | Checkpoint A — Foundations (25% weight) |
| **Filename** | `02_git_status_log.png` |
| **Target Directory** | `evidence/checkpoint-a/<github-username>/` |
| **Status** | Required for Checkpoint A |
| **Format** | PNG (lowercase_snake_case, strictly no spaces) |

#### Terminal execution to display:
```bash
git status
git log --oneline -5
```

#### Verification objective:
Demonstrates that the student understands working tree and repository state (`git status`), and shows a clean, meaningful local Git commit history (`git log --oneline`) where individual contributions are clearly identifiable.

### Checkpoint A Summary Matrix so far:

| Lab | Checkpoint A Artefact | Purpose |
|---|---|---|
| **TD01 / TD02** | `01_terminal_python.png` | Project navigation & MarketPulse execution |
| **TD03** | `02_git_status_log.png` | Git repository state & commit history |
| **TD04** | `03_branch_merge.png` | Feature branch creation & successful merge |

> **Note:** Each student stores their own evidence in `evidence/checkpoint-a/<github-username>/` along with their individual `README.md`. Final capture and submission take place at the end of TD04.

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied.

## Optional 1 - Tracked vs untracked

Create a temporary file:

```bash
touch td03_notes.txt
git status
```

Observe that the file is untracked.

Remove it:

```bash
rm td03_notes.txt
git status
```

Do not commit the temporary file.

## Optional 2 - Stage one file while another remains modified

Create two small harmless modifications in different files.

Inspect:

```bash
git status
git diff
```

Stage only one file:

```bash
git add <one-file>
```

Then compare:

```bash
git status
git diff
git diff --staged
```

Do not keep experimental modifications unless they are meaningful.

Ask the instructor before using a destructive recovery command.

## Optional 3 - Filter file history

Try:

```bash
git log --oneline -- src/main.py
```

Question:

> What does this command filter?

## Optional 4 - Graph view

Try:

```bash
git log --oneline --graph --decorate
```

The graph becomes more useful after branches are introduced in TD04.

## Optional 5 - Author filtering

Try:

```bash
git log --author="<your name>" --oneline
```

Use the author name configured in your Git environment.

## Optional 6 - Tracked files

Try:

```bash
git ls-files
```

This command is useful reference material, not a CORE requirement.

# ADVANCED

Complete advanced work only after TD03 CORE is complete.

Advanced work is not required for Checkpoint A.

## ADV-GIT-02 - Restore, Revert and Reset

Status:

```text
READY_TO_TEACH
```

Prerequisites:

```text
TD03 CORE complete
basic commits and status understood
```

Estimated duration:

```text
60 minutes
```

Support:

[ADV-GIT-02 - Restore, Revert and Reset](../advanced/ADV_GIT_02_RESTORE_REVERT_RESET.md)

# TROUBLESHOOTING

## Nothing to commit

Run:

```bash
git status
git diff
```

Possible explanations:

- TD02 changes were already committed;
- no tracked file was modified;
- the wrong working directory is open.

If TD02 changes were already committed, use one small meaningful MarketPulse or documentation improvement approved by the instructor.

Do not create random noise only to produce a commit.

## Git identity error

Check:

```bash
git config user.name
git config user.email
```

Ask the instructor before changing values if you are unsure.

## Wrong file staged

Do not use destructive commands at random.

Ask the instructor how to unstage the file while preserving the working change.

## Unexpected large diff

Run:

```bash
git status
git diff
git diff --staged
```

Check for accidental formatting or unrelated modifications.

## MarketPulse fails

Run:

```bash
python src/main.py
```

Inspect the working or staged diff before creating additional commits.

# Final readiness check

Each student should confirm:

```text
[ ] I know my Git author identity
[ ] I understand working tree vs staging area vs commit
[ ] I used git status
[ ] I used git diff
[ ] I used git diff --staged
[ ] I staged intended work deliberately
[ ] I created an understandable local commit
[ ] I can find the commit in git log
[ ] I can inspect it with git show
[ ] I can explain my own diff
[ ] MarketPulse still runs
[ ] I did not need a remote push or Pull Request
```

# What comes next?

TD04 introduces feature isolation:

```text
main
  |
  +--> feature branch
            |
            v
          commit
            |
            v
          merge
```

The local history created in TD03 becomes the foundation for branch work.
