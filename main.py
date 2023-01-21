import random


# name_player = "Alex Makedonian III"
# hp_player = 100
# power_attack_player = 10
# heal_player = 10
# armor_player = 5


# name_monster = "Silver ork"
# hp_monster = 90
# power_attack_monster = 14
# heal_monster = 5
# armor_monster = 3


# player = {
#     'name_player': "Alex Makedonian III",
#     'hp_player': 100,
#     'power_attack_player': 10,
#     'heal_player': 10,
#     'armor_player': 5
# }
#
# monster = {
#     'name_monster': "Silver ork",
#     'hp_monster': 90,
#     'power_attack_monster': 14,
#     'heal_monster': 5,
#     'armor_monster': 3
# }
#
#
# print(player['name_player'])
#
# monster['hp_monster'] = monster['hp_monster'] - player['power_attack_player'] + monster['armor_monster']


class Hero:
    def __init__(self, name, hp_player, power_attack_player, heal_player, armor_player):
        self.name = name
        self.hp = hp_player
        self.power_attack = power_attack_player
        self.heal = heal_player
        self.armor = armor_player

    def show_characteristics(self):
        print(
            f'{self.name.capitalize()}:\nздоровье - {self.hp}\nсила атаки - {self.power_attack}\nлечение - {self.heal}\nброня - {self.armor}')

    def get_action(self):
        pass

    def damage_deal(self, damage):
        self.hp = self.hp - damage

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.power_attack

    def turn(self):
        pass

    def is_dead(self):
        pass

class Monster:
    def __init__(self, name, hp, power_attack, heal, armor):
        self.name = name
        self.hp = hp
        self.power_attack = power_attack
        self.heal = heal
        self.armor = armor

    def show_characteristics(self):
        print(
            f'{self.name.capitalize()}:\nздоровье - {self.hp}\nсила атаки - {self.power_attack}\nлечение - {self.heal}\nброня - {self.armor}\n{"-" * 20}\n')

    def get_action(self):
        pass

    def damage_deal(self, damage):
        self.hp = self.hp - damage

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.power_attack

    def turn(self, action_game):
        pass

    def is_dead(self):
        pass



name_player = input("What your name?")
player = Hero(name_player, 100, 10, 10, 5)  # создаем объект на основе класса Hero
print(player.name)

monster1 = Monster("Ork", 60, 10, 10, 3)  # создаем объект на основе класса Monster

monster2 = Monster("Goblin", 70, 10, 10, 3)

while True:
    player.show_characteristics()

    monster1.show_characteristics()


    action = player.get_action()

    player.turn(action, target)

    monster1.is_dead()

    break
