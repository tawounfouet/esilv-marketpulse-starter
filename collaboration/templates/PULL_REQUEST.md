# Modèle de description de Pull Request

> À copier dans une **PR du fork d'équipe vers son main**. Remplacer le numéro ci-dessous par celui de **l'Issue de ce même dépôt**.

## Issue liée

Closes #123

**Note :** #123 est un EXEMPLE. Ne laissez pas ce numéro si ce n'est pas celui de l'Issue réelle.

## Développeur et reviewer

- Developer : @developer
- Reviewer demandé : @reviewer (différent du Developer)

## Ce que change cette PR

- [Fonctionnalité réalisée]
- [Fichiers modifiés et pourquoi]
- [Changement non inclus volontairement]

## Validation effectuée

- [ ] J'ai exécuté `python src/main.py`, ou j'ai expliqué pourquoi cela n'est pas encore possible.
- [ ] J'ai comparé les sorties avec les critères de l'Issue.
- [ ] Les chemins modifiés correspondent au besoin.
- [ ] Aucune donnée sensible / aucun mot de passe n'est publié.
- [ ] Mon code ne contient pas de valeurs de marché codées en dur.

**Résultat observé / commande :** [à renseigner honnêtement]

## Pour le reviewer

- Points à examiner : [calcul / données / régression / périmètre]
- Limites ou blocages connus : [à compléter]

## Avant merge

- [ ] Revue réelle reçue.
- [ ] Corrections seulement si défaut réel.
- [ ] Critères d'acceptation respectés.
- [ ] Destination confirmée : `main` de l'équipe.
