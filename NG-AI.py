from Gameboard import *
import copy, pickle

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

def minimax(board, player):
    '''Takes a board and returns a tuple whose first element is the score of the
    best move and the second element is a tuple that represents the best move.
    '''
    assert board.winner is None, "Board is already an end state!"
    print(board)
    moves_dict = {}
    for move, new_board in possible_moves(board, player).items():
        if is_winning_board(new_board):
            moves_dict[move] = measure_of_advantage(new_board)
        else:
            if position_change(board):
                moves_dict[move] = minimax(new_board, player)[0]
            else:
                moves_dict[move] = minimax(new_board, 3 - player)[0]
    minimax_score = minimax_dict[player](moves_dict.values())
    for move, score in moves_dict.items():
        if score == minimax_score:
            return score, move

def memoize(f):
    '''Returns a memoized version of minimax whose cache can be reset.
    '''
    inputs = {}
    def memoized(*args):
        nonlocal inputs
        if not isinstance(args[0], Bigboard) and args[0] == 'reset':
            inputs = {}
        else:
            string = pickle.dumps((args[0], args[1]), 1)
            if string in inputs.keys():
                return inputs[string]
            else:
                inputs[string] = f(args[0], args[1])
                return inputs[string]
    return memoized, inputs

minimax, inputs = memoize(minimax)
