# ADV-LNX-04 - Environment Variables

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
30 minutes
```

## 1. Objective

Understand the difference between:

```text
shell variable
environment variable
Python variable
```

and how a process receives configuration from its environment.

## 2. Prerequisites

```text
TD02 CORE complete
basic Python imports understood
```

This activity is not required for any checkpoint.

## 3. Shell variable vs exported environment variable

Run:

```bash
MARKETPULSE_MODE=demo
python -c 'import os; print(os.environ.get("MARKETPULSE_MODE"))'
```

Expected:

```text
None
```

Now export it:

```bash
export MARKETPULSE_MODE=demo
python -c 'import os; print(os.environ.get("MARKETPULSE_MODE"))'
```

Expected:

```text
demo
```

## 4. Python variable

Run:

```bash
python -c 'mode = "python-demo"; print(mode)'
```

Explain:

```text
Python variable
=
value inside the Python process

environment variable
=
name/value inherited from the process environment
```

## 5. Temporary single-command environment

Run:

```bash
MARKETPULSE_MODE=temporary python -c 'import os; print(os.environ.get("MARKETPULSE_MODE"))'
```

Then:

```bash
echo "$MARKETPULSE_MODE"
```

The exported shell value remains unchanged.

## 6. Definition of done

```text
[ ] distinguish shell vs environment variable
[ ] read an environment variable from Python
[ ] use one-command environment assignment
[ ] explain why configuration and secrets are different concerns
```

## 7. Cleanup

```bash
unset MARKETPULSE_MODE
```

Verify:

```bash
python -c 'import os; print(os.environ.get("MARKETPULSE_MODE"))'
```

Expected:

```text
None
```

## 8. Security guardrails

Do not use a real:

```text
password
API key
token
Bloomberg credential
cloud credential
```

for this exercise.

Environment variables can hold secrets in real systems, but this lab uses only non-sensitive demo values.

## 9. Qualification evidence

The exercise uses Python standard library `os` and POSIX-style shell environment semantics.

No project file or CORE command is modified.

## 10. Optional extension

Create a disposable Python file that prints a non-sensitive environment setting with a default value.

Do not commit real secrets.
