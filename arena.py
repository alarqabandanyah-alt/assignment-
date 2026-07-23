from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:

    def __init__(self):

        self.team_one = Team(input("Team One Name: "))
        self.team_two = Team(input("Team Two Name: "))

    def create_ability(self):

        name = input("Ability Name: ")
        damage = int(input("Max Damage: "))
        return Ability(name, damage)

    def create_weapon(self):

        name = input("Weapon Name: ")
        damage = int(input("Weapon Damage: "))
        return Weapon(name, damage)

    def create_armor(self):

        name = input("Armor Name: ")
        block = int(input("Max Block: "))
        return Armor(name, block)

    def create_hero(self):

        hero = Hero(input("Hero Name: "))

        while True:

            choice = input(
"""1 Ability
2 Weapon
3 Armor
4 Done
Choice: """)

            if choice == "1":
                hero.add_ability(self.create_ability())

            elif choice == "2":
                hero.add_weapon(self.create_weapon())

            elif choice == "3":
                hero.add_armor(self.create_armor())

            elif choice == "4":
                break

        return hero

    def build_team_one(self):

        members = int(input("Number of heroes on Team One: "))

        for i in range(members):
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):

        members = int(input("Number of heroes on Team Two: "))

        for i in range(members):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):

        self.team_one.attack(self.team_two)

    def show_stats(self):

        print("\nTEAM ONE")
        self.team_one.stats()

        print("\nTEAM TWO")
        self.team_two.stats()

        kills = sum(hero.kills for hero in self.team_one.heroes)
        deaths = sum(hero.deaths for hero in self.team_one.heroes)

        if deaths == 0:
            deaths = 1

        print("Team One K/D:", kills / deaths)

        kills = sum(hero.kills for hero in self.team_two.heroes)
        deaths = sum(hero.deaths for hero in self.team_two.heroes)

        if deaths == 0:
            deaths = 1

        print("Team Two K/D:", kills / deaths)

        print("\nSurvivors Team One")
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(hero.name)

        print("\nSurvivors Team Two")
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(hero.name)


if __name__ == "__main__":

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    arena.team_battle()

    arena.show_stats()
    
    