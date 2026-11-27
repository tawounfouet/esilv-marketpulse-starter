# ADV-RMT-03 - systemd Service

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
60-90 minutes
```

## 1. Objective

Run the MarketPulse dashboard as a managed Linux service and inspect its lifecycle with systemd.

## 2. Prerequisites

```text
TD11 CORE complete
python src/dashboard.py works
remote Linux host available
systemd is the active service manager
approved privilege model exists
```

This activity is not required for Checkpoint C.

## 3. Delivery gate

Verify before teaching:

```text
[ ] remote host uses systemd
[ ] systemctl operates normally
[ ] students have approved service-management permissions
[ ] MarketPulse environment path is known
[ ] Python executable path is known
[ ] dashboard command works on the host
[ ] no secret is required inside the unit file
```

## 4. Unit-file template

Create an instructor-approved unit outside the repository or from a disposable template.

Example:

```ini
[Unit]
Description=MarketPulse training dashboard
After=network.target

[Service]
Type=simple
User=<approved-user>
WorkingDirectory=<absolute-marketpulse-path>
ExecStart=<absolute-python-path> src/dashboard.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Do not commit environment-specific absolute paths to the common course repository.

## 5. Validate the unit before activation

Where available:

```bash
systemd-analyze verify <unit-file>
```

Fix syntax or executable-path errors before installation.

## 6. Install through the approved host procedure

The exact install command depends on the instructor-approved privilege model.

Typical administrator-managed systems place service units under a system service directory.

Do not teach students to copy files into privileged locations unless the environment was provisioned for that purpose.

## 7. Service lifecycle

Once installed and reloaded through the approved procedure:

```bash
systemctl status <service-name>
systemctl start <service-name>
systemctl status <service-name>
journalctl -u <service-name> --no-pager -n 30
systemctl stop <service-name>
systemctl status <service-name>
```

Use the exact command form authorized for the teaching host.

## 8. Definition of done

```text
[ ] explain Unit / Service / Install sections
[ ] validate the unit structure
[ ] start the approved service
[ ] inspect service status
[ ] inspect recent logs
[ ] stop the service cleanly
[ ] explain Restart=on-failure
```

## 9. Security guardrails

Do not place:

```text
password
API token
Bloomberg credential
private key
cloud secret
```

inside a committed unit file.

Do not use unrestricted sudo as a teaching shortcut.

## 10. Cleanup

Stop and disable/remove the training service using the instructor-approved host procedure.

Remove environment-specific training units when the exercise is over.

The common MarketPulse repository must remain runnable without systemd.

## 11. Qualification status

The unit-file model can be statically validated with `systemd-analyze verify`.

Actual:

```text
start
status
journalctl
stop
```

requires a real systemd teaching host.

Therefore:

```text
unit syntax
=
LOCALLY VERIFIABLE

service lifecycle
=
EXTERNAL VERIFY
```

Promotion to unconditional READY_TO_TEACH requires the host delivery gate.
