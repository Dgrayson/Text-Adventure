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
            print(self.name + " attacks")
            print("You defended yourself")
            sleep(1)
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

class Boss(Enemy):

    def __init__(self):

        Enemy.__init__(self)
        self.maxHP = 100
        self.hp = 100
        self.counter = 0

    def turn(self, player):

        if player.defend:
            print(self.name + " attacks"); sleep(1)
            print("You defended yourself"); sleep(1)

            if self.counter >= 3:
                self.counter = 0
            else:
                self.counter += 1

        elif self.counter == 3:
            self.special(player)
            self.counter = 0
        else:
            print(self.name + " attacks.\nDeals 5 damage!")
            player.currHP -= 10
            self.counter += 1

        if player.currHP <= 0:
            print("You have been defeated!")
            player.alive = False


class Dragon(Boss):

    def __init__(self):

        Boss.__init__(self)
        self.name = 'Dragon'

    def special(self, player):
        print("Special Attack!")
        sleep(1)
        print(self.name + " uses Fire breath"); sleep(1)
        print(player.name + ' takes 20 damage'); sleep(1)
        player.currHP -= 20
