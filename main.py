import random


class Char_1:

    def __init__(self, sp_attack, sp_defense, speed, attack, defense, max_health,
                 level, name):
        self.sp_attack = sp_attack
        self.sp_defence = sp_defense
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.level = level
        self.current_health = max_health
        self.is_knocked_out = False
        self.name = name

    def attack(self, oppo_defence, base):
        modifier = round(random.uniform(0.9, 1.2), 2)
        damage_done = (((2 * self.level + 10) / 250 * self.attack / oppo_defence * base + 2) * modifier)
        truefalse = (True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,)
        chance = random.choice(truefalse)
        if chance:
            damage_done *= 1.5
        else:
            pass
        return damage_done

    def lose_health(self, damage_taken):
        if damage_taken > self.current_health:
            self.current_health = 0
            self.is_knocked_out = True
        else:
            self.current_health -= damage_taken
        return self.current_health

    def knock_out(self):
        self.is_knocked_out = True
