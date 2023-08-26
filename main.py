import random

class Char_1():

    def __init__(self, sp_attack, sp_defence, speed, attack, defence, health,
                 level):
        self.sp_attack = sp_attack
        self.sp_defence = sp_defence
        self.speed = speed
        self.attack = attack
        self.defence = defence
        self.health = health
        self.level = level

    def Attack(self, oppo_defence, base):
        modifier = round(random.uniform(0.9, 1.2), 2)
        damage_done = (
            ((2 * self.level + 10) / 250 * self.attack / oppo_defence * base +
             2) * modifier)

