from main.Board import *
#import math
import random
#import time


def instantiate_AI():
    return AI()

class AI():
    WIN_PATTERNS = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
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

    def get_viable_pairs(self, board):
        state = board.get
