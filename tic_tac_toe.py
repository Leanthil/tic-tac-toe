import random


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    move = input('Please enter your move: ')

    if 'a' in move.lower():
        row = 0
    elif 'b' in move.lower():
        row = 1
    elif 'c' in move.lower():
        row = 2

    if '1' in move:
        col = 0
    elif '2' in move:
        col = 1
    elif '3' in move:
        col = 2

    if board[row][col] != '.':
        print('That is already taken')
        return get_move(board, player)

    if move.lower() == 'quit':
        print('QUIT')
        exit()

    if move.lower() not in moves:
        print('That is not a valid move!')
        return get_move(board, player)

    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    for i in range(3):
        for j in range(3):
            if board[row][col] == '.':
                board[row][col] = player
    return board


def has_won(board, player):
    """Returns True if player has won the game."""
    if (board[0][0] == board[0][1] == board[0][2] == player or
       board[1][0] == board[1][1] == board[1][2] == player or
       board[2][0] == board[2][1] == board[2][2] == player or
       board[0][0] == board[1][0] == board[2][0] == player or
       board[0][1] == board[1][1] == board[2][1] == player or
       board[0][2] == board[1][2] == board[2][2] == player or
       board[0][0] == board[1][1] == board[2][2] == player or
       board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False


def is_full(board):
    """Returns True if board is full."""
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                count += 1
    if count == 0:
        return True
    else:
        return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    new_board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                new_board[x][y] = '.'
            if board[x][y] == 1:
                new_board[x][y] = 'X'
            if board[x][y] == 2:
                new_board[x][y] = 'O'
    print('''
               1   2   3
            A  {} | {} | {}
              ---+---+---
            B  {} | {} | {}
              ---+---+---
            C  {} | {} | {}
        '''.format(new_board[0][0], new_board[0][1], new_board[0][2],
                   new_board[1][0], new_board[1][1], new_board[1][2],
                   new_board[2][0], new_board[2][1], new_board[2][2]))


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print("It's a tie!")
    if winner == 1:
        print('X won!')
    if winner == 2:
        print('O won!')


def tictactoe_game(mode):
    board = init_board()
    player = 1
    winner = 0
    while not has_won(board, player):
        print_board(board)
        legal_moves = [[x, y] for x, li in enumerate(board) for y, val in enumerate(li) if val == '.']
        if mode == 2 and player == 2:
            board = mark(board, player, random.choice(legal_moves)[0], random.choice(legal_moves)[1])
        else:
            row, col = get_move(board, player)
            board = mark(board, player, row, col)
        if is_full(board):
            break
        if player == 1:
            player = 2
        else:
            player = 1
        if has_won(board, 1):
            winner = 1
            break
        elif has_won(board, 2):
            winner = 2
            break
    print_result(winner)


def main_menu():
    print("\033c")
    print("""  _____ _            _             _       __ _               
 |_   _(_) ___   ___| |_ __ _  ___| | __  / _| | _____      __
   | | | |/ __| / __| __/ _` |/ __| |/ / | |_| |/ _ \ \ /\ / /
   | | | | (__  \__ \ || (_| | (__|   <  |  _| | (_) \ V  V / 
   |_| |_|\___| |___/\__\__,_|\___|_|\_\ |_| |_|\___/ \_/\_/  
                                                              
        Hi! Welcome to a game of Tic - tac - toe!
        1: HUMAN VS HUMAN        2: HUMAN VS AI""")
    mode = int(input("      Please choose a game mode! (1/2): "))
    tictactoe_game(mode)


if __name__ == '__main__':
    main_menu()
