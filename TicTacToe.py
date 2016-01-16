from Gameboard import *
import AI
import re
import os

plyr = {1: 'X', 2: 'O'}

################################# Functions ###################################

def try_loop(prompt, *args):
    while True:
        try:
            prompt(args)
            break
        except AssertionError as e:
            print(e)

def prompt_for_board(nil):
    print("Player " + str(player) + ", please choose the board you would like to play on.")
    response = input("Enter a number 0 - 2, followed by another number 0 - 2, separated by a space.\n\n")
    assert re.search(r'[0-2] [0-2]', response) is not None, "Invalid input. Please try again."
    x, y = response.split()
    x, y = int(x), int(y)
    assert board[x,y].winner is None, "Board is already won. Please choose another board."
    board.position = (x, y)

def prompt_for_move(nil):
    print("Player " + str(player) + ", please choose a spot.")
    response = input("Enter a number 0 - 2, followed by another number 0 - 2, separated by a space.\n\n")
    assert re.search(r'[0-2] [0-2]', response) is not None, "Invalid input. Please try again."
    x, y = response.split()
    x, y = int(x), int(y)
    board.change(x, y, plyr[player])

def AI_setup(module):
    AI.minimax('reset')
    response = input("Will you go first (X), or second (O)? ")
    assert response == 'X' or response == 'O', "Invalid input, please try again."
    if response == 'X':
        AI.AI_player, AI.minimax_dict = 2, {1: min, 2: max}
    else:
        AI.AI_player, AI.minimax_dict = 1, {1: max, 2: min}

###############################################################################

while True:
    while True:
        try:
            response = input("Welcome to Tic-Tac-Toe! Please type either 'next-gen' or 'classic', without quotes.\n\n")
            assert response == 'next-gen' or response == 'classic'
            break
        except AssertionError:
            print(response + 'is not valid input. Please try again.')

    if response == 'classic':
        while True:
            try:
                AI_plays = input("Play with an AI player? (Y/N) ")
                assert AI_plays == 'Y' or AI_plays == 'N', "Invalid input, please try again."
                break
            except AssertionError as e:
                print(e)

        if AI_plays == 'Y':
            try_loop(AI_setup, AI)

        board, player = Classicboard(), 1
        print(board)

        while board.winner is None:
            if AI_plays == 'Y' and player == AI.AI_player:
                print("\n")
                move = AI.minimax(board, AI.AI_player)[1]
                print(move[0], move[1])
                board.change(move[0], move[1], plyr[AI.AI_player])
            else:
                try_loop(prompt_for_move)

            if board.winner is None:
                print(board)
                player = 3 - player

    elif response == 'next-gen':
        board, player = Bigboard(), 1
        print(board)

        try_loop(prompt_for_board)

        while board.winner is None:
            try_loop(prompt_for_move)

            if board.winner is None:
                print(board)
                player = 3 - player

                if board[board.position].winner is not None:
                    try_loop(prompt_for_board)

    print(board)

    if board.winner != 'T':
        print("Congratulations, player " + str(player) + "!")
    else:
        print("It's a tie!")

    while True:
        try:
            response = input("Play again? (Y/N) ")
            assert response == 'Y' or response == 'N'
            break
        except AssertionError:
            print("Invalid input. Please try again.")

    if response == 'N':
        print('Goodbye!')
        os._exit(-1)
