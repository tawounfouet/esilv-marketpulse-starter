
1. pwd -> Affiche le chemin actuel (/workspaces/esilv-marketpulse-g05-t05)

2. cd /workspaces/esilv-marketpulse-g05-t05/evidence -> Change de répertoire vers evidence
3. mkdir evidence -> Crée un dossier evidence

4. touch td-03_linux-basics.sh -> Crée un fichier vide

5. mv td-03_linux-basics.sh nassim_slaouti -> Déplace le fichier vers le sous-dossier

6. cd evidence/nassim_slaouti -> Entre dans le dossier nassim_slaouti

7. cat td-03_linux-basics.sh -> Affiche le contenu du fichier

8. cd /workspaces/esilv-marketpulse-g05-t05/data/sample -> Va dans le dossier des données

9. head prices.csv -> Affiche le début du fichier CSV

    2026-09-01,AAPL,249.20,251.50,248.00,250.00,38000000
2026-09-01,SP500,6592.00,6615.00,6580.00,6600.00,0
2026-09-02,AAPL,250.80,252.80,249.60,251.30,39500000
2026-09-02,SP500,6607.00,6627.00,6595.00,6612.00,0
2026-09-03,AAPL,249.60,251.30,248.40,249.80,41000000
2026-09-03,SP500,6596.00,6613.00,6584.00,6598.00,0
2026-09-04,AAPL,251.30,253.60,250.10,252.10,42500000
2026-09-04,SP500,6612.00,6635.00,6600.00,6620.00,0
2026-09-08,AAPL,251.90,253.90,250.70,252.40,44000000

10. grep "APPL" sample/prices.csv -> Affiche uniquement les lignes où le texte "AAPL" apparaît.
