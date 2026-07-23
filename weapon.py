import random
from ability import Ability

class Weapon(Ability):

    def attack(self):
        half = self.max_damage // 2
        return random.randint(half, self.max_damage)
    