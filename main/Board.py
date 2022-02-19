from abc import ABC, abstractmethod


def instantiate_board(depth):
    if depth == 0:
        return BaseBoard(depth)
    else:
        return RecursiveBoard(depth)


class Board(ABC):
    SYMBOLS = ('_', 'X', 'O', 'T')
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
    def update_board_state(self):
        pass

    @abstractmethod
    def is_valid_move(self, coords, player):
        pass

    @abstractmethod
    def make_move(self, coords, player):
        pass

    @abstractmethod
    def get_state(self):
        pass


class BaseBoard(Board):

    def __init__(self, depth: int):
        self.depth = depth
        self.board_states = ['_'] * 9
        self.move_count = 0
        self.turn = 'X'
        self.state = '_'

    def __str__(self):
        return "".join(self.board_states)

    def update_board_state(self):
        for player in self.PLAYERS:
            for pattern in self.WIN_PATTERNS:
                if self.board_states[pattern[0]] == self.board_states[pattern[1]] == self.board_states[pattern[2]] == player:
                    self.state = player
        if self.move_count == 9:
            self.state = 'T'

    """
    coords is an array of numbers 0-8 representing coordinates in different layers
    coords[0] is the coordinate on the smallest board, coords[1] is the layer up from that, etc.
    """
    def is_valid_move(self, coords, player):
        return self.board_states[coords[0]] == '_' and player == self.turn

    """
    player is 'X' or 'O'
    """
    def make_move(self, coords, player):
        if not self.is_valid_move(coords, player) or self.state != '_':
            return False

        self.board_states[coords[0]] = player

        # Check for ties or wins
        self.move_count += 1
        self.update_board_state()

        # Switch turn
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

        return True

    def get_state(self):
        return self.state


class RecursiveBoard(Board):

    def __init__(self, depth: int):
        self.depth = depth
        self.board_states = ['_'] * 9
        self.valid_boards = [True] * 9
        self.move_count = 0
        self.tied = False
        self.turn = 'X'

        self.boards = []
        for _ in range(9):
            self.boards.append(instantiate_board(depth - 1))

    def __str__(self):
        return ('\n' * self.depth).join([str(board) for board in self.boards])

    def update_board_state(self):
        # Update the states of the subboards first
        for i in range(9):
            self.board_states[i] = self.boards[i].update_board_state()

        for player in self.PLAYERS:
            for pattern in self.WIN_PATTERNS:
                if self.board_states[pattern[0]] == self.board_states[pattern[1]] == self.board_states[pattern[2]] == player:
                    return player
        return '_'

    def is_valid_move(self, coords, player):
        # Check that:
        # State of desired subboard is not won
        # The move is valid within the subboard
        # This is a legal subboard to move to (based on previous moves)
        # It is this player's turn
        return self.board_states[coords[-1]] == '-' \
               and self.boards[coords[-1]].is_valid_move(coords[:-1]) \
               and self.valid_boards[coords[-1]] \
               and player == self.turn

    """
    Returns if the requested move was successful (i.e. was it valid)
    """
    def make_move(self, coords, player):
        if not self.is_valid_move(coords, player):
            return False

        current_coord = coords[-1]
        current_subboard = self.boards[current_coord]
        current_subboard.make_move(coords[:-1], player)

        # Check for ties
        self.move_count += 1
        if self.move_count == 9:
            self.tied = True

        # Update subboard states
        self.board_states = [board.update_board_state() for board in self.boards]

        # Switch turn
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

        # Update valid subboards for the next move
        if not current_subboard.tied and self.board_states[current_coord] == '_':
            self.valid_boards = [False] * 9
            self.valid_boards[current_coord] = True
        else:
            self.valid_boards = [True] * 9
        return True


T = instantiate_board(0)
print(T)
print()

print(T.make_move([0], 'X'))
print(T.get_state())
print(T)
print()

print(T.make_move([1], 'O'))
print(T.get_state())
print(T)
print()

print(T.make_move([2], 'X'))
print(T.get_state())
print(T)
print()

print(T.make_move([3], 'O'))
print(T.get_state())
print(T)
print()

print(T.make_move([4], 'X'))
print(T.get_state())
print(T)
print()

print(T.make_move([6], 'O'))
print(T.get_state())
print(T)
print()

print(T.make_move([5], 'X'))
print(T.get_state())
print(T)
print()

print(T.make_move([8], 'O'))
print(T.get_state())
print(T)
print()

print(T.make_move([7], 'X'))
print(T.get_state())
print(T)
print()

print(T.make_move([7], 'X'))
print(T.get_state())
print(T)
print()
