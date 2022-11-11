import tic_tac_toe as game


def gameplay(player: game.Player, computer: game.Computer, base_board: game.Board):
    count_move = 0
    while True:
        try:
            print("Доступые клетки:", base_board.get_free_sells())
            command = int(input("Выберите куда сходить: ")) - 1
        except ValueError:
            print("Некорректные данные!")
        else:
            if not player.move(command, base_board):
                continue
            count_move += 1
            if board.win_game('X'):
                show_game(base_board)
                print("\n{} выиграли!".format(player.name))
                break
            if count_move == 9:
                show_game(base_board)
                print("Ничья!")
                break
            computer.rand_move(base_board)
            show_game(base_board)
            count_move += 1
            if board.win_game('O'):
                print("\nКомпьютер выиграл!")
                break


def show_game(base_board: game.Board):
    cinema = '\n'
    for index in range(9):
        if base_board.self_board[index].value_cell is None:
            cinema += '_'
        else:
            cinema += base_board.self_board[index].value_cell
        if index % 3 == 2:
            cinema += '\n'
    print(cinema)


board = game.Board()
name_player = input("Введите свое имя: ")
user_player = game.Player(name_player)
this_computer = game.Computer()
gameplay(user_player, this_computer, board)
