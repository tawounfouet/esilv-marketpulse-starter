# 02 - Branche, Pull Request et Code Review

**Prérequis :** une vraie Issue d'équipe, un Developer assigné, un Reviewer prévu et une branche `main` à jour. Lire le [TD06 officiel](../docs/labs/TD06_CODE_REVIEW.md) si nécessaire.

## 1. Vérifier sa copie locale

Exécuter depuis **votre dépôt d'équipe**, pas depuis le Starter de l'instructeur :

```bash
git remote -v
git branch --show-current
git status
git switch main
git pull origin main
python src/main.py
```

Si `origin` ne pointe pas vers votre fork d'équipe, **ne pas pousser** : vérifier les remotes avec votre responsable d'équipe.

## 2. Créer la branche liée à l'Issue

**Uniquement après création et attribution de l'Issue.** Exemple, si votre numéro d'Issue est 12 :

```bash
git switch -c feature/issue-12-analytics
# Modifier les fichiers nécessaires puis tester.
git status
git diff
python src/main.py
git add src/analytics.py src/main.py
git commit -m "feat: compare instrument and benchmark"
git push -u origin feature/issue-12-analytics
```

Adapter les chemins à **vos véritables modifications** : ne pas ajouter un fichier inexistant ou hors périmètre. Une contribution sans code utile, ou avec un test qui échoue, n'est pas prête pour la revue.

## 3. Ouvrir la PR au bon endroit

Dans le fork **de votre équipe**, ouvrir `Pull requests > New pull request` :

- **Base repository** : dépôt de votre équipe.
- **Base branch** : `main` de votre équipe.
- **Head / compare** : votre branche `feature/issue-12-analytics`.
- Ajouter un titre descriptif et [la description de PR](templates/PULL_REQUEST.md).
- Inclure `Closes #12` dans la description pour relier **l'Issue n°12 du même dépôt**.
- Demander officiellement la revue au Reviewer prévu dans l'Issue.

**Erreur classique :** envoyer la PR au Starter `tawounfouet/esilv-marketpulse-starter`. Stopper l'intégration et vérifier la destination avec l'instructeur ; ne jamais fusionner cette PR dans le Starter.

## 4. Vérifier une PR d'un autre étudiant

Dans `Files changed` :

1. Lire l'Issue et la description de la PR.
2. Contrôler les chemins modifiés et le périmètre.
3. Comprendre les changements, sans se limiter au nombre de commits.
4. Vérifier les effets métiers, les données instrument **et** benchmark.
5. Contrôler la sortie du script si l'environnement le permet.
6. Rédiger un avis technique qui explique **ce qui a été réellement vérifié**.

| Résultat GitHub | Quand l'utiliser |
| --- | --- |
| `Comment` | Question ou remarque non bloquante |
| `Request changes` | Défaut réel qui empêche le merge |
| `Approve` | Diff inspecté et aucun défaut bloquant |

**Exemples utiles :**

> J'ai contrôlé l'alignement AAPL / SP500 et la base 100 initiale. La différence de rendements est exprimée en points de pourcentage. Le script s'exécute : j'approuve.

> La branche calcule le rendement sur des dates différentes entre instrument et benchmark. Corrigez l'alignement avant le merge ; je revérifierai la même PR.

Un simple « LGTM » non argumenté, une réaction, ou une approbation sans inspection ne suffit pas.

## 5. Correction et intégration

Une correction n'est requise **que si** la revue révèle un véritable problème. Dans ce cas, le Developer corrige **sur la même branche**, commit et push. La PR se met à jour automatiquement ; le reviewer examine de nouveau.

Après approbation, fusionner dans **team main** puis :

```bash
git switch main
git pull origin main
git status
git log --oneline -5
python src/main.py
```

La PR doit afficher **Merged**. Si le résultat ne s'exécute plus, le travail n'est pas terminé.

## Check de sortie

- [ ] Issue d'équipe identifiable, liée dans la PR.
- [ ] Developer et Reviewer différents et visibles.
- [ ] PR ciblant `team main`, jamais le Starter.
- [ ] Revue technique réelle et documentée.
- [ ] Correction justifiée si nécessaire.
- [ ] Merge après approbation et `main` synchronisé.
- [ ] MarketPulse toujours exécutable.

Voir aussi [le guide de revue](templates/REVIEW_GUIDE.md), [le dépannage](07_DEPANNAGE.md) et [le contrat officiel de preuves](../docs/04_CHECKPOINTS_AND_EVIDENCE.md).
