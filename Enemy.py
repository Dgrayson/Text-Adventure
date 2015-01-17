__author__ = 'dgrayson'

from Player import Player
from time import sleep
import random

class Enemy:

    name = ''

    def __init__(self):
        self.maxHP = None
        self.hp = None
        self.alive = True

    def turn(self, player):

        if player.defend:
            print(self.name + " attacks"); sleep(1)
            print("You defended yourself"); sleep(1)
        else:
            print(self.name + " attacks.\nDeals 5 damage!")
            player.currHP -= 5

        if player.currHP <= 0:
            print("You have been defeated!")
            player.alive = False

class Skeleton(Enemy):

    def __init__(self):

        Enemy.__init__(self)
        self.name = 'Skeleton'
        self.maxHP = 20
        self.hp = 20

class Bat(Enemy):

    def __init__(self):

        Enemy.__init__(self)
        self.name = 'Bat'
        self.maxHP = 10
        self.hp = 10