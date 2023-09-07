import random


class Pokemon:

    def __init__(self, name, type, total, hp, attack, defense, sp_attack, sp_defense, speed, attack_1, sp_attack_1):
        self.sp_attack = sp_attack
        self.total = total
        self.sp_defence = sp_defense
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

        modifier = round(random.uniform(0.75, 0.9), 2)
        damage_done = ((0.84 * self.attack / oppo_defence * base + 2) * modifier)
        truefalse = (
            True, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False,)
        chance = random.choice(truefalse)
        if chance:
            damage_done *= 1.5
        self.calculate_damage(atk_type, damage_done, oppo_type)

    def sp_attack(self, atk_type, oppo_sp_defence, base, oppo_type):
        atk_type = "Normal"
        if self.attack_1 == "Hyper_Beam":
            atk_type = "Normal"
            base = 120
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
        print(self.name + "is knocked out")

    def calculate_damage(self, atk_type, damage_done, oppo_type):
        if atk_type == "Normal":
            if oppo_type == "Rock":
                damage_done /= 2
            if oppo_type == "Ghost":
                damage_done = 0
            if oppo_type == "Steel":
                damage_done /= 2
        elif atk_type == "Fire":
            if oppo_type == "Fire":
                damage_done /= 2
            if oppo_type == "Water":
                damage_done /= 2
            if oppo_type == "Grass":
                damage_done *= 2
            if oppo_type == "Ice":
                damage_done *= 2
            if oppo_type == "Bug":
                damage_done *= 2
            if oppo_type == "Rock":
                damage_done /= 2
            if oppo_type == "Dragon":
                damage_done /= 2
            if oppo_type == "Steel":
                damage_done *= 2
        elif atk_type == "Water":
            if oppo_type == "Fire":
                damage_done *= 2
            if oppo_type == "Water":
                damage_done /= 2
            if oppo_type == "Grass":
                damage_done /= 2
            if oppo_type == "Ground":
                damage_done *= 2
            if oppo_type == "Rock":
                damage_done *= 2
            if oppo_type == "Dragon":
                damage_done /= 2
        elif atk_type == "Electric":
            if oppo_type == "Water":
                damage_done *= 2
            if oppo_type == "Electric":
                damage_done /= 2
            if oppo_type == "Grass":
                damage_done /= 2
            if oppo_type == "Ground":
                damage_done = 0
            if oppo_type == "Flying":
                damage_done *= 2
            if oppo_type == "Dragon":
                damage_done /= 2
        elif atk_type == "Grass":
            if oppo_type == "Fire":
                damage_done /= 2
            if oppo_type == "Water":
                damage_done *= 2
            if oppo_type == "Grass":
                damage_done /= 2
            if oppo_type == "Poison":
                damage_done /= 2
            if oppo_type == "Ground":
                damage_done *= 2
            if oppo_type == "Flying":
                damage_done /= 2
            if oppo_type == "Bug":
                damage_done /= 2
            if oppo_type == "Rock":
                damage_done *= 2
            if oppo_type == "Dragon":
                damage_done /= 2
            if oppo_type == "Steel":
                damage_done /= 2
        return damage_done

