# 06 - Fin de séance : preuves et prochaine action

**Source officielle unique pour les captures et la validation :** [docs/04_CHECKPOINTS_AND_EVIDENCE.md](../docs/04_CHECKPOINTS_AND_EVIDENCE.md). Ce fichier est un **mémo de séance**, pas un nouveau barème.

## Bilan express par équipe (16h35-16h45)

Montrez à l'instructeur :

- [ ] L'Issue TD07 dans le **fork d'équipe**, avec Developer assigné et Reviewer prévu.
- [ ] Votre branche feature et, si elle existe, la PR liée à l'Issue du même dépôt.
- [ ] Une revue technique argumentée ; résultat `Comment`, `Request changes` ou `Approve` cohérent.
- [ ] Le mini-lab de conflit jetable : marqueurs identifiés, choix expliqué, working tree propre.
- [ ] TD07 : valeur des calculs réellement vérifiée et exécution de `python src/main.py`.
- [ ] TD08 : état réel (non commencé, en cours, bloqué externe, vérifié), sans embellissement.
- [ ] Un blocage précis et **la prochaine action** de l'équipe.

La PR n'a pas besoin d'être fusionnée si un défaut réel subsiste. L'avancement honnête est préférable à une fusion prématurée.

## Checkpoint B - après TD08

Les quatre captures **officielles** sont :

| Fichier | Ce qu'il doit réellement prouver |
| --- | --- |
| `01_pull_request.png` | PR individuelle traçable |
| `02_code_review.png` | Vraie revue technique faite par l'étudiant |
| `03_yahoo_market_data.png` | Données Yahoo réellement récupérées pour AAPL et SP500 |
| `04_instrument_benchmark.png` | Comparaison cohérente instrument / benchmark |

Emplacement prévu par le contrat :

```text
evidence/checkpoint-b/<github-username>/
```

L'étudiant doit aussi rédiger son `README.md` individuel de checkpoint selon [le modèle canonique](../docs/04_CHECKPOINTS_AND_EVIDENCE.md). Ne pas déposer de preuves fictives ou des captures appartenant à d'autres étudiants.

**Checkpoint B n'est pas automatiquement terminé après cette séance.** Il se clôture après TD08 et les validations prescrites.

## Questions d'auto-évaluation

1. Pourquoi une branche de feature doit-elle être liée à une Issue d'équipe attribuée ?
2. Quelle est la différence entre une Code Review et la résolution d'un conflit de merge ?
3. Qu'est-ce qui distingue `Approve` de `Request changes` ?
4. Pourquoi faut-il aligner les dates avant de comparer deux rendements ?
5. Pourquoi `SP500` et `^GSPC` désignent-ils deux niveaux d'identifiant différents ?

## Préparation au projet final

La séance entraîne une méthode : **Issue -> rôles -> branche -> tests -> PR -> review -> merge -> démonstration**.

Le projet final envisagé devra reconstruire MarketPulse à partir d'**un nouveau dépôt vierge** et réutiliser cette démarche avec plus d'autonomie. Le cadrage du projet final doit encore être validé par l'équipe pédagogique.

**Confidentialité :** ne jamais publier dans les dépôts GitHub les emails scolaires, `Student_pk`, photos du trombinoscope, notes ou documents internes de suivi.
