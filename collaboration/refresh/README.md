# Refresh TD01-TD06 | Linux, Python, Git et GitHub

**20 minutes de rappel actif, puis un laboratoire à refaire en autonomie.**

Vous n'avez pas besoin de mémoriser 50 commandes. Vous devez comprendre **quel problème professionnel chaque outil résout**, et savoir diagnostiquer la situation avant d'agir.

> Linux / Bash = observer et automatiser l'environnement.  
> Python = traiter des données et traduire un besoin métier en fonctions.  
> Git = enregistrer l'histoire des changements.  
> GitHub = coordonner les personnes, les PR et les décisions de revue.

Les scripts sont **pédagogiques**. Ils récapitulent les TD01-TD06, mais ne remplacent ni les labs CORE officiels, ni les preuves d'évaluation. Ils ne créent pas automatiquement les forks, les PR, les commentaires ou les approvals dans vos dépôts.

## Démarrage rapide - Codespaces ou Linux

Ouvrir le terminal à la racine du **fork partagé de votre équipe**, où se trouvent `src/`, `data/` et `collaboration/`.

```bash
bash collaboration/refresh/scripts/run_refresh.sh
```

**Mode par défaut : lecture seule.** Il vérifie l'environnement (TD01), explore les fichiers et commandes Linux (TD01) et explique les données CSV/JSON en Python (TD02).

Pour les simulations Git TD03-TD04, **dans des dépôts temporaires distincts** :

```bash
bash collaboration/refresh/scripts/run_refresh.sh --labs
```

Pour examiner votre situation Git/GitHub avant une vraie contribution :

```bash
bash collaboration/refresh/scripts/05_github_readonly_audit.sh
python3 collaboration/refresh/scripts/06_review_preflight.py --help
```

Sans Python 3 disponible sous `python3`, utiliser `python` si c'est Python 3. Ces scripts n'ont pas besoin de `pip install`.

## Ce que couvre le dossier

| TD | Question professionnelle | Script | Modèle mental |
| --- | --- | --- | --- |
| [TD01](../../docs/labs/TD01_BOOTSTRAP_LINUX.md) | Où suis-je, quels fichiers et outils ai-je ? | [00_preflight.sh](scripts/00_preflight.sh), [01_linux_explorer.sh](scripts/01_linux_explorer.sh) | L'environnement de travail est observable et reproductible |
| [TD02](../../docs/labs/TD02_PYTHON_CSV_JSON.md) | Comment exploiter des données financières reçues en CSV/JSON ? | [02_python_csv_json.py](scripts/02_python_csv_json.py) | Entrées -> traitement -> sortie, avec types et fonctions |
| [TD03](../../docs/labs/TD03_GIT_LOCAL_WORKFLOW.md) | Comment retracer ce qui a changé ? | [03_git_local_demo.sh](scripts/03_git_local_demo.sh) | Working tree -> staging area -> commit |
| [TD04](../../docs/labs/TD04_BRANCHES_AND_MERGE.md) | Comment isoler une fonctionnalité ? | [04_git_branches_demo.sh](scripts/04_git_branches_demo.sh) | main stable + feature isolée -> merge |
| [TD05](../../docs/labs/TD05_FORK_AND_PULL_REQUEST.md) | Comment synchroniser une contribution avec l'équipe ? | [05_github_readonly_audit.sh](scripts/05_github_readonly_audit.sh) | Local -> origin (fork partagé) -> PR ciblant team main |
| [TD06](../../docs/labs/TD06_CODE_REVIEW.md) | Comment décider si une modification est intégrable ? | [06_review_preflight.py](scripts/06_review_preflight.py) | Critères + diff + test + humain -> décision de review |

Lire aussi [les modèles mentaux](MENTAL_MODELS.md) et [les exercices / prolongements](EXERCISES.md).

## Plan de révision en séance (13h30-13h50)

- **4 min** : reconstituer collectivement le parcours des six TD.
- **7 min** : six questions flash en binômes.
- **7 min** : exécuter `00_preflight.sh` et/ou `01_linux_explorer.sh`, puis observer la branche, le remote et `git status`.
- **2 min** : formuler le passage de l'historique Git à **Issue -> Developer / Reviewer -> Branch -> PR -> Review -> Merge**.

**Important :** ce parcours court n'exécute pas la totalité des six démonstrations. Les scripts Git et Python complémentaires peuvent être étudiés en autonomie.

## Sécurité et limites

- Les scripts `00`, `01`, `02`, `05` et `06` sont **en lecture seule** sur le dépôt de l'équipe.
- Les scripts `03` et `04` créent leurs commits et leurs merges **uniquement dans un dépôt de laboratoire temporaire**, affiché à l'écran. Ils ne poussent rien sur GitHub.
- Le laboratoire ne se supprime pas automatiquement, pour que vous puissiez explorer son historique.
- `05` accepte éventuellement `--github` pour **consulter** le dépôt/les PR avec la CLI `gh` si elle est installée et authentifiée. Aucune action GitHub n'est déclenchée par défaut.
- `06` vérifie la cohérence des informations que vous fournissez. Il **ne prouve pas** l'assignation GitHub, l'approbation d'un reviewer ou l'exécution des tests.
- **Ne jamais copier des tokens, mots de passe, données scolaires ou documents privés** dans un dépôt public.
- Ne pas lancer ce kit comme remplaçant des instructions officielles du TD ni comme générateur de captures obligatoires.

## Direction : après les TD01-TD06

La nouvelle méthode est [Issue-First](../01_ISSUES_ET_ROLES.md). Pour TD07 et TD08, les mêmes outils servent à intégrer des fonctions [Analytics](../04_TD07_ANALYTICS.md) puis un fournisseur [Yahoo](../05_TD08_YAHOO.md), après validation du socle.

Au projet final, vous devrez pouvoir refaire cette organisation **sans Starter**, dans un nouveau dépôt, et expliquer vos décisions. C'est l'autonomie que l'on construit progressivement.

**Pour l'instructeur :** cette synthèse est une réactivation formative des six notions, pas une attestation d'achèvement individuel des six CORE.
