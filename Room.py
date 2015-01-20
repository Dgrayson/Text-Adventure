__author__ = 'dgrayson'

import random
from Player import Player

class Board:

    def __init__(self):

        self.board = [[0 for x in range(5)] for x in range(5)]

    def createBoard(self):

        i = 0
        j = 0


        while i < 5:
            j = 0
            while j < 5:
                self.board[i][j] = random.randint(0,3)
                j += 1
            i += 1

        i = random.randint(0,4)
        j = random.randint(0,4)

        self.board[i][j] = 5

        if i != 0:
            self.board[i-1][j] = 4
        if i != 4:
            self.board[i+1][j] = 4
        if j != 0:
            self.board[i][j-1] = 4
        if j != 4:
            self.board[i][j+1] = 4


    def printBoard(self, player):

        i = 0
        j = 0

        while i < 5:
            j = 0
            while j < 5:

                if j == 4:
                    if i == player.x and j == player.y:
                        print('*')
                    else:
                        print(str(self.board[i][j]))
                else:
                    if i == player.x and j == player.y:
                        print('*', end = ' ')
                    else:
                        print(str(self.board[i][j]) + " |", end = ' '),
                j += 1

            print('------------------')

            i += 1

    def printText(self, player):

        if self.board[player.x][player.y] == 0:
            print("There is nothing of interest in the room")
        elif self.board[player.x][player.y] == 1:
            print("1")
        elif self.board[player.x][player.y] == 2:
            print("2")
        elif self.board[player.x][player.y] == 3:
            print("You see a chest in the room")
        elif self.board[player.x][player.y] == 4:
            print("You see a light from one of the doorways. The exit is near!")