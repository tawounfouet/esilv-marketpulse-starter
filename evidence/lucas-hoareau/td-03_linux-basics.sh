# 1 - afficer le chemin du repertoire
pwd

# 2 -
cd

# 3 -
cd ..

# 4 - 
cd ../..

# 5
ls -la

# 6
mkdir lucas-hoareau

# 7 
cd lucas-hoareau
pwd
touch td-03_linux-basics.sh

# 8 
cat data/sample/instruments.json
# @lucashoareaumichel-eng ➜ /workspaces/G06-T04 (lucas-hoareau) $ cat data/sample/instruments.json 
# {
#   "instrument": {
#     "ticker": "AAPL",
#     "name": "Apple Inc.",
#     "currency": "USD",
#     "market": "NASDAQ"
  
#   },
#   "benchmark": {
#     "ticker": "SP500",
#     "name": "S&P 500",
#     "currency": "USD",
#     "market": "US"
#   }
# }
# 9
head data/sample/intruments.json
@lucashoareaumichel-eng ➜ /workspaces/G06-T04 (lucas-hoareau) $ head data/sample/instruments.json 
# {
#   "instrument": {
#     "ticker": "AAPL",
#     "name": "Apple Inc.",
#     "currency": "USD",
#     "market": "NASDAQ"
#   },
#   "benchmark": {
#     "ticker": "SP500",
#     "name": "S&P 500",

# 10
grep AAPL data/sample/prices.csv
# 2026-09-08,AAPL,251.90,253.90,250.70,252.40,44000000
# 2026-09-09,AAPL,254.00,255.70,252.80,254.20,38000000
# 2026-09-10,AAPL,254.30,256.60,253.10,255.10,3:9500000
# 2026-09-11,AAPL,254.20,256.20,253.00,254.70,41000000
# 2026-09-14,AAPL,256.60,258.30,255.40,256.80,42500000
# 2026-09-15,AAPL,257.20,259.50,256.00,258.00,44000000
# 2026-09-16,AAPL,256.70,258.70,255.50,257.20,38000000
# 2026-09-17,AAPL,259.20,260.90,258.00,259.40,39500000
# 2026-09-18,AAPL,259.30,261.60,258.10,260.10,41000000
# 2026-09-21,AAPL,259.10,261.10,257.90,259.60,42500000
# 2026-09-22,AAPL,261.10,262.80,259.90,261.30,44000000
# 2026-09-23,AAPL,261.20,263.50,260.00,262.00,38000000
# 2026-09-24,AAPL,263.00,265.00,261.80,263.50,39500000
# 2026-09-25,AAPL,262.60,264.30,261.40,262.80,41000000
# 2026-09-28,AAPL,263.30,265.60,262.10,264.10,42500000
# 2026-09-29,AAPL,264.50,266.50,263.30,265.00,44000000
# 2026-09-30,AAPL,266.00,267.70,264.80,266.20,38000000