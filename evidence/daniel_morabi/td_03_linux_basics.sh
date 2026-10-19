 cat data/sample/instruments.json
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
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (daniel-morabi) $ head data/sample/prices.csv
date,ticker,open,high,low,close,volume
2026-09-01,AAPL,249.20,251.50,248.00,250.00,38000000
2026-09-01,SP500,6592.00,6615.00,6580.00,6600.00,0
2026-09-02,AAPL,250.80,252.80,249.60,251.30,39500000
2026-09-02,SP500,6607.00,6627.00,6595.00,6612.00,0
2026-09-03,AAPL,249.60,251.30,248.40,249.80,41000000
2026-09-03,SP500,6596.00,6613.00,6584.00,6598.00,0
2026-09-04,AAPL,251.30,253.60,250.10,252.10,42500000
2026-09-04,SP500,6612.00,6635.00,6600.00,6620.00,0
2026-09-08,AAPL,251.90,253.90,250.70,252.40,44000000









 $ git branch
* daniel-morabi
  main
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (daniel-morabi) $ git add /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (daniel-morabi) $ git commit -m "ajout fichier daniel_morabi"
[daniel-morabi a89b413] ajout fichier daniel_morabi
 2 files changed, 43 insertions(+)
 create mode 100644 evidence/daniel_morabi/td_03_linux_basics.sh
 create mode 100644 evidence/daniel_morabi/test_branch_daniel_morabi.txt
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (daniel-morabi) $ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 919 bytes | 919.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/dmorabi/esilv-marketpulse-g05-t06
   0364382..a89b413  daniel-morabi -> daniel-morabi
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (daniel-morabi) $ cd evidence/daniel_morabi
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel-morabi) $ ls -la
total 16
drwxrwxrwx+ 2 codespace codespace 4096 Oct 16 14:07 .
drwxrwxrwx+ 3 codespace root      4096 Oct 16 14:07 ..
-rw-rw-rw-  1 codespace codespace  868 Oct 16 14:14 td_03_linux_basics.sh
-rw-rw-rw-  1 codespace codespace  273 Oct 14 14:33 test_branch_daniel_morabi.txt
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel-morabi) $ cp test_branch_daniel_morabi.txt td_02_git_and_github_basics.txt
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel-morabi) $ rm test_branch_daniel_morabi.txt





















@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel_morabi) $ git branch -d daniel-morabi
warning: not deleting branch 'daniel-morabi' that is not yet merged to
         'refs/remotes/origin/daniel-morabi', even though it is merged to HEAD
error: the branch 'daniel-morabi' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D daniel-morabi'
hint: Disable this message with "git config set advice.forceDeleteBranch false"
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel_morabi) $ git branch -D daniel-morabi
Deleted branch daniel-morabi (was 71320e3).
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel_morabi) $ git branch
* daniel_morabi
  main
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (dan
iel_morabi) $ git merge daniel_morabi
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel_morabi) $ git branch
* daniel_morabi
  main
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel_morabi) $ git branch main
fatal: a branch named 'main' already exists
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (daniel_morabi) $ git checkout main
D       TEAM_TEMPLATE.md
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git merge daniel_morabi
Updating 4cc1356..71320e3
Fast-forward
 evidence/daniel_morabi/td_02_git_and_github_basics.txt | 17 +++++++++++++++++
 evidence/daniel_morabi/td_03_linux_basics.sh           | 63 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 evidence/test_branch_daniel_morabi.txt                 | 17 +++++++++++++++++
 3 files changed, 97 insertions(+)
 create mode 100644 evidence/daniel_morabi/td_02_git_and_github_basics.txt
 create mode 100644 evidence/daniel_morabi/td_03_linux_basics.sh
 create mode 100644 evidence/test_branch_daniel_morabi.txt
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../../TEAM_TEMPLATE.md

no changes added to commit (use "git add" and/or "git commit -a")
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git push
To https://github.com/dmorabi/esilv-marketpulse-g05-t06
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/dmorabi/esilv-marketpulse-g05-t06'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git pull
remote: Enumerating objects: 25, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 25 (delta 8), reused 7 (delta 7), pack-reused 13 (from 1)
Unpacking objects: 100% (25/25), 6.19 KiB | 1.24 MiB/s, done.
From https://github.com/dmorabi/esilv-marketpulse-g05-t06
   4cc1356..2d1ce6d  main                   -> origin/main
 * [new branch]      bennas                 -> origin/bennas
 * [new branch]      bennas_mohammed        -> origin/bennas_mohammed
 * [new branch]      gaspard-le_cam         -> origin/gaspard-le_cam
 * [new branch]      lina-bchibchi          -> origin/lina-bchibchi
 * [new branch]      manon-gay              -> origin/manon-gay
 * [new branch]      revert-1-daniel-morabi -> origin/revert-1-daniel-morabi
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git config pull.rebase false 
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git pull
hint: Waiting for your editor to close the file... 

git config pull.rebase false 
^C
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ ^C
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 2 and 7 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        new file:   ../test_branch_bennas.txt
        new file:   ../test_branch_lina.bchibchi.txt
        new file:   ../test_branch_manon.gay.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../../TEAM_TEMPLATE.md

@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git pull
error: You have not concluded your merge (MERGE_HEAD exists).
hint: Please, commit your changes before merging.
fatal: Exiting because of unfinished merge.
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ git add deleted:    ../../TEAM_TEMPLATE.mdc^C
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence/daniel_morabi (main) $ cd ..
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06/evidence (main) $ cd ..
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 2 and 7 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        new file:   evidence/test_branch_bennas.txt
        new file:   evidence/test_branch_lina.bchibchi.txt
        new file:   evidence/test_branch_manon.gay.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    TEAM_TEMPLATE.md

@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ git add TEAM_TEMPLATE.md
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ git statys
git: 'statys' is not a git command. See 'git --help'.

The most similar command is
        status
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 2 and 7 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        deleted:    TEAM_TEMPLATE.md
        new file:   evidence/test_branch_bennas.txt
        new file:   evidence/test_branch_lina.bchibchi.txt
        new file:   evidence/test_branch_manon.gay.txt

@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ git commit -m "Updated Files"
[main 2566f17] Updated Files
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ git pull
Already up to date.
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ git push
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 2 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.60 KiB | 1.60 MiB/s, done.
Total 8 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To https://github.com/dmorabi/esilv-marketpulse-g05-t06
   2d1ce6d..2566f17  main -> main
@dmorabi ➜ /workspaces/esilv-marketpulse-g05-t06 (main) $ 