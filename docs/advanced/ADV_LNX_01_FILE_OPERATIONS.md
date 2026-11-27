# ADV-LNX-01 - File Operations

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

Practice safe Linux file operations with:

```text
mkdir
touch
cp
mv
rm
```

without modifying real MarketPulse project files.

## 2. Prerequisites

```text
TD01 CORE complete
comfortable with pwd / ls / cd
```

This activity is not required for any checkpoint.

## 3. MarketPulse relationship

The lab uses a disposable directory that resembles a small data workspace.

It reinforces Linux autonomy without changing the MarketPulse runtime.

## 4. Setup

From the repository root:

```bash
mkdir -p sandbox/raw sandbox/archive sandbox/notes
touch sandbox/raw/aapl.csv
printf "date,ticker,close\n2026-09-01,AAPL,250.00\n" > sandbox/raw/aapl.csv
```

Inspect:

```bash
find sandbox -maxdepth 2 -type f -o -type d
```

## 5. Exercise

Create a note:

```bash
touch sandbox/notes/session.txt
```

Copy the sample:

```bash
cp sandbox/raw/aapl.csv sandbox/archive/aapl_copy.csv
```

Rename it:

```bash
mv sandbox/archive/aapl_copy.csv sandbox/archive/aapl_snapshot.csv
```

Inspect:

```bash
ls -R sandbox
cat sandbox/archive/aapl_snapshot.csv
```

Remove only the disposable note:

```bash
rm sandbox/notes/session.txt
```

## 6. Definition of done

```text
[ ] create a directory
[ ] create a file
[ ] copy a file
[ ] move or rename a file
[ ] remove a disposable file
[ ] explain copy vs move
[ ] verify real project files were not modified
```

## 7. Expected result

The final disposable tree should contain:

```text
sandbox/
├── archive/
│   └── aapl_snapshot.csv
├── notes/
└── raw/
    └── aapl.csv
```

## 8. Cleanup

Remove only the sandbox:

```bash
rm -rf sandbox
```

Before running the command, verify:

```bash
pwd
ls sandbox
```

Never adapt this cleanup command to a real project directory.

## 9. Safety guardrails

Do not:

```text
rm -rf .
rm -rf ..
remove src/
remove data/
remove .git/
practice inside a production directory
```

## 10. Qualification evidence

Validated with a disposable Linux filesystem workflow:

```text
mkdir
touch
printf
cp
mv
ls
cat
rm
rm -rf sandbox
```

The exercise has deterministic observable output and an explicit cleanup path.

## 11. Optional extension

Add a second disposable ticker file and create a second archive snapshot.

Keep the exercise inside `sandbox/`.
