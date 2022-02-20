from main.Board import *
#import math
import random
#import time


def instantiate_AI():
    return AI()

class AI():

    def chooseMove(self,board):
        possibleMoves = []
        for i in range(9):
            for j in range(9):
                if board.is_valid_move([i,j]):
                    possibleMoves.append([i,j])
        return random.choice(possibleMoves)


