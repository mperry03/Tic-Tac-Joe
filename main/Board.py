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
    def is_valid_move(self, coords):
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
    def is_valid_move(self, coords):
        return self.board_states[coords[-1]] == '_'

    def make_move(self, coords, player):
        if not self.is_valid_move(coords) or self.state != '_':
            return False

        self.board_states[coords[-1]] = player

        # Check for ties or wins
        self.move_count += 1
        self.update_board_state()

        return True

    def get_state(self):
        return self.state


class RecursiveBoard(Board):

    def __init__(self, depth: int):
        self.depth = depth
        self.board_states = ['_'] * 9
        self.valid_boards = [True] * 9
        self.state = '_'

        self.boards = []
        for _ in range(9):
            self.boards.append(instantiate_board(depth - 1))

    def __str__(self):
        return ('\n' * self.depth).join([str(board) for board in self.boards])

    def update_board_state(self):
        # Update the states of the subboards first
        for i in range(9):
            self.boards[i].update_board_state()
            self.board_states[i] = self.boards[i].get_state()

        for player in self.PLAYERS:
            for pattern in self.WIN_PATTERNS:
                if self.board_states[pattern[0]] == self.board_states[pattern[1]] == self.board_states[pattern[2]] == player:
                    self.state = player
        flag = True
        for state in self.board_states:
            if state == '_':
                flag = False
        if flag:
            self.state = 'T'

    def is_valid_move(self, coords):
        # Check that:
        # The move is valid within the subboard
        # This is a legal subboard to move to (based on previous moves)
        return self.boards[coords[-1]].is_valid_move(coords[:-1]) \
               and self.valid_boards[coords[-1]]

    """
    Returns if the requested move was successful (i.e. was it valid)
    """
    def make_move(self, coords, player):
        if not self.is_valid_move(coords) or self.state != '_':
            return False

        # Make the move
        if not self.boards[coords[-1]].make_move(coords[:-1], player):
            return False

        # Check for ties or wins
        self.update_board_state()
        print(self.board_states)

        # Update valid boards
        if self.boards[coords[-2]].get_state() == '_':
            self.valid_boards = [False] * 9
            self.valid_boards[coords[-2]] = True
        else:
            for i in range(9):
                self.valid_boards[i] = self.boards[i].get_state() == '_'
        print(self.valid_boards)

        return True

    def get_state(self):
        return self.state

    def get_valid_boards(self):
        return self.valid_boards


T = instantiate_board(1)
print(T)
print()


print(T.make_move([0, 4], 'X'))
print(T.get_state())
print(T)
print()

print(T.make_move([4, 0], 'O'))
print(T.get_state())
print(T)
print()

print(T.make_move([1, 4], 'X'))
print(T.get_state())
print(T)
print()

print(T.make_move([4, 1], 'O'))
print(T.get_state())
print(T)
print()


print(T.make_move([2, 4], 'X'))
print(T.get_state())
print(T)
print()


print(T.make_move([4, 2], 'O'))
print(T.get_state())
print(T)
print()

print(T.make_move([0, 0], 'X'))
print(T.get_state())
print(T)
print()


print(T.make_move([2, 0], 'O'))
print(T.get_state())
print(T)
print()


print(T.make_move([0, 2], 'X'))
print(T.get_state())
print(T)
print()


print(T.make_move([6, 0], 'O'))
print(T.get_state())
print(T)
print()


print(T.make_move([0, 6], 'X'))
print(T.get_state())
print(T)
print()


print(T.make_move([3, 1], 'O'))
print(T.get_state())
print(T)
print()


print(T.make_move([0, 3], 'X'))
print(T.get_state())
print(T)
print()

print(T.make_move([5, 1], 'O'))
print(T.get_state())
print(T)
print()

print(T.make_move([1, 5], 'X'))
print(T.get_state())
print(T)
print()


print(T.make_move([3, 2], 'O'))
print(T.get_state())
print(T)
print()


print(T.make_move([1, 3], 'X'))
print(T.get_state())
print(T)
print()


print(T.make_move([5, 2], 'O'))
print(T.get_state())
print(T)
print()

print(T.make_move([5, 2], 'O'))
print(T.get_state())
print(T)
print()
