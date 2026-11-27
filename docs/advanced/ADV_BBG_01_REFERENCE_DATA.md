# ADV-BBG-01 - Bloomberg Reference Data

Status:

```text
PENDING_EXTERNAL
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

Explore non-historical Bloomberg reference data in an instructor-approved LIVE environment.

## 2. Prerequisites

```text
TD09 CORE complete
TD10 CORE complete
Bloomberg LIVE environment validated
instructor-approved access method known
```

This activity is not required for Checkpoint C.

## 3. Delivery gate

Before teaching, verify:

```text
[ ] LIVE Bloomberg access succeeds
[ ] approved connector or Terminal workflow is known
[ ] chosen identifiers are authorized
[ ] chosen fields are actually available
[ ] no credential is exposed
[ ] current field names are observed rather than guessed
```

If the gate fails:

```text
SKIP THE LAB
```

Do not convert APPROVED_SAMPLE into fake LIVE reference-data evidence.

## 4. Candidate learning questions

Use the current approved environment to answer questions such as:

```text
What is the security name?
What security type is reported?
What currency is reported?
What exchange code is reported?
```

The exact field identifiers must come from the verified current environment.

## 5. Record observed request context

Students should record:

```text
canonical ticker
provider identifier
observed field name
observed value
access mode = LIVE
```

Example structure:

```text
canonical ticker : AAPL
provider id      : AAPL US Equity
field            : <observed field>
value            : <observed value>
mode             : LIVE
```

## 6. Compare with MarketPulse historical acquisition

Explain:

```text
reference data
=
descriptive/security attributes

historical data
=
observations over time
```

The advanced exercise does not change the 1 month / Daily CORE.

## 7. Definition of done

```text
[ ] use the approved LIVE mechanism
[ ] retrieve at least one instructor-approved reference field
[ ] record the provider identifier
[ ] record the observed field name
[ ] record the observed value
[ ] distinguish reference data from historical data
[ ] expose no credential
```

## 8. Guardrails

Do not:

```text
guess Bloomberg field names
claim APPROVED_SAMPLE is LIVE
add an unverified package to requirements.txt
share Bloomberg credentials
invent values when access fails
```

## 9. Cleanup

Remove temporary scratch output that contains environment-specific metadata if it is not intended for the repository.

No credential or workstation detail belongs in Git.

## 10. Qualification status

The pedagogical support is complete.

Real execution cannot be validated without the approved Bloomberg LIVE environment.

Therefore:

```text
support design
=
COMPLETE

Bloomberg reference retrieval
=
EXTERNAL VERIFY
```

Promotion to unconditional READY_TO_TEACH requires the Bloomberg pre-class LIVE gate.
