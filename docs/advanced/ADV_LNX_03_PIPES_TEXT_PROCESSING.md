# ADV-LNX-03 - Pipes and Text Processing

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
60-90 minutes
```

## 1. Objective

Practice Unix composition using:

```text
|
grep
wc
awk
sed
```

on project-controlled text data.

## 2. Prerequisites

```text
TD01 CORE complete
local MarketPulse files available
```

This activity is not required for any checkpoint.

## 3. Data rule

Use:

```text
data/sample/prices.csv
```

or a disposable copy.

Do not use arbitrary web scraping in this lab.

## 4. Count AAPL rows

Run:

```bash
grep AAPL data/sample/prices.csv | wc -l
```

Expected common sample result:

```text
21
```

Then:

```bash
grep SP500 data/sample/prices.csv | wc -l
```

Expected:

```text
21
```

## 5. Extract selected columns with awk

Inspect the header first:

```bash
head -n 1 data/sample/prices.csv
```

Then extract the date and ticker columns:

```bash
awk -F',' 'NR==1 {print $1 "," $2} NR>1 && $2=="AAPL" {print $1 "," $2}' data/sample/prices.csv | head
```

Explain:

```text
-F','
=
comma delimiter

NR
=
current record number

$1 / $2
=
selected fields
```

## 6. Compose grep and awk

Example:

```bash
grep AAPL data/sample/prices.csv | awk -F',' '{print $1 "," $2 "," $6}' | head
```

Explain that each command performs one step.

## 7. Use sed on disposable output

Create:

```bash
mkdir -p sandbox
grep AAPL data/sample/prices.csv > sandbox/aapl_rows.csv
```

Preview a harmless substitution:

```bash
sed 's/AAPL/APPLE_DEMO/g' sandbox/aapl_rows.csv | head
```

The source file is not modified.

## 8. Definition of done

```text
[ ] use one pipe
[ ] combine grep and wc
[ ] use awk on comma-delimited text
[ ] extract selected fields
[ ] use sed without overwriting the source
[ ] explain why each command has one responsibility
```

## 9. Cleanup

```bash
rm -rf sandbox
```

## 10. Safety guardrails

Do not:

```text
scrape external sites for this exercise
overwrite data/sample/prices.csv
use sed -i on the canonical sample
pipe secrets into logs
```

## 11. Qualification evidence

The core commands are standard Unix tools and produce deterministic results against the 21 + 21 MarketPulse sample.

## 12. Optional extension

Explore one regular expression with `grep -E`.

Keep the extension read-only.
