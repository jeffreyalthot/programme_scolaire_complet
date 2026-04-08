from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import argparse
import json
import random
import tkinter as tk
from tkinter import ttk
from typing import List


COMPETENCES_QUEBEC = [
    "Développement physique et moteur",
    "Développement affectif",
    "Développement social",
    "Développement langagier",
    "Développement cognitif",
]


THEMES_MENSUELS = [
    ("Août", "Rentrée et adaptation"),
    ("Septembre", "Moi, l'école et mes amis"),
    ("Octobre", "Automne, récoltes et couleurs"),
    ("Novembre", "Famille, entraide et communauté"),
    ("Décembre", "Fêtes, cultures et traditions"),
    ("Janvier", "Hiver, neige et environnement"),
    ("Février", "Corps humain, santé et émotions"),
    ("Mars", "Animaux et habitats"),
    ("Avril", "Eau, météo et sciences"),
    ("Mai", "Nature, jardin et croissance"),
    ("Juin", "Bilan, projets finaux et transition"),
]


@dataclass
class Activite:
    titre: str
    domaine: str
    description: str
    materiel: List[str]
    duree_minutes: int
    interaction: str
    evaluation: str


@dataclass
class Semaine:
    numero: int
    theme: str
    objectifs: List[str]
    routine_quotidienne: List[str]
    activites: List[Activite]
    collaboration_famille: str


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
    principes_pedagogiques: List[str]
    mois: List[Mois]

    def to_dict(self) -> dict:
        return asdict(self)


def objectifs_hebdomadaires() -> List[str]:
    return [
        "Développer l'autonomie (routines, transitions, choix de matériel).",
        "Favoriser la communication orale et l'écoute active.",
        "Renforcer les habiletés socioaffectives: coopération, partage, gestion des émotions.",
        "Explorer la numératie (quantités, comparaison, formes, régularités).",
        "Stimuler la curiosité scientifique et artistique par la manipulation.",
    ]


def activites_par_defaut(theme: str) -> List[Activite]:
    return [
        Activite(
            titre=f"Causerie et lecture interactive - {theme}",
            domaine="Développement langagier",
            description=(
                "Lecture dialoguée d'un album, questions de compréhension et reformulation par les enfants."
            ),
            materiel=["Album illustré", "Marottes", "Cartes de vocabulaire"],
            duree_minutes=30,
            interaction="Prise de parole en cercle, vote d'idées et jeu des rimes.",
            evaluation="Grille d'observation: vocabulaire, articulation et écoute.",
        ),
        Activite(
            titre=f"Parcours moteur coopératif - {theme}",
            domaine="Développement physique et moteur",
            description=(
                "Parcours de motricité globale avec stations d'équilibre, de saut et de coordination."
            ),
            materiel=["Cerceaux", "Cônes", "Tapis", "Poutre basse", "Ballons mous"],
            duree_minutes=35,
            interaction="Défis en duo et encouragement entre pairs.",
            evaluation="Observation des stratégies motrices, endurance et sécurité.",
        ),
        Activite(
            titre=f"Atelier émotions et vivre-ensemble - {theme}",
            domaine="Développement affectif",
            description=(
                "Jeux de rôle, cartes d'émotions et coin calme pour reconnaître et nommer ses ressentis."
            ),
            materiel=["Cartes d'émotions", "Miroir", "Marionnette", "Affiche des solutions"],
            duree_minutes=25,
            interaction="Expression guidée: “Je ressens… quand…”.",
            evaluation="Journal de classe: participation et stratégies d'autorégulation.",
        ),
        Activite(
            titre=f"Mini-laboratoire de découverte - {theme}",
            domaine="Développement cognitif",
            description=(
                "Manipulations, tri, classement et résolution de petits problèmes selon le thème de la semaine."
            ),
            materiel=["Bacs sensoriels", "Objets à trier", "Pinces", "Loupes"],
            duree_minutes=30,
            interaction="Prédiction, expérimentation et partage d'hypothèses.",
            evaluation="Trace anecdotique des stratégies et du raisonnement.",
        ),
        Activite(
            titre=f"Création artistique et musicale - {theme}",
            domaine="Développement social",
            description=(
                "Projet d'art collectif combiné à des rythmes simples, chants et mouvements."
            ),
            materiel=["Peinture", "Papiers texturés", "Instruments rythmiques", "Colle"],
            duree_minutes=40,
            interaction="Création en équipes avec rôles tournants.",
            evaluation="Autoévaluation visuelle (smileys) et rétroaction positive.",
        ),
    ]


def creer_programme_annuel(annee_scolaire: str = "2026-2027") -> ProgrammeMaternelle:
    mois_programme: List[Mois] = []
    semaine_no = 1

    for nom_mois, theme_general in THEMES_MENSUELS:
        semaines: List[Semaine] = []
        for index in range(1, 5):
            theme = f"{theme_general} - Semaine {index}"
            semaines.append(
                Semaine(
                    numero=semaine_no,
                    theme=theme,
                    objectifs=objectifs_hebdomadaires(),
                    routine_quotidienne=[
                        "Accueil et jeu libre guidé (15 min)",
                        "Causerie du matin et calendrier (20 min)",
                        "Blocs d'ateliers actifs (2 x 35 min)",
                        "Jeu extérieur / motricité (45 min)",
                        "Retour réflexif et lecture détente (20 min)",
                    ],
                    activites=activites_par_defaut(theme),
                    collaboration_famille=(
                        "Envoyer une capsule famille: défi de vocabulaire, lecture partagée et activité pratique à la maison."
                    ),
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
        principes_pedagogiques=[
            "Approche par le jeu actif et signifiant.",
            "Différenciation pédagogique et inclusion.",
            "Partenariat école-famille-communauté.",
            "Évaluation formative continue par observation.",
        ],
        mois=mois_programme,
    )


def sauvegarder_programme(chemin: Path, annee_scolaire: str = "2026-2027") -> ProgrammeMaternelle:
    programme = creer_programme_annuel(annee_scolaire)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(
        json.dumps(programme.to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return programme


class ProgrammeMaternelleApp(tk.Tk):
    def __init__(self, programme: ProgrammeMaternelle) -> None:
        super().__init__()
        self.programme = programme
        self.title("Programme Maternelle Québec - Interface éducative")
        self.geometry("1200x760")
        self.configure(bg="#F3F8FF")

        self.current_month_idx = 0
        self.current_week_idx = 0
        self.quiz_answer = tk.IntVar(value=0)

        self._build_ui()
        self._refresh_content()
        self._animate_header()

    def _build_ui(self) -> None:
        header = tk.Frame(self, bg="#D9ECFF", height=150)
        header.pack(fill="x", side="top")

        self.banner = tk.Canvas(header, height=150, bg="#D9ECFF", highlightthickness=0)
        self.banner.pack(fill="both", expand=True)
        self.sun = self.banner.create_oval(25, 20, 95, 90, fill="#FFD54F", outline="")
        self.cloud = self.banner.create_oval(930, 35, 1060, 95, fill="#FFFFFF", outline="")
        self.cloud2 = self.banner.create_oval(980, 20, 1120, 85, fill="#FFFFFF", outline="")
        self.mascot = self.banner.create_oval(520, 40, 600, 120, fill="#7ED957", outline="")
        self.eye1 = self.banner.create_oval(545, 68, 555, 78, fill="#1B4332", outline="")
        self.eye2 = self.banner.create_oval(565, 68, 575, 78, fill="#1B4332", outline="")
        self.banner.create_text(
            250,
            45,
            text="Maternelle 5 ans - Programme annuel interactif",
            fill="#0F3D91",
            font=("Helvetica", 20, "bold"),
            anchor="w",
        )
        self.banner.create_text(
            250,
            85,
            text="Découvrir, jouer, apprendre - Une année complète alignée pour la petite enfance.",
            fill="#1F5DAA",
            font=("Helvetica", 13),
            anchor="w",
        )

        body = tk.Frame(self, bg="#F3F8FF")
        body.pack(fill="both", expand=True, padx=14, pady=14)

        left = tk.Frame(body, bg="#F3F8FF")
        left.pack(side="left", fill="y", padx=(0, 10))

        ttk.Label(left, text="Mois", font=("Helvetica", 12, "bold")).pack(anchor="w")
        self.month_list = tk.Listbox(left, height=12, width=28, exportselection=False, font=("Helvetica", 11))
        self.month_list.pack(pady=(5, 12))
        for mois in self.programme.mois:
            self.month_list.insert("end", mois.nom)
        self.month_list.bind("<<ListboxSelect>>", self._on_month_select)
        self.month_list.selection_set(0)

        ttk.Label(left, text="Semaines du mois", font=("Helvetica", 12, "bold")).pack(anchor="w")
        self.week_list = tk.Listbox(left, height=10, width=28, exportselection=False, font=("Helvetica", 11))
        self.week_list.pack(pady=(5, 8))
        self.week_list.bind("<<ListboxSelect>>", self._on_week_select)

        right = tk.Frame(body, bg="#FFFFFF", highlightbackground="#C9DEF8", highlightthickness=2)
        right.pack(side="left", fill="both", expand=True)

        tool_bar = tk.Frame(right, bg="#FFFFFF")
        tool_bar.pack(fill="x", padx=12, pady=10)
        ttk.Button(tool_bar, text="Objectifs", command=lambda: self._refresh_content("objectifs")).pack(side="left", padx=4)
        ttk.Button(tool_bar, text="Activités", command=lambda: self._refresh_content("activites")).pack(side="left", padx=4)
        ttk.Button(tool_bar, text="Évaluation", command=lambda: self._refresh_content("evaluation")).pack(side="left", padx=4)
        ttk.Button(tool_bar, text="Jeu rapide", command=self._open_quiz).pack(side="left", padx=4)

        self.text = tk.Text(right, wrap="word", font=("Helvetica", 11), bg="#FFFFFF", padx=10, pady=10)
        self.text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def _on_month_select(self, _event: object) -> None:
        selection = self.month_list.curselection()
        if not selection:
            return
        self.current_month_idx = selection[0]
        self.current_week_idx = 0
        self._load_weeks()
        self._refresh_content()

    def _on_week_select(self, _event: object) -> None:
        selection = self.week_list.curselection()
        if not selection:
            return
        self.current_week_idx = selection[0]
        self._refresh_content()

    def _load_weeks(self) -> None:
        self.week_list.delete(0, "end")
        mois = self.programme.mois[self.current_month_idx]
        for semaine in mois.semaines:
            self.week_list.insert("end", f"S{semaine.numero} - {semaine.theme}")
        self.week_list.selection_set(0)

    def _refresh_content(self, mode: str = "activites") -> None:
        if self.week_list.size() == 0:
            self._load_weeks()

        mois = self.programme.mois[self.current_month_idx]
        semaine = mois.semaines[self.current_week_idx]

        self.text.delete("1.0", "end")
        self.text.insert("end", f"{mois.nom} • {semaine.theme}\n", "title")
        self.text.insert("end", f"Période: {mois.periode}\n\n")

        if mode == "objectifs":
            self.text.insert("end", "Objectifs ciblés:\n")
            for obj in semaine.objectifs:
                self.text.insert("end", f"  • {obj}\n")
            self.text.insert("end", "\nRoutine quotidienne:\n")
            for routine in semaine.routine_quotidienne:
                self.text.insert("end", f"  • {routine}\n")
        elif mode == "evaluation":
            self.text.insert("end", "Évaluation formative:\n")
            for activite in semaine.activites:
                self.text.insert("end", f"\n- {activite.titre}\n")
                self.text.insert("end", f"  Domaine: {activite.domaine}\n")
                self.text.insert("end", f"  Critère observé: {activite.evaluation}\n")
            self.text.insert("end", f"\nLien famille-école:\n{semaine.collaboration_famille}\n")
        else:
            self.text.insert("end", "Ateliers de la semaine:\n")
            for activite in semaine.activites:
                self.text.insert("end", f"\n- {activite.titre}\n")
                self.text.insert("end", f"  Domaine: {activite.domaine}\n")
                self.text.insert("end", f"  Durée: {activite.duree_minutes} minutes\n")
                self.text.insert("end", f"  Description: {activite.description}\n")
                self.text.insert("end", f"  Interaction enfant: {activite.interaction}\n")
                self.text.insert("end", "  Matériel: " + ", ".join(activite.materiel) + "\n")

        self.text.tag_config("title", font=("Helvetica", 15, "bold"), foreground="#0F3D91")

    def _open_quiz(self) -> None:
        quiz = tk.Toplevel(self)
        quiz.title("Mini-jeu éducatif")
        quiz.geometry("420x310")
        quiz.configure(bg="#FFF9E8")

        a = random.randint(1, 5)
        b = random.randint(1, 5)
        bonne_reponse = a + b

        tk.Label(
            quiz,
            text="Jeu de numératie - Compte les objets!",
            bg="#FFF9E8",
            fg="#A05A00",
            font=("Helvetica", 14, "bold"),
        ).pack(pady=10)

        tk.Label(
            quiz,
            text=f"Combien font {a} + {b} ?",
            bg="#FFF9E8",
            font=("Helvetica", 13),
        ).pack(pady=8)

        ttk.Entry(quiz, textvariable=self.quiz_answer, width=8).pack(pady=8)
        feedback = tk.Label(quiz, text="", bg="#FFF9E8", font=("Helvetica", 11, "bold"))
        feedback.pack(pady=8)

        stars = tk.Canvas(quiz, width=280, height=80, bg="#FFF9E8", highlightthickness=0)
        stars.pack(pady=6)
        star_items = [stars.create_oval(20 + i * 60, 20, 50 + i * 60, 50, fill="#D0D0D0", outline="") for i in range(4)]

        def verifier() -> None:
            if self.quiz_answer.get() == bonne_reponse:
                feedback.config(text="Bravo! Excellente réponse 🎉", fg="#2B9348")
                for item in star_items:
                    stars.itemconfig(item, fill="#FFD60A")
            else:
                feedback.config(text="Essaye encore, tu peux le faire 💪", fg="#D00000")
                for item in star_items:
                    stars.itemconfig(item, fill="#D0D0D0")

        ttk.Button(quiz, text="Vérifier", command=verifier).pack(pady=4)

    def _animate_header(self) -> None:
        self.banner.move(self.sun, 0.6, 0)
        self.banner.move(self.cloud, -1.1, 0)
        self.banner.move(self.cloud2, -0.9, 0)

        x1, _, x2, _ = self.banner.coords(self.sun)
        if x2 > 1240:
            self.banner.coords(self.sun, 25, 20, 95, 90)

        cx1, _, cx2, _ = self.banner.coords(self.cloud)
        if cx2 < -20:
            self.banner.coords(self.cloud, 930, 35, 1060, 95)

        cx1b, _, cx2b, _ = self.banner.coords(self.cloud2)
        if cx2b < -30:
            self.banner.coords(self.cloud2, 980, 20, 1120, 85)

        phase = random.choice([-1, 1]) * 1.2
        for item in (self.mascot, self.eye1, self.eye2):
            self.banner.move(item, 0, phase)

        self.after(90, self._animate_header)


def lancer_interface(programme: ProgrammeMaternelle) -> None:
    app = ProgrammeMaternelleApp(programme)
    app.mainloop()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Générateur et interface du programme annuel de maternelle (Québec)."
    )
    parser.add_argument("--annee", default="2026-2027", help="Année scolaire (ex: 2026-2027)")
    parser.add_argument(
        "--sortie",
        default="data/maternelle_annee_complete.json",
        help="Chemin du fichier JSON de sortie",
    )
    parser.add_argument(
        "--ui",
        action="store_true",
        help="Lancer l'interface Tkinter interactive après la génération",
    )

    args = parser.parse_args()
    programme = sauvegarder_programme(Path(args.sortie), args.annee)
    print(f"Programme annuel généré : {args.sortie}")

    if args.ui:
        lancer_interface(programme)


if __name__ == "__main__":
    main()
