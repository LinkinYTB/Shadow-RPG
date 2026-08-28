import tkinter as tk
from tkinter import messagebox
import random
from pathlib import Path
from PIL import Image, ImageTk, ImageOps


# ============================================================
# SHADOW RPG
# Tkinter Version - English
# ============================================================

class ShadowRPG:

    def __init__(self, root):

        self.root = root
        self.root.title("SHADOW RPG")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)

        # ====================================================
        # BACKGROUND IMAGE
        # ====================================================
        # The image is searched in the SAME folder as this .py file.
        # This works even if the game is launched from another folder.
        self.game_folder = Path(__file__).resolve().parent
        self.image_path = self.game_folder / "images.jpeg"

        if self.image_path.exists():
            self.background_image = Image.open(
                self.image_path
            ).convert("RGB")

            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            self.background_image = ImageOps.fit(
                self.background_image,
                (screen_width, screen_height),
                method=Image.Resampling.LANCZOS
            )

            self.background_photo = ImageTk.PhotoImage(
                self.background_image
            )

            self.background_label = tk.Label(
                self.root,
                image=self.background_photo,
                bd=0
            )

            self.background_label.place(
                x=0,
                y=0,
                relwidth=1,
                relheight=1
            )

            self.background_label.lower()

        else:
            # If the image is missing, the game still starts normally.
            self.background_label = None
            print(
                f"WARNING: Image not found: {self.image_path}"
            )

        self.bg = "black"
        self.fg = "white"
        self.button_bg = "#202020"
        self.button_active = "#404040"

        self.root.bind("<Escape>", self.quit_game)

        self.name = self.ask_name()

        # ====================================================
        # PLAYER
        # ====================================================

        self.max_hp = 100
        self.hp = 100

        self.max_mana = 100
        self.mana = 100

        self.base_attack = 20
        self.base_defense = 5

        self.level = 1
        self.xp = 0

        self.coins = 50
        self.potions = 3

        self.mobs_defeated = 0

        # ====================================================
        # SECRET SWORD
        # ====================================================

        self.secret_sword_discovered = False

        # ====================================================
        # CLASSES
        # ====================================================

        self.current_class = "Adventurer"

        self.classes = {

            "Adventurer": {
                "price": 0,
                "attack": 0,
                "defense": 0,
                "hp": 0,
                "mana": 0
            },

            "Warrior": {
                "price": 1000,
                "attack": 15,
                "defense": 10,
                "hp": 50,
                "mana": 0
            },

            "Mage": {
                "price": 1200,
                "attack": 5,
                "defense": 2,
                "hp": 0,
                "mana": 100
            },

            "Knight": {
                "price": 2000,
                "attack": 20,
                "defense": 20,
                "hp": 100,
                "mana": 0
            },

            "Shadow Lord": {
                "price": 5000,
                "attack": 35,
                "defense": 15,
                "hp": 50,
                "mana": 100
            }
        }

        self.owned_classes = ["Adventurer"]

        # ====================================================
        # EASTER EGGS
        # ====================================================

        if self.name == "snow":

            self.max_hp = 150
            self.hp = 150
            self.base_attack = 25
            self.base_defense = 8

        elif self.name == "take":

            self.base_attack = 0

        elif self.name == "louis":

            self.max_hp = 150
            self.hp = 150
            self.base_attack = 25
            self.base_defense = 8

        elif self.name == "sans":

            self.base_attack = 22

        elif self.name == "modo":

            self.level = 9999
            self.coins = 9999
            self.mobs_defeated = 9999
            self.base_attack = 9999
            self.base_defense = 9999
            self.max_mana = 9999
            self.mana = 9999

        elif self.name == "admin":

            self.level = 9999
            self.coins = 999999
            self.mobs_defeated = 9999
            self.base_attack = 9999
            self.base_defense = 9999
            self.max_mana = 9999
            self.mana = 9999
            self.max_hp = 999999
            self.hp = 999999

        elif self.name == "money":

            self.coins = 999999

        # ====================================================
        # WEAPONS
        # ====================================================

        self.weapons = {

            "Wooden Sword": {
                "attack": 0,
                "price": 0,
                "required_level": 1,
                "level": 1
            },

            "Iron Sword": {
                "attack": 10,
                "price": 100,
                "required_level": 2,
                "level": 1
            },

            "Iron Spear": {
                "attack": 20,
                "price": 250,
                "required_level": 4,
                "level": 1
            },

            "Lightning Dagger": {
                "attack": 35,
                "price": 500,
                "required_level": 7,
                "level": 1
            },

            "Dark Scythe": {
                "attack": 50,
                "price": 1000,
                "required_level": 10,
                "level": 1
            },

            "Fallen Knight Blade": {
                "attack": 70,
                "price": 3000,
                "required_level": 20,
                "level": 1
            },

            "Absolute Hero Blade": {
                "attack": 200,
                "price": 5000,
                "required_level": 25,
                "level": 1
            }
        }

        self.weapon_inventory = ["Wooden Sword"]
        self.equipped_weapon = "Wooden Sword"

        # ====================================================
        # ARMOR
        # ====================================================

        self.armors = {

            "Simple Clothes": {
                "defense": 0,
                "hp": 0,
                "price": 0,
                "required_level": 1,
                "level": 1
            },

            "Iron Armor": {
                "defense": 8,
                "hp": 30,
                "price": 200,
                "required_level": 3,
                "level": 1
            },

            "Knight Armor": {
                "defense": 15,
                "hp": 70,
                "price": 500,
                "required_level": 6,
                "level": 1
            },

            "Shadow Armor": {
                "defense": 25,
                "hp": 120,
                "price": 1000,
                "required_level": 10,
                "level": 1
            },

            "Fallen King's Armor": {
                "defense": 40,
                "hp": 200,
                "price": 2000,
                "required_level": 15,
                "level": 1
            }
        }

        self.armor_inventory = ["Simple Clothes"]
        self.equipped_armor = "Simple Clothes"

        # ====================================================
        # SPELLS
        # ====================================================

        self.spells = {

            "Fireball": {
                "price": 400,
                "mana": 10,
                "multiplier": 1.20,
                "required_level": 3
            },

            "Lightning": {
                "price": 800,
                "mana": 15,
                "multiplier": 1.50,
                "required_level": 5
            },

            "Ice Nova": {
                "price": 1500,
                "mana": 20,
                "multiplier": 2.00,
                "required_level": 10
            },

            "Soul Drain": {
                "price": 2500,
                "mana": 30,
                "multiplier": 1.30,
                "required_level": 15
            }
        }

        self.learned_spells = []

        # ====================================================
        # ZONES
        # ====================================================

        self.zones = {

            "Plains": {
                "level": 1,
                "boss": "Plain Warrior",
                "boss_defeated": False,
                "required_mobs": 0,

                "monsters": [
                    ["Slime", 45, 10, 2, 15, 10],
                    ["Goblin", 50, 12, 3, 20, 15],
                    ["Wolf", 60, 14, 4, 25, 20]
                ],

                "boss_stats": [250, 25, 8, 100, 100]
            },

            "Forest": {
                "level": 3,
                "boss": "Goblin Master",
                "boss_defeated": False,
                "required_mobs": 10,

                "monsters": [
                    ["Giant Wolf", 90, 20, 7, 35, 30],
                    ["Ent", 120, 18, 10, 45, 40],
                    ["Black Goblin", 100, 23, 8, 50, 45]
                ],

                "boss_stats": [400, 35, 12, 150, 150]
            },

            "Mountain": {
                "level": 6,
                "boss": "Dark Dragon King",
                "boss_defeated": False,
                "required_mobs": 20,

                "monsters": [
                    ["Golem", 180, 30, 15, 70, 60],
                    ["Dragon Whelp", 160, 35, 12, 80, 70],
                    ["Ogre", 220, 32, 18, 90, 80]
                ],

                "boss_stats": [650, 45, 20, 250, 250]
            },

            "Shadow Realm": {
                "level": 10,
                "boss": "Shadow King",
                "boss_defeated": False,
                "required_mobs": 35,

                "monsters": [
                    ["Shadow", 250, 45, 20, 120, 100],
                    ["Demon", 300, 50, 25, 150, 130],
                    ["Dark Knight", 350, 55, 30, 180, 160]
                ],

                "boss_stats": [1000, 65, 35, 400, 400]
            },

            "Fallen Capital": {
                "level": 15,
                "boss": "Fallen King",
                "boss_defeated": False,
                "required_mobs": 50,

                "monsters": [
                    ["Fallen Guard", 800, 65, 30, 220, 180],
                    ["Cursed Knight", 1000, 75, 35, 260, 220],
                    ["Fallen Lord", 1200, 85, 40, 300, 250]
                ],

                "boss_stats": [2000, 95, 50, 700, 600]
            },

            "Fallen Citadel": {
                "level": 20,
                "boss": "Fallen Knight",
                "boss_defeated": False,
                "required_mobs": 75,

                "monsters": [
                    ["Fallen Soldier", 1400, 90, 45, 350, 300],
                    ["Corrupted Knight", 1700, 105, 55, 400, 350],
                    ["Citadel Guardian", 2000, 120, 65, 450, 400]
                ],

                "boss_stats": [3500, 130, 70, 1000, 900]
            },

            "Abyss": {
                "level": 25,
                "boss": "Lord of the Abyss",
                "boss_defeated": False,
                "required_mobs": 100,

                "monsters": [
                    ["Abyss Demon", 2500, 140, 75, 600, 500],
                    ["Abyssal Creature", 3000, 155, 85, 700, 600],
                    ["Abyssal Knight", 3500, 170, 100, 800, 700]
                ],

                "boss_stats": [6000, 190, 120, 1500, 1200]
            },

            "???": {
                "level": 1,
                "boss": "Shadow",
                "boss_defeated": False,
                "required_mobs": 100,

                "monsters": [
                    ["??? Creature", 1000, 70, 40, 250, 250],
                    ["??? Shadow", 1200, 80, 90, 300, 300],
                    ["??? Soul", 1500, 90, 110, 350, 350]
                ],

                "boss_stats": [10000, 100, 50, 1000, 1000]
            }
        }

        self.current_zone = "Plains"

        # ====================================================
        # INTERFACE
        # ====================================================

        self.create_interface()
        self.update_interface()

    # ========================================================
    # NAME
    # ========================================================

    def ask_name(self):

        window = tk.Toplevel(self.root)

        window.title("SHADOW RPG")
        window.configure(bg="black")
        window.geometry("500x250")

        window.transient(self.root)
        window.grab_set()

        result = {"name": "Adventurer"}

        tk.Label(
            window,
            text="What is your name?",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=30)

        entry = tk.Entry(
            window,
            bg="#202020",
            fg="white",
            insertbackground="white",
            font=("Arial", 16)
        )

        entry.pack()

        def validate():

            name = entry.get().strip()

            if name:
                result["name"] = name.lower()

            window.destroy()

        tk.Button(
            window,
            text="Start",
            command=validate,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=18,
            height=2
        ).pack(pady=25)

        self.root.wait_window(window)

        return result["name"]

    # ========================================================
    # QUIT
    # ========================================================

    def quit_game(self, event=None):

        if not self.root.winfo_exists():
            return

        answer = messagebox.askyesno(
            "Quit SHADOW RPG",
            "Do you really want to quit the game?",
            parent=self.root
        )

        if answer:
            self.root.destroy()

    # ========================================================
    # MESSAGE
    # ========================================================

    def show_message(self, text):

        messagebox.showinfo(
            "SHADOW RPG",
            text,
            parent=self.root
        )

    # ========================================================
    # MAIN INTERFACE
    # ========================================================

    def create_interface(self):

        tk.Label(
            self.root,
            text="SHADOW RPG",
            bg="black",
            fg="white",
            font=("Arial", 32, "bold")
        ).pack(pady=15)

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

        def button(text, command, row, column):

            tk.Button(
                frame,
                text=text,
                command=command,
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=18,
                height=2,
                font=("Arial", 11, "bold")
            ).grid(
                row=row,
                column=column,
                padx=5,
                pady=5
            )

        button("Explore", self.explore, 0, 0)
        button("Zones", self.zone_menu, 0, 1)
        button("Bosses", self.boss_menu, 0, 2)
        button("Shop", self.shop, 0, 3)

        button("Inventory", self.inventory, 1, 0)
        button("Potion", self.use_potion, 1, 1)
        button("Statistics", self.show_stats, 1, 2)
        button("Classes", self.class_menu, 1, 3)

        button("???", self.secret_zone, 2, 1)

    # ========================================================
    # LOG
    # ========================================================

    def display(self, text):

        self.log.config(state="normal")
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.config(state="disabled")

    # ========================================================
    # STATS
    # ========================================================

    def get_attack(self):

        weapon = self.weapons[self.equipped_weapon]
        player_class = self.classes[self.current_class]

        return (
            self.base_attack
            + player_class["attack"]
            + weapon["attack"]
            + (weapon["level"] - 1) * 5
        )

    def get_defense(self):

        armor = self.armors[self.equipped_armor]
        player_class = self.classes[self.current_class]

        return (
            self.base_defense
            + player_class["defense"]
            + armor["defense"]
            + (armor["level"] - 1) * 3
        )

    def get_max_hp(self):

        armor = self.armors[self.equipped_armor]
        player_class = self.classes[self.current_class]

        return (
            self.max_hp
            + player_class["hp"]
            + armor["hp"]
            + (armor["level"] - 1) * 10
        )

    def get_max_mana(self):

        player_class = self.classes[self.current_class]

        return (
            self.max_mana
            + player_class["mana"]
            + (self.level - 1) * 5
        )

    # ========================================================
    # UPDATE
    # ========================================================

    def update_interface(self):

        max_hp = self.get_max_hp()
        max_mana = self.get_max_mana()

        self.hp = min(self.hp, max_hp)
        self.mana = min(self.mana, max_mana)

        self.stats.config(
            text=(
                f"Name: {self.name}    "
                f"Class: {self.current_class}    "
                f"Level: {self.level}    "
                f"XP: {self.xp}/{self.level * 50}\n"

                f"HP: {self.hp}/{max_hp}    "
                f"Mana: {self.mana}/{max_mana}    "
                f"Attack: {self.get_attack()}    "
                f"Defense: {self.get_defense()}    "
                f"Coins: {self.coins}    "
                f"Potions: {self.potions}\n"

                f"Weapon: {self.equipped_weapon}    "
                f"Armor: {self.equipped_armor}    "
                f"Mobs defeated: {self.mobs_defeated}"
            )
        )

        self.zone_label.config(
            text=f"Zone: {self.current_zone}"
        )

    # ========================================================
    # DODGE
    # ========================================================

    def player_dodges(self):

        if self.name == "fizz":

            if random.randint(1, 100) <= 15:

                self.display(
                    "Fizz dodges the attack!"
                )

                return True

        elif self.name == "louis":

            if random.randint(1, 100) <= 25:

                self.display(
                    "Louis dodges the attack!"
                )

                return True

        elif self.name == "admin":

            self.display(
                "Admin dodges with a cheat!"
            )

            return True

        return False

    # ========================================================
    # EXPLORE
    # ========================================================

    def explore(self):

        if self.current_zone == "???":

            self.shadow_combat()
            return

        chance = random.randint(1, 100)

        if chance <= 70:

            self.combat()

        elif chance <= 82:

            gain = random.randint(10, 40)

            self.coins += gain

            self.display(
                f"You find {gain} coins!"
            )

        elif chance <= 94:

            healing = random.randint(10, 30)

            self.hp = min(
                self.get_max_hp(),
                self.hp + healing
            )

            self.display(
                f"You recover {healing} HP."
            )

        else:

            self.display(
                "A mysterious traveler appears..."
            )

        self.update_interface()

    # ========================================================
    # NORMAL COMBAT
    # ========================================================

    def combat(self):

        zone = self.zones[self.current_zone]

        monster = random.choice(
            zone["monsters"]
        )

        self.combat_interface(
            monster[0],
            monster[1],
            monster[2],
            monster[3],
            monster[4],
            monster[5]
        )

    # ========================================================
    # SHADOW COMBAT
    # ========================================================

    def shadow_combat(self):

        stats = self.zones["???"]["boss_stats"]

        self.combat_interface(
            "Shadow",
            stats[0],
            stats[1],
            stats[2],
            stats[3],
            stats[4],
            boss=True,
            boss_zone="???"
        )

    # ========================================================
    # COMBAT
    # ========================================================

    def combat_interface(
        self,
        enemy_name,
        enemy_hp,
        enemy_attack,
        enemy_defense,
        xp_gain,
        coins_gain,
        boss=False,
        boss_zone=None
    ):

        window = tk.Toplevel(self.root)

        window.title(
            f"Combat - {enemy_name}"
        )

        window.configure(
            bg="black"
        )

        window.attributes(
            "-fullscreen",
            True
        )

        window.grab_set()

        label = tk.Label(
            window,
            text="",
            bg="black",
            fg="white",
            font=("Arial", 22, "bold")
        )

        label.pack(pady=20)

        message = tk.Text(
            window,
            width=100,
            height=16,
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
        combat_finished = [False]
        enemy_frozen = [False]

        def combat_log(text):

            message.config(state="normal")
            message.insert("end", text + "\n")
            message.see("end")
            message.config(state="disabled")

        def update_combat():

            label.config(
                text=(
                    f"{self.name}: "
                    f"{self.hp}/{self.get_max_hp()} HP    "
                    f"{self.mana}/{self.get_max_mana()} Mana\n\n"

                    f"{enemy_name}: "
                    f"{max(0, enemy_hp)} HP"
                )
            )

        def close():

            if window.winfo_exists():

                try:
                    window.grab_release()
                except:
                    pass

                window.destroy()

            self.update_interface()

        # ====================================================
        # VICTORY
        # ====================================================

        def victory():

            if combat_finished[0]:
                return

            combat_finished[0] = True

            self.mobs_defeated += 1

            self.xp += xp_gain
            self.coins += coins_gain

            combat_log("")
            combat_log("VICTORY!")
            combat_log(f"+{xp_gain} XP")
            combat_log(f"+{coins_gain} coins")

            if boss and boss_zone:

                self.zones[
                    boss_zone
                ]["boss_defeated"] = True

                combat_log(
                    f"Boss defeated: {enemy_name}"
                )

                if boss_zone == "???":

                    combat_log(
                        "You defeated Shadow!"
                    )

                elif boss_zone == "Abyss":

                    combat_log(
                        "The Lord of the Abyss has fallen!"
                    )

            self.level_up()

            self.update_interface()

            window.after(
                1000,
                close
            )

        # ====================================================
        # ATTACK
        # ====================================================

        def attack():

            nonlocal enemy_hp

            if combat_finished[0]:
                return

            if self.name == "take":

                combat_log(
                    "Take is too lazy to fight..."
                )

            else:

                dodge = False

                if enemy_name == "fizz":

                    dodge = (
                        random.randint(1, 100) <= 15
                    )

                elif enemy_name == "louis":

                    dodge = (
                        random.randint(1, 100) <= 25
                    )

                if dodge:

                    combat_log(
                        f"{enemy_name} dodges your attack!"
                    )

                else:

                    total_attack = self.get_attack()

                    damage = random.randint(
                        max(
                            1,
                            total_attack - 5
                        ),
                        total_attack + 5
                    )

                    damage = max(
                        1,
                        damage - enemy_defense
                    )

                    enemy_hp -= damage

                    combat_log(
                        f"You deal {damage} damage!"
                    )

                    # CRITICAL HIT

                    if random.randint(1, 100) <= 10:

                        critical = int(
                            damage * 0.5
                        )

                        enemy_hp -= critical

                        combat_log(
                            f"CRITICAL HIT! "
                            f"+{critical} damage!"
                        )

                    # DARK SCYTHE

                    if self.equipped_weapon == "Dark Scythe":

                        healing = int(
                            damage * 0.25
                        )

                        self.hp = min(
                            self.get_max_hp(),
                            self.hp + healing
                        )

                        combat_log(
                            f"The Dark Scythe "
                            f"heals you for {healing} HP."
                        )

                    # FALLEN KNIGHT BLADE

                    if self.equipped_weapon == "Fallen Knight Blade":

                        healing = int(
                            damage * 0.50
                        )

                        self.hp = min(
                            self.get_max_hp(),
                            self.hp + healing
                        )

                        combat_log(
                            f"The Fallen Knight Blade "
                            f"heals you for {healing} HP."
                        )

                    # ABSOLUTE HERO BLADE

                    if self.equipped_weapon == "Absolute Hero Blade":

                        healing = int(
                            damage * 0.60
                        )

                        self.hp = min(
                            self.get_max_hp(),
                            self.hp + healing
                        )

                        combat_log(
                            f"The Absolute Hero Blade "
                            f"heals you for {healing} HP."
                        )

                    # SANS

                    if self.name == "sans":

                        self.hp = min(
                            self.get_max_hp(),
                            self.hp + damage
                        )

                        combat_log(
                            f"Sans recovers {damage} HP."
                        )

            if enemy_hp <= 0:

                victory()
                return

            update_combat()

            enemy_turn()

        # ====================================================
        # SPELL
        # ====================================================

        def cast_spell(spell_name):

            nonlocal enemy_hp

            if combat_finished[0]:
                return

            if spell_name not in self.learned_spells:

                combat_log(
                    "You have not learned this spell."
                )

                return

            spell = self.spells[spell_name]

            if self.mana < spell["mana"]:

                combat_log(
                    f"Not enough mana! "
                    f"You need {spell['mana']} mana."
                )

                return

            self.mana -= spell["mana"]

            # Spells use the weapon attack

            weapon_attack = self.get_attack()

            base_damage = random.randint(
                max(
                    1,
                    weapon_attack - 5
                ),
                weapon_attack + 5
            )

            damage = int(
                base_damage
                * spell["multiplier"]
            )

            damage = max(
                1,
                damage - enemy_defense
            )

            enemy_hp -= damage

            combat_log("")
            combat_log(
                f"You cast {spell_name}!"
            )

            combat_log(
                f"{damage} damage!"
            )

            # =================================================
            # ICE NOVA
            # =================================================

            if spell_name == "Ice Nova":

                if random.randint(1, 100) <= 15:

                    enemy_frozen[0] = True

                    combat_log(
                        "The enemy is FROZEN!"
                    )

                    combat_log(
                        "It will not be able to attack this turn."
                    )

                else:

                    combat_log(
                        "The ice failed to freeze the enemy."
                    )

            # =================================================
            # SOUL DRAIN
            # =================================================

            if spell_name == "Soul Drain":

                hp_coefficient = (
                    self.get_max_hp() / 100
                )

                healing = int(
                    damage
                    * 0.40
                    * hp_coefficient
                )

                healing = max(
                    1,
                    healing
                )

                old_hp = self.hp

                self.hp = min(
                    self.get_max_hp(),
                    self.hp + healing
                )

                actual_healing = self.hp - old_hp

                combat_log(
                    f"Soul Drain restores "
                    f"{actual_healing} HP."
                )

                combat_log(
                    f"(Healing based on your "
                    f"{self.get_max_hp()} max HP)"
                )

            if enemy_hp <= 0:

                victory()
                return

            update_combat()

            enemy_turn()

        # ====================================================
        # SPELL MENU
        # ====================================================

        def combat_spell_menu():

            if combat_finished[0]:
                return

            spell_window = tk.Toplevel(
                window
            )

            spell_window.title(
                "Spells"
            )

            spell_window.configure(
                bg="black"
            )

            spell_window.geometry(
                "500x450"
            )

            spell_window.transient(
                window
            )

            spell_window.grab_set()

            tk.Label(
                spell_window,
                text="SPELLS",
                bg="black",
                fg="white",
                font=("Arial", 22, "bold")
            ).pack(pady=20)

            if not self.learned_spells:

                tk.Label(
                    spell_window,
                    text="You have not learned any spells.",
                    bg="black",
                    fg="white",
                    font=("Arial", 13)
                ).pack(pady=20)

            else:

                for spell_name in self.learned_spells:

                    spell = self.spells[spell_name]

                    tk.Button(
                        spell_window,
                        text=(
                            f"{spell_name} - "
                            f"{spell['mana']} mana"
                        ),
                        command=lambda s=spell_name: (
                            spell_window.destroy(),
                            cast_spell(s)
                        ),
                        bg="#202020",
                        fg="white",
                        activebackground="#404040",
                        activeforeground="white",
                        width=32,
                        height=2,
                        font=("Arial", 11, "bold")
                    ).pack(pady=6)

            tk.Button(
                spell_window,
                text="Back",
                command=spell_window.destroy,
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=20,
                height=2
            ).pack(pady=20)

        # ====================================================
        # DEFEND
        # ====================================================

        def defend():

            if combat_finished[0]:
                return

            defense_bonus[0] = 10

            combat_log(
                "You take a defensive stance."
            )

            enemy_turn()

        # ====================================================
        # POTION
        # ====================================================

        def potion():

            if combat_finished[0]:
                return

            if self.potions <= 0:

                combat_log(
                    "You have no potions left."
                )

                return

            if (
                self.hp >= self.get_max_hp()
                and self.mana >= self.get_max_mana()
            ):

                combat_log(
                    "Your HP and mana are already full."
                )

                return

            self.potions -= 1

            hp_healing = random.randint(
                20,
                40
            )

            mana_healing = random.randint(
                10,
                25
            )

            old_hp = self.hp
            old_mana = self.mana

            self.hp = min(
                self.get_max_hp(),
                self.hp + hp_healing
            )

            self.mana = min(
                self.get_max_mana(),
                self.mana + mana_healing
            )

            actual_hp_healing = self.hp - old_hp
            actual_mana_healing = self.mana - old_mana

            combat_log(
                f"Potion: +{actual_hp_healing} HP "
                f"and +{actual_mana_healing} mana."
            )

            update_combat()

            enemy_turn()

        # ====================================================
        # FLEE
        # ====================================================

        def flee():

            if combat_finished[0]:
                return

            if boss:

                combat_log(
                    "You cannot flee from a boss."
                )

                return

            if random.randint(1, 100) <= 50:

                combat_log(
                    "You successfully flee."
                )

                window.after(
                    500,
                    close
                )

            else:

                combat_log(
                    "You fail to escape."
                )

                enemy_turn()

        # ====================================================
        # ENEMY TURN
        # ====================================================

        def enemy_turn():

            if combat_finished[0]:
                return

            if enemy_hp <= 0:
                return

            # FROZEN ENEMY

            if enemy_frozen[0]:

                combat_log(
                    f"{enemy_name} is frozen "
                    f"and cannot attack!"
                )

                enemy_frozen[0] = False
                defense_bonus[0] = 0

                update_combat()

                return

            # TAKE

            if enemy_name == "take":

                combat_log(
                    "Take is too lazy."
                )

                combat_log(
                    "He does not attack you."
                )

            # CHIBICAT

            elif enemy_name == "chibicat12364":

                combat_log(
                    "Chibicat12364 screams at you!"
                )

                combat_log(
                    "She leaves you at 1 HP and walks away."
                )

                self.hp = 1

                window.after(
                    500,
                    close
                )

                return

            else:

                if self.player_dodges():

                    defense_bonus[0] = 0

                    update_combat()

                    return

                damage = random.randint(
                    max(
                        1,
                        enemy_attack - 3
                    ),
                    enemy_attack + 3
                )

                damage -= self.get_defense()
                damage -= defense_bonus[0]

                damage = max(
                    1,
                    damage
                )

                self.hp -= damage

                combat_log(
                    f"{enemy_name} deals "
                    f"{damage} damage to you!"
                )

            defense_bonus[0] = 0

            update_combat()

            if self.hp <= 0:

                combat_finished[0] = True

                self.death()

        # ====================================================
        # COMBAT BUTTONS
        # ====================================================

        buttons = tk.Frame(
            window,
            bg="black"
        )

        buttons.pack(pady=15)

        def combat_button(
            text,
            command,
            column
        ):

            tk.Button(
                buttons,
                text=text,
                command=command,
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=15,
                height=2,
                font=("Arial", 11, "bold")
            ).grid(
                row=0,
                column=column,
                padx=5
            )

        combat_button(
            "Attack",
            attack,
            0
        )

        combat_button(
            "Spells",
            combat_spell_menu,
            1
        )

        combat_button(
            "Defend",
            defend,
            2
        )

        combat_button(
            "Potion",
            potion,
            3
        )

        combat_button(
            "Flee",
            flee,
            4
        )

        update_combat()

    # ========================================================
    # LEVEL UP
    # ========================================================

    def level_up(self):

        while self.xp >= self.level * 50:

            self.xp -= self.level * 50

            self.level += 1

            self.max_hp += 20
            self.max_mana += 5

            self.base_attack += 3
            self.base_defense += 2

            self.hp = self.get_max_hp()
            self.mana = self.get_max_mana()

            self.display(
                f"LEVEL UP! "
                f"You are now level "
                f"{self.level}."
            )

    # ========================================================
    # POTION OUTSIDE COMBAT
    # ========================================================

    def use_potion(self):

        if self.potions <= 0:

            self.show_message(
                "You have no potions left."
            )

            return

        if (
            self.hp >= self.get_max_hp()
            and self.mana >= self.get_max_mana()
        ):

            self.show_message(
                "Your HP and mana are already full."
            )

            return

        self.potions -= 1

        hp_healing = random.randint(
            20,
            40
        )

        mana_healing = random.randint(
            10,
            25
        )

        old_hp = self.hp
        old_mana = self.mana

        self.hp = min(
            self.get_max_hp(),
            self.hp + hp_healing
        )

        self.mana = min(
            self.get_max_mana(),
            self.mana + mana_healing
        )

        actual_hp_healing = self.hp - old_hp
        actual_mana_healing = self.mana - old_mana

        self.display(
            f"Potion: +{actual_hp_healing} HP "
            f"and +{actual_mana_healing} mana."
        )

        self.update_interface()

    # ========================================================
    # SHOP
    # ========================================================

    def shop(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Shop"
        )

        window.configure(
            bg="black"
        )

        window.attributes(
            "-fullscreen",
            True
        )

        # ====================================================
        # TITLE
        # ====================================================

        tk.Label(
            window,
            text="SHOP",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=8)

        # ====================================================
        # CLOSE
        # ====================================================

        tk.Button(
            window,
            text="X",
            command=window.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=4,
            height=2,
            font=("Arial", 12, "bold")
        ).place(
            relx=0.97,
            rely=0.02,
            anchor="ne"
        )

        # ====================================================
        # COINS
        # ====================================================

        tk.Label(
            window,
            text=f"Coins: {self.coins}",
            bg="black",
            fg="white",
            font=("Arial", 16)
        ).pack(pady=2)

        # ====================================================
        # CONTENT
        # ====================================================

        content = tk.Frame(
            window,
            bg="black"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=5
        )

        # ====================================================
        # LEFT
        # WEAPONS + ARMOR
        # ====================================================

        left = tk.Frame(
            content,
            bg="black"
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15
        )

        tk.Label(
            left,
            text="WEAPONS",
            bg="black",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(pady=4)

        for weapon, info in self.weapons.items():

            if (
                weapon == "Absolute Hero Blade"
                and not self.secret_sword_discovered
            ):
                continue

            if weapon in self.weapon_inventory:
                continue

            text = (
                f"{weapon}\n"
                f"+{info['attack']} ATK | "
                f"{info['price']} coins | "
                f"Lvl. {info['required_level']}"
            )

            tk.Button(
                left,
                text=text,
                command=lambda w=weapon:
                self.buy_weapon(w),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=38,
                height=2
            ).pack(pady=2)

        tk.Label(
            left,
            text="ARMOR",
            bg="black",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(pady=5)

        for armor, info in self.armors.items():

            if armor in self.armor_inventory:
                continue

            text = (
                f"{armor}\n"
                f"+{info['defense']} DEF | "
                f"+{info['hp']} HP | "
                f"{info['price']} coins | "
                f"Lvl. {info['required_level']}"
            )

            tk.Button(
                left,
                text=text,
                command=lambda a=armor:
                self.buy_armor(a),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=38,
                height=2
            ).pack(pady=2)

        # ====================================================
        # RIGHT
        # SPELLS
        # ====================================================

        right = tk.Frame(
            content,
            bg="black"
        )

        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=15
        )

        tk.Label(
            right,
            text="SPELLS",
            bg="black",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(pady=4)

        for spell_name, info in self.spells.items():

            if spell_name in self.learned_spells:

                text = (
                    f"{spell_name}\n"
                    f"ALREADY LEARNED"
                )

            else:

                text = (
                    f"{spell_name}\n"
                    f"{info['mana']} mana | "
                    f"{info['price']} coins | "
                    f"Lvl. {info['required_level']}"
                )

            tk.Button(
                right,
                text=text,
                command=lambda s=spell_name:
                self.buy_spell(s),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=38,
                height=3
            ).pack(pady=4)

        # ====================================================
        # POTION
        # ====================================================

        tk.Label(
            right,
            text="POTIONS",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=5)

        tk.Button(
            right,
            text="Potion - 10 coins",
            command=self.buy_potion,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=25,
            height=2
        ).pack(pady=3)

        # ====================================================
        # UPGRADES
        # ====================================================

        upgrades = tk.Frame(
            window,
            bg="black"
        )

        upgrades.pack(
            pady=2
        )

        tk.Button(
            upgrades,
            text="Upgrade equipped weapon",
            command=self.upgrade_weapon,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=28
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        tk.Button(
            upgrades,
            text="Upgrade equipped armor",
            command=self.upgrade_armor,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=28
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        # ====================================================
        # BACK
        # ====================================================

        tk.Button(
            window,
            text="Back",
            command=window.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=5)

        # ====================================================
        # INVISIBLE SECRET BUTTON
        # ====================================================

        tk.Button(
            window,
            text="",
            command=lambda:
            self.discover_secret_sword(window),
            bg="black",
            activebackground="black",
            relief="flat",
            bd=0,
            highlightthickness=0,
            width=4,
            height=2
        ).place(
            relx=0.0,
            rely=1.0,
            anchor="sw"
        )

    # ========================================================
    # SECRET SWORD
    # ========================================================

    def discover_secret_sword(
        self,
        window
    ):

        if self.secret_sword_discovered:

            self.show_message(
                "You have already discovered the secret..."
            )

            return

        self.secret_sword_discovered = True

        self.display(
            "An underground forge has appeared..."
        )

        self.show_message(
            "You discovered a secret weapon!\n\n"
            "Absolute Hero Blade\n"
            "+200 ATK\n"
            "Price: 5000 coins\n"
            "Required level: 25"
        )

        window.destroy()

        self.update_interface()

    # ========================================================
    # BUY POTION
    # ========================================================

    def buy_potion(self):

        if self.coins < 10:

            self.show_message(
                "You do not have enough coins."
            )

            return

        self.coins -= 10
        self.potions += 1

        self.display(
            "You bought a potion."
        )

        self.update_interface()

    # ========================================================
    # BUY WEAPON
    # ========================================================

    def buy_weapon(
        self,
        weapon
    ):

        if weapon in self.weapon_inventory:

            self.show_message(
                "You already own this weapon."
            )

            return

        info = self.weapons[weapon]

        if self.level < info["required_level"]:

            self.show_message(
                f"Level "
                f"{info['required_level']} required."
            )

            return

        if self.coins < info["price"]:

            self.show_message(
                "You do not have enough coins."
            )

            return

        self.coins -= info["price"]

        self.weapon_inventory.append(
            weapon
        )

        self.display(
            f"You bought {weapon}."
        )

        self.update_interface()

    # ========================================================
    # BUY ARMOR
    # ========================================================

    def buy_armor(
        self,
        armor
    ):

        if armor in self.armor_inventory:

            self.show_message(
                "You already own this armor."
            )

            return

        info = self.armors[armor]

        if self.level < info["required_level"]:

            self.show_message(
                f"Level "
                f"{info['required_level']} required."
            )

            return

        if self.coins < info["price"]:

            self.show_message(
                "You do not have enough coins."
            )

            return

        self.coins -= info["price"]

        self.armor_inventory.append(
            armor
        )

        self.display(
            f"You bought {armor}."
        )

        self.update_interface()

    # ========================================================
    # BUY SPELL
    # ========================================================

    def buy_spell(
        self,
        spell_name
    ):

        if spell_name in self.learned_spells:

            self.show_message(
                "You already know this spell."
            )

            return

        info = self.spells[spell_name]

        if self.level < info["required_level"]:

            self.show_message(
                f"You must be level "
                f"{info['required_level']}."
            )

            return

        if self.coins < info["price"]:

            self.show_message(
                "You do not have enough coins."
            )

            return

        self.coins -= info["price"]

        self.learned_spells.append(
            spell_name
        )

        self.display(
            f"You learned the spell: "
            f"{spell_name}!"
        )

        self.show_message(
            f"Spell learned: {spell_name}!\n\n"
            f"Cost: {info['mana']} mana\n"
            f"Multiplier: "
            f"x{info['multiplier']}"
        )

        self.update_interface()

    # ========================================================
    # UPGRADE WEAPON
    # ========================================================

    def upgrade_weapon(self):

        weapon = self.weapons[
            self.equipped_weapon
        ]

        next_level = (
            weapon["level"] + 1
        )

        price = next_level * 50

        if self.level < next_level:

            self.show_message(
                f"You must be level "
                f"{next_level}."
            )

            return

        if self.coins < price:

            self.show_message(
                "You do not have enough coins."
            )

            return

        self.coins -= price

        weapon["level"] += 1

        self.display(
            f"{self.equipped_weapon} reaches "
            f"level {weapon['level']}."
        )

        self.update_interface()

    # ========================================================
    # UPGRADE ARMOR
    # ========================================================

    def upgrade_armor(self):

        armor = self.armors[
            self.equipped_armor
        ]

        next_level = (
            armor["level"] + 1
        )

        price = next_level * 60

        if self.level < next_level:

            self.show_message(
                f"You must be level "
                f"{next_level}."
            )

            return

        if self.coins < price:

            self.show_message(
                "You do not have enough coins."
            )

            return

        self.coins -= price

        armor["level"] += 1

        self.display(
            f"{self.equipped_armor} reaches "
            f"level {armor['level']}."
        )

        self.update_interface()

    # ========================================================
    # CLASSES
    # ========================================================

    def class_menu(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Classes"
        )

        window.configure(
            bg="black"
        )

        window.attributes(
            "-fullscreen",
            True
        )

        tk.Label(
            window,
            text="CLASSES",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=20)

        tk.Label(
            window,
            text=f"Current class: {self.current_class}",
            bg="black",
            fg="white",
            font=("Arial", 15)
        ).pack(pady=5)

        for class_name, info in self.classes.items():

            if class_name in self.owned_classes:

                if class_name == self.current_class:

                    text = (
                        f"{class_name}\n"
                        f"EQUIPPED"
                    )

                else:

                    text = (
                        f"{class_name}\n"
                        f"OWNED - click to equip"
                    )

            else:

                text = (
                    f"{class_name}\n"
                    f"{info['price']} coins | "
                    f"+{info['attack']} ATK | "
                    f"+{info['defense']} DEF | "
                    f"+{info['hp']} HP | "
                    f"+{info['mana']} Mana"
                )

            tk.Button(
                window,
                text=text,
                command=lambda c=class_name:
                self.buy_class(c),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=55,
                height=3
            ).pack(pady=5)

        tk.Button(
            window,
            text="Back",
            command=window.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=15)

    # ========================================================
    # BUY / EQUIP CLASS
    # ========================================================

    def buy_class(
        self,
        class_name
    ):

        if class_name in self.owned_classes:

            self.current_class = class_name

            self.hp = min(
                self.hp,
                self.get_max_hp()
            )

            self.mana = min(
                self.mana,
                self.get_max_mana()
            )

            self.display(
                f"You equip the "
                f"{class_name} class."
            )

            self.update_interface()

            return

        info = self.classes[
            class_name
        ]

        if self.coins < info["price"]:

            self.show_message(
                "You do not have enough coins."
            )

            return

        self.coins -= info["price"]

        self.owned_classes.append(
            class_name
        )

        self.current_class = class_name

        self.hp = self.get_max_hp()
        self.mana = self.get_max_mana()

        self.display(
            f"You obtained the "
            f"{class_name} class!"
        )

        self.update_interface()

    # ========================================================
    # INVENTORY
    # ========================================================

    def inventory(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Inventory"
        )

        window.configure(
            bg="black"
        )

        window.attributes(
            "-fullscreen",
            True
        )

        tk.Label(
            window,
            text="INVENTORY",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=15)

        tk.Label(
            window,
            text=f"Equipped class: {self.current_class}",
            bg="black",
            fg="white",
            font=("Arial", 16)
        ).pack(pady=5)

        # WEAPONS

        tk.Label(
            window,
            text="WEAPONS",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=8)

        for weapon in self.weapon_inventory:

            info = self.weapons[weapon]

            text = (
                f"{weapon} | "
                f"+{info['attack']} ATK | "
                f"Level {info['level']}"
            )

            if weapon == self.equipped_weapon:

                text += " | EQUIPPED"

            tk.Button(
                window,
                text=text,
                command=lambda w=weapon:
                self.equip_weapon(w),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=55,
                height=2
            ).pack(pady=2)

        # ARMOR

        tk.Label(
            window,
            text="ARMOR",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        for armor in self.armor_inventory:

            info = self.armors[armor]

            text = (
                f"{armor} | "
                f"+{info['defense']} DEF | "
                f"+{info['hp']} HP"
            )

            if armor == self.equipped_armor:

                text += " | EQUIPPED"

            tk.Button(
                window,
                text=text,
                command=lambda a=armor:
                self.equip_armor(a),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=55,
                height=2
            ).pack(pady=2)

        # SPELLS

        tk.Label(
            window,
            text="LEARNED SPELLS",
            bg="black",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        if self.learned_spells:

            for spell_name in self.learned_spells:

                spell = self.spells[spell_name]

                tk.Label(
                    window,
                    text=(
                        f"{spell_name} | "
                        f"{spell['mana']} mana"
                    ),
                    bg="black",
                    fg="white",
                    font=("Arial", 13)
                ).pack(pady=2)

        else:

            tk.Label(
                window,
                text="No spells learned.",
                bg="black",
                fg="white"
            ).pack()

        tk.Button(
            window,
            text="Back",
            command=window.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=15)

    # ========================================================
    # EQUIP WEAPON
    # ========================================================

    def equip_weapon(
        self,
        weapon
    ):

        self.equipped_weapon = weapon

        self.display(
            f"You equip {weapon}."
        )

        self.update_interface()

    # ========================================================
    # EQUIP ARMOR
    # ========================================================

    def equip_armor(
        self,
        armor
    ):

        self.equipped_armor = armor

        self.display(
            f"You equip {armor}."
        )

        self.update_interface()

    # ========================================================
    # ZONES
    # ========================================================

    def zone_menu(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Zones"
        )

        window.configure(
            bg="black"
        )

        window.attributes(
            "-fullscreen",
            True
        )

        tk.Label(
            window,
            text="CHOOSE A ZONE",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=20)

        order = [
            "Plains",
            "Forest",
            "Mountain",
            "Shadow Realm",
            "Fallen Capital",
            "Fallen Citadel",
            "Abyss"
        ]

        for zone_name in order:

            zone = self.zones[
                zone_name
            ]

            text = (
                f"{zone_name} "
                f"(Level {zone['level']})"
            )

            tk.Button(
                window,
                text=text,
                command=lambda z=zone_name:
                self.change_zone(
                    z,
                    window
                ),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=35,
                height=2
            ).pack(pady=4)

        tk.Button(
            window,
            text="Back",
            command=window.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=15)

    # ========================================================
    # CHANGE ZONE
    # ========================================================

    def change_zone(
        self,
        zone_name,
        window
    ):

        zone = self.zones[
            zone_name
        ]

        if self.level < zone["level"]:

            self.show_message(
                f"You must be level "
                f"{zone['level']}."
            )

            return

        if self.mobs_defeated < zone["required_mobs"]:

            self.show_message(
                f"You must defeat "
                f"{zone['required_mobs']} mobs."
            )

            return

        order = [
            "Plains",
            "Forest",
            "Mountain",
            "Shadow Realm",
            "Fallen Capital",
            "Fallen Citadel",
            "Abyss"
        ]

        index = order.index(
            zone_name
        )

        if index > 0:

            previous = order[
                index - 1
            ]

            if not self.zones[
                previous
            ]["boss_defeated"]:

                self.show_message(
                    f"You must defeat the boss of "
                    f"{previous} before entering here."
                )

                return

        self.current_zone = zone_name

        window.destroy()

        self.display(
            f"You enter the zone: "
            f"{zone_name}"
        )

        self.update_interface()

    # ========================================================
    # BOSSES
    # ========================================================

    def boss_menu(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Bosses"
        )

        window.configure(
            bg="black"
        )

        window.attributes(
            "-fullscreen",
            True
        )

        tk.Label(
            window,
            text="AVAILABLE BOSSES",
            bg="black",
            fg="white",
            font=("Arial", 28, "bold")
        ).pack(pady=20)

        order = [
            "Plains",
            "Forest",
            "Mountain",
            "Shadow Realm",
            "Fallen Capital",
            "Fallen Citadel",
            "Abyss"
        ]

        for zone_name in order:

            zone = self.zones[
                zone_name
            ]

            text = (
                f"{zone['boss']} "
                f"(Lvl. {zone['level']})"
            )

            if zone["boss_defeated"]:

                text += " - DEFEATED"

            tk.Button(
                window,
                text=text,
                command=lambda z=zone_name:
                self.start_boss(
                    z,
                    window
                ),
                bg="#202020",
                fg="white",
                activebackground="#404040",
                activeforeground="white",
                width=35,
                height=2
            ).pack(pady=4)

        tk.Button(
            window,
            text="Back",
            command=window.destroy,
            bg="#202020",
            fg="white",
            activebackground="#404040",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=15)

    # ========================================================
    # START BOSS
    # ========================================================

    def start_boss(
        self,
        zone_name,
        window
    ):

        zone = self.zones[
            zone_name
        ]

        if zone["boss_defeated"]:

            self.show_message(
                "You have already defeated this boss."
            )

            return

        if self.level < zone["level"]:

            self.show_message(
                f"You must be level "
                f"{zone['level']}."
            )

            return

        if self.mobs_defeated < zone["required_mobs"]:

            self.show_message(
                f"You must defeat "
                f"{zone['required_mobs']} mobs."
            )

            return

        order = [
            "Plains",
            "Forest",
            "Mountain",
            "Shadow Realm",
            "Fallen Capital",
            "Fallen Citadel",
            "Abyss"
        ]

        index = order.index(
            zone_name
        )

        if index > 0:

            previous = order[
                index - 1
            ]

            if not self.zones[
                previous
            ]["boss_defeated"]:

                self.show_message(
                    f"You must first defeat "
                    f"the boss of {previous}."
                )

                return

        window.destroy()

        stats = zone[
            "boss_stats"
        ]

        self.combat_interface(
            zone["boss"],
            stats[0],
            stats[1],
            stats[2],
            stats[3],
            stats[4],
            boss=True,
            boss_zone=zone_name
        )

    # ========================================================
    # SECRET ZONE
    # ========================================================

    def secret_zone(self):

        if self.mobs_defeated < 100:

            self.show_message(
                "The secret zone is inaccessible."
            )

            return

        self.current_zone = "???"

        self.display(
            "A strange presence draws you in..."
        )

        self.display(
            "You arrive in the ??? zone."
        )

        self.update_interface()

    # ========================================================
    # STATISTICS
    # ========================================================

    def show_stats(self):

        spells = (
            ", ".join(self.learned_spells)
            if self.learned_spells
            else "None"
        )

        self.show_message(
            f"===== STATS =====\n\n"

            f"Name: {self.name}\n"
            f"Class: {self.current_class}\n"
            f"Level: {self.level}\n"
            f"XP: {self.xp}/{self.level * 50}\n\n"

            f"HP: {self.hp}/{self.get_max_hp()}\n"
            f"Mana: {self.mana}/{self.get_max_mana()}\n"
            f"Attack: {self.get_attack()}\n"
            f"Defense: {self.get_defense()}\n\n"

            f"Weapon: {self.equipped_weapon}\n"
            f"Armor: {self.equipped_armor}\n\n"

            f"Spells: {spells}\n\n"

            f"Coins: {self.coins}\n"
            f"Potions: {self.potions}\n"
            f"Mobs defeated: {self.mobs_defeated}\n\n"

            f"Zone: {self.current_zone}"
        )

    # ========================================================
    # DEATH
    # ========================================================

    def death(self):

        messagebox.showinfo(
            "SHADOW RPG",
            f"You died.\n\n"
            f"Level reached: {self.level}\n"
            f"Mobs defeated: {self.mobs_defeated}",
            parent=self.root
        )

        self.root.destroy()


# ============================================================
# LAUNCH
# ============================================================

root = tk.Tk()

game = ShadowRPG(root)

root.mainloop()
