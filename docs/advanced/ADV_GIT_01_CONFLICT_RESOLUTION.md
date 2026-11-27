# ADV-GIT-01 - Conflict Resolution

Status:

```text
READY_TO_TEACH
```

Mode:

```text
MINI_LAB
```

Estimated duration:

```text
30-45 minutes
```

## 1. Objective

Create, inspect and resolve one controlled Git merge conflict intentionally.

## 2. Prerequisites

```text
TD04 CORE complete
branch and merge understood
```

This activity is not required for Checkpoint A.

## 3. Safety model

Use a disposable repository.

Do not create the first conflict inside:

```text
src/main.py
analytics.py
provider files
team main
```

## 4. Create the disposable repository

```bash
mkdir conflict-lab
cd conflict-lab
git init
git config user.name "MarketPulse Lab"
git config user.email "lab@example.invalid"
printf "provider=csv\n" > config.txt
git add config.txt
git commit -m "chore: add base config"
```

## 5. Create the feature change

```bash
git switch -c feature/provider
printf "provider=yahoo\n" > config.txt
git add config.txt
git commit -m "feat: select yahoo provider"
```

## 6. Create the competing main change

```bash
git switch main
printf "provider=bloomberg-stage\n" > config.txt
git add config.txt
git commit -m "chore: select bloomberg stage"
```

If your Git version created `master` instead of `main`, rename it before the exercise:

```bash
git branch -m main
```

## 7. Trigger and inspect the conflict

```bash
git merge feature/provider
```

Expected:

```text
merge conflict
```

Inspect:

```bash
git status
cat config.txt
```

Identify:

```text
<<<<<<<
=======
>>>>>>>
```

## 8. Resolve deliberately

Choose one final value only after explaining the competing intent.

Example:

```bash
printf "provider=bloomberg-stage\n" > config.txt
git add config.txt
git commit -m "merge: resolve provider selection"
```

Verify:

```bash
git status
git log --oneline --graph --decorate --all
cat config.txt
```

## 9. Definition of done

```text
[ ] trigger a real conflict
[ ] identify conflict markers
[ ] inspect git status
[ ] explain both competing versions
[ ] resolve intentionally
[ ] stage the resolved file
[ ] complete the merge
[ ] finish with a clean working tree
```

## 10. Cleanup

From the parent directory:

```bash
rm -rf conflict-lab
```

## 11. Guardrails

Do not teach:

```text
blind ours/theirs selection
force-push as conflict resolution
deleting one branch to hide the conflict
```

The objective is human reconciliation.

## 12. Qualification evidence

The complete merge-conflict lifecycle is reproducible in a disposable local repository.

No network access is required.
