#!/usr/bin/env bash
# TD01 : vérifier l'environnement, sans le modifier.
# En entreprise, avant de chercher un bug métier, on vérifie le contexte d'exécution.
# Lancer depuis n'importe quel dossier : le script retrouve la racine du Starter.
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd -- "$SCRIPT_DIR/../../.." && pwd)"

section() { printf '\n== %s ==\n' "$1"; }

section "TD01 : où suis-je ?"
printf 'Dossier d appel : %s\n' "$PWD"
printf 'Racine du dépôt : %s\n' "$ROOT"

# Le script refuse de diagnostiquer un autre projet sans prévenir.
if [[ ! -f "$ROOT/src/main.py" || ! -f "$ROOT/data/sample/prices.csv" ]]; then
  printf 'ERREUR : fichiers MarketPulse introuvables.\n' >&2
  exit 1
fi

section "Outils disponibles"
if ! command -v git >/dev/null 2>&1; then
  printf 'ERREUR : Git indisponible.\n' >&2
  exit 1
fi
git --version

# Sur Codespaces, python ou python3 peuvent être disponibles.
if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  printf 'ERREUR : Python indisponible.\n' >&2
  exit 1
fi
"$PYTHON" --version

section "Carte des fichiers"
for file in "README.md" "data/sample/instruments.json" "data/sample/prices.csv" "src/main.py" "collaboration/README.md"; do
  if [[ -f "$ROOT/$file" ]]; then
    printf '[OK] %s\n' "$file"
  else
    printf '[A VERIFIER] %s\n' "$file"
  fi
done

section "Git : observation (aucune écriture)"
if git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git -C "$ROOT" status --short
  printf 'Branche active : '
  git -C "$ROOT" branch --show-current
  printf 'Remotes déclarés : '
  git -C "$ROOT" remote | tr '\n' ' '
  printf '\n'
else
  printf 'Pas un checkout Git : révision de fichiers possible, Git non disponible ici.\n'
fi

section "Exécuter le programme métier existant"
# Un sous-shell change de dossier sans modifier celui de votre terminal.
(cd "$ROOT" && "$PYTHON" src/main.py)
printf '\nA retenir : Bash prépare le contexte, Python produit le résultat métier.\n'
