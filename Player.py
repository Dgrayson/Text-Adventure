__author__ = 'dgrayson'

from time import sleep
import random
import Items

class Player:

    def __init__(self, name):
        self.maxHP = 100
        self.currHP = 100
        self.maxMP = 50
        self.currMP = 50
        self.x = 0
        self.y = 0
        self.name = name
        self.alive = True
        self.defend = False
        self.inventory = []

    def turn(self, enemy):

        inMenu = True
        self.defend = False

        while inMenu:
            print("What will you do?\n\n1. Attack 2. Defend\n3. Magic 4. Run\n5. Items")
            choice = int(input())

            if choice == 1:
                print(self.name + " attacks")

                self.attack(enemy)
                inMenu = False
            elif choice == 2:
                print("You defend"); sleep(1)
                inMenu = False

                self.defend = True
            elif choice == 3:
                self.magic(enemy)
                inMenu = False

            elif choice == 4:
                print("You've run away")
                inMenu = False
                return -1
            elif choice == 5:
                i = 0
                for x in self.inventory:
                    print(str(i) + " " + x.name)
                    i += 1

                print("Enter the number of the item you want to use")

                choice = int(input())

                item = self.inventory[choice]

                self.useItem(item)



    def move(self, direction):

        moved = False

        while moved == False:
            if direction == 'w' and self.y != 0:
                self.y -= 1
                moved = True
            elif direction == 'e' and self.y != 4:
                self.y += 1
                moved = True
            elif direction == 'n' and self.x != 4:
                self.x += 1
                moved = True
            elif direction == 's' and self.x != 0:
                self.x -= 1
                moved = True
            else:
                print("Invalid move please choose again")
                direction = input()

    def magic(self, enemy):
        print("Select a spell")

        choosing = True

        while choosing:

            print("1. Fire 2. Blizzard\n3. Lighting 4. Rapid Slash\n5. Cure")

            choice = int(input())

            if choice == 1 and self.currMP >= 5:

                print(self.name + " uses Fire"); sleep(1)
                print("You deal 10 damage\n"); sleep(1)
                enemy.hp -= 10
                self.currMP -= 5
            elif choice == 2 and self.currMP >= 5:

                print(self.name + " uses Blizzard"); sleep(1)
                print("You deal 10 damage"); sleep(1)
                enemy.hp -= 10
                self.currMP -= 5
            elif choice == 3 and self.currMP >= 5:

                print(self.name + " uses Lightning"); sleep(1)
                print("You deal 10 damage"); sleep(1)
                enemy.hp -= 10
                self.currMP -= 5
            elif choice == 4 and self.currMP >= 15:

                print(self.name + " uses Rapid Slash")

                numAttacks = random.randint(1,5)
                currAttacks = 0

                while currAttacks < numAttacks:

                    self.attack(enemy)

                    if not enemy.alive:
                        break

                    currAttacks += 1

                self.currMP -= 15
            elif choice == 5 and self.currMP >= 10:

               print(self.name + " uses Cure!"); sleep(1)
               print("10HP recovered!"); sleep(1)

               self.currHP += 10
               self.currMP -= 10
            else:
                print("Not Enough MP")

            choosing = False

        self.checkEnemy(enemy)

    def attack(self, enemy):

        critical = random.randint(0, 100)

        if critical % 9 == 0:
            print("Critical Hit!");
            enemy.hp -= 20
            print("You dealt 20 damage!\n"); sleep(1.5)
            self.inMenu = False
        else:
            enemy.hp -= 5
            print("You deal 5 damage\n");sleep(1.5)
            self.inMenu = False

        self.checkEnemy(enemy)

    def checkEnemy(self, enemy):

        if enemy.hp <= 0:
                print("You have defeated the enemy\n\n")
                print("**********\n\n");sleep(1.5)
                enemy.alive = False
                inMenu = False

    def addToInventory(self, item):

        self.inventory.append(item)

    def removefrominventory(self, item):

        self.inventory.remove(item)

    def useItem(self, item):

        if item.type == 'rec':
            if item.name == 'Potion':
                print("You used Potion")
                self.currHP += item.value
            elif item.name == 'Ether':
                self.currMP += item.value
