__author__ = 'dgrayson'

from time import sleep
import random

class Player:

    def __init__(self, name):
        self.maxHP = 100
        self.currHP = 100
        self.x = 0
        self.y = 0
        self.name = name
        self.alive = True
        self.defend = False
        self.inventory = []

    def turn(self, enemy):

        self.defend = False

        print("What will you do?\n\n1. Attack 2. Defend\n3. Heal 4. Run")
        choice = int(input())

        if choice == 1:
            print(self.name + " attacks")

            critical = random.randint(0, 100)

            if critical % 9 == 0:
                print("Critical Hit!");
                enemy.hp -= 20
                print("You dealt 20 damage!\n"); sleep(1.5)
            else:
                enemy.hp -= 5
                print("You deal 5 damage\n");sleep(1.5)

            if enemy.hp <= 0:
                print("You have defeated the enemy\n\n")
                print("**********\n\n");sleep(1.5)
                enemy.alive = False
        elif choice == 2:
            print("You defend"); sleep(1)

            self.defend = True
        elif choice == 3:
            print("You Heal 10 HP")

            self.currHP += 10
        elif choice == 4:
            print("You've run away")

            return -1

    def move(self, direction):

        moved = False

        while moved == False:
            if direction == 'w' and self.x != 0:
                self.x -= 1
                moved = True
            elif direction == 'e' and self.x != 4:
                self.x += 1
                moved = True
            elif direction == 'n' and self.y != 4:
                self.y += 1
                moved = True
            elif direction == 's' and self.y != 0:
                self.y -= 1
                moved = True
            else:
                print("Invalid move please choose again")
                direction = input()

    def addToInventory(self, item):

        self.inventory.append(item)
