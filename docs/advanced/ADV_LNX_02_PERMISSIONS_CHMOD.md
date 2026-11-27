# ADV-LNX-02 - Permissions and chmod

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

Understand:

```text
read
write
execute
owner
group
others
```

and safely use:

```text
chmod
```

## 2. Prerequisites

```text
TD01 CORE complete
basic file operations understood
```

This activity is not required for any checkpoint.

## 3. Setup

Create a disposable script:

```bash
mkdir -p sandbox/scripts
printf '#!/usr/bin/env bash\necho "MarketPulse permissions lab"\n' > sandbox/scripts/hello.sh
chmod 644 sandbox/scripts/hello.sh
ls -l sandbox/scripts/hello.sh
```

## 4. Observe the failure

Try:

```bash
./sandbox/scripts/hello.sh
```

Expected:

```text
execution is denied because execute permission is absent
```

The exact shell error wording may vary.

## 5. Add execute permission safely

Run:

```bash
chmod u+x sandbox/scripts/hello.sh
ls -l sandbox/scripts/hello.sh
./sandbox/scripts/hello.sh
```

Expected output:

```text
MarketPulse permissions lab
```

## 6. Read the permission model

Use the left side of:

```bash
ls -l sandbox/scripts/hello.sh
```

to identify:

```text
owner permissions
group permissions
other permissions
```

Explain:

```text
u = user / owner
g = group
o = others
+x = add execute permission
```

## 7. Definition of done

```text
[ ] inspect ls -l
[ ] identify owner/group/others
[ ] explain read/write/execute
[ ] add execute permission to owner
[ ] execute the harmless script
[ ] explain why chmod 777 is not a generic fix
```

## 8. Cleanup

```bash
rm -rf sandbox
```

## 9. Security guardrails

Do not use:

```text
chmod 777
sudo as a generic fix
system files
real credentials
SSH private keys
production scripts
```

## 10. Qualification evidence

The workflow is locally reproducible using standard Linux permissions.

The exercise explicitly avoids privileged operations and system files.

## 11. Optional extension

Remove execute permission again:

```bash
chmod u-x sandbox/scripts/hello.sh
```

Explain why the file is still readable but no longer directly executable.
