#!/usr/bin/env bash
# TD04 : une branche permet de préparer une feature sans changer main.
# Le merge de ce fichier est une simulation locale dans /tmp.
# Les contributions à un vrai projet passent ensuite par Issue et PR.
set -euo pipefail
command -v git >/dev/null || { echo "Git requis" >&2; exit 1; }

LAB="$(mktemp -d "${TMPDIR:-/tmp}/marketpulse-td04-XXXXXX")"
git -C "$LAB" init -q
git -C "$LAB" symbolic-ref HEAD refs/heads/main
git -C "$LAB" config user.name "MarketPulse Refresh Lab"
git -C "$LAB" config user.email "refresh@example.invalid"

printf 'application=MarketPulse\n' > "$LAB/config.txt"
git -C "$LAB" add config.txt
git -C "$LAB" commit -q -m "chore: initialize shared baseline"

printf '\n=== 1. Départ d une branche feature ===\n'
git -C "$LAB" switch -q -c feature/market-label
printf 'instrument=AAPL\n' > "$LAB/market.txt"
git -C "$LAB" add market.txt
git -C "$LAB" commit -q -m "feat: document market instrument"

printf '\n=== 2. main ne contient pas encore la feature ===\n'
git -C "$LAB" switch -q main
git -C "$LAB" ls-tree --name-only HEAD
printf 'L historique feature est isolé.\n'

printf '\n=== 3. Merge pédagogique (pas de push) ===\n'
git -C "$LAB" merge -q --no-ff feature/market-label -m "merge: integrate market label"
git -C "$LAB" log --oneline --graph --decorate --all -6
git -C "$LAB" status --short

printf '\nLaboratoire TD04 (conservé) : %s\n' "$LAB"
printf 'Pourquoi le merge est-il autorisé ici sans PR ? Parce que ce laboratoire local\n'
printf 'n est pas un dépôt d équipe. Dans le travail réel, une PR et une review sont attendues.\n'
printf 'Pour un conflit : collaboration/03_LAB_CONFLITS_GIT.md\n'
