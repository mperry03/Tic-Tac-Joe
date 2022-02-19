from abc import ABC, abstractmethod


def instantiate_board(depth):
    if depth == 0:
        return BaseBoard(depth)
    else:
        return RecursiveBoard(depth)


class Board(ABC):
    SYMBOLS = ('_', 'X', 'O')
    PLAYERS = ('X', 'O')
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

    @abstractmethod
    def __init__(self, depth: int):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_board_state(self):
        pass

    @abstractmethod
    def is_valid_move(self, coords):
        pass

    @abstractmethod
    def make_move(self, coords, player):
        pass


class BaseBoard(Board):

    def __init__(self, depth: int):
        self.depth = depth
        self.board_states = ['_'] * 9

    def __str__(self):
        return "".join(self.board_states)

    def get_board_state(self):
        for player in self.PLAYERS:
            for pattern in self.WIN_PATTERNS:
                if self.board_states[pattern[0]] == self.board_states[pattern[1]] == self.board_states[pattern[2]] == player:
                    return player
        return '_'

    """
    coords is an array of numbers 0-8 representing coordinates in different layers
    coords[0] is the coordinate on the smallest board, coords[1] is the layer up from that, etc.
    """
    def is_valid_move(self, coords):
        return self.board_states[coords[0]] == '-'

    """
    player is 'X' or 'O'
    """
    def make_move(self, coords, player):
        if not self.is_valid_move(coords):
            return False
        self.board_states[coords[0]] = player
        return True

class RecursiveBoard(Board):

    def __init__(self, depth: int):
        self.depth = depth
        self.board_states = ['_'] * 9
        self.valid_boards = [True] * 9

        self.boards = []
        for _ in range(9):
            self.boards.append(instantiate_board(depth - 1))

    def __str__(self):
        return ('|' * self.depth).join([str(board) for board in self.boards])

    def get_board_state(self):
        # Update the states of the subboards first
        for i in range(9):
            self.board_states[i] = self.boards[i].get_board_state()

        for player in self.PLAYERS:
            for pattern in self.WIN_PATTERNS:
                if self.board_states[pattern[0]] == self.board_states[pattern[1]] == self.board_states[pattern[2]] == player:
                    return player
        return '_'

    def is_valid_move(self, coords):
        # Check that:
        # State of desired subboard is not won
        # The move is valid within the subboard
        # This is a legal subboard to move to (based on previous moves)
        return self.board_states[coords[-1]] == '-' \
               and self.boards[coords[-1]].is_valid_move() \
               and self.valid_boards[coords[-1]]


T = instantiate_board(1)
print(T)
