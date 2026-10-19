# create directory
mkdir evidence/clemence-morin

# move to evidence directory
cd evidence

# print working directory path
pwd

# move file to the new directory
mv test_branch_clemence-morin.txt clemence-morin/test_branch_clemence-morin.txt

# move to the new directory
cd clemence-morin

# create an empty .sh file
touch td-03_linux-basics.sh

# print the content of the .sh file
cat td-03_linux-basics.sh

# mv to root directory
cd ../..

# display instruments
cat data/samples/instruments.json

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

# display SP500 prices
grep SP500 data/sample/prices.csv

# 2026-09-01,SP500,6592.00,6615.00,6580.00,6600.00,0
# 2026-09-02,SP500,6607.00,6627.00,6595.00,6612.00,0
# 2026-09-03,SP500,6596.00,6613.00,6584.00,6598.00,0
# 2026-09-04,SP500,6612.00,6635.00,6600.00,6620.00,0
# 2026-09-08,SP500,6623.00,6643.00,6611.00,6628.00,0
# 2026-09-09,SP500,6640.00,6657.00,6628.00,6642.00,0
# 2026-09-10,SP500,6642.00,6665.00,6630.00,6650.00,0
# 2026-09-11,SP500,6642.00,6662.00,6630.00,6647.00,0
# 2026-09-14,SP500,6663.00,6680.00,6651.00,6665.00,0
# 2026-09-15,SP500,6664.00,6687.00,6652.00,6672.00,0
# 2026-09-16,SP500,6663.00,6683.00,6651.00,6668.00,0
# 2026-09-17,SP500,6683.00,6700.00,6671.00,6685.00,0
# 2026-09-18,SP500,6684.00,6707.00,6672.00,6692.00,0
# 2026-09-21,SP500,6683.00,6703.00,6671.00,6688.00,0
# 2026-09-22,SP500,6703.00,6720.00,6691.00,6705.00,0
# 2026-09-23,SP500,6704.00,6727.00,6692.00,6712.00,0
# 2026-09-24,SP500,6715.00,6735.00,6703.00,6720.00,0
# 2026-09-25,SP500,6713.00,6730.00,6701.00,6715.00,0
# 2026-09-28,SP500,6720.00,6743.00,6708.00,6728.00,0
# 2026-09-29,SP500,6729.00,6749.00,6717.00,6734.00,0
# 2026-09-30,SP500,6740.00,6757.00,6728.00,6742.00,0

# copy the file to a new file 
cp test_branch_clemence-morin.txt td-02_clemence-morin.txt

# remove the file
rm test_branch_clemence-morin.txt