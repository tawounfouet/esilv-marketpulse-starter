# Les modèles mentaux qui rendent Linux, Python et Git utiles

## 1. Une vraie question de finance

Vous arrivez dans une équipe de marché. Un collègue vous transmet `instruments.json` et `prices.csv`. On vous demande de présenter le cours d'AAPL et le benchmark SP500, puis de faire évoluer l'application à plusieurs développeurs.

**Quel outil répond à quelle question ?**

```text
Environnement de travail (Linux / Bash)
    Où est mon programme ? Dans quel dossier ? Mes outils sont-ils prêts ?
                        |
                        v
Entrées métier (Python)
    Quel instrument ? Quelles lignes ? CSV texte ou valeur numérique ?
                        |
                        v
Application MarketPulse
    Même programme, même résultat reproductible pour l'équipe
                        |
                        v
Historique technique (Git)
    Qu'est-ce qui a changé ? Pourquoi ? Puis-je retrouver la version ?
                        |
                        v
Collaboration (GitHub)
    Qui propose ? Qui relit ? Quand intègre-t-on la feature dans main ?
```

## 2. Linux : le système de fichiers est une carte

`pwd` répond « où suis-je ? », `ls` répond « qu'y a-t-il ici ? », `cd` répond « où aller ? », `cat/head/grep` répondent « que contiennent les fichiers ? ».

**Modèle mental :** vous naviguez dans un espace structuré, pas dans une collection d'icônes. Les chemins relatifs dépendent de votre dossier courant.

**En entreprise :** diagnostic d'une application sur serveur Linux, inspection de logs, exécution reproductible d'un pipeline, prise en main d'un conteneur ou d'une VM. Un script Bash coordonne plusieurs commandes système.

Question : que se passe-t-il si vous lancez `python src/main.py` depuis le mauvais dossier ?

## 3. Python : entrée, contrat, transformation et sortie

`JSON` fournit des objets structurés, souvent représentés en dictionnaires Python. `CSV` fournit des lignes tabulaires, souvent représentées en **liste de dictionnaires**.

Attention : un champ `"close"` lu depuis un CSV arrive comme chaîne de caractères. `float("250.00")` est un nombre, alors que `"250.00"` est du texte.

**Modèle mental :** 
- entrée et schéma attendu ;
- vérification des types ;
- fonctions réutilisables ;
- sortie vérifiable.

Exemple : la même fonction de synthèse peut traiter AAPL et SP500. On ne duplique pas le code métier lorsqu'une donnée change.

**En entreprise :** reporting financier, réconciliation de fichiers de marché, contrôles qualité, intégration de données fournisseur, back-office et API. Un programme Python exprime la logique métier ; Bash l'orchestration du système.

Question : pourquoi faut-il séparer `load_prices()`, `filter_prices()` et `main()` ?

## 4. Git local : trois espaces, trois questions

```text
Working tree      -> ce que j'ai modifié sur mon disque
    |
  git add
    v
Staging area      -> les changements que je CHOISIS d'enregistrer
    |
  git commit
    v
Historique Git    -> un instantané traçable et son message
```

`git status` est le tableau de bord. `git diff` montre des changements non indexés. `git diff --staged` montre ce qui entre dans le prochain commit. `git log` montre l'histoire.

**En entreprise :** comprendre un bug, comparer deux versions, passer le relais, auditer une modification et revenir à un état connu avec précaution.

Question : pourquoi `git add .` sans inspection peut-il être risqué ?

## 5. Les branches : travailler sans casser la baseline

`main` représente la version commune. Une branche `feature/...` est un espace isolé pour préparer un changement. Fusionner, c'est intégrer une histoire compatible dans la baseline.

Un conflit peut survenir lorsque deux contributions modifient de façon incompatible une même zone. Git détecte l'ambiguïté ; **les personnes choisissent la bonne intention métier**.

**En entreprise :** livraison incrémentale, développement parallèle, séparation de travaux en cours et version partagée.

Question : est-ce qu'un merge crée toujours un nouveau commit ? Non, pas nécessairement : il existe notamment les fast-forward merges.

## 6. Git n'est pas GitHub

- **Git** est le moteur local d'historique, de branches et de merges.
- **GitHub** héberge des dépôts distants et organise le travail en équipe.
- **origin** est un nom de remote, pas une garantie qu'il pointe vers le bon dépôt.
- **fork partagé** : dépôt d'équipe de la promotion, distinct du Starter enseignant.
- **Pull Request** : proposition argumentée d'intégration, avec une branche source et une base cible.
- **Code Review** : une personne examine réellement le diff et les critères avant de recommander l'intégration.

**En entreprise :** revue par les pairs, séparation des responsabilités, conformité, traçabilité, collaboration asynchrone.

Question : pourquoi une PR vers le Starter de l'instructeur est-elle une mauvaise destination pour le travail d'une équipe ?

## 7. Le nouveau modèle : partir du besoin

```text
Issue (besoin + critères)
  -> Developer assigné + Reviewer prévu
  -> feature branch
  -> implémentation + tests
  -> PR liée à l'Issue
  -> Code Review humaine
  -> merge dans team main
  -> synchronisation
  -> démonstration métier
```

Dans cette séance, les scripts servent à **voir le fonctionnement interne des outils**. Ensuite, vous devrez choisir les bonnes commandes sans vous reposer aveuglément sur une automatisation.

## 8. Choisir le bon outil plutôt que tout faire avec un seul

| Besoin | Premier outil | Pourquoi |
| --- | --- | --- |
| Où est mon fichier ? | Linux / Bash | Inspecter la structure du système |
| Vérifier les versions des programmes | Linux / Bash | Diagnostiquer l'environnement |
| Lire et filtrer CSV / JSON | Python | Manipuler des structures de données |
| Réutiliser une règle de calcul | Python | Fonction métier, testable |
| Voir ce qui a changé | Git | Diff et historique |
| Isoler une feature | Git | Branche |
| Soumettre à un pair | GitHub | PR et Code Review |
| Décrire une feature avant de coder | GitHub Issues | Objectifs et responsabilités |

**Pour aller plus loin :** automatisation de tests, CI/CD et déploiement feront sens une fois ces primitives comprises. Ce sont des étapes d'approfondissement, pas un prérequis nouveau pour la révision.
