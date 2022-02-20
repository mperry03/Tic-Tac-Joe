from main.Board import *
#import math
import random
#import time


def instantiate_AI():
    return AI()

class AI():

    def __init__(self):
        self.state = True

    def setState(self, state):
        self.state = state

    def chooseMove(self,board):
        if self.state == True:
            possibleMoves = []
            for i in range(9):
                for j in range(9):
                    if board.is_valid_move([i,j]):
                        possibleMoves.append([i,j])
            return random.choice(possibleMoves)


