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

    def attack(self, oppo_defence, base, oppo_type, a):
        atk_type = "Normal"
        if self.attack_1 == "Double_Edge":
            atk_type = "Normal"
            base = 100

        modifier = round(random.uniform(0.5, 0.7), 2)
        damage_done = ((0.84 * self.attack / oppo_defence * base + 2) * modifier)
        truefalse = (
            True, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False,)
        chance = random.choice(truefalse)
        if chance:
            damage_done *= 1.5
        self.calculate_damage(atk_type, damage_done, oppo_type)

    def sp_attack(self, oppo_sp_defence, base, oppo_type):
        atk_type = "Normal"
        if True:
            if self.attack_1 == "Hyper_Beam":
                atk_type = "Normal"
                base = 120
            elif self.attack_1 == "Blast_Burn":
                atk_type = "Fire"
                base = 150
            # Add more special attacks and their types and base damage

        modifier = round(random.uniform(0.75, 0.9), 2)
        damage_done = ((0.84 * self.sp_attack / oppo_sp_defence * base + 2) * modifier)
        truefalse = (
            True, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False,)
        chance = random.choice(truefalse)
        if chance:
            damage_done *= 1.5
        self.calculate_damage(atk_type, damage_done, oppo_type)

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

    def calculate_damage(self, atk_type, damage_done, oppo_type):
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
            # Add more type matchups for remaining types if needed
        }

        if atk_type in effectiveness and oppo_type in effectiveness[atk_type]:
            effectiveness_value = effectiveness[atk_type][oppo_type]
        else:
            effectiveness_value = 1  # Neutral effectiveness

        damage_done *= effectiveness_value
        return damage_done
