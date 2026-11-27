# Guide de Code Review - aide-mémoire

**Reviewer :** autre étudiant que le Developer.  
**Objet :** une Pull Request réelle du dépôt d'équipe.

## Avant de commenter

- [ ] Je connais l'Issue et ses critères d'acceptation.
- [ ] La PR cible `team main` et pas le Starter.
- [ ] J'ai ouvert **Files changed**.
- [ ] Je peux expliquer les modifications et leurs conséquences.
- [ ] Les fichiers modifiés sont pertinents et sans secret.
- [ ] J'ai observé un test, une commande ou une démonstration honnête.

## Choisir une issue de revue

**Comment** : question / remarque non bloquante.

**Request changes** : le code ne remplit pas un critère, ne s'exécute plus, ou présente un vrai risque.

**Approve** : la modification est comprise, vérifiée et prête à être intégrée.

## Exemple de revue utile : pas de défaut

> J'ai comparé la PR à l'Issue et inspecté les fonctions d'alignement des dates. Le calcul du rendement se fait à partir des prix et la base 100 commence à 100. J'ai vérifié l'exécution du script. Aucun défaut bloquant trouvé, j'approuve.

## Exemple de revue utile : correction nécessaire

> Je vois que les deux séries sont calculées sans alignement sur les dates communes. La performance relative risque donc de comparer des périodes différentes. Peux-tu corriger ce point et montrer la nouvelle sortie du script sur la même PR ?

## À éviter

- « LGTM » sans inspection.
- Approuver son propre travail.
- Exiger une correction fictive pour générer un commit.
- Fusionner dans le Starter de l'instructeur.
- Juger la qualité uniquement au nombre de commits.

Voir [TD06 - Code Review](../../docs/labs/TD06_CODE_REVIEW.md) pour le contrat pédagogique complet.
