"""
Tic Tac Toe Player
"""

import math
import copy
from util import Node, StackFrontier, QueueFrontier

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_X = 0
    number_of_O = 0
    number_of_EMPTY = 0

    for row in board:
        for position in row:
            if position == X:
                number_of_X += 1
            elif position == O:
                number_of_O += 1
            else:
                number_of_EMPTY += 1

    if number_of_EMPTY == 9 or number_of_X == number_of_O:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions: list[tuple[int, int]] = []

    for row in range(len(board)):
        for position in range(len(board[row])):
            if board[row][position] == EMPTY:
                actions.append((row, position))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    else:
        raise Exception("Move is not allowed!")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    number_of_EMPTY = 0

    for row in board:
        for position in row:
            if position == EMPTY:
                number_of_EMPTY += 1

    if number_of_EMPTY == 0:
        return True

    if winner(board) is None:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        player_that_won = winner(board)
        if player_that_won == X:
            return 1
        elif player_that_won == O:
            return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move: tuple[int, int] = None

    for action in actions(board):
        current_min_value, _ = min_value(result(board, action))

        if current_min_value > v:
            v = current_min_value
            move = action
            if v == 1:
                return v, move
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move: tuple[int, int] = None

    for action in actions(board):
        current_max_value, _ = max_value(result(board, action))

        if current_max_value < v:
            v = current_max_value
            move = action
            if v == -1:
                return v, move
    return v, move

# if __name__ == "__main__":
#     board = initial_state()
#     plr = player(board)
#     print(f"Player: {plr}")
#     available_actions = actions(board)
#     print(f"Actions: {available_actions}")
#     updated_board1 = result(board, available_actions[0])
#     updated_board2 = result(updated_board1, available_actions[3])
#     updated_board3 = result(updated_board2, available_actions[2])
#     updated_board4 = result(updated_board3, available_actions[5])
#     updated_board5 = result(updated_board4, available_actions[1])
#     print(updated_board5)
#     temp_res = winner(updated_board5)
#     print(f"Winner: {temp_res}")
#
#     game_finished = terminal(updated_board5)
#     print(f"Terminal: {game_finished}")
#     util = utility(updated_board5)
#     print(f"Utility: {util}")
#     # minimax(updated_board1)
#     val = max_value(updated_board1)
#     print(f"Max Value: {val}")