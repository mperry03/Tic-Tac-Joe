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
            valids = board.get_valid_boards()
            possibleMoves = []
            priorityMoves = []
            subboards = board.get_subboards()
            for i in range(9):
                for j in range(9):
                    if valids[j]:
                        current_board = subboards[j]
                        viable_gaps = [k[1] for k in self.get_viable_pairs(current_board)]
                        if board.is_valid_move([i,j]):
                            possibleMoves.append([i,j])
                            if i in viable_gaps:
                                priorityMoves.append([i, j])


            if len(priorityMoves) > 0:
                print(priorityMoves)
                return random.choice(priorityMoves)
            else:
                return random.choice(possibleMoves)

    def get_viable_pairs(self, board):
        state = board.get_board_states()
        valid_pairs = []

        # A valid pair is a 3-tuple:
        # (winning_combo, gap_coord, player)
        for player in ['X', 'O']:
            for combo in self.WIN_PATTERNS:
                for i in range(3):
                    flag = True
                    for j in range(3):
                        if i == j and state[combo[j]] != '_':
                            flag = False
                        elif state[combo[j]] != player:
                            flag = False
                    if flag:
                        valid_pairs.append([combo, i, player])
        print(valid_pairs)
        return valid_pairs