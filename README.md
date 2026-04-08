# programme_scolaire_complet

Base de travail pour construire un **programme d'éducation officiel du Québec**, en commençant par la **maternelle 5 ans**.

## Contenu

- `src/programme_maternelle.py` :
  - génère un programme annuel complet (11 mois, 44 semaines),
  - exporte un JSON prêt à utiliser,
  - propose une interface Tkinter interactive pour consultation pédagogique.
- `data/maternelle_annee_complete.json` : sortie de référence.

## Couverture pédagogique (maternelle)

Le programme inclut :

- Les 5 compétences globales (physique/moteur, affectif, social, langagier, cognitif).
- 11 mois (août à juin), 4 semaines par mois.
- Pour chaque semaine :
  - objectifs pédagogiques,
  - routine quotidienne structurée,
  - 5 ateliers complets (langage, motricité, émotions, découverte, création),
  - matériel, durée, interactions enfant,
  - modalités d'évaluation formative,
  - proposition de collaboration famille-école.

## Générer le programme

```bash
python3 src/programme_maternelle.py
```

## Lancer l'interface Tkinter (avec animations)

```bash
python3 src/programme_maternelle.py --ui
```

Fonctionnalités de l'interface :

- Navigation par mois et semaines.
- Affichage détaillé : objectifs, activités, évaluation.
- Bandeau animé attractif (soleil, nuages, mascotte) adapté aux jeunes enfants.
- Mini-jeu interactif de numératie avec rétroaction immédiate.

## Personnalisation rapide

- Changer l'année scolaire : `--annee 2027-2028`
- Changer le chemin de sortie JSON : `--sortie data/autre_fichier.json`

## Prochaines améliorations possibles

1. Ajouter des profils d'adaptation (EHDAA, enrichissement, soutien ciblé).
2. Ajouter des fiches imprimables hebdomadaires automatiquement.
3. Ajouter des mini-jeux supplémentaires (lettres, sons, séquences).
4. Connecter une banque d'images/sons éducatifs sous licence libre.
