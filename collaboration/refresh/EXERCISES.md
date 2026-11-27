# Exercices, questions flash et prolongements

## A. Challenge de 20 minutes - séance du 27 novembre

**Sans notation, par binôme.** La consigne n'est pas de prouver que tous les CORE ont été terminés.

1. Quel est le rôle de `pwd`, `ls` et `cd` ? Sur quel dossier devez-vous lancer `python src/main.py` ?
2. Un CSV renvoie `"250.00"` et un JSON renvoie un objet. Quels types Python reconnaissez-vous ?
3. Qu'est-ce qui distingue `git status`, `git add` et `git commit` ?
4. Pourquoi faut-il une branche `feature/...` plutôt que travailler directement sur `main` ?
5. Votre remote `origin` cible-t-il le fork partagé de l'équipe ou le Starter de l'instructeur ? Comment vérifier ?
6. Que doit faire un reviewer avant d'approuver une Pull Request ?

**Mini-vérification technique :**

```bash
bash collaboration/refresh/scripts/00_preflight.sh
bash collaboration/refresh/scripts/01_linux_explorer.sh
git branch --show-current
git status
```

Énoncez une chose que vous comprenez et une chose que vous avez encore besoin de clarifier.

## B. Autonomie après la séance - 30 à 45 minutes

1. **TD02 :** lancer `python3 collaboration/refresh/scripts/02_python_csv_json.py`. Identifier liste, dictionnaire et conversion numérique. Modifier oralement l'explication pour la série SP500.
2. **TD03 :** lancer `bash collaboration/refresh/scripts/03_git_local_demo.sh`, repérer trois états successifs et expliquer le rôle du staging.
3. **TD04 :** lancer `bash collaboration/refresh/scripts/04_git_branches_demo.sh`, observer `git log --graph --all` et expliquer ce que le merge intègre.
4. **TD05 :** lancer `bash collaboration/refresh/scripts/05_github_readonly_audit.sh` et confirmer la destination du remote. Ne rien pousser.
5. **TD06 :** lancer `python3 collaboration/refresh/scripts/06_review_preflight.py --issue 12 --developer alice --reviewer bob` avec des **valeurs fictives**, lire les avertissements. Remplacer ensuite par les véritables rôles de l'Issue d'équipe et vérifier manuellement dans GitHub.
6. Reprendre [le parcours collaboratif public](../README.md) et le [laboratoire de résolution des conflits](../03_LAB_CONFLITS_GIT.md).

Les scripts 03/04 créent des dépôts Git **distincts et temporaires**. Gardez leur chemin affiché si vous souhaitez les réexaminer. Ne les mélangez pas avec votre fork MarketPulse.

## C. Questions de transfert vers la vie professionnelle

- Un analyste remarque un écart de cours dans une extraction CSV. Que fait Bash ? Que fait Python ? Qu'apporte Git ?
- Deux développeurs changent `src/main.py`. Pourquoi une branche ne suffit-elle pas à assurer la qualité ?
- Une PR comporte deux commits, une autre vingt. Peut-on déduire laquelle est meilleure ?
- Un workflow automatisé annonce « tous les tests passent ». Pourquoi faut-il parfois encore une revue humaine ?
- Votre collègue n'arrive pas à exécuter MarketPulse. Quelles informations collecter avant d'installer de nouveaux outils ?

## D. Vers TD07 et TD08

Après ce rappel :
- [TD07 Analytics](../04_TD07_ANALYTICS.md) : normaliser, aligner les dates et comparer les performances.
- [TD08 Yahoo](../05_TD08_YAHOO.md) : réutiliser les analytics avec une acquisition distante après validation TD07.
- [Issues et rôles](../01_ISSUES_ET_ROLES.md) : la nouvelle règle de planification avant la branche.

**Le but n'est pas de jouer les scripts comme une recette.** Le but est d'être capable de reconstruire les étapes, les diagnostiquer et les expliquer à un collègue.
