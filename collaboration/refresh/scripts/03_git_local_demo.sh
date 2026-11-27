#!/usr/bin/env bash
# TD03 : travailler, indexer et committer sont TROIS moments différents.
# Les commits ci-dessous sont créés dans un dépôt jetable sous /tmp, JAMAIS
# dans le dépôt MarketPulse de votre équipe.
set -euo pipefail
command -v git >/dev/null || { echo "Git requis" >&2; exit 1; }

LAB="$(mktemp -d "${TMPDIR:-/tmp}/marketpulse-td03-XXXXXX")"
git -C "$LAB" init -q
git -C "$LAB" symbolic-ref HEAD refs/heads/main
git -C "$LAB" config user.name "MarketPulse Refresh Lab"
git -C "$LAB" config user.email "refresh@example.invalid"

printf 'Version 1 : cours local à analyser\n' > "$LAB/notes.txt"
git -C "$LAB" add notes.txt
git -C "$LAB" commit -q -m "docs: add initial market note"
printf 'Version 2 : contrôler les changements avant partage\n' >> "$LAB/notes.txt"

printf '\n=== 1. WORKING TREE : changement pas encore stage ===\n'
git -C "$LAB" status --short
git -C "$LAB" diff -- notes.txt

printf '\n=== 2. STAGING AREA : le changement choisi ===\n'
git -C "$LAB" add notes.txt
git -C "$LAB" status --short
git -C "$LAB" diff --staged -- notes.txt

printf '\n=== 3. COMMIT : instantané durable ===\n'
git -C "$LAB" commit -q -m "docs: explain change checks"
git -C "$LAB" log --oneline -3
git -C "$LAB" status --short

printf '\nLaboratoire TD03 (conservé pour exploration) : %s\n' "$LAB"
printf 'Question : pourquoi inspecter git diff --staged avant un commit ?\n'
printf 'Dans une équipe, un commit utile permet de comprendre qui a change quoi et pourquoi.\n'
