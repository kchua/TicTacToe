from AI import *
import copy

def position_change(board):
    '''Takes a non-endstate board and returns whether the current player has to
    choose a position.
    '''
    return board.position is None or board[board.position].winner is not None

def possible_moves(board, player):
    '''Takes a non-endstate board and returns all possible moves. If the current
    position is None or a completed mini-board, then the function returns all
    possible positions.
    '''
    moves_dict = {}
    if position_change(board):
        for i in range(3):
            for j in range(3):
                if board[i,j].winner is None:
                    moves_dict[(i,j)] = copy.deepcopy(board)
                    moves_dict[(i,j)].position = (i,j)
    else:
        for i in range(3):
            for j in range(3):
                if board[board.position][i,j] == '-':
                    moves_dict[(i,j)] = copy.deepcopy(board)
                    moves_dict[(i,j)].change(i, j, plyr[player])
    return moves_dict
