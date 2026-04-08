from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import List


COMPETENCES_QUEBEC = [
    "Développement physique et moteur",
    "Développement affectif",
    "Développement social",
    "Développement langagier",
    "Développement cognitif",
]


@dataclass
class Activite:
    titre: str
    domaine: str
    description: str
    materiel: List[str]
    evaluation: str


@dataclass
class Semaine:
    numero: int
    theme: str
    objectifs: List[str]
    activites: List[Activite]


@dataclass
class Mois:
    nom: str
    periode: str
    semaines: List[Semaine]


@dataclass
class ProgrammeMaternelle:
    niveau: str
    annee_scolaire: str
    competences: List[str]
    mois: List[Mois]

    def to_dict(self) -> dict:
        return asdict(self)


def activites_par_defaut(theme: str) -> List[Activite]:
    return [
        Activite(
            titre=f"Atelier langage - {theme}",
            domaine="Développement langagier",
            description=(
                "Discussion guidée, lecture d'album et production orale en lien avec le thème."
            ),
            materiel=["Album illustré", "Cartes de vocabulaire", "Tableau"],
            evaluation="Grille d'observation du vocabulaire, de l'écoute et de la participation.",
        ),
        Activite(
            titre=f"Atelier moteur - {theme}",
            domaine="Développement physique et moteur",
            description=(
                "Parcours moteur favorisant l'équilibre, la coordination et la motricité globale."
            ),
            materiel=["Cerceaux", "Cônes", "Tapis", "Cordes"],
            evaluation="Observation des habiletés motrices et de la persévérance.",
        ),
        Activite(
            titre=f"Atelier découverte - {theme}",
            domaine="Développement cognitif",
            description=(
                "Manipulations, tri, classification et résolution de problèmes adaptés à 5 ans."
            ),
            materiel=["Objets à trier", "Bacs sensoriels", "Pictogrammes"],
            evaluation="Trace anecdotique sur les stratégies et l'autonomie.",
        ),
    ]


def creer_programme_annuel(annee_scolaire: str = "2026-2027") -> ProgrammeMaternelle:
    calendrier = [
        ("Août", "Rentrée et adaptation"),
        ("Septembre", "Moi et mon école"),
        ("Octobre", "Automne et récoltes"),
        ("Novembre", "Famille et communauté"),
        ("Décembre", "Fêtes et traditions"),
        ("Janvier", "Hiver et environnement"),
        ("Février", "Corps humain et santé"),
        ("Mars", "Animaux et habitats"),
        ("Avril", "Eau, météo et sciences"),
        ("Mai", "Jardin, nature et croissance"),
        ("Juin", "Bilan et transition vers la 1re année"),
    ]

    mois_programme: List[Mois] = []

    semaine_no = 1
    for nom_mois, theme_general in calendrier:
        semaines: List[Semaine] = []
        for indice in range(1, 5):
            theme = f"{theme_general} - Semaine {indice}"
            semaines.append(
                Semaine(
                    numero=semaine_no,
                    theme=theme,
                    objectifs=[
                        "Développer l'autonomie dans les routines de classe.",
                        "Renforcer les habiletés sociales par le jeu coopératif.",
                        "Stimuler le langage oral et les premières notions en littératie.",
                        "Explorer les bases en numératie et raisonnement logique.",
                    ],
                    activites=activites_par_defaut(theme),
                )
            )
            semaine_no += 1

        mois_programme.append(
            Mois(
                nom=nom_mois,
                periode=f"{nom_mois} {annee_scolaire}",
                semaines=semaines,
            )
        )

    return ProgrammeMaternelle(
        niveau="Maternelle 5 ans",
        annee_scolaire=annee_scolaire,
        competences=COMPETENCES_QUEBEC,
        mois=mois_programme,
    )


def sauvegarder_programme(chemin: Path, annee_scolaire: str = "2026-2027") -> None:
    programme = creer_programme_annuel(annee_scolaire)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(
        json.dumps(programme.to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    sortie = Path("data/maternelle_annee_complete.json")
    sauvegarder_programme(sortie)
    print(f"Programme annuel généré : {sortie}")
