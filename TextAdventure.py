__author__ = 'dgrayson'

import random
from time import sleep

class Player:

    def __init__(self, name):
        self.hp = 100
        self.x = 0
        self.y = 0
        self.name = name
        self.alive = True
        self.defend = False

    def turn(self):

        self.defend = False

        print("What will you do?\n\n1. Attack 2. Defend\n3. Heal 4. Run")
        choice = int(input())

        if choice == 1:
            print("You attack"); sleep(1.5)

            critical = random.randint(0,100)

            if critical % 9 == 0:
                print("Critical Hit!"); sleep(1.5)
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

            self.hp += 10
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

class Enemy:

    def __init__(self):
        self.hp = 20
        self.alive = True

    def turn(self):

        if player.defend == True:
            print("Enemy attacks"); sleep(1)
            print("You defended yourself"); sleep(1)
        else:
            print("Enemy attacks.\nDeals 5 damage!")
            player.hp -= 5

        if player.hp <= 0:
            print("You have been defeated!")
            player.alive = False

def battle():

    while player.alive and enemy.alive:

        print("Player HP: " + str(player.hp) + "\nEnemy HP: " + str(enemy.hp))

        num = player.turn()

        if enemy.alive == False or num == -1:
            break

        enemy.turn()

def examine():
    print("Examine")

board = [[0 for x in range(5)] for x in range(5)]

i = 0
j = 0


while i < 5:
    j = 0
    while j < 5:
        board[i][j] = random.randint(0,1)
        j += 1
    i += 1

i = random.randint(0,4)
j = random.randint(0,4)

board[i][j] = 2

print("What is your name?")

name = input()

print("Welcome " + name + "! This is a simple text adventure game"); sleep(1.5)
print("Type in N/S/E/W when promted to move around the board"); sleep(1.5)
print("Type l to examine the room"); sleep(1.5)
print("Try to find your way out of the cave to win!\n Let's get started");sleep(1.5)

player = Player(name)

while player.alive:

    print("Enter a direction to go N/S/E/W, or enter L/l to examine the room")

    choice = input()

    if choice == 'l' or choice == 'L':
        examine()
    else:
        player.move(choice)

    num = random.randint(0, 100)

    if num % 9 == 0:
        enemy = Enemy()
        battle()
    else:
        pass

    if board[player.x][player.y] == 2:
        print("Congratulations! You made it to the end!")
        break