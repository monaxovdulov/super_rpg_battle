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

    def get_damage(self, enemy):
        self.hp = self.hp - enemy.power_attack

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.power_attack


class Monster:
    def __init__(self, name, hp, power_attack, heal, armor):
        self.name = name
        self.hp = hp
        self.power_attack = power_attack
        self.heal = heal
        self.armor = armor

    def get_damage(self, enemy):
        self.hp = self.hp - enemy.power_attack

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.power_attack


name_player = input("What your name?")
player = Hero(name_player, 100, 10, 10, 5)
print(player.name)

monster = Monster("Ork", 90, 10, 10, 3)

print("Герой актакует монстра")
player.attack(monster)
print(monster.hp)

