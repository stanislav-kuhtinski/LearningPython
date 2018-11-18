__author__ = 'stanislav-kuhtinski'

import random


def init_board():
    return [' '] * 10


def choose_first_mover():
    # Randomly choose the player who goes first and his letter
    rnd_symbol = random.choice("X0")
    if random.randint(0, 1) == 0:
        return 'computer', rnd_symbol
    else:
        return 'player', rnd_symbol


def whoes_letter(person, letter):
    # Returns dict with owners of the X and 0
    if person == 'computer' and letter == '0':
        return {'computer': '0', 'player': 'X'}
    elif person == 'player' and letter == 'X':
        return {'player': 'X', 'computer': '0'}
    else:
        return {'computer': 'X', 'player': '0'}


def draw_board(board):
    print(" ", board[7], "|", board[8], "|", board[9])
    print("-------------")
    print(" ", board[4], "|", board[5], "|", board[6])
    print("-------------")
    print(" ", board[1], "|", board[2], "|", board[3])
    print("\n")


def player_move(board, symbol):
    # Determine where to move and return that move.
    # First, check if we can win in the next move

    # Check if the player could win on their next move, and block them.

    # Try to take one of the corners, if they are free.

    # Try to take the center, if it is free.

    # Move on one of the sides.
    input('input player_move ')
    return False


def ai_move(board, symbol):
    print('symbol ', symbol)
    input('input player_move ')
    return False


def check_victory(board):
    win_combinations = [
        (1, 2, 3),  # botton
        (4, 5, 6),  # middle
        (7, 8, 9),  # top
        (1, 4, 7),  # down the left side
        (2, 5, 8),  # down the middle
        (3, 6, 9),  # down the right side
        (1, 5, 9),  # diagonal 1
        (3, 5, 7),  # diagonal 2
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] == board[b] == board[c] != ' ':
            print("Player {0} wins! Congratulations!\n".format(board[a]))
            return True
    if 9 == sum((pos == 'X' or pos == '0') for pos in board):
        print("The game ends in a tie\n")
        return True
    return False


def play_again():
    # Returns True if the player wants to play again
    return input('Would you like to play again (yes or no)? ').lower().startswith('y')


while True:
    # Reset the board
    board = init_board()
    draw_board(board)
    first_mover, symbol = choose_first_mover()
    print('whos_move & symbol: ', first_mover, symbol)
    whois = whoes_letter(first_mover, symbol)
    print(whois)
    print('Whois ', whois.get('computer', None))

    while not check_victory(board):
        if first_mover == 'computer':
            ai_move(board, whois.get('computer', None))
        else:
            player_move(board, symbol)

    if not play_again():
        break
