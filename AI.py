from Gameboard import *
import copy
''' Minimax algorithm (tree-recursive)
Base case: winning board
Recursive case: board with many options
AI player only for classic boards at this point
'''
minimax_dict = {1: max, 0: min}

# AI player will be 'O' for testing purposes.
plyr = {1: 'O', 0: 'X'}

def is_winning_board(board):
    '''Checks if a board is an end state.
    '''
    return board.winner is not None

def measure_of_advantage(board):
    '''Takes an end state board and assigns a value of 0 for a tied board,
    1 for which the maximizer wins, and -1 for which a maximizer loses (or a
    minimizer wins).
    '''
    assert is_winning_board(board), "Not an end state!"
    if board.winner == 'T':
        return 0
    elif board.winner == plyr[1]:
        return 1
    else:
        return -1

def possible_moves(board, player):
    '''Takes a non-end state board and returns a dictionary of all possible
    moves mapped to the board that results from making the move.
    '''
    moves_dict = {}
    for i in range(3):
        for j in range(3):
            if board[i,j] == '-':
                moves_dict[(i, j)] = copy.deepcopy(board).change(i,j, plyr[player])
    return moves_dict

def minimax(board, player=1,):
    '''Takes a board and returns the best move for the player, as well as a
    dictionary of all possible moves mapped to how favorable they are.'''
    pass
