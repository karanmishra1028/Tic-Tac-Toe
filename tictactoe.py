# board display
from IPython.display import clear_output

test_board = [' '] * 10



def board_display(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


board_display(test_board)

from IPython.display import clear_output


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, please select your input X or O: ').upper()
        if marker != 'X' and marker != 'O':
            print('Please enter a valid marker!')

    player1 = marker
    if player1 == 'O':
        return ('O', 'X')
    else:
        return ('X', 'O')


def place_marker(board, marker, position):
    board[position] = marker


def board_win(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


import random


def first_player():
    if random.randint(0, 1) == 1:
        return 'Player 2'
    else:
        return 'Player 1'


def free_position(board, position):
    return board[position] == ' '


def fullboard_check(board):
    for i in range(1, 10):
        if free_position(board, i):
            return False
    return True


def board_fill(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not free_position(board, position):
        position = int(input('Please select your next move position: '))

    return position


def play_again():
    replay = input('Would you like to play again? ')

    if replay.lower()[0] == 'y':
        return replay


print('Welcome to Tic TacToe!')

while True:
    test_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = first_player()
    print(turn + ' will go first!')
    play_game = input('Are you ready to play? ')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        break

    while game_on:
        if turn == 'Player 1':
            board_display(test_board)
            position = board_fill(test_board)
            place_marker(test_board, player1_marker, position)

            if board_win(test_board, player1_marker):
                board_display(test_board)
                print('Congratulations! You won Player 1!')
                game_on = False
            else:
                if fullboard_check(test_board):
                    board_display(test_board)
                    print("Awww shucks! It's a draw!")
                    break
                else:
                    turn = 'Player 2'

        else:
            board_display(test_board)
            position = board_fill(test_board)
            place_marker(test_board, player2_marker, position)

            if board_win(test_board, player2_marker):
                board_display(test_board)
                print('Congratulations! You won Player 2!')
                game_on = False
            else:
                if fullboard_check(test_board):
                    board_display(test_board)
                    print("Awww shucks! It's a draw!")
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break
