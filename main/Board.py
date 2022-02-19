from abc import ABC, abstractmethod


def instantiate_board(depth):
    if depth == 0:
        return BaseBoard(depth)
    else:
        return RecursiveBoard(depth)


class Board(ABC):
    WIN_PATTERNS = "test" #TODO

    @abstractmethod
    def __init__(self, depth: int):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod


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
