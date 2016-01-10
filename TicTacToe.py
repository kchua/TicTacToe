from Gameboard import *
import re
import os

plyr = {1: 'O', 2: 'X'}

while True:
    while True:
        try:
            response = input("Welcome to Tic-Tac-Toe! Please type either 'next-gen' or 'classic', without quotes.\n\n")
            assert response == 'next-gen' or response == 'classic'
            break
        except AssertionError:
            print(response + 'is not valid input. Please try again.')

    if response == 'classic':
        pass

    elif response == 'next-gen':
        board, player = Bigboard(), 1
        print(board)

        while True:
            try:
                print("Player 1, please choose the board you would like to play on.")
                response = input("Enter a number 0 - 2, followed by another number 0 - 2, separated by a space.\n\n")
                assert re.search(r'[0-2] [0-2]', response) is not None
                break
            except AssertionError:
                print("Invalid input. Please try again.")

        x, y = response.split()
        x, y = int(x), int(y)
        board.position = (x, y)

        while board.winner is None:
            while True:
                try:
                    print("Player " + str(player) + ", please choose a spot.")
                    response = input("Enter a number 0 - 2, followed by another number 0 - 2, separated by a space.\n\n")
                    assert re.search(r'[0-2] [0-2]', response) is not None, "Invalid input. Please try again."
                    x, y = response.split()
                    x, y = int(x), int(y)
                    board.change(x, y, plyr[player])
                    break
                except AssertionError as e:
                    print(e)

            if board.winner is None:
                print(board)
                player = 3 - player

                if board[board.position].winner is not None:
                    while True:
                        try:
                            print("Player " + str(player) + ", please choose the board you would like to play on.")
                            response = input("Enter a number 0 - 2, followed by another number 0 - 2, separated by a space.\n\n")
                            assert re.search(r'[0-2] [0-2]', response) is not None, "Invalid input. Please try again."
                            x, y = response.split()
                            x, y = int(x), int(y)
                            assert board[x,y].winner is None, "Board is already won. Please choose another board."
                            board.position = (x, y)
                            break
                        except AssertionError as e:
                            print(e)

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
