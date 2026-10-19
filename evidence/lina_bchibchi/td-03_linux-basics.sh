@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06 (lina-bchibchi) $ cat data/sample/instruments.json
{
  "instrument": {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "currency": "USD",
    "market": "NASDAQ"
  },
  "benchmark": {
    "ticker": "SP500",
    "name": "S&P 500",
    "currency": "USD",
    "market": "US"
  }
}





nothing added to commit but untracked files present (use "git add" to track)
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06 (lina-bchibchi) $ git show --stat 92257f9
commit 92257f97fbd1471cdf21c11a692604403f81e35a
Author: Thomas AWOUNFOUET <thomas.awounfouet@gmail.com>
Date:   Wed Oct 14 12:10:20 2026 +0200

    Adde labs 1 & 2

 docs/01_STUDENT_ONBOARDING.md                     | 195 ++++++++++++++
 docs/04_CHECKPOINTS_AND_EVIDENCE.md               | 694 ++++++++++++++++++++++++++++++++++++++++++++++++++
 docs/advanced/ADV_BBG_01_REFERENCE_DATA.md        | 156 ++++++++++++
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06 (lina-bchibchi) $ git show --stat 40b3bf5
commit 40b3bf52a4a643584fe4848ec52e44d631a29404 (HEAD -> lina-bchibchi, origin/lina-bchibchi)
Author: lina-042 <lina.bchibchi@edu.devinci.fr>
Date:   Wed Oct 14 14:41:13 2026 +0000

    Commit test branch lina bchibchi

 evidence/test_branch_lina.bchibchi.txt | 21 +++++++++++++++++++++
 1 file changed, 21 insertions(+)
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06 (lina-bchibchi) $ git status
On branch lina-bchibchi
Your branch is up to date with 'origin/lina-bchibchi'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        evidence/lina_bchibchi/
        how --stat 40b3bf5

nothing added to commit but untracked files present (use "git add" to track)
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06 (lina-bchibchi) $ git diff
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06 (lina-bchibchi) $ cd evidence/
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06/evidence (lina-bchibchi) $ cp test-branch_lina.bchichi.txt td02_linabchichi.txt
cp: cannot stat 'test-branch_lina.bchichi.txt': No such file or directory
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06/evidence (lina-bchibchi) $ cd lina_chichi
bash: cd: lina_chichi: No such file or directory
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06/evidence (lina-bchibchi) $ cd lina_bchibchi/
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/lina_bchibchi (lina-bchibchi) $  cp test-branch_lina.bchichi.txt td02_linabchichi.txt
cp: cannot stat 'test-branch_lina.bchichi.txt': No such file or directory
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/lina_bchibchi (lina-bchibchi) $  cp test_-branch_lina.bchic
hi.txt td02_linabchichi.txt
cp: cannot stat 'test_-branch_lina.bchichi.txt': No such file or directory
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/lina_bchibchi (lina-bchibchi) $  cp test_branch_lina.bchic
hi.txt td02_linabchichi.txt
cp: missing destination file operand after 'test_branch_lina.bchic'
Try 'cp --help' for more information.
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/lina_bchibchi (lina-bchibchi) $  cp test_branch_lina.bchibchi.txt td02_linabchibchi
@lina-042 ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/lina_bchibchi (lina-bchibchi) $ rm test_branch_lina.bchibchi.txt



