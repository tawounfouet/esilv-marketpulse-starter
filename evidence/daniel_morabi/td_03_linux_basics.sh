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
