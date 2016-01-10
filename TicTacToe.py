from Gameboard import *
import re
import os

plyr = {1: 'O', 2: 'X'}

################################# Functions ###################################

def try_loop(prompt):
    while True:
        try:
            prompt()
            break
        except AssertionError as e:
            print(e)

def prompt_for_board():
    print("Player " + str(player) + ", please choose the board you would like to play on.")
    response = input("Enter a number 0 - 2, followed by another number 0 - 2, separated by a space.\n\n")
    assert re.search(r'[0-2] [0-2]', response) is not None, "Invalid input. Please try again."
    x, y = response.split()
    x, y = int(x), int(y)
    assert board[x,y].winner is None, "Board is already won. Please choose another board."
    board.position = (x, y)

def prompt_for_move():
    print("Player " + str(player) + ", please choose a spot.")
    response = input("Enter a number 0 - 2, followed by another number 0 - 2, separated by a space.\n\n")
    assert re.search(r'[0-2] [0-2]', response) is not None, "Invalid input. Please try again."
    x, y = response.split()
    x, y = int(x), int(y)
    board.change(x, y, plyr[player])

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
        board, player = Classicboard(), 1
        print(board)

        while board.winner is None:
            try_loop(prompt_for_move)

            if board.winner is None:
                print(board)
                player = 3 - player

        print(board)
        print("Congratulations, player " + str(player) + "!")

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
        print("Congratulations, player " + str(player) + "!")

    while True:
        try:
            response = input("Play again? (Y/N)")
            assert response == 'Y' or response == 'N'
            break
        except AssertionError:
            print("Invalid input. Please try again.")

    if response == 'N':
        print('Goodbye!')
        os._exit(-1)
