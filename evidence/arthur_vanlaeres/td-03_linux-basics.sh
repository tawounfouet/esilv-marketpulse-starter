@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ python src/main.py
=== MarketPulse ===

Instrument
AAPL - Apple Inc.
Last price: 266.20 USD

Benchmark
SP500 - S&P 500
Last level: 6742.00

Period: 1 month
Interval: Daily

Observations
AAPL: 21
SP500: 21
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ git pull
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 28 (delta 4), reused 2 (delta 2), pack-reused 19 (from 1)
Unpacking objects: 100% (28/28), 57.35 KiB | 3.82 MiB/s, done.
From https://github.com/hasaddd20/esilv-marketpulse-g06-t03
   93e96a0..0ee0bad  arthur-vanlaeres -> origin/arthur-vanlaeres
   234b439..185877b  gabriel-suissa   -> origin/gabriel-suissa
   dcd50c5..53e6a60  hugo-dussart     -> origin/hugo-dussart
Updating 93e96a0..0ee0bad
Fast-forward
 evidence/Arthur_Vanlaeres_Td2 | 11 +++++++++++
 1 file changed, 11 insertions(+)
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ git switch main
Switched to branch 'main'
Your branch is behind 'origin/main' by 3 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (main) $ git pull
Updating 80cebf6..462eeb0
Fast-forward
 TEAM.md | 64 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 64 insertions(+)
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (main) $ git pull
remote: Enumerating objects: 2, done.
remote: Counting objects: 100% (2/2), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (2/2), 1.26 KiB | 1.26 MiB/s, done.
From https://github.com/hasaddd20/esilv-marketpulse-g06-t03
   462eeb0..0cf130b  main       -> origin/main
Updating 462eeb0..0cf130b
Fast-forward
 data/README.md                          | 320 +++++++
 docs/labs/TD04_BRANCHES_AND_MERGE.md    | 812 +++++++++++++++++
 docs/labs/TD05_FORK_AND_PULL_REQUEST.md | 907 +++++++++++++++++++
 docs/labs/TD06_CODE_REVIEW.md           | 678 ++++++++++++++
 notebooks/00_python_fundamentals.ipynb  | 734 +++++++++++++++
 notebooks/00_td02_sandbox.ipynb         | 425 +++++++++
 notebooks/01_analytics.ipynb            | 287 ++++++
 notebooks/02_yahoo_provider.ipynb       | 218 +++++
 notebooks/03_bloomberg_provider.ipynb   | 249 +++++
 notebooks/04_market_snapshot_main.ipynb | 280 ++++++
 notebooks/05_dashboard.ipynb            | 552 +++++++++++
 notebooks/README.md                     |  86 ++
 12 files changed, 5548 insertions(+)
 create mode 100644 data/README.md
 create mode 100644 docs/labs/TD04_BRANCHES_AND_MERGE.md
 create mode 100644 docs/labs/TD05_FORK_AND_PULL_REQUEST.md
 create mode 100644 docs/labs/TD06_CODE_REVIEW.md
 create mode 100644 notebooks/00_python_fundamentals.ipynb
 create mode 100644 notebooks/00_td02_sandbox.ipynb
 create mode 100644 notebooks/01_analytics.ipynb
 create mode 100644 notebooks/02_yahoo_provider.ipynb
 create mode 100644 notebooks/03_bloomberg_provider.ipynb
 create mode 100644 notebooks/04_market_snapshot_main.ipynb
 create mode 100644 notebooks/05_dashboard.ipynb
 create mode 100644 notebooks/README.md
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (main) $ git switch arthur-vanlaeres
Switched to branch 'arthur-vanlaeres'
Your branch is up to date with 'origin/arthur-vanlaeres'.
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ git pull
Already up to date.
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (main) $ git switch arthur-vanlaeres
Switched to branch 'arthur-vanlaeres'
Your branch is up to date with 'origin/arthur-vanlaeres'.
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ git branch
* arthur-vanlaeres
  main
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ git status
On branch arthur-vanlaeres
Your branch is up to date with 'origin/arthur-vanlaeres'.

nothing to commit, working tree clean
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ git diff --name-status main...arthur-vanlaeres
A       evidence/Arthur_Vanlaeres_Td2
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ pwd
/workspaces/esilv-marketpulse-g06-t03
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ ls -la
total 64
drwxrwxrwx+ 8 codespace root       4096 Oct 23 06:49 .
drwxr-xrwx+ 5 codespace root       4096 Oct 16 07:26 ..
drwxrwxrwx+ 8 codespace root       4096 Oct 23 06:52 .git
-rw-rw-rw-  1 codespace root        178 Oct 16 07:26 .gitignore
-rw-rw-rw-  1 codespace root       2943 Oct 16 07:26 CONTRIBUTING.md
-rw-rw-rw-  1 codespace root      10270 Oct 16 07:26 README.md
-rw-rw-rw-  1 codespace codespace     1 Oct 23 06:49 TEAM.md
-rw-rw-rw-  1 codespace root       1446 Oct 16 07:26 TEAM_TEMPLATE.md
drwxrwxrwx+ 2 codespace root       4096 Oct 16 07:26 config
drwxrwxrwx+ 3 codespace root       4096 Oct 23 06:49 data
drwxrwxrwx+ 4 codespace root       4096 Oct 16 07:26 docs
drwxrwxrwx+ 2 codespace root       4096 Oct 23 06:49 evidence
-rw-rw-rw-  1 codespace root        133 Oct 16 07:26 requirements.txt
drwxrwxrwx+ 2 codespace root       4096 Oct 16 07:26 src
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ cd data
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/data (arthur-vanlaeres) $ pwd
/workspaces/esilv-marketpulse-g06-t03/data
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/data (arthur-vanlaeres) $ cd ..
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ pwd
/workspaces/esilv-marketpulse-g06-t03
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ cd data
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/data (arthur-vanlaeres) $ cd sample
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/data/sample (arthur-vanlaeres) $ cd data/sample
bash: cd: data/sample: No such file or directory
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/data/sample (arthur-vanlaeres) $ ls
bloomberg_reference_expected.json
bloomberg_reference_sample.json
instruments.json
prices.csv
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/data/sample (arthur-vanlaeres) $ cd data
bash: cd: data: No such file or directory
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/data/sample (arthur-vanlaeres) $ cd ..
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/data (arthur-vanlaeres) $ cd ..
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ cd evidence
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/evidence (arthur-vanlaeres) $ cd evidence/
bash: cd: evidence/: No such file or directory
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/evidence (arthur-vanlaeres) $ mkdir arthur_vanlaeres
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/evidence (arthur-vanlaeres) $ mv Arthur_Vanlaeres_Td2 evidence/arthur_vanlaeres
mv: cannot move 'Arthur_Vanlaeres_Td2' to 'evidence/arthur_vanlaeres': No such file or directory
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/evidence (arthur-vanlaeres) $ cd ..
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ pwd
/workspaces/esilv-marketpulse-g06-t03
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03 (arthur-vanlaeres) $ cd evidence/arthur_vanlaeres
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/evidence/arthur_vanlaeres (arthur-vanlaeres) $ ls -la
total 8
drwxrwxrwx+ 2 codespace codespace 4096 Oct 23 07:02 .
drwxrwxrwx+ 3 codespace root      4096 Oct 23 07:02 ..
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/evidence/arthur_vanlaeres (arthur-vanlaeres) $ touch td-03_linux-basics.sh
@arthurvlrs05-rgb ➜ /workspaces/esilv-marketpulse-g06-t03/evidence/arthur_vanlaeres (arthur-vanlaeres) $ 