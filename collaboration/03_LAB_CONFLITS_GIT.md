# 03 - Mini-lab : comprendre et résoudre un conflit Git

**Parcours ADVANCED guidé - 30 minutes pendant la séance du 27 novembre.**

Ce mini-lab est adapté de [ADV-GIT-01 - Conflict Resolution](../docs/advanced/ADV_GIT_01_CONFLICT_RESOLUTION.md), dont la durée indicative est de 30 à 45 minutes. Il n'ajoute **aucune capture obligatoire** au Checkpoint A.

## Règle de sécurité

Travaillez dans un **nouveau dossier jetable en dehors du dépôt MarketPulse**.

**Ne provoquez pas votre premier conflit dans** `src/main.py`, `analytics.py`, les providers ou le `main` de votre équipe. N'utilisez pas `git push --force`, `git reset --hard` ou une suppression massive de fichiers pour « corriger » le conflit.

## A. Préparer une base commune

Depuis un répertoire personnel **hors du dépôt d'équipe**, sur Linux / Codespaces :

```bash
mkdir conflict-lab
cd conflict-lab
git init -b main
git config user.name "MarketPulse Lab"
git config user.email "lab@example.invalid"
printf 'provider=csv\n' > config.txt
git add config.txt
git commit -m "chore: add base config"
```

`git init -b main` nécessite une version de Git compatible. Si l'option n'est pas reconnue, utiliser `git init`, faire le commit initial, puis `git branch -m main`.

## B. Première intention : travailler avec Yahoo

```bash
git switch -c feature/provider
printf 'provider=yahoo\n' > config.txt
git add config.txt
git commit -m "feat: select yahoo provider"
```

## C. Intention concurrente sur main

```bash
git switch main
printf 'provider=bloomberg-stage\n' > config.txt
git add config.txt
git commit -m "chore: select bloomberg stage"
```

## D. Déclencher le conflit

```bash
git merge feature/provider
git status
cat config.txt
```

Le merge doit s'arrêter. Dans le fichier vous trouverez une forme de conflit de ce type :

```text
<<<<<<< HEAD
provider=bloomberg-stage
=======
provider=yahoo
>>>>>>> feature/provider
```

**Questions à résoudre à l'oral :**

- Quelle branche a choisi Yahoo ?
- Quelle branche a choisi Bloomberg stage ?
- Pourquoi Git ne peut-il pas décider à notre place de la valeur métier correcte ?
- Quelle valeur l'équipe souhaite-t-elle conserver et pour quelle raison ?

## E. Choisir et finaliser une résolution

Exemple **d'une décision explicitement choisie** : conserver `bloomberg-stage`. Ce n'est pas le seul choix possible.

```bash
printf 'provider=bloomberg-stage\n' > config.txt
git add config.txt
git commit -m "merge: resolve provider selection"
git status
cat config.txt
git log --oneline --graph --decorate --all
```

Vérifiez que le fichier ne contient **plus aucun marqueur de conflit**, que `git status` est propre et que le merge commit relie les deux histoires.

## Définition de terminé

- [ ] Un conflit réel a été reproduit.
- [ ] Je sais lire `git status` et les marqueurs de conflit.
- [ ] Je peux expliquer **les deux intentions**, pas seulement le texte modifié.
- [ ] La résolution est choisie, non automatique et arbitraire.
- [ ] Le merge est terminé et le working tree est propre.

**Nettoyage :** conserver le répertoire pendant les vérifications, puis le supprimer manuellement depuis son dossier parent après avoir confirmé qu'il s'agit bien de `conflict-lab`. Pas de commande de suppression automatique dans ce guide.

**Suite :** retour au [workflow de PR et revue](02_BRANCH_PR_CODE_REVIEW.md) de l'équipe.
