#!/usr/bin/env bash
# TD01 : Linux est une carte navigable.
# pwd = localisation ; ls = inventaire ; cd = déplacement ;
# cat/head/grep = inspection. Rien n'est modifié dans le dépôt d'équipe.
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd -- "$SCRIPT_DIR/../../.." && pwd)"
cd "$ROOT"

printf '\n=== 1. pwd : ou suis-je ? ===\n'
pwd
printf '\n=== 2. ls : quels fichiers ici ? ===\n'
ls -la
printf '\n=== 3. cd : je navigue dans les donnees ===\n'
cd data/sample
pwd
ls
printf '\n=== 4. cat : le JSON porte les metadonnees métier ===\n'
cat instruments.json
printf '\n=== 5. head : apercu des observations CSV ===\n'
head -n 6 prices.csv
printf '\n=== 6. grep : combien de lignes pour chaque ticker ? ===\n'
grep -c ',AAPL,' prices.csv
grep -c ',SP500,' prices.csv
printf '\n=== 7. retour a la racine du depot ===\n'
cd ../..
pwd

# Modèle mental : un chemin relatif est résolu depuis le dossier courant.
printf '\nQuestion : que deviendra src/main.py si vous changez de dossier ?\n'
printf 'Usage professionnel : inspecter un pipeline, diagnostiquer des fichiers, lire des logs.\n'
