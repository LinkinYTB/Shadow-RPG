import tkinter as tk
from tkinter import messagebox
import random


# ============================================================
# SHADOW RPG
# Version Tkinter - thème noir / blanc
# ============================================================

class ShadowRPG:

    def __init__(self, root):

        self.root = root

        self.root.title("SHADOW RPG")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)

        self.bg = "black"
        self.fg = "white"
        self.button_bg = "#202020"
        self.button_active = "#404040"

        self.nom = self.demander_nom()

        # ====================================================
        # JOUEUR
        # ====================================================

        self.pv_max = 100
        self.pv = 100

        self.attaque_base = 20
        self.defense_base = 5

        self.niveau = 1
        self.xp = 0

        self.pieces = 50
        self.potions = 3

        self.mobs_vaincus = 0

        # ====================================================
        # ÉPÉE SECRÈTE
        # ====================================================

        self.epee_secrete_decouverte = False

        # ====================================================
        # EASTER EGGS
        # ====================================================

        if self.nom == "snow":

            self.pv_max = 150
            self.pv = 150
            self.attaque_base = 25
            self.defense_base = 8

        elif self.nom == "take":

            self.attaque_base = 0

        elif self.nom == "fizz":

            pass

        elif self.nom == "louis":

            self.pv_max = 150
            self.pv = 150
            self.attaque_base = 25
            self.defense_base = 8

        elif self.nom == "sans":

            self.attaque_base = 22

        elif self.nom == "modo":

            self.niveau = 9999
            self.pieces = 9999
            self.mobs_vaincus = 9999
            self.attaque_base = 9999
            self.defense_base = 9999

        # ====================================================
        # ARMES
        # ====================================================

        self.armes = {

            "Épée en bois": {
                "attaque": 0,
                "prix": 0,
                "niveau_requis": 1,
                "niveau": 1
            },

            "Épée en fer": {
                "attaque": 10,
                "prix": 100,
                "niveau_requis": 2,
                "niveau": 1
            },

            "Lance en fer": {
                "attaque": 20,
                "prix": 250,
                "niveau_requis": 4,
                "niveau": 1
            },

            "Dague de la foudre": {
                "attaque": 35,
                "prix": 500,
                "niveau_requis": 7,
                "niveau": 1
            },

            "Faux des ténèbres": {
                "attaque": 50,
                "prix": 1000,
                "niveau_requis": 10,
                "niveau": 1
            },

            "Lame du Chevalier Déchu": {
                "attaque": 70,
                "prix": 3000,
                "niveau_requis": 20,
                "niveau": 1
            },

            # =================================================
            # ÉPÉE SECRÈTE
            # =================================================

            "Lame du Héro Absolu": {
                "attaque": 200,
                "prix": 5000,
                "niveau_requis": 25,
                "niveau": 1
            }
        }

        self.inventaire_armes = ["Épée en bois"]
        self.arme_equipee = "Épée en bois"

        # ====================================================
        # ARMURES
        # ====================================================

        self.armures = {

            "Vêtements simples": {
                "defense": 0,
                "pv": 0,
                "prix": 0,
                "niveau_requis": 1,
                "niveau": 1
            },

            "Armure de fer": {
                "defense": 8,
                "pv": 30,
                "prix": 200,
                "niveau_requis": 3,
                "niveau": 1
            },

            "Armure du chevalier": {
                "defense": 15,
                "pv": 70,
                "prix": 500,
                "niveau_requis": 6,
                "niveau": 1
            },

            "Armure des ombres": {
                "defense": 25,
                "pv": 120,
                "prix": 1000,
                "niveau_requis": 10,
                "niveau": 1
            },

            "Armure du roi déchu": {
                "defense": 40,
                "pv": 200,
                "prix": 2000,
                "niveau_requis": 15,
                "niveau": 1
            }
        }

        self.inventaire_armures = ["Vêtements simples"]
        self.armure_equipee = "Vêtements simples"

        # ====================================================
        # ZONES
        # ====================================================

        self.zones = {

            "Plaine": {
                "niveau": 1,
                "boss": "Boss de la Plaine",
                "boss_vaincu": False,
                "mobs_requis": 0,

                "monstres": [
                    ["Slime", 45, 10, 2, 15, 10],
                    ["Gobelin", 50, 12, 3, 20, 15],
                    ["Loup", 60, 14, 4, 25, 20]
                ],

                "boss_stats": [250, 25, 8, 100, 100]
            },

            "Forêt": {
                "niveau": 3,
                "boss": "Boss de la Forêt",
                "boss_vaincu": False,
                "mobs_requis": 10,

                "monstres": [
                    ["Loup géant", 90, 20, 7, 35, 30],
                    ["Ent", 120, 18, 10, 45, 40],
                    ["Gobelin noir", 100, 23, 8, 50, 45]
                ],

                "boss_stats": [400, 35, 12, 150, 150]
            },

            "Montagne": {
                "niveau": 6,
                "boss": "Boss de la Montagne",
                "boss_vaincu": False,
                "mobs_requis": 20,

                "monstres": [
                    ["Golem", 180, 30, 15, 70, 60],
                    ["Dragonnet", 160, 35, 12, 80, 70],
                    ["Ogre", 220, 32, 18, 90, 80]
                ],

                "boss_stats": [650, 45, 20, 250, 250]
            },

            "Royaume des Ombres": {
                "niveau": 10,
                "boss": "Roi des Ombres",
                "boss_vaincu": False,
                "mobs_requis": 35,

                "monstres": [
                    ["Ombre", 250, 45, 20, 120, 100],
                    ["Démon", 300, 50, 25, 150, 130],
                    ["Chevalier noir", 350, 55, 30, 180, 160]
                ],

                "boss_stats": [1000, 65, 35, 400, 400]
            },

            "Capitale déchue": {
                "niveau": 15,
                "boss": "Roi déchu",
                "boss_vaincu": False,
                "mobs_requis": 50,

                "monstres": [
                    ["Garde déchu", 800, 65, 30, 220, 180],
                    ["Chevalier maudit", 1000, 75, 35, 260, 220],
                    ["Seigneur déchu", 1200, 85, 40, 300, 250]
                ],

                "boss_stats": [2000, 95, 50, 700, 600]
            },

            "Citadelle déchue": {
                "niveau": 20,
                "boss": "Chevalier Déchu",
                "boss_vaincu": False,
                "mobs_requis": 75,

                "monstres": [
                    ["Soldat déchu", 1400, 90, 45, 350, 300],
                    ["Chevalier corrompu", 1700, 105, 55, 400, 350],
                    ["Gardien de la Citadelle", 2000, 120, 65, 450, 400]
                ],

                "boss_stats": [3500, 130, 70, 1000, 900]
            },

            # =================================================
            # ABYSSES
            # =================================================

            "Abysses": {
                "niveau": 25,
                "boss": "Seigneur des Abysses",
                "boss_vaincu": False,
                "mobs_requis": 100,

                "monstres": [
                    ["Démon des Abysses", 2500, 140, 75, 600, 500],
                    ["Créature abyssale", 3000, 155, 85, 700, 600],
                    ["Chevalier abyssal", 3500, 170, 100, 800, 700]
                ],

                "boss_stats": [6000, 190, 120, 1500, 1200]
            },

            # =================================================
            # ZONE SECRÈTE
            # =================================================

            "???": {
                "niveau": 1,
                "boss": "Shadow",
                "boss_vaincu": False,
                "mobs_requis": 100,

                "monstres": [
                    ["Créature ???", 1000, 70, 40, 250, 250],
                    ["Ombre ???", 1200, 80, 90, 300, 300],
                    ["Âme ???", 1500, 90, 110, 350, 350]
                ],

                "boss_stats": [10000, 100, 50, 1000, 1000]
            }
        }

        self.zone_actuelle = "Plaine"

        # ====================================================
        # INTERFACE
        # ====================================================

        self.creer_interface()
        self.actualiser()

    # ========================================================
    # NOM
    # ========================================================

    def demander_nom(self):

        fenetre = tk.Toplevel(self.root)

        fenetre.title("SHADOW RPG")
        fenetre.configure(bg="black")
        fenetre.geometry("500x250")

        fenetre.transient(self.root)
        fenetre.grab_set()

        resultat = {
            "nom": "Aventurier"
        }

        tk.Label(
            fenetre,
            text="Comment t'appelles-tu ?",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=30)

        entree = tk.Entry(
            fenetre,
            bg="#202020",
            fg="white",
            insertbackground="white",
            font=("Arial", 16)
        )

        entree.pack()

        def valider():

            nom = entree.get().strip()

            if nom:
                resultat["nom"] = nom.lower()

            fenetre.destroy()

        tk.Button(
            fenetre,
            text="Commencer",
            command=valider,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=18,
            height=2
        ).pack(pady=25)

        self.root.wait_window(fenetre)

        return resultat["nom"]

    # ========================================================
    # QUITTER AVEC ECHAP
    # ========================================================

    def quitter_jeu(self, event=None):

        reponse = messagebox.askyesno(
            "Quitter SHADOW RPG",
            "Veux-tu vraiment quitter le jeu ?",
            parent=self.root
        )

        if reponse:
            self.root.destroy()

    # ========================================================
    # MESSAGE
    # ========================================================

    def message(self, texte):

        messagebox.showinfo(
            "SHADOW RPG",
            texte,
            parent=self.root
        )

    # ========================================================
    # INTERFACE PRINCIPALE
    # ========================================================

    def creer_interface(self):

        titre = tk.Label(
            self.root,
            text="SHADOW RPG",
            bg="black",
            fg="white",
            font=("Arial", 32, "bold")
        )

        titre.pack(pady=15)

        self.stats = tk.Label(
            self.root,
            text="",
            bg="black",
            fg="white",
            font=("Arial", 14),
            justify="left"
        )

        self.stats.pack()

        self.zone_label = tk.Label(
            self.root,
            text="",
            bg="black",
            fg="white",
            font=("Arial", 22, "bold")
        )

        self.zone_label.pack(pady=10)

        self.log = tk.Text(
            self.root,
            width=110,
            height=18,
            bg="black",
            fg="white",
            insertbackground="white",
            selectbackground="#404040",
            font=("Consolas", 11),
            relief="solid",
            bd=1
        )

        self.log.pack(pady=10)

        self.log.config(state="disabled")

        frame = tk.Frame(
            self.root,
            bg="black"
        )

        frame.pack(pady=5)

        def bouton(texte, commande, ligne, colonne):

            tk.Button(
                frame,
                text=texte,
                command=commande,
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=18,
                height=2,
                font=("Arial", 11, "bold")
            ).grid(
                row=ligne,
                column=colonne,
                padx=5,
                pady=5
            )

        bouton("Explorer", self.explorer, 0, 0)
        bouton("Zones", self.menu_zones, 0, 1)
        bouton("Boss", self.menu_boss, 0, 2)
        bouton("Boutique", self.boutique, 0, 3)

        bouton("Inventaire", self.inventaire, 1, 0)
        bouton("Potion", self.utiliser_potion, 1, 1)
        bouton("Statistiques", self.afficher_stats, 1, 2)
        bouton("???", self.zone_secret, 1, 3)

    # ========================================================
    # LOG
    # ========================================================

    def afficher(self, texte):

        self.log.config(state="normal")
        self.log.insert("end", texte + "\n")
        self.log.see("end")
        self.log.config(state="disabled")

    # ========================================================
    # STATS
    # ========================================================

    def get_attaque(self):

        arme = self.armes[self.arme_equipee]

        return (
            self.attaque_base
            + arme["attaque"]
            + (arme["niveau"] - 1) * 5
        )

    def get_defense(self):

        armure = self.armures[self.armure_equipee]

        return (
            self.defense_base
            + armure["defense"]
            + (armure["niveau"] - 1) * 3
        )

    def get_pv_max(self):

        armure = self.armures[self.armure_equipee]

        return (
            self.pv_max
            + armure["pv"]
            + (armure["niveau"] - 1) * 10
        )

    # ========================================================
    # ACTUALISER
    # ========================================================

    def actualiser(self):

        pv_max = self.get_pv_max()

        if self.pv != float("inf"):

            if self.pv > pv_max:
                self.pv = pv_max

        self.stats.config(
            text=(
                f"Nom : {self.nom}    "
                f"Niveau : {self.niveau}    "
                f"XP : {self.xp}/{self.niveau * 50}\n"
                f"PV : {self.pv}/{pv_max}    "
                f"Attaque : {self.get_attaque()}    "
                f"Défense : {self.get_defense()}    "
                f"Pièces : {self.pieces}    "
                f"Potions : {self.potions}\n"
                f"Arme : {self.arme_equipee}    "
                f"Armure : {self.armure_equipee}    "
                f"Mobs vaincus : {self.mobs_vaincus}"
            )
        )

        self.zone_label.config(
            text=f"Zone : {self.zone_actuelle}"
        )

    # ========================================================
    # ESQUIVE
    # ========================================================

    def joueur_esquive(self):

        if self.nom == "fizz":

            if random.randint(1, 100) <= 15:

                self.afficher(
                    "Fizz esquive l'attaque !"
                )

                return True

        elif self.nom == "louis":

            if random.randint(1, 100) <= 25:

                self.afficher(
                    "Louis esquive l'attaque !"
                )

                return True

        return False

    # ========================================================
    # EXPLORER
    # ========================================================

    def explorer(self):

        if self.zone_actuelle == "???":

            self.combat_shadow()
            return

        chance = random.randint(1, 100)

        if chance <= 70:

            self.combat()

        elif chance <= 82:

            gain = random.randint(10, 40)

            self.pieces += gain

            self.afficher(
                f"Tu trouves {gain} pièces !"
            )

        elif chance <= 94:

            soin = random.randint(10, 30)

            if self.pv != float("inf"):

                self.pv = min(
                    self.get_pv_max(),
                    self.pv + soin
                )

            self.afficher(
                f"Tu récupères {soin} PV."
            )

        else:

            self.afficher(
                "Un mystérieux voyageur apparaît..."
            )

        self.actualiser()

    # ========================================================
    # COMBAT NORMAL
    # ========================================================

    def combat(self):

        zone = self.zones[self.zone_actuelle]

        monstre = random.choice(zone["monstres"])

        self.combat_interface(
            monstre[0],
            monstre[1],
            monstre[2],
            monstre[3],
            monstre[4],
            monstre[5]
        )

    # ========================================================
    # BOSS
    # ========================================================

    def menu_boss(self):

        fenetre = tk.Toplevel(self.root)

        fenetre.title("Boss")
        fenetre.configure(bg="black")

        fenetre.attributes(
            "-fullscreen",
            True
        )

        tk.Label(
            fenetre,
            text="BOSS DISPONIBLES",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        ordre = [
            "Plaine",
            "Forêt",
            "Montagne",
            "Royaume des Ombres",
            "Capitale déchue",
            "Citadelle déchue",
            "Abysses"
        ]

        for zone_nom in ordre:

            zone = self.zones[zone_nom]

            if zone["boss_vaincu"]:

                texte = (
                    f"{zone['boss']} - VAINCU"
                )

            else:

                texte = (
                    f"{zone['boss']} "
                    f"(Niv. {zone['niveau']})"
                )

            tk.Button(
                fenetre,
                text=texte,
                command=lambda z=zone_nom:
                self.lancer_boss(z, fenetre),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=35,
                height=2,
                font=("Arial", 13)
            ).pack(pady=7)

        tk.Button(
            fenetre,
            text="Retour",
            command=fenetre.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=30)

    # ========================================================
    # LANCER BOSS
    # ========================================================

    def lancer_boss(self, zone_nom, fenetre):

        zone = self.zones[zone_nom]

        if zone["boss_vaincu"]:

            self.message(
                "Tu as déjà vaincu ce boss."
            )

            return

        if self.niveau < zone["niveau"]:

            self.message(
                f"Tu dois être niveau {zone['niveau']}."
            )

            return

        if self.mobs_vaincus < zone["mobs_requis"]:

            self.message(
                f"Tu dois avoir vaincu "
                f"{zone['mobs_requis']} mobs."
            )

            return

        ordre = [
            "Plaine",
            "Forêt",
            "Montagne",
            "Royaume des Ombres",
            "Capitale déchue",
            "Citadelle déchue",
            "Abysses"
        ]

        index = ordre.index(zone_nom)

        if index > 0:

            precedente = ordre[index - 1]

            if not self.zones[precedente]["boss_vaincu"]:

                self.message(
                    f"Tu dois d'abord vaincre "
                    f"le boss de {precedente}."
                )

                return

        fenetre.destroy()

        stats = zone["boss_stats"]

        self.combat_interface(
            zone["boss"],
            stats[0],
            stats[1],
            stats[2],
            stats[3],
            stats[4],
            boss=True,
            zone_boss=zone_nom
        )

    # ========================================================
    # SHADOW
    # ========================================================

    def combat_shadow(self):

        stats = self.zones["???"]["boss_stats"]

        self.combat_interface(
            "Shadow",
            stats[0],
            stats[1],
            stats[2],
            stats[3],
            stats[4],
            boss=True,
            zone_boss="???"
        )

    # ========================================================
    # COMBAT
    # ========================================================

    def combat_interface(
        self,
        nom_ennemi,
        pv_ennemi,
        attaque_ennemi,
        defense_ennemi,
        xp_gain,
        pieces_gain,
        boss=False,
        zone_boss=None
    ):

        fenetre = tk.Toplevel(self.root)

        fenetre.title(
            f"Combat - {nom_ennemi}"
        )

        fenetre.configure(
            bg="black"
        )

        fenetre.attributes(
            "-fullscreen",
            True
        )

        fenetre.grab_set()

        label = tk.Label(
            fenetre,
            text="",
            bg="black",
            fg="white",
            font=("Arial", 22, "bold")
        )

        label.pack(pady=25)

        message = tk.Text(
            fenetre,
            width=100,
            height=18,
            bg="black",
            fg="white",
            insertbackground="white",
            font=("Consolas", 12),
            relief="solid",
            bd=1
        )

        message.pack(pady=10)

        message.config(state="disabled")

        defense_bonus = [0]
        combat_termine = [False]

        def log(texte):

            message.config(state="normal")
            message.insert("end", texte + "\n")
            message.see("end")
            message.config(state="disabled")

        def actualiser_combat():

            label.config(
                text=(
                    f"{self.nom} : "
                    f"{self.pv}/{self.get_pv_max()}\n\n"
                    f"{nom_ennemi} : "
                    f"{max(0, pv_ennemi)} PV"
                )
            )

        def fermer_combat():

            if fenetre.winfo_exists():

                try:
                    fenetre.grab_release()
                except:
                    pass

                fenetre.destroy()

            self.actualiser()

        # ====================================================
        # VICTOIRE
        # ====================================================

        def victoire():

            if combat_termine[0]:
                return

            combat_termine[0] = True

            self.mobs_vaincus += 1
            self.xp += xp_gain
            self.pieces += pieces_gain

            log("")
            log("VICTOIRE !")
            log(f"+{xp_gain} XP")
            log(f"+{pieces_gain} pièces")

            if boss and zone_boss:

                self.zones[zone_boss]["boss_vaincu"] = True

                log("")
                log(
                    f"Boss vaincu : {nom_ennemi}"
                )

                if zone_boss == "???":

                    log(
                        "Tu as vaincu Shadow !"
                    )

                elif zone_boss == "Capitale déchue":

                    log(
                        "La Capitale déchue est désormais conquise."
                    )

                elif zone_boss == "Citadelle déchue":

                    log(
                        "Le Chevalier Déchu est tombé !"
                    )

                    log(
                        "La Citadelle déchue est désormais conquise."
                    )

                elif zone_boss == "Abysses":

                    log(
                        "Le Seigneur des Abysses est tombé !"
                    )

                    log(
                        "Les Abysses sont désormais conquises."
                    )

            self.level_up()

            self.actualiser()

            fenetre.after(
                1000,
                fermer_combat
            )

        # ====================================================
        # ATTAQUER
        # ====================================================

        def attaque():

            nonlocal pv_ennemi

            if combat_termine[0]:
                return

            if self.nom == "take":

                log(
                    "Take a la flemme de se battre..."
                )

            else:

                esquive = False

                if nom_ennemi == "fizz":

                    if random.randint(1, 100) <= 15:
                        esquive = True

                elif nom_ennemi == "louis":

                    if random.randint(1, 100) <= 25:
                        esquive = True

                if esquive:

                    log(
                        f"{nom_ennemi} esquive ton attaque !"
                    )

                else:

                    attaque_totale = self.get_attaque()

                    degats = random.randint(
                        max(1, attaque_totale - 5),
                        attaque_totale + 5
                    )

                    degats = max(
                        1,
                        degats - defense_ennemi
                    )

                    pv_ennemi -= degats

                    log(
                        f"Tu infliges {degats} dégâts !"
                    )

                    # COUP CRITIQUE

                    if random.randint(1, 100) <= 10:

                        degats_crit = int(
                            degats * 0.5
                        )

                        pv_ennemi -= degats_crit

                        log(
                            f"COUP CRITIQUE ! "
                            f"+{degats_crit} dégâts !"
                        )

                    # FAUX DES TENEBRES

                    if self.arme_equipee == "Faux des ténèbres":

                        soin = int(
                            degats * 0.25
                        )

                        if self.pv != float("inf"):

                            self.pv = min(
                                self.get_pv_max(),
                                self.pv + soin
                            )

                        log(
                            f"La Faux des ténèbres "
                            f"te soigne de {soin} PV."
                        )

                    # LAME DU CHEVALIER DECHU

                    if self.arme_equipee == "Lame du Chevalier Déchu":

                        soin = int(
                            degats * 0.50
                        )

                        if self.pv != float("inf"):

                            self.pv = min(
                                self.get_pv_max(),
                                self.pv + soin
                            )

                        log(
                            f"La Lame du Chevalier Déchu "
                            f"te soigne de {soin} PV."
                        )

                    # EPEE DES ABYSSES

                    if self.arme_equipee == "Lame du Héro Absolu":

                        soin = int(
                            degats * 0.60
                        )

                        if self.pv != float("inf"):

                            self.pv = min(
                                self.get_pv_max(),
                                self.pv + soin
                            )

                        log(
                            f"L'Lame du Héro Absolu "
                            f"te soigne de {soin} PV."
                        )

                    # SANS

                    if self.nom == "sans":

                        soin = degats

                        if self.pv != float("inf"):

                            self.pv = min(
                                self.get_pv_max(),
                                self.pv + soin
                            )

                        log(
                            f"Sans récupère {soin} PV."
                        )

            if pv_ennemi <= 0:

                victoire()
                return

            actualiser_combat()

            tour_ennemi()

        # ====================================================
        # DEFENDRE
        # ====================================================

        def defendre():

            if combat_termine[0]:
                return

            defense_bonus[0] = 10

            log(
                "Tu te mets en position défensive."
            )

            tour_ennemi()

        # ====================================================
        # POTION
        # ====================================================

        def potion():

            if combat_termine[0]:
                return

            if self.potions <= 0:

                log(
                    "Tu n'as plus de potions."
                )

                return

            if self.pv == self.get_pv_max():

                log(
                    "Tes PV sont déjà au maximum."
                )

                return

            self.potions -= 1

            soin = random.randint(20, 40)

            if self.pv != float("inf"):

                self.pv = min(
                    self.get_pv_max(),
                    self.pv + soin
                )

            log(
                f"Tu récupères {soin} PV."
            )

            actualiser_combat()

            tour_ennemi()

        # ====================================================
        # FUIR
        # ====================================================

        def fuir():

            if combat_termine[0]:
                return

            if boss:

                log(
                    "Impossible de fuir devant un boss."
                )

                return

            if random.randint(1, 100) <= 50:

                log(
                    "Tu réussis à fuir."
                )

                fenetre.after(
                    500,
                    fermer_combat
                )

            else:

                log(
                    "Tu n'arrives pas à fuir."
                )

                tour_ennemi()

        # ====================================================
        # TOUR ENNEMI
        # ====================================================

        def tour_ennemi():

            if combat_termine[0]:
                return

            if pv_ennemi <= 0:
                return

            if nom_ennemi == "take":

                log(
                    "Take a la flemme."
                )

                log(
                    "Il ne t'attaque pas."
                )

            elif nom_ennemi == "chibicat12364":

                log(
                    "Chibicat12364 vous hurle dessus !"
                )

                log(
                    "Elle vous laisse à 1 PV et part."
                )

                self.pv = 1

                fenetre.after(
                    500,
                    fermer_combat
                )

                return

            else:

                if self.joueur_esquive():

                    actualiser_combat()

                    defense_bonus[0] = 0

                    return

                degats = random.randint(
                    max(1, attaque_ennemi - 3),
                    attaque_ennemi + 3
                )

                degats -= self.get_defense()
                degats -= defense_bonus[0]

                degats = max(
                    1,
                    degats
                )

                if self.pv != float("inf"):

                    self.pv -= degats

                log(
                    f"{nom_ennemi} t'inflige "
                    f"{degats} dégâts !"
                )

            defense_bonus[0] = 0

            actualiser_combat()

            if self.pv != float("inf"):

                if self.pv <= 0:

                    combat_termine[0] = True

                    fenetre.after(
                        500,
                        fermer_combat
                    )

                    self.mort()

        # ====================================================
        # BOUTONS COMBAT
        # ====================================================

        boutons = tk.Frame(
            fenetre,
            bg="black"
        )

        boutons.pack(pady=20)

        def bouton_combat(
            texte,
            commande,
            colonne
        ):

            tk.Button(
                boutons,
                text=texte,
                command=commande,
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=18,
                height=2,
                font=("Arial", 12, "bold")
            ).grid(
                row=0,
                column=colonne,
                padx=8
            )

        bouton_combat("Attaquer", attaque, 0)
        bouton_combat("Défendre", defendre, 1)
        bouton_combat("Potion", potion, 2)
        bouton_combat("Fuir", fuir, 3)

        actualiser_combat()

    # ========================================================
    # LEVEL UP
    # ========================================================

    def level_up(self):

        while self.xp >= self.niveau * 50:

            self.xp -= self.niveau * 50

            self.niveau += 1

            self.pv_max += 20
            self.attaque_base += 3
            self.defense_base += 2

            self.pv = self.get_pv_max()

            self.afficher(
                f"LEVEL UP ! Tu es maintenant "
                f"niveau {self.niveau}."
            )

    # ========================================================
    # POTION HORS COMBAT
    # ========================================================

    def utiliser_potion(self):

        if self.potions <= 0:

            self.message(
                "Tu n'as plus de potions."
            )

            return

        if self.pv == self.get_pv_max():

            self.message(
                "Tes PV sont déjà au maximum."
            )

            return

        self.potions -= 1

        soin = random.randint(20, 40)

        self.pv = min(
            self.get_pv_max(),
            self.pv + soin
        )

        self.afficher(
            f"Tu utilises une potion "
            f"et récupères {soin} PV."
        )

        self.actualiser()

    # ========================================================
    # MENU ZONES
    # ========================================================

    def menu_zones(self):

        fenetre = tk.Toplevel(self.root)

        fenetre.title("Zones")
        fenetre.configure(bg="black")

        fenetre.attributes(
            "-fullscreen",
            True
        )

        tk.Label(
            fenetre,
            text="CHOISIS UNE ZONE",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        zones_visibles = [
            "Plaine",
            "Forêt",
            "Montagne",
            "Royaume des Ombres",
            "Capitale déchue",
            "Citadelle déchue",
            "Abysses"
        ]

        for zone_nom in zones_visibles:

            zone = self.zones[zone_nom]

            texte = (
                f"{zone_nom} "
                f"(Niveau {zone['niveau']})"
            )

            tk.Button(
                fenetre,
                text=texte,
                command=lambda z=zone_nom:
                self.changer_zone(z, fenetre),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=35,
                height=2,
                font=("Arial", 13)
            ).pack(pady=7)

        tk.Button(
            fenetre,
            text="Retour",
            command=fenetre.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=30)

    # ========================================================
    # CHANGER DE ZONE
    # ========================================================

    def changer_zone(self, zone_nom, fenetre):

        zone = self.zones[zone_nom]

        if self.niveau < zone["niveau"]:

            self.message(
                f"Tu dois être niveau "
                f"{zone['niveau']}."
            )

            return

        if self.mobs_vaincus < zone["mobs_requis"]:

            self.message(
                f"Tu dois avoir vaincu "
                f"{zone['mobs_requis']} mobs."
            )

            return

        ordre = [
            "Plaine",
            "Forêt",
            "Montagne",
            "Royaume des Ombres",
            "Capitale déchue",
            "Citadelle déchue",
            "Abysses"
        ]

        index = ordre.index(zone_nom)

        if index > 0:

            precedente = ordre[index - 1]

            if not self.zones[precedente]["boss_vaincu"]:

                self.message(
                    f"Tu dois vaincre le boss de "
                    f"{precedente} avant d'entrer ici."
                )

                return

        self.zone_actuelle = zone_nom

        fenetre.destroy()

        self.afficher(
            f"Tu entres dans la zone : {zone_nom}"
        )

        self.actualiser()

    # ========================================================
    # ZONE SECRETE
    # ========================================================

    def zone_secret(self):

        if self.mobs_vaincus < 100:

            self.message(
                "La zone secrète est inaccessible."
            )

            return

        self.zone_actuelle = "???"

        self.afficher(
            "Une étrange présence t'attire..."
        )

        self.afficher(
            "Tu arrives dans la zone ???"
        )

        self.actualiser()

    # ========================================================
    # INVENTAIRE
    # ========================================================

    def inventaire(self):

        fenetre = tk.Toplevel(self.root)

        fenetre.title("Inventaire")
        fenetre.configure(bg="black")

        fenetre.attributes(
            "-fullscreen",
            True
        )

        tk.Label(
            fenetre,
            text="INVENTAIRE",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=25)

        tk.Label(
            fenetre,
            text="ARMES",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack()

        for arme in self.inventaire_armes:

            info = self.armes[arme]

            texte = (
                f"{arme} | "
                f"+{info['attaque']} attaque | "
                f"Niveau {info['niveau']}"
            )

            if arme == self.arme_equipee:
                texte += " | ÉQUIPÉE"

            tk.Button(
                fenetre,
                text=texte,
                command=lambda a=arme:
                self.equiper_arme(a),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=55,
                height=2
            ).pack(pady=4)

        tk.Label(
            fenetre,
            text="ARMURES",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        for armure in self.inventaire_armures:

            info = self.armures[armure]

            texte = (
                f"{armure} | "
                f"+{info['defense']} défense | "
                f"+{info['pv']} PV"
            )

            if armure == self.armure_equipee:
                texte += " | ÉQUIPÉE"

            tk.Button(
                fenetre,
                text=texte,
                command=lambda a=armure:
                self.equiper_armure(a),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=55,
                height=2
            ).pack(pady=4)

        tk.Button(
            fenetre,
            text="Retour",
            command=fenetre.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=30)

    # ========================================================
    # EQUIPER ARME
    # ========================================================

    def equiper_arme(self, arme):

        self.arme_equipee = arme

        self.afficher(
            f"Tu équipes {arme}."
        )

        self.actualiser()

    # ========================================================
    # EQUIPER ARMURE
    # ========================================================

    def equiper_armure(self, armure):

        self.armure_equipee = armure

        self.afficher(
            f"Tu équipes {armure}."
        )

        self.actualiser()

    # ========================================================
    # BOUTIQUE
    # ========================================================

    def boutique(self):

        fenetre = tk.Toplevel(self.root)

        fenetre.title("Boutique")
        fenetre.configure(bg="black")

        fenetre.attributes(
            "-fullscreen",
            True
        )

        # ====================================================
        # TITRE
        # ====================================================

        tk.Label(
            fenetre,
            text="BOUTIQUE",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=15)

        # ====================================================
        # BOUTON QUITTER
        # ====================================================

        bouton_quitter = tk.Button(
            fenetre,
            text="X",
            command=fenetre.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=4,
            height=2,
            font=("Arial", 12, "bold")
        )

        bouton_quitter.place(
            relx=0.97,
            rely=0.02,
            anchor="ne"
        )

        # ====================================================
        # PIECES
        # ====================================================

        tk.Label(
            fenetre,
            text=f"Pièces : {self.pieces}",
            bg="black",
            fg="white",
            font=("Arial", 16)
        ).pack(pady=5)

        # ====================================================
        # POTION
        # ====================================================

        tk.Button(
            fenetre,
            text="Potion - 10 pièces",
            command=self.acheter_potion,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=25,
            height=1
        ).pack(pady=5)

        # ====================================================
        # ARMES
        # ====================================================

        tk.Label(
            fenetre,
            text="ARMES",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=8)

        for arme, info in self.armes.items():

            # L'épée secrète ne doit pas être visible
            # avant sa découverte.

            if arme == "Lame du Héro Absolu":

                if not self.epee_secrete_decouverte:
                    continue

            if arme in self.inventaire_armes:
                continue

            texte = (
                f"{arme} | "
                f"+{info['attaque']} ATK | "
                f"{info['prix']} pièces | "
                f"Niv. {info['niveau_requis']}"
            )

            tk.Button(
                fenetre,
                text=texte,
                command=lambda a=arme:
                self.acheter_arme(a),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=55,
                height=1,
                font=("Arial", 9)
            ).pack(pady=2)

        # ====================================================
        # ARMURES
        # ====================================================

        tk.Label(
            fenetre,
            text="ARMURES",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=8)

        for armure, info in self.armures.items():

            if armure in self.inventaire_armures:
                continue

            texte = (
                f"{armure} | "
                f"+{info['defense']} DEF | "
                f"+{info['pv']} PV | "
                f"{info['prix']} pièces | "
                f"Niv. {info['niveau_requis']}"
            )

            tk.Button(
                fenetre,
                text=texte,
                command=lambda a=armure:
                self.acheter_armure(a),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=55,
                height=1,
                font=("Arial", 9)
            ).pack(pady=2)

        # ====================================================
        # AMELIORATIONS
        # ====================================================

        tk.Label(
            fenetre,
            text="AMÉLIORATIONS",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=8)

        tk.Button(
            fenetre,
            text="Améliorer l'arme équipée",
            command=self.ameliorer_arme,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=28,
            height=1
        ).pack(pady=3)

        tk.Button(
            fenetre,
            text="Améliorer l'armure équipée",
            command=self.ameliorer_armure,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=28,
            height=1
        ).pack(pady=3)

        # ====================================================
        # BOUTON SECRET INVISIBLE
        # ====================================================

        bouton_secret = tk.Button(
            fenetre,
            text="",
            command=lambda: self.decouvrir_epee_secrete(fenetre),
            bg="black",
            activebackground="black",
            relief="flat",
            bd=0,
            highlightthickness=0,
            width=4,
            height=2
        )

        bouton_secret.place(
            relx=0.0,
            rely=1.0,
            anchor="sw"
        )

    # ========================================================
    # DÉCOUVRIR L'ÉPÉE SECRÈTE
    # ========================================================

    def decouvrir_epee_secrete(self, fenetre):

        if self.epee_secrete_decouverte:

            self.message(
                "Tu as déjà découvert le secret..."
            )

            return

        self.epee_secrete_decouverte = True

        self.afficher(
            "Une forge sous terraine est apparu !"
        )

        self.message(
            "Tu as découvert une arme secrète !\n\n"
            "Lame du Héro Absolu\n"
            "+100 ATK\n"
            "Prix : 5000 pièces\n"
            "Niveau requis : 25"
        )

        # Ferme la boutique pour pouvoir la rouvrir
        # avec l'épée désormais visible.

        fenetre.destroy()

        self.actualiser()

    # ========================================================
    # ACHETER POTION
    # ========================================================

    def acheter_potion(self):

        if self.pieces < 10:

            self.message(
                "Tu n'as pas assez de pièces."
            )

            return

        self.pieces -= 10
        self.potions += 1

        self.afficher(
            "Tu achètes une potion."
        )

        self.actualiser()

    # ========================================================
    # ACHETER ARME
    # ========================================================

    def acheter_arme(self, arme):

        info = self.armes[arme]

        if self.niveau < info["niveau_requis"]:

            self.message(
                f"Niveau {info['niveau_requis']} requis."
            )

            return

        if self.pieces < info["prix"]:

            self.message(
                "Tu n'as pas assez de pièces."
            )

            return

        self.pieces -= info["prix"]

        self.inventaire_armes.append(arme)

        self.afficher(
            f"Tu achètes {arme}."
        )

        self.actualiser()

    # ========================================================
    # ACHETER ARMURE
    # ========================================================

    def acheter_armure(self, armure):

        info = self.armures[armure]

        if self.niveau < info["niveau_requis"]:

            self.message(
                f"Niveau {info['niveau_requis']} requis."
            )

            return

        if self.pieces < info["prix"]:

            self.message(
                "Tu n'as pas assez de pièces."
            )

            return

        self.pieces -= info["prix"]

        self.inventaire_armures.append(armure)

        self.afficher(
            f"Tu achètes {armure}."
        )

        self.actualiser()

    # ========================================================
    # AMELIORER ARME
    # ========================================================

    def ameliorer_arme(self):

        arme = self.armes[self.arme_equipee]

        prochain_niveau = arme["niveau"] + 1
        prix = prochain_niveau * 50

        if self.niveau < prochain_niveau:

            self.message(
                f"Il faut être niveau {prochain_niveau}."
            )

            return

        if self.pieces < prix:

            self.message(
                "Tu n'as pas assez de pièces."
            )

            return

        self.pieces -= prix

        arme["niveau"] += 1

        self.afficher(
            f"{self.arme_equipee} passe niveau "
            f"{arme['niveau']}."
        )

        self.actualiser()

    # ========================================================
    # AMELIORER ARMURE
    # ========================================================

    def ameliorer_armure(self):

        armure = self.armures[self.armure_equipee]

        prochain_niveau = armure["niveau"] + 1
        prix = prochain_niveau * 60

        if self.niveau < prochain_niveau:

            self.message(
                f"Il faut être niveau {prochain_niveau}."
            )

            return

        if self.pieces < prix:

            self.message(
                "Tu n'as pas assez de pièces."
            )

            return

        self.pieces -= prix

        armure["niveau"] += 1

        self.afficher(
            f"{self.armure_equipee} passe niveau "
            f"{armure['niveau']}."
        )

        self.actualiser()

    # ========================================================
    # STATISTIQUES
    # ========================================================

    def afficher_stats(self):

        self.message(
            f"===== STATS =====\n\n"
            f"Nom : {self.nom}\n"
            f"Niveau : {self.niveau}\n"
            f"XP : {self.xp}/{self.niveau * 50}\n\n"
            f"PV : {self.pv}/{self.get_pv_max()}\n"
            f"Attaque : {self.get_attaque()}\n"
            f"Défense : {self.get_defense()}\n\n"
            f"Arme : {self.arme_equipee}\n"
            f"Armure : {self.armure_equipee}\n\n"
            f"Pièces : {self.pieces}\n"
            f"Potions : {self.potions}\n"
            f"Mobs vaincus : {self.mobs_vaincus}\n\n"
            f"Zone : {self.zone_actuelle}"
        )

    # ========================================================
    # MORT
    # ========================================================

    def mort(self):

        messagebox.showinfo(
            "SHADOW RPG",
            f"Tu es mort.\n\n"
            f"Niveau atteint : {self.niveau}\n"
            f"Mobs vaincus : {self.mobs_vaincus}",
            parent=self.root
        )

        self.root.destroy()


# ============================================================
# LANCEMENT
# ============================================================

root = tk.Tk()

jeu = ShadowRPG(root)

root.bind("<Escape>", jeu.quitter_jeu)

root.mainloop()
