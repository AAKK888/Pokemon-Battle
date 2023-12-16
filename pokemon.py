import random

class Pokemon:
    def __init__(self, name, type, total, hp, attack, defense, sp_attack, sp_defense, speed, attack_1, sp_attack_1):
        self.sp_attack = sp_attack
        self.total = total
        self.sp_defense = sp_defense
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.max_health = hp
        self.current_health = hp
        self.is_knocked_out = False
        self.name = name
        self.type = type
        self.attack_1 = attack_1
        self.sp_attack_1 = sp_attack_1

    def attack(self, oppo_defence, oppo_type, move_name):
        atk_type = "Normal"
        base = 0
        modifier = round(random.uniform(0.5, 0.7), 2)
        damage_done = 0

        if move_name == "Double_Edge":
            atk_type = "Normal"
            base = 100
        elif move_name == "Fly":
            atk_type = "Flying"
            base = 90
        elif move_name == "Night_Slash":
            atk_type = "Dark"
            base = 70
        elif move_name == "Iron_Tail":
            atk_type = "Steel"
            base = 100
        elif move_name == "Leaf_Blade":
            atk_type = "Grass"
            base = 90
        elif move_name == "Waterfall":
            atk_type = "Water"
            base = 80
        elif move_name == "Close_Combat":
            atk_type = "Fighting"
            base = 120
        elif move_name == "Stone_Edge":
            atk_type = "Rock"
            base = 100
        elif move_name == "Aqua_Tail":
            atk_type = "Water"
            base = 90
        elif move_name == "Zenn_Headbutt":
            atk_type = "Psychic"
            base = 80
        elif move_name == "Bug_Bite":
            atk_type = "Bug"
            base = 60
        elif move_name == "Poltergeist":
            atk_type = "Ghost"
            base = 110
        elif move_name == "Outrage":
            atk_type = "Dragon"
            base = 120
        elif move_name == "Power_Gem":
            atk_type = "Rock"
            base = 80
        elif move_name == "Psycho_Boost":
            atk_type = "Psychic"
            base = 140
        elif move_name == "Headlong_Rush":
            atk_type = "Rock"
            base = 100
        elif move_name == "Dragon_Rush":
            atk_type = "Dragon"
            base = 100
        elif move_name == "Phantom_Force":
            atk_type = "Ghost"
            base = 90
        elif move_name == "Ice_Beam":
            atk_type = "Ice"
            base = 90

        damage_done = ((0.84 * self.attack / oppo_defence * base + 2) * modifier)
        effectiveness = self.calculate_damage(atk_type, oppo_type)
        
        if atk_type == self.type:
            damage_done *= 1.5  # Applying STAB bonus if move's type matches Pokemon's type

        damage_done *= effectiveness

        if random.choice([True, False, False]):
            damage_done *= 1.5  # Critical hit

        self.inflict_damage(damage_done)

    def sp_attack(self, oppo_sp_defence, base, oppo_type):
        atk_type = "Normal"
        # Add more special attacks and their types and base damage...

    def lose_health(self, damage_taken):
        if damage_taken > self.current_health:
            self.current_health = 0
            self.is_knocked_out = True
        else:
            self.current_health -= damage_taken
        return self.current_health

    def knock_out(self):
        self.is_knocked_out = True
        print(self.name + " is knocked out")

    def calculate_damage(self, atk_type, oppo_type):
        effectiveness = {
            "Normal": {"Rock": 0.5, "Ghost": 0, "Steel": 0.5},
            "Fire": {"Fire": 0.5, "Water": 0.5, "Grass": 2, "Ice": 2, "Bug": 2, "Rock": 0.5, "Dragon": 0.5, "Steel": 2},
            "Water": {"Fire": 2, "Water": 0.5, "Grass": 0.5, "Ground": 2, "Rock": 2, "Dragon": 0.5},
            "Electric": {"Water": 2, "Electric": 0.5, "Grass": 0.5, "Ground": 0, "Flying": 2, "Dragon": 0.5},
            "Grass": {"Fire": 0.5, "Water": 2, "Grass": 0.5, "Poison": 0.5, "Ground": 2, "Flying": 0.5,
                      "Bug": 0.5, "Rock": 2, "Dragon": 0.5, "Steel": 0.5},
            "Ice": {"Fire": 0.5, "Water": 0.5, "Grass": 2, "Ice": 0.5, "Ground": 2, "Flying": 2, "Dragon": 2,
                    "Steel": 0.5},
            "Fighting": {"Normal": 2, "Ice": 2, "Poison": 0.5, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Rock": 2,
                         "Ghost": 0, "Dark": 2, "Steel": 2, "Fairy": 0.5},
            "Poison": {"Grass": 2, "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Ghost": 0.5, "Steel": 0, "Fairy": 2},
            "Ground": {"Fire": 2, "Electric": 2, "Grass": 0.5, "Poison": 2, "Flying": 0, "Bug": 0.5, "Rock": 2,
                       "Steel": 2},
            "Flying": {"Electric": 0.5, "Grass": 2, "Fighting": 2, "Bug": 2, "Rock": 0.5, "Steel": 0.5},
            "Psychic": {"Fighting": 2, "Poison": 2, "Psychic": 0.5, "Dark": 0, "Steel": 0.5},
            "Bug": {"Fire": 0.5, "Grass": 2, "Fighting": 0.5, "Flying": 0.5, "Poison": 0.5, "Ghost": 0.5,
                    "Steel": 0.5, "Fairy": 0.5},
            "Rock": {"Fire": 2, "Ice": 2, "Fighting": 0.5, "Ground": 0.5, "Flying": 2, "Bug": 2, "Steel": 0.5},
            "Ghost": {"Normal": 0, "Psychic": 2, "Ghost": 2, "Dark": 0.5},
            "Dragon": {"Dragon": 2, "Steel": 0.5, "Fairy": 0},
            "Dark": {"Fighting": 0.5, "Psychic": 2, "Ghost": 2, "Dark": 0.5, "Fairy": 0.5},
            "Steel": {"Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Ice": 2, "Rock": 2, "Steel": 0.5, "Fairy": 2},
            "Fairy": {"Fire": 0.5, "Fighting": 2, "Poison": 0.5, "Dragon": 2, "Dark": 2, "Steel": 0.5},
        }

        if atk_type in effectiveness and oppo_type in effectiveness[atk_type]:
            effectiveness_value = effectiveness[atk_type][oppo_type]
        else:
            effectiveness_value = 1  # Neutral effectiveness

        return effectiveness_value

    def inflict_damage(self, damage):
        if damage > self.current_health:
            self.current_health = 0
            self.is_knocked_out = True
        else:
            self.current_health -= damage
