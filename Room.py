i__author__ = 'dgrayson'

import random
from Player import Player
import Items
from time import sleep

class Board:

    def __init__(self):

        self.board = [[0 for x in range(5)] for x in range(5)]

    def createBoard(self):

        i = 0
        j = 0


        while i < 5:
            j = 0
            while j < 5:
                self.board[i][j] = random.randint(0,2)
                j += 1
            i += 1

        i = random.randint(0,3)
        j = random.randint(0,3)

        self.board[i][j] = 4

        if i != 0:
            self.board[i-1][j] = 3
        if i != 4:
            self.board[i+1][j] = 3
        if j != 0:
            self.board[i][j-1] = 3
        if j != 4:
            self.board[i][j+1] = 3


    def printBoard(self, player):

        i = 4
        j = 0

        while i >= 0:
            j = 0
            while j < 5:

                if j == 0:
                    if i == player.x and j == player.y:
                        print('*' + " |", end = ' ')
                    else:
                        print(str(self.board[i][j]) + " |", end = ' ')
                else:
                    if i == player.x and j == player.y:
                        print('* |', end = ' ')
                    else:
                        print(str(self.board[i][j]) + " |", end = ' '),
                j += 1

            print('\n------------------')

            i -= 1

    def printText(self, player):

        if self.board[player.x][player.y] == 0:
            print("There is nothing of interest in the room")
        elif self.board[player.x][player.y] == 1:
            print("This is a room of recovery! 20HP and 10MP recovered")

            player.currHP += 20
            player.currMP += 10

            if player.currHP > player.maxHP:
                player.currHP = player.maxHP

            if player.currMP > player.maxMP:
                player.currMP = player.maxMP

            #set room to zero to avoid repeateing the effect
            self.board[player.x][player.y] = 0

        elif self.board[player.x][player.y] == 2:
            print("You see a chest in the room. Open it? Y/N")

            choice = str(input())

            if choice == 'y' or choice == 'Y':

                print("You open the chest"); sleep(1)

                chance = random.randint(0,2)

                if chance == 0:
                    print("You got a potion!")
                    print("\n\n*********\n\n")
                    item = Items.Potion()
                    player.addToInventory(item)
                elif chance == 1:
                    print("You got an Ether")
                    print("\n\n*********\n\n");sleep(1)
                    item = Items.Ether()
                    player.addToInventory(item)
                else:
                    print("Its a trap!");sleep(1)
                    print("10HP lost!")
                    print("\n\n*********\n\n");sleep(1)
                    player.currHP -= 10

            # Set room to 0 to prevent repeating the effect
            self.board[player.x][player.y] = 0



        elif self.board[player.x][player.y] == 3:
            print("You see a light from one of the doorways. The exit is near!")