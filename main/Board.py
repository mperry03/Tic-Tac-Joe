from abc import ABC, abstractmethod


def instantiate_board(depth):
    if depth == 0:
        return BaseBoard(depth)
    else:
        return RecursiveBoard(depth)


class Board(ABC):
    WIN_PATTERNS = [
        ([0, 0], [0, 1], [0, 2]),
        ([1, 0], [1, 1], [1, 2]),
        ([2, 0], [2, 1], [2, 2]),
        ([0, 0], [1, 0], [2, 0]),
        ([0, 1], [1, 1], [2, 1]),
        ([0, 2], [1, 2], [2, 2]),
        ([0, 0], [1, 1], [2, 2]),
        ([0, 2], [1, 1], [2, 0]),
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


class BaseBoard(Board):

    def __init__(self, depth: int):
        self.boards = (['_'] * 9, [None] * 9)

    def __str__(self):
        return "".join(self.boards[0])


class RecursiveBoard(Board):

    def __init__(self, depth: int):
        self.boards = (['_'] * 9, [])
        for _ in range(9):
            self.boards[1].append(instantiate_board(depth - 1))

    def __str__(self):
        return "|".join([str(board) for board in self.boards[1]])


T = instantiate_board(1);
print(T)
