import random

class Team:

    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)

    def view_all_heroes(self):

        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):

        living_heroes = [hero for hero in self.heroes if hero.is_alive()]
        living_opponents = [hero for hero in other_team.heroes if hero.is_alive()]

        while living_heroes and living_opponents:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.battle(opponent)

            living_heroes = [hero for hero in self.heroes if hero.is_alive()]
            living_opponents = [hero for hero in other_team.heroes if hero.is_alive()]

    def revive_heroes(self):

        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):

        for hero in self.heroes:
            print(hero.name)
            print("Kills:", hero.kills)
            print("Deaths:", hero.deaths)