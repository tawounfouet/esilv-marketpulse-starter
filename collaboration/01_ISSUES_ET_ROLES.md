# 01 - Issue-First : préparer une fonctionnalité avant de coder

**Objectif :** exprimer un besoin, préciser comment vérifier le résultat et attribuer clairement le travail **avant** de créer une branche.

## 1. Où ouvrir l'Issue ?

Chaque équipe a son **fork partagé**. Toutes les Issues de travail y sont créées, jamais dans le dépôt pédagogique de l'instructeur.

1. Ouvrir le fork de votre équipe.
2. Aller dans **Issues**. Si l'onglet n'est pas disponible, le propriétaire active `Settings > General > Features > Issues`.
3. Choisir **New issue** et copier [le modèle d'Issue](templates/ISSUE_FEATURE.md).
4. Prendre pour référence les attentes [TD07 du Starter, Issue #39](https://github.com/tawounfouet/esilv-marketpulse-starter/issues/39).
5. Compléter les rôles et les critères avant de commencer.

**Attention :** l'Issue #39 du Starter n'est pas votre Issue d'équipe ; les numéros sont propres à chaque dépôt. Si l'activation d'Issues est impossible, prévenir l'instructeur et préparer la description hors-ligne. Ne pas déclarer la règle Issue-First remplie.

## 2. Définir les responsabilités

| Rôle | Où l'indiquer | Responsabilité |
| --- | --- | --- |
| **Developer** | Champ GitHub `Assignees` de l'Issue | Implémente et vérifie le changement |
| **Reviewer prévu** | Corps de l'Issue | Étudie la contribution et donne un avis technique |
| **Reviewer demandé** | Champ `Reviewers` de la PR, à son ouverture | Reçoit officiellement la demande de revue |
| **Équipe** | Issue et dépôt partagé | Intègre dans son propre `main` |

Le Developer et le Reviewer doivent être **différents**. Un étudiant ne s'approuve pas lui-même. Les équipes de deux ou cinq membres répartissent les rôles selon leur effectif réel, sans inventer des membres.

## 3. Exemple TD07

**Titre d'Issue :** `[TD07] Normaliser et comparer AAPL à SP500`

**Besoin :** comparer l'instrument et le benchmark sur les **mêmes dates**, pour connaître leur rendement et leur performance relative.

**Livrables :** `src/analytics.py`, intégration dans `src/main.py`, vérification sur le CSV d'exemple.

**Critères d'acceptation :**

- [ ] Les cours CSV sont convertis en numériques.
- [ ] Les séries sont alignées sur les mêmes dates, sans liste vide.
- [ ] Le rendement de période est calculé à partir des prix.
- [ ] La base 100 commence à 100 pour chaque série.
- [ ] Performance relative = rendement instrument moins benchmark, en **points de pourcentage**.
- [ ] `python src/main.py` fonctionne après intégration.
- [ ] PR vers `main` **de l'équipe**, revue par un autre membre.

Cette liste n'ajoute pas de nouvel exercice obligatoire au [CORE TD07](../docs/labs/TD07_DATA_NORMALIZATION_AND_COMPARISON.md).

## 4. Quand peut-on créer la branche ?

**GO** seulement si l'Issue contient : besoin, périmètre, critères, Developer attribué, Reviewer prévu et vérification de la baseline.

```text
Issue d'équipe #12 (exemple)
  ├─ Developer : @alice (Assignee)
  ├─ Reviewer : @bob (dans l'Issue)
  ├─ Critères : connus
  └─ Branche : feature/issue-12-analytics
```

Le numéro 12 est un **exemple**, remplacez-le par le vrai numéro affiché dans **votre fork**.

## 5. Et pour TD08 ?

TD08 reprend les mêmes règles et référence l'[Issue pédagogique #40](https://github.com/tawounfouet/esilv-marketpulse-starter/issues/40).

Avant de commencer sa branche : les Analytics TD07 doivent être **fusionnées et exécutables** sur `main` de l'équipe. Renseigner cette dépendance dans l'Issue TD08.

## À montrer à l'instructeur

- Lien de l'Issue **du dépôt de votre équipe**.
- Developer visible dans `Assignees`.
- Reviewer prévu identifiable et différent.
- Critères de réussite discutés, compris et vérifiables.

**Prochaine étape :** [02 - Branche, PR et Code Review](02_BRANCH_PR_CODE_REVIEW.md).
