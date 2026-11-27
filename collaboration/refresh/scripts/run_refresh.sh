#!/usr/bin/env bash
# Chef d'orchestre pédagogique. Bash coordonne plusieurs programmes.
# Usage par défaut : actions en lecture seule.
# Mode --labs : Git local TD03/04 exclusivement sur des dépôts jetables.
set -euo pipefail

HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  printf 'Python 3 requis pour ce parcours.\n' >&2
  exit 1
fi

if [[ "$#" -gt 1 ]]; then
  printf 'Usage : bash %s [--labs|--all]\n' "$0" >&2
  exit 2
fi
MODE="${1:---quick}"
case "$MODE" in
  --quick)
    printf 'REFRESH rapide : environnement + Linux + Python (lecture seule).\n'
    bash "$HERE/00_preflight.sh"
    bash "$HERE/01_linux_explorer.sh"
    "$PYTHON" "$HERE/02_python_csv_json.py"
    ;;
  --labs)
    printf 'LABS Git TD03/TD04 : les commits et merges restent dans /tmp.\n'
    bash "$HERE/03_git_local_demo.sh"
    bash "$HERE/04_git_branches_demo.sh"
    ;;
  --all)
    printf 'REFRESH complet : lecture seule puis laboratoires temporaires.\n'
    bash "$HERE/00_preflight.sh"
    bash "$HERE/01_linux_explorer.sh"
    "$PYTHON" "$HERE/02_python_csv_json.py"
    bash "$HERE/03_git_local_demo.sh"
    bash "$HERE/04_git_branches_demo.sh"
    bash "$HERE/05_github_readonly_audit.sh"
    "$PYTHON" "$HERE/06_review_preflight.py"
    ;;
  *)
    printf 'Usage : bash %s [--labs|--all]\n' "$0" >&2
    exit 2
    ;;
esac
printf '\nEtape suivante : lire collaboration/refresh/MENTAL_MODELS.md\n'
