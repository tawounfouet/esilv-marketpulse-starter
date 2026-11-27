#!/usr/bin/env python3
"""TD06 : diagnostic local avant PR / review - aucune écriture.

Ce script ne peut pas savoir si un reviewer a réellement approuvé dans GitHub.
Les valeurs --issue, --developer et --reviewer sont des DECLARATIONS à vérifier
dans l'interface GitHub de votre fork. Le jugement humain reste obligatoire.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[3]


def git(*args: str) -> tuple[bool, str]:
    """Observer Git : aucune commande de modification ici."""
    proc = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.returncode == 0, (proc.stdout.strip() or proc.stderr.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="Checklist de préparation d'une vraie PR (lecture seule).")
    parser.add_argument("--issue", type=int, help="Numéro d'Issue du dépôt d'équipe, non du Starter")
    parser.add_argument("--developer", help="Identifiant GitHub du développeur")
    parser.add_argument("--reviewer", help="Identifiant GitHub du reviewer prévu")
    args = parser.parse_args()

    print("=== TD06 : AVANT LA PR / CODE REVIEW ===")
    ok, branch = git("branch", "--show-current")
    if not ok:
        print("Impossible de lire Git :", branch)
        return 1
    print("Branche locale :", branch or "(non disponible)")
    _, status = git("status", "--short")
    print("Modifications non commitées :", status or "(aucune)")
    _, remotes = git("remote")
    print("Remotes déclarés :", remotes or "(aucun)")

    if branch == "main":
        print("[STOP] Vous êtes sur main : ne pas développer une nouvelle feature directement ici.")
    if args.issue is not None and args.issue <= 0:
        print("[STOP] Le numéro de l'Issue doit être positif.")
        return 2

    role_ok = bool(args.developer and args.reviewer and args.developer.lower().lstrip("@") != args.reviewer.lower().lstrip("@"))
    print("\nDéclarations reçues (NON validées sur GitHub) :")
    print("  Issue d'équipe :", args.issue if args.issue else "(à renseigner)")
    print("  Developer :", args.developer or "(à renseigner)")
    print("  Reviewer prévu :", args.reviewer or "(à renseigner)")
    print("  Rôles distincts :", "oui, déclarés" if role_ok else "NON VÉRIFIÉ / à corriger")

    # Comparer la branche à origin/main sans fetch, si la référence locale existe.
    has_base, _ = git("rev-parse", "--verify", "refs/remotes/origin/main")
    if has_base:
        _, files = git("diff", "--name-only", "origin/main...HEAD")
        print("\nFichiers modifiés depuis origin/main (référence locale) :")
        print(files or "(aucune différence observée)")
        print("Attention : origin/main local peut être ancien, aucune synchronisation automatique.")
    else:
        print("\norigin/main absent en local : comparaison de branches indisponible.")
    print("\nRevue HUMAINE à faire dans la PR du fork :")
    print(" [ ] Issue, critères d'acceptation et développeur assigné")
    print(" [ ] Reviewer demandé officiellement et différent du développeur")
    print(" [ ] Base repository = dépôt d'équipe ; base branch = main")
    print(" [ ] Files changed et commits inspectés")
    print(" [ ] Tests / démonstration métier réellement exécutés")
    print(" [ ] Comment, Request changes ou Approve justifiés")
    print(" [ ] Merge après approbation, puis main synchronisé")

    print("\nAucune PR, approbation, merge ou commit n'a été créé par ce script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
