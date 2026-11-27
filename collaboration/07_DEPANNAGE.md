# 07 - Dépannage GitHub, Git, Python et Yahoo

Ce guide sert à **diagnostiquer avant de modifier**. Pour les règles de review, voir [TD06](../docs/labs/TD06_CODE_REVIEW.md).

## L'onglet Issues n'apparaît pas sur le fork

- Le propriétaire ouvre `Settings > General > Features` et active `Issues`.
- Vérifier que vous êtes sur **le fork de votre équipe**, pas sur le Starter.
- Si l'option est indisponible, prévenir l'instructeur ; documenter le besoin, mais **ne pas déclarer l'Issue d'équipe créée**.

## Ma PR va vers le Starter de l'instructeur

Inspecter **base repository**, **base branch**, **head repository** et **compare branch**.

La destination doit être le **main du dépôt d'équipe**. Ne pas fusionner la PR vers Starter. Corriger la cible avec l'instructeur, éventuellement en ouvrant une PR dans le bon dépôt ; éviter de créer plusieurs PR redondantes.

## Reviewer impossible à sélectionner

- Vérifier que le reviewer est connecté au bon compte et invité comme collaborateur du fork.
- S'assurer que le reviewer n'est pas le Developer de la PR.
- Le nom présent dans l'Issue indique un **reviewer prévu** ; la demande officielle doit se faire dans la PR.

## Je ne sais plus quelle branche / quel remote sont actifs

```bash
git remote -v
git branch -vv
git status
git log --oneline --graph --decorate --all -12
```

Ne pas exécuter des commandes destructives tant que l'état n'est pas compris.

## Je ne retrouve pas le commit dans la PR

```bash
git branch --show-current
git status
git remote get-url origin
git log --oneline -5
```

Comparer le nom de la branche locale à la branche source de la PR et pousser **la même branche** si nécessaire. Ne pas forcer le push.

## Mon main local ne contient pas la fusion récente

```bash
git switch main
git pull origin main
git log --oneline -5
python src/main.py
```

Si Git refuse de changer de branche à cause de modifications locales, **arrêter et demander de l'aide** ; ne pas effacer de travail.

## Un conflit apparaît

```bash
git status
git diff
```

Identifier les intentions concurrentes, éditer les marqueurs et terminer selon la situation. Le [mini-lab contrôlé](03_LAB_CONFLITS_GIT.md) explique le cas d'un merge ; il ne faut pas transposer mécaniquement une résolution au code métier.

## Python échoue au TD07

Vérifier :

- `close` et les autres prix sont convertis en `float` depuis le CSV.
- Les séries ont des **dates communes** et un premier close non nul.
- Le benchmark n'est pas remplacé par l'instrument dans l'appel.
- `calculate_base_100()` commence bien à 100 et conserve l'ordre des dates.
- `src/main.py` importe les fonctions dans le bon module.

La première vérification reste :

```bash
python src/main.py
```

## Pas de données Yahoo / ModuleNotFoundError

- Lire la [procédure d'indisponibilité TD08](../docs/labs/TD08_YAHOO_FINANCE.md).
- Vérifier la connexion, la présence de `yfinance`, le symbole `^GSPC` et la réponse réellement retournée.
- Ne pas traiter des lignes locales comme des réponses Yahoo.
- Documenter le blocage `PENDING_EXTERNAL` seulement lorsque les conditions officielles du checkpoint sont réunies.

## Une PR a été approuvée sans commentaire utile

Une approbation ne prouve pas automatiquement une revue substantielle. Demander au reviewer d'expliquer ce qu'il a inspecté et la décision technique, sans fabriquer de défaut pour produire une nouvelle révision.

**Si vous êtes bloqués plus de quelques minutes :** capturez l'état avec `git status`, les noms de dépôt et de branches, l'erreur exacte et l'action essayée, puis sollicitez l'instructeur.
