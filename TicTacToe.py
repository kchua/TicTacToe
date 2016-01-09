from Gameboard import *
import re

plyr = {1: 'O', 2: 'X'}

while True:
    while True:
        try:
            response = input("Welcome to Tic-Tac-Toe! Please type either 'next-gen' or 'classic'.\n\n")
            assert response == 'next-gen' or response == 'classic', "Invalid response"
            break
        except AssertionError:
            print(response + 'is not valid input. Please try again.')

    if response == 'classic':
        print("This feature has not yet been implemented. Please come back soon! \n")

    elif response == 'next-gen':
        board, player = Bigboard(), 1

        while True:
            try:
                print("Player 1, please choose the board you would like to play on.")
                response = input("Enter a number 0 - 2, followed by another number 0 - 2, separated by a space.")
                assert re.search(r'[1-3] [1-3]', response) is not None, "Invalid input, please try again."
                break
            except AssertionError:
                print("Invalid input. Please try again.")

        x, y = response.split()
        x, y = int(x), int(y)
        b.position = (x, y)
