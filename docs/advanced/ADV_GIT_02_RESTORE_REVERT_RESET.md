# ADV-GIT-02 - Restore, Revert and Reset

Status:

```text
READY_TO_TEACH
```

Mode:

```text
ADVANCED_LAB
```

Estimated duration:

```text
60 minutes
```

## 1. Objective

Distinguish three different Git recovery mechanisms:

```text
restore
revert
reset
```

## 2. Prerequisites

```text
TD03 CORE complete
basic commits and status understood
```

This activity is not required for any checkpoint.

## 3. Safety rule

Use a disposable repository only.

Never learn destructive reset first on the team repository.

## 4. Setup

```bash
mkdir git-undo-lab
cd git-undo-lab
git init
git config user.name "MarketPulse Lab"
git config user.email "lab@example.invalid"
printf "version=1\n" > state.txt
git add state.txt
git commit -m "chore: add initial state"
```

## 5. Restore an unstaged change

```bash
printf "version=broken\n" > state.txt
git diff
git restore state.txt
cat state.txt
```

Expected:

```text
version=1
```

## 6. Unstage safely

```bash
printf "version=2\n" > state.txt
git add state.txt
git diff --staged
git restore --staged state.txt
git status
```

The working change remains.

Commit it deliberately:

```bash
git add state.txt
git commit -m "feat: move to version 2"
```

## 7. Revert a commit

Create another commit:

```bash
printf "version=3\n" > state.txt
git add state.txt
git commit -m "feat: move to version 3"
```

Then:

```bash
git revert --no-edit HEAD
git log --oneline -4
cat state.txt
```

Explain:

```text
revert
=
new commit that reverses a previous commit
```

## 8. Observe reset safely

Create a disposable commit:

```bash
printf "temporary=yes\n" >> state.txt
git add state.txt
git commit -m "test: disposable commit"
git log --oneline -3
```

Save its identifier:

```bash
git rev-parse HEAD
```

Then move the branch back one commit:

```bash
git reset --hard HEAD~1
git log --oneline -3
```

Explain:

```text
reset
=
move the current branch reference

--hard
=
also replace index and working tree
```

This is why it is dangerous on real work.

## 9. Definition of done

```text
[ ] restore an unstaged change
[ ] unstage while keeping the working change
[ ] revert a commit
[ ] inspect the extra revert commit
[ ] demonstrate reset only in a disposable repo
[ ] explain why reset --hard is dangerous
```

## 10. Cleanup

From the parent directory:

```bash
rm -rf git-undo-lab
```

## 11. Guardrails

Do not:

```text
run reset --hard on team main
rewrite published history for this exercise
use force push
practice with unpreserved work
```

## 12. Qualification evidence

All recovery commands are designed for a disposable local repository and leave no dependency on GitHub or external services.
