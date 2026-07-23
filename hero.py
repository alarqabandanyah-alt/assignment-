from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.abilities = []
        self.armors = []

        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        damage = 0

        for ability in self.abilities:
            damage += ability.attack()

        return damage

    def defend(self):
        defense = 0

        for armor in self.armors:
            defense += armor.block()

        return defense

    def take_damage(self, damage):
        damage -= self.defend()

        if damage > 0:
            self.current_health -= damage

    def is_alive(self):
        return self.current_health > 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self):
        self.deaths += 1

    def battle(self, opponent):

        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():

            opponent.take_damage(self.attack())

            if opponent.is_alive():
                self.take_damage(opponent.attack())

        if self.is_alive():
            self.add_kill(1)
            opponent.add_death()
            print(self.name + " won!")

        else:
            opponent.add_kill(1)
            self.add_death()
            print(opponent.name + " won!")


if __name__ == "__main__":

    hero1 = Hero("Batman")
    hero2 = Hero("Superman")

    hero1.add_weapon(Weapon("Batarang",40))
    hero2.add_weapon(Weapon("Laser Eyes",45))

    hero1.battle(hero2)
