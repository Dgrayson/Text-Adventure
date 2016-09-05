__author__ = 'dgrayson'

import random
import Player
import Enemy
import Room
from time import sleep

def battle():

    print(enemy.name + " has appeared!")

    while player.alive and enemy.alive:

        print("\nPlayer HP: " + str(player.currHP) + " Player MP: " + str(player.currMP) + "\nEnemy HP: " + str(enemy.hp))

        num = player.turn(enemy)

        if enemy.alive == False or num == -1:
            break

        enemy.turn(player)

def printText():

    if player.x == 0 and player.y == 0:
        print(name + " wakes up in a strange place."); #sleep(1)
        print("During your travels the ground collapsed beneath your feet "
              "and you seem to have fallen into a cave.\n"); #sleep(1)

def examine():
    print("Examine")

print("What is your name?")

name = input()
board = Room.Board()

board.createBoard()

print("Welcome " + name + "! This is a simple text adventure game"); sleep(1.5)
print("Type in N/S/E/W when promted to move around the board");sleep(1.5)
print("Type l to examine the room"); sleep(1.5)
print("Try to find your way out of the cave to win!\nLet's get started\n\n*********\n\n");sleep(1.5)

player = Player.Player(name)

printText()

while player.alive:

    board.printText(player)

    print("Enter a direction to go N/S/E/W, or enter L/l to examine the room")

    choice = input()

    if choice == 'l' or choice == 'L':
        board.printBoard(player)
    else:
        player.move(choice)

    num = random.randint(0, 100)

    if board.board[player.x][player.y] == 4:
        enemy = Enemy.Dragon()

        print("You've made it to the end of the cave, but a dragon stands in your way!"); sleep(1)
        battle()

        if player.alive:
            print("Congratulations! You made it to the end!")
        else:
            print("You have been defeated")
        break
    elif num % 9 == 0:

        num = random.randint(0,2)

        if num == 0:
            enemy = Enemy.Skeleton()
        elif num == 1:
            enemy = Enemy.Bat()
        elif num == 2:
            enemy = Enemy.Skeleton()

        battle()
    else:
        pass
