# MarketPulse Advanced Track

## 1. Purpose

This directory contains optional advanced student practice for MarketPulse.

The advanced track exists to provide additional professional depth after the common TD objectives are complete.

It is not a second mandatory curriculum.

The governing rule is:

```text
CORE
before
ADVANCED
```

and:

```text
ADVANCED
is never required
for Checkpoint A, B or C
```

Student-facing CORE labs remain under:

```text
docs/labs/
```

Instructor conceptual depth remains under:

```text
docs/instructor/
```

## 2. Status model

Advanced supports use these operational statuses.

### READY_TO_TEACH

```text
support exists
+
required execution has been validated
+
student-facing activation is allowed
```

### PENDING_EXTERNAL

```text
support exists
+
local/static qualification is complete
+
a real external environment is still required
```

A `PENDING_EXTERNAL` support must not be presented as a validated student exercise until its delivery gate passes.

### DEFERRED

```text
intentionally postponed
```

## 3. Current P1 state

```text
12 P1 supports exist

7 READY_TO_TEACH
5 PENDING_EXTERNAL
0 ambiguous
```

READY_TO_TEACH:

```text
ADV-LNX-01
ADV-LNX-02
ADV-LNX-03
ADV-LNX-04
ADV-GIT-01
ADV-GIT-02
ADV-GIT-04
```

PENDING_EXTERNAL:

```text
ADV-RMT-01
ADV-RMT-03
ADV-BBG-01
ADV-DASH-01
ADV-DASH-02
```

## 4. How to use the advanced track

A student should start an advanced activity only when:

```text
the current TD CORE is complete
+
checkpoint preparation is not at risk
+
the prerequisites are satisfied
+
the support status permits delivery
```

Recommended decision flow:

```text
CORE complete?
    |
   no
    |
    v
stay in CORE

    |
   yes
    |
    v
OPTIONAL useful?
    |
   maybe
    |
    v
complete lightweight extension

    |
    v
ADVANCED prerequisite satisfied?
    |
   no
    |
    v
stop

    |
   yes
    |
    v
support READY_TO_TEACH?
    |
   no
    |
    v
do not activate

    |
   yes
    |
    v
start advanced practice
```

## 5. Delivery modes

### SELF_STUDY_CAPABLE

The activity can be completed independently from the written support after prerequisites are met.

The instructor may still help, but no special infrastructure or proprietary access is required.

### INSTRUCTOR_GUIDED

The activity is executable locally, but instructor guidance is useful because the operation may be destructive, conceptually subtle or workflow-sensitive.

### INSTRUCTOR_DEPENDENT

The support depends on an instructor-approved external environment, proprietary access, service-management permissions or another controlled delivery gate.

Do not self-provision paid infrastructure merely to complete it.

## 6. P1 catalog

| ID | Domain | Topic | Status | Mode | Duration | Delivery | Main prerequisite |
|---|---|---|---|---|---|---|---|
| ADV-LNX-01 | Linux | File operations | READY_TO_TEACH | MINI_LAB | 30 min | SELF_STUDY_CAPABLE | TD01 CORE |
| ADV-LNX-02 | Linux | Permissions and chmod | READY_TO_TEACH | MINI_LAB | 30-45 min | SELF_STUDY_CAPABLE | TD01 CORE + file operations |
| ADV-LNX-03 | Linux | Pipes and text processing | READY_TO_TEACH | ADVANCED_LAB | 60-90 min | SELF_STUDY_CAPABLE | TD01 CORE |
| ADV-LNX-04 | Linux/Python | Environment variables | READY_TO_TEACH | MINI_LAB | 30 min | SELF_STUDY_CAPABLE | TD02 CORE |
| ADV-GIT-01 | Git | Conflict resolution | READY_TO_TEACH | MINI_LAB | 30-45 min | INSTRUCTOR_GUIDED | TD04 CORE |
| ADV-GIT-02 | Git | Restore, revert and reset | READY_TO_TEACH | ADVANCED_LAB | 60 min | INSTRUCTOR_GUIDED | TD03 CORE |
| ADV-GIT-04 | Git | Tags and releases | READY_TO_TEACH | MINI_LAB | 30-45 min | SELF_STUDY_CAPABLE | TD12 CORE |
| ADV-RMT-01 | Remote Linux | SSH fundamentals | PENDING_EXTERNAL | ADVANCED_LAB | 60 min | INSTRUCTOR_DEPENDENT | TD01 CORE + approved host |
| ADV-RMT-03 | Remote Linux | systemd service | PENDING_EXTERNAL | ADVANCED_LAB | 60-90 min | INSTRUCTOR_DEPENDENT | TD11 CORE + approved systemd host |
| ADV-BBG-01 | Bloomberg | Reference data | PENDING_EXTERNAL | MINI_LAB | 30-45 min | INSTRUCTOR_DEPENDENT | TD09-TD10 CORE + Bloomberg LIVE |
| ADV-DASH-01 | Dash | Callback | PENDING_EXTERNAL | MINI_LAB | 30-45 min | INSTRUCTOR_DEPENDENT | TD11 CORE + validated Dash runtime |
| ADV-DASH-02 | Dash | Instrument selector | PENDING_EXTERNAL | MINI_LAB | 30-45 min | INSTRUCTOR_DEPENDENT | ADV-DASH-01 + parameterized application |

## 7. Linux path

Recommended order:

```text
TD01 CORE
   |
   v
ADV-LNX-01
   |
   v
ADV-LNX-02

TD01 CORE
   |
   v
ADV-LNX-03

TD02 CORE
   |
   v
ADV-LNX-04
```

Supports:

- [ADV-LNX-01 - File Operations](ADV_LNX_01_FILE_OPERATIONS.md)
- [ADV-LNX-02 - Permissions and chmod](ADV_LNX_02_PERMISSIONS_CHMOD.md)
- [ADV-LNX-03 - Pipes and Text Processing](ADV_LNX_03_PIPES_TEXT_PROCESSING.md)
- [ADV-LNX-04 - Environment Variables](ADV_LNX_04_ENVIRONMENT_VARIABLES.md)

Use this path when the student wants stronger command-line autonomy.

## 8. Git path

Recommended order:

```text
TD03 CORE
   |
   v
ADV-GIT-02

TD04 CORE
   |
   v
ADV-GIT-01

TD12 CORE
   |
   v
ADV-GIT-04
```

Supports:

- [ADV-GIT-01 - Conflict Resolution](ADV_GIT_01_CONFLICT_RESOLUTION.md)
- [ADV-GIT-02 - Restore, Revert and Reset](ADV_GIT_02_RESTORE_REVERT_RESET.md)
- [ADV-GIT-04 - Tags and Releases](ADV_GIT_04_TAGS_RELEASES.md)

Important:

```text
destructive Git concepts
must be practiced in disposable repositories
before they are used on shared work
```

## 9. Remote Linux path

Planned path:

```text
TD12 or approved post-CORE context
        |
        v
ADV-RMT-01
        |
        v
ADV-RMT-03
```

Supports:

- [ADV-RMT-01 - SSH Fundamentals](ADV_RMT_01_SSH_FUNDAMENTALS.md)
- [ADV-RMT-03 - systemd Service](ADV_RMT_03_SYSTEMD_SERVICE.md)

Current status:

```text
PENDING_EXTERNAL
```

External requirements include:

```text
approved Linux host
approved account model
SSH client
systemd where relevant
approved permissions
```

Never require:

```text
personal cloud payment
personal credit card
shared private key
committed credential
```

## 10. Bloomberg path

Current P1 support:

- [ADV-BBG-01 - Bloomberg Reference Data](ADV_BBG_01_REFERENCE_DATA.md)

Current status:

```text
PENDING_EXTERNAL
```

Required environment:

```text
validated Bloomberg LIVE access
+
approved connector or Terminal workflow
+
observed current identifiers/fields
```

If LIVE access is unavailable:

```text
skip the lab
```

Do not convert:

```text
APPROVED_SAMPLE
```

into fake LIVE evidence.

## 11. Dash path

Planned order:

```text
TD11 CORE
   |
   v
ADV-DASH-01
   |
   v
ADV-DASH-02
```

Supports:

- [ADV-DASH-01 - Callback](ADV_DASH_01_CALLBACK.md)
- [ADV-DASH-02 - Instrument Selector](ADV_DASH_02_INSTRUMENT_SELECTOR.md)

Current status:

```text
PENDING_EXTERNAL
```

Activation requires:

```text
real Dash runtime validation
+
application boundary preserved
```

For ADV-DASH-02, also require:

```text
parameterized application state
```

Do not implement:

```text
callback
-> direct provider-specific logic
-> duplicated analytics
```

## 12. Infrastructure matrix

| Support | Network required | External host | Proprietary access | Elevated permissions | Local-only possible |
|---|---:|---:|---:|---:|---:|
| ADV-LNX-01 | No | No | No | No | Yes |
| ADV-LNX-02 | No | No | No | No | Yes |
| ADV-LNX-03 | No | No | No | No | Yes |
| ADV-LNX-04 | No | No | No | No | Yes |
| ADV-GIT-01 | No | No | No | No | Yes |
| ADV-GIT-02 | No | No | No | No | Yes |
| ADV-GIT-04 | No | No | No | No | Yes |
| ADV-RMT-01 | Yes | Yes | No | No by default | No |
| ADV-RMT-03 | Yes | Yes | No | Environment-dependent | No |
| ADV-BBG-01 | Environment-dependent | Bloomberg environment | Yes | No | No |
| ADV-DASH-01 | No after dependencies exist | No | No | No | Yes after runtime validation |
| ADV-DASH-02 | No after dependencies exist | No | No | No | Yes after runtime validation |

## 13. Diagnostic-driven selection

Diagnostic results may guide which advanced activities are realistic for a cohort.

They must never change the mandatory CORE.

### Strong Linux ceiling

Possible choices:

```text
ADV-LNX-01
ADV-LNX-02
ADV-LNX-03
ADV-LNX-04
```

### Strong Git ceiling

Possible choices:

```text
ADV-GIT-01
ADV-GIT-02
ADV-GIT-04
```

### Strong Dash knowledge

Potential future activation:

```text
ADV-DASH-01
ADV-DASH-02
```

only after their delivery gates pass.

### Strong Bloomberg cohort

Potential future activation:

```text
ADV-BBG-01
```

only with validated LIVE access.

Important:

```text
strong diagnostic results
!=
permission to increase checkpoint requirements
```

## 14. Selection by available time

### 15-30 minutes

Choose a short READY_TO_TEACH activity such as:

```text
ADV-LNX-01
ADV-LNX-04
```

or begin a 30-45 minute mini-lab only when the real remaining time is sufficient.

### 30-45 minutes

Good choices:

```text
ADV-LNX-02
ADV-GIT-01
ADV-GIT-04
```

### 60 minutes

Good choice:

```text
ADV-GIT-02
```

### 60-90 minutes

Good choice:

```text
ADV-LNX-03
```

External-gated 60-90 minute supports remain unavailable until their gate passes.

## 15. Self-study recommendations

Best current self-study candidates:

```text
ADV-LNX-01
ADV-LNX-02
ADV-LNX-03
ADV-LNX-04
ADV-GIT-04
```

Instructor-guided candidates:

```text
ADV-GIT-01
ADV-GIT-02
```

Instructor-dependent candidates:

```text
ADV-RMT-01
ADV-RMT-03
ADV-BBG-01
ADV-DASH-01
ADV-DASH-02
```

## 16. Relationship with instructor material

Advanced student practice and instructor enrichment are different layers.

```text
docs/advanced/
=
student practice

docs/instructor/deep-dives/
=
teacher mental models

docs/instructor/02_TD_ENRICHMENT_CAPSULES.md
=
short teacher-led classroom explanations
```

Example:

```text
CAP-LNX-02
=
5-minute permissions explanation

ADV-LNX-02
=
30-45 minute permissions practice
```

Do not merge these layers.

## 17. Relationship with OPTIONAL work

OPTIONAL remains inside each TD.

OPTIONAL means:

```text
lightweight continuation
normally 5 to 20 minutes
same local concept
no major new capability
```

ADVANCED means:

```text
deeper practice
new capability or deeper engineering model
dedicated support
own prerequisites
own DoD
own cleanup/security rules
```

## 18. P2 and P3 backlog

This directory currently packages the implemented P1 supports only.

Other Legacy-derived candidates remain governed by:

```text
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
```

Examples include:

```text
ADV-LNX-05 Bash scripting
ADV-LNX-06 Cron scheduling

ADV-GIT-03 Interactive rebase
ADV-GIT-05 Git aliases

ADV-RMT-02 SCP
ADV-RMT-04 VPS deployment

ADV-BBG-02 xbbg exploration
ADV-BBG-03 blpapi low-level request
ADV-BBG-04 Intraday bars

ADV-DEP-01 Docker
ADV-DEP-02 GitHub Actions
ADV-DEP-03 Service + reverse proxy
```

These are not automatically READY_TO_TEACH.

Do not create a student link merely because an item exists in the backlog.

## 19. Promotion rule for PENDING_EXTERNAL

A support may move:

```text
PENDING_EXTERNAL
->
READY_TO_TEACH
```

only when:

```text
real required environment exists
commands or runtime are executed
expected output is observed
cleanup/recovery is verified
security constraints are satisfied
no fabricated evidence is used
```

After promotion:

```text
update support status
update docs/labs/README.md
activate the relevant TD link
update the backlog
update the migration registry
update R7 closure evidence if useful
```

The frozen CORE does not need to be reopened.

## 20. Student safety checklist

Before any advanced activity:

```text
[ ] CORE is complete
[ ] checkpoint preparation is safe
[ ] support status permits delivery
[ ] prerequisites are satisfied
[ ] disposable environment is used where required
[ ] no secret is committed
[ ] no personal payment is required
[ ] cleanup procedure is understood
```

## 21. Instructor delivery checklist

Before offering an advanced activity:

```text
[ ] support status checked
[ ] duration fits real remaining time
[ ] prerequisites are actually met
[ ] external gates verified when applicable
[ ] checkpoint preparation will not be harmed
[ ] recovery/cleanup path is known
[ ] advanced work is still clearly optional
```

## 22. Canonical references

Teaching taxonomy and active links:

```text
docs/labs/README.md
```

Advanced backlog:

```text
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
```

Final P1 qualification:

```text
docs/legacy/07_R7_4_ADVANCED_QUALIFICATION_AND_CLOSURE.md
```

Legacy roadmap:

```text
docs/legacy/04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
```

Instructor enrichment:

```text
docs/instructor/02_TD_ENRICHMENT_CAPSULES.md
```

## 23. Packaging conclusion

The advanced track is now packaged as:

```text
one navigable index
+
12 P1 support documents
+
status-aware activation
+
diagnostic-driven selection guidance
+
time-based selection guidance
+
infrastructure gates
+
self-study / guided / dependent delivery modes
```

Rule:

```text
advanced track
!=
second mandatory curriculum
```
