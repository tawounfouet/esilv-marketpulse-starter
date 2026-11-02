# 1. Créer le dossier evidence/manon-gay
mkdir -p evidence/manon-gay

# 2. Afficher le chemin du répertoire actuel
pwd

# 3. Entrer dans le dossier evidence
cd evidence/

# 4. Créer le fichier du TP sur les bases de Linux
touch td-03_linux-basics.sh

# 5. Afficher le contenu du fichier créé
cat td-03_linux-basics.sh

# 6. Afficher le contenu du fichier JSON
cat data/sample/instruments.json

# 7. Entrer dans le dossier manon-gay
cd manon-gay/

# 8. Vérifier les fichiers disponibles
ls

# 9. Copier le fichier source et le renommer
cp test_branch_manon.gay.txt td-02_manon_gay.txt

# 10. Revenir dans le dossier evidence
cd ..

# 11. Vérifier les fichiers présents avant suppression
ls

# 12. Supprimer le fichier original s'il se trouve ici
rm test_branch_manon.gay.txt
```