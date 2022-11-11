from random import randint


class Cell:

    def __init__(self, index: int):
        self.index = index
        self.is_free = True
        self.value_cell = None


class Board:

    def __init__(self):
        self.self_board = self.create_board()

    def get_free_sells(self):
        return [cell.index + 1 for cell in self.self_board if cell.is_free]

    @staticmethod
    def create_board():
        return [Cell(index_cell) for index_cell in range(9)]

    def win_game(self, symbol):
        for index in range(0, 9, 3):
            if self.self_board[index].value_cell == symbol and self.self_board[index + 1].value_cell == symbol \
                    and self.self_board[index + 2].value_cell == symbol:
                return True
        for index in range(3):
            if self.self_board[index].value_cell == symbol and self.self_board[index + 3].value_cell == symbol \
                    and self.self_board[index + 6].value_cell == symbol:
                return True
        return (self.self_board[0].value_cell == symbol
                and self.self_board[4].value_cell == symbol
                and self.self_board[8].value_cell == symbol) or (self.self_board[2].value_cell == symbol
                                                                 and self.self_board[4].value_cell == symbol
                                                                 and self.self_board[6].value_cell == symbol)


class Player:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def move(move_index, board):
        if board.self_board[move_index].is_free:
            board.self_board[move_index].value_cell = 'X'
            board.self_board[move_index].is_free = False
            return True
        else:
            print('Клетка занята!')
            return False


class Computer:
    @staticmethod
    def rand_move(board):
        while True:
            rand_index = randint(0, 8)
            if board.self_board[rand_index].is_free:
                board.self_board[rand_index].value_cell = 'O'
                board.self_board[rand_index].is_free = False
                break
