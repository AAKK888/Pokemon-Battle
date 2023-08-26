import random

class Char_1():

    def __init__(self, sp_attack, sp_defense, speed, attack, defense, max_health,
                 level):
        self.sp_attack = sp_attack
        self.sp_defence = sp_defence
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.level = level
        self.current_health = max_health
        self.is_knocked_out = False

    def Attack(self, oppo_defence, base):
        modifier = round(random.uniform(0.9, 1.2), 2)
        damage_done = (
            ((2 * self.level + 10) / 250 * self.attack / oppo_defence * base +
             2) * modifier)

    def lose_health(self, damage_taken):
        if amount > self.current_health:  
          self.current_health = 0
          self.is_knocked_out = True 
        else:
          self.current_health -= amount 
