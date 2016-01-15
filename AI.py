from Gameboard import *
import copy
import pickle

plyr = {1: 'X', 2: 'O'}

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
    elif board.winner == plyr[AI_player]:
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
                moves_dict[(i,j)] = copy.deepcopy(board)
                moves_dict[(i,j)].change(i, j, plyr[player])
    return moves_dict

def minimax(board, player):
    '''Takes a board and returns a tuple whose first element is the score of the
    best move and the second element is a tuple that represents the best move.
    '''
    assert is_winning_board(board) is False, "Board is already an end state!"
    moves_dict = {}
    print(board)
    for move, new_board in possible_moves(board, player).items():
        if is_winning_board(new_board):
            moves_dict[move] = measure_of_advantage(new_board)
        else:
            moves_dict[move] = minimax(new_board, 3 - player)[0]
    minimax_score = minimax_dict[player](moves_dict.values())
    for move, score in moves_dict.items():
        if score == minimax_score:
            return score, move

def memoize(f):
    '''Returns a memoized version of minimax.
    '''
    inputs = {}
    def memoized(board, player):
        string = pickle.dumps((board, player), 1)
        if string in inputs.keys():
            return inputs[string]
        else:
            inputs[string] = f(board, player)
            return inputs[string]
    return memoized

minimax = memoize(minimax)
