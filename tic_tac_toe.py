def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 3, 3
    moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    move = input('Please enter your move: ')

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


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
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
    # if winner == 0:
    #     print("It's a tie!")
    if winner == 1:
        print('X won!')
    if winner == 2:
        print('O won!')


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
