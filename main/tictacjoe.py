from main.Board import *
#import math
import random
#import time

class AI():

    def instantiate_AI(self):
        return self

    def chooseMove(board):
        possibleMoves = []
        for i in range(9):
            for j in range(9):
                if board.is_valid_move([i,j]):
                    possibleMoves.append([i,j])
        return random.choice(possibleMoves)


