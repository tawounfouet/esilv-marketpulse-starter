# ADV-GIT-04 - Tags and Releases

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

Understand the difference between:

```text
commit
branch
tag
release
```

and create an annotated local Git tag.

## 2. Prerequisites

```text
TD12 CORE complete
clean completed repository
```

This activity is not required for Checkpoint C.

## 3. Safety model

Use the team repository only if the instructor explicitly approves creating a real tag.

Otherwise use a disposable repository.

## 4. Disposable setup

```bash
mkdir tag-lab
cd tag-lab
git init
git config user.name "MarketPulse Lab"
git config user.email "lab@example.invalid"
printf "MarketPulse release candidate\n" > README.md
git add README.md
git commit -m "chore: add release candidate"
```

## 5. Inspect tags

```bash
git tag
```

Expected:

```text
no tag yet
```

## 6. Create an annotated tag

```bash
git tag -a v1.0.0-training -m "MarketPulse training release"
git tag
git show v1.0.0-training
```

Identify:

```text
tag name
tag message
tagger
target commit
```

## 7. Compare branch and tag behaviour

Create another commit:

```bash
printf "post-release change\n" >> README.md
git add README.md
git commit -m "docs: add post release change"
```

Inspect:

```bash
git log --oneline --decorate -3
git show v1.0.0-training --stat
```

Explain:

```text
branch
=
moves as new commits are added

tag
=
normally remains attached to the selected object
```

## 8. Definition of done

```text
[ ] list tags
[ ] create an annotated tag
[ ] inspect an annotated tag
[ ] explain commit vs branch vs tag
[ ] explain that a GitHub Release is a platform layer built around a tag
```

## 9. Cleanup

From the parent directory:

```bash
rm -rf tag-lab
```

## 10. Guardrails

Do not push training tags to a shared repository unless approved.

Do not invent a production semantic-versioning policy for MarketPulse.

## 11. Qualification evidence

Local annotated-tag creation and inspection require only Git and a disposable repository.

GitHub Release creation remains an optional platform extension.

## 12. Optional extension

If the teaching repository permissions and context allow it, demonstrate a GitHub Release from an approved tag.

The platform action is not required for READY_TO_TEACH status of this local lab.
