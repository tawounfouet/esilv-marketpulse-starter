# 04 - TD07 en collaboration : Analytics et comparaison financière

**Notebook :** [01_analytics.ipynb](../notebooks/01_analytics.ipynb)  
**Guide faisant foi pour le CORE :** [TD07 - Data Normalization + Comparison](../docs/labs/TD07_DATA_NORMALIZATION_AND_COMPARISON.md)  
**Issue pédagogique d'exemple :** [Starter #39](https://github.com/tawounfouet/esilv-marketpulse-starter/issues/39)

## Question métier

> AAPL surperforme-t-elle ou sous-performe-t-elle SP500 **sur la même période et à la même fréquence** ?

Comparer directement le niveau de prix d'AAPL et le niveau de l'indice SP500 n'a pas de sens ; il faut aligner les dates et comparer des performances ou des séries ramenées à 100.

## Cycle Issue-First

1. Dans **votre dépôt d'équipe**, créer l'Issue TD07 et choisir Developer / Reviewer.
2. Vérifier que `main` et `python src/main.py` fonctionnent.
3. Seulement ensuite, créer `feature/issue-<numéro>-analytics`.
4. Prototyper dans notebook 01, transférer les calculs stables vers `src/analytics.py`.
5. Soumettre une PR avec `Closes #<numéro>`, obtenir une vraie review puis intégrer si le CORE est vérifié.

## Apprentissage technique

Les lignes de données canoniques ont la structure :

```text
date, ticker, open, high, low, close, volume
```

Le CSV les livre d'abord sous forme de texte. Après normalisation, les prix sont numériques et `volume` est un entier.

Fonctions de référence attendues :

| Fonction | Responsabilité |
| --- | --- |
| `index_by_date()` | Indexer les observations d'un instrument par date |
| `align_series()` | Conserver uniquement les dates communes |
| `calculate_period_return()` | Calculer le rendement à partir des cours |
| `calculate_relative_performance()` | Instrument moins benchmark, en points de pourcentage |
| `calculate_base_100()` | Mettre chaque série à 100 à sa première observation |

Formules à comprendre, et **non à coder en dur** :

```text
Rendement (%) = (close_final / close_initial - 1) * 100
Base 100 = (close_date / close_initial) * 100
Performance relative (points) = rendement instrument - rendement benchmark
```

## Contrôle sur les données pédagogiques du Starter

Le CSV d'exemple [prices.csv](../data/sample/prices.csv) produit, dans le guide officiel, les repères suivants :

- Dates communes de septembre 2026, du 01/09 au 30/09, **21 observations**.
- Rendement instrument AAPL : **+6,48 %**.
- Rendement benchmark SP500 : **+2,15 %**.
- Performance relative : **+4,33 points de pourcentage**.
- Base 100 initiale : **100,00** pour les deux séries.

Ces chiffres concernent **uniquement les données pédagogiques locales** ; ils ne sont pas des cours certifiés et ne seront pas les valeurs obtenues sur Yahoo aujourd'hui.

## Revue avant merge

Le reviewer vérifie les calculs, les dates communes, l'absence de rendement codé en dur, et le comportement de `python src/main.py`. La couche `analytics.py` ne doit contenir aucune dépendance spécifique à Yahoo, Bloomberg, AAPL ou SP500.

**GO TD08** si les analytics sont fonctionnelles **sur team main** après review, merge et exécution. Sinon, corriger ou terminer la PR TD07, sans déclarer TD08 validé.

## Répartition de groupe

Deux personnes peuvent travailler sur les calculs pendant que les autres vérifient la normalisation, les tests et la revue. Chaque étudiant doit pouvoir expliquer une contribution réelle. Adapter la répartition à l'effectif réel, sans PR artificielle pour « remplir » des captures.

**Étape suivante :** [05 - TD08 Yahoo Finance](05_TD08_YAHOO.md).
