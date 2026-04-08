# programme_scolaire_complet

Base de travail pour construire un **programme d'éducation officiel du Québec**, en commençant par la **maternelle 5 ans**.

## Contenu ajouté

- `src/programme_maternelle.py` : script Python qui génère la structure annuelle complète.
- `data/maternelle_annee_complete.json` : sortie prête à être exploitée (11 mois, 44 semaines, activités planifiées).

## Ce que contient la base (maternelle)

Le programme annuel généré inclut :

- Les compétences globales ciblées (physique/moteur, affectif, social, langagier, cognitif).
- Une planification mensuelle (août à juin).
- 4 semaines par mois.
- Pour chaque semaine :
  - objectifs pédagogiques,
  - activités (langage, motricité, découverte),
  - matériel,
  - modalité d'évaluation formative.

## Générer / régénérer le programme

```bash
python3 src/programme_maternelle.py
```

Fichier produit : `data/maternelle_annee_complete.json`.

## Prochaines étapes suggérées

1. Aligner les objectifs sur les formulations exactes du **Programme-cycle de l'éducation préscolaire du Québec**.
2. Ajouter des compétences/attentes mesurables par étape (périodes de l'année).
3. Ajouter une différenciation (soutien, enrichissement, adaptation).
4. Générer des fiches hebdomadaires imprimables à partir du JSON.
