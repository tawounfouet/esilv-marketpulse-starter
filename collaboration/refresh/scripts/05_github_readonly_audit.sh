#!/usr/bin/env bash
# TD05 : observer la relation local / remote / PR.
# AUCUN git fetch, git push, creation de branche, ou changement de dépôt.
# Avec --github, lecture en ligne via gh (optionnelle, avec auth preexistante).
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd -- "$SCRIPT_DIR/../../.." && pwd)"

if [[ "$#" -gt 1 ]] || { [[ "$#" -eq 1 ]] && [[ "$1" != "--github" ]]; }; then
  echo "Usage : bash 05_github_readonly_audit.sh [--github]" >&2
  exit 2
fi
if ! git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Pas de dépôt Git local détecté, ouvrir votre fork via Codespaces." >&2
  exit 1
fi

printf '\n=== Répertoire et branche ===\n'
printf 'Repository local : %s\n' "$ROOT"
git -C "$ROOT" branch --show-current
git -C "$ROOT" status --short

printf '\n=== Remotes : vérifier que origin cible le dépôt d équipe ===\n'
git -C "$ROOT" remote
if git -C "$ROOT" remote get-url origin >/dev/null 2>&1; then
  # Certains clones historiques incluent un token dans leur URL :
  # on masque tout identifiant placé avant @ pour éviter de l'afficher.
  git -C "$ROOT" remote get-url origin | sed -E 's#(https?://)[^/@]+@#\1[identifiant-masque]@#g'
else
  echo "Aucun remote origin : demandez de l'aide avant de pousser."
fi

printf '\n=== Historique local ===\n'
git -C "$ROOT" log --oneline -5
printf '\nModele : commit local != push vers le fork != PR != Code Review.\n'
printf 'La destination d une PR doit être team main, jamais le Starter enseignant.\n'

if [[ "${1:-}" == "--github" ]]; then
  if ! command -v gh >/dev/null 2>&1; then
    echo "CLI gh indisponible : vérification manuelle via GitHub."
  elif ! gh auth status >/dev/null 2>&1; then
    echo "CLI gh non authentifiée : vérification manuelle via GitHub."
  else
    printf '\n=== GitHub, lecture uniquement ===\n'
    (cd "$ROOT" && gh repo view --json nameWithOwner,isFork,url --jq '.nameWithOwner, .url, .isFork')
    (cd "$ROOT" && gh pr list --state all --limit 10 --json number,title,baseRefName,headRefName,state --jq '.[] | [.number, .title, .baseRefName, .headRefName, .state] | @tsv')
  fi
fi
printf '\nPour créer une Issue, une PR et demander une review, suivre collaboration/01_ISSUES_ET_ROLES.md et 02_BRANCH_PR_CODE_REVIEW.md.\n'
