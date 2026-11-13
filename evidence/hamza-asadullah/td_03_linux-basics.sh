# 1 afficher le chemin du répertoire
pwd

# 2 se déplacer dans un dossier fille 
cd

# 3  se déplacer dans un dossier parent

cd..

# 4 remonter de 2 dossier parents

cd ../..

# 5 afficher les fichiers

ls

# 6 afficher les fichiers visibles et cachés

ls -la

# 7 créer un nouveau dossier 
mkdir hamza-asadullah
cd hamza-asadullah
pwd

# 8 créer un nouveau fichier .sh
touch TD3_linux-basics.sh 

# 9 
cat /workspaces/esilv-marketpulse-g06-t03/data/sample/instruments.json

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

head /workspaces/esilv-marketpulse-g06-t03/data/sample/prices.csv
# 2026-09-02,AAPL,250.80,252.80,249.60,251.30,39500000
# 2026-09-02,SP500,6607.00,6627.00,6595.00,6612.00,0
# 2026-09-03,AAPL,249.60,251.30,248.40,249.80,41000000
# 2026-09-03,SP500,6596.00,6613.00,6584.00,6598.00,0
# 2026-09-04,AAPL,251.30,253.60,250.10,252.10,42500000
# 2026-09-04,SP500,6612.00,6635.00,6600.00,6620.00,0
# 2026-09-08,AAPL,251.90,253.90,250.70,252.40,44000000

grep AAPL /workspaces/esilv-marketpulse-g06-t03/data/sample/prices.csv

# 2026-09-22,AAPL,261.10,262.80,259.90,261.30,44000000
# 2026-09-23,AAPL,261.20,263.50,260.00,262.00,38000000
# 2026-09-24,AAPL,263.00,265.00,261.80,263.50,39500000
# 2026-09-25,AAPL,262.60,264.30,261.40,262.80,41000000
# 2026-09-28,AAPL,263.30,265.60,262.10,264.10,42500000
# 2026-09-29,AAPL,264.50,266.50,263.30,265.00,44000000
# 2026-09-30,AAPL,266.00,267.70,264.80,266.20,38000000

grep SP500 /workspaces/esilv-marketpulse-g06-t03/data/sample/prices.csv

# 2026-09-22,SP500,6703.00,6720.00,6691.00,6705.00,0
# 2026-09-23,SP500,6704.00,6727.00,6692.00,6712.00,0
# 2026-09-24,SP500,6715.00,6735.00,6703.00,6720.00,0
# 2026-09-25,SP500,6713.00,6730.00,6701.00,6715.00,0
# 2026-09-28,SP500,6720.00,6743.00,6708.00,6728.00,0
# 2026-09-29,SP500,6729.00,6749.00,6717.00,6734.00,0
# 2026-09-30,SP500,6740.00,6757.00,6728.00,6742.00,0