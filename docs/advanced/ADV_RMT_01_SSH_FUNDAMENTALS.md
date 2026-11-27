# ADV-RMT-01 - SSH Fundamentals

Status:

```text
PENDING_EXTERNAL
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

Connect safely to a pre-provisioned remote Linux host and understand:

```text
host
user
port
private key
known_hosts
remote shell
```

## 2. Prerequisites

```text
TD01 CORE complete
instructor-provisioned or school-provided Linux host
SSH client installed
individual access material distributed securely
```

This activity is not required for any checkpoint.

## 3. Delivery gate

Before teaching, the instructor must verify:

```text
[ ] SSH client exists in the student environment
[ ] remote host is reachable
[ ] student accounts or approved credentials exist
[ ] host key policy is known
[ ] no shared private key is required
[ ] no personal cloud account is required
[ ] no payment card is required
```

If this gate fails, skip the lab.

## 4. Inspect the client

Run:

```bash
ssh -V
```

Optional configuration inspection:

```bash
ssh -G <user>@<host> | head
```

Use instructor-provided values only.

## 5. Connect

Canonical shape:

```bash
ssh <user>@<host>
```

If a non-default port is required:

```bash
ssh -p <port> <user>@<host>
```

If an approved key file is required:

```bash
ssh -i <private-key-path> <user>@<host>
```

Do not place the private key inside the repository.

## 6. Verify the remote context

After connecting:

```bash
whoami
hostname
pwd
python --version
```

Explain:

```text
local shell
!=
remote shell
```

## 7. Run a harmless remote Python command

```bash
python -c 'print("MarketPulse remote environment")'
```

## 8. Disconnect

```bash
exit
```

Confirm you are back in the local shell.

## 9. Definition of done

```text
[ ] identify local vs remote shell
[ ] connect to the approved host
[ ] verify remote user and working directory
[ ] verify Python remotely
[ ] run a harmless Python command
[ ] disconnect cleanly
[ ] explain why private keys must remain secret
```

## 10. Security guardrails

Never require:

```text
personal cloud billing
shared account password
shared private key
committed SSH key
copying a key into TEAM.md
disabling host-key checking globally
```

## 11. Cleanup

No cloud resource is created by this lab.

If a temporary local key file was provisioned for the session, follow the instructor-approved removal procedure after the course.

Do not invent a cleanup command for credentials.

## 12. Qualification status

The support is complete, but this runner does not contain an SSH client or an approved remote teaching host.

Therefore:

```text
support design
=
COMPLETE

real SSH execution
=
EXTERNAL VERIFY
```

Promotion to unconditional READY_TO_TEACH requires the pre-class delivery gate to be executed in the actual teaching environment.
