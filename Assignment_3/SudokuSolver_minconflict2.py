import numpy as np
from Sudoku import Sudoku
import math
import random
import copy

def is_valid_state (state) :
    for row in range (state.shape[0]) :
        for column in range (state.shape[1]) :
            if state[row][column] == 0 :
                continue

            if state[row][column] > 9 or state[row][column] < 0 :
                return False

            for i in range (state.shape[0]) :
                if state[i][column] == state[row][column] and i != row:
                    return False

            for j in range (state.shape[1]) :
                if state[row][j] == state[row][column] and j != column:
                    return False

            for i in range (3 * (row // 3), 3 * (row // 3) + 3) :
                for j in range (3 * (column // 3), 3 * (column // 3) + 3) :
                    if state[row][column] == state[i][j] and not (i == row and j == column):
                        return False

    return True

def random_board (initial_board) :
    board = np.zeros ((9, 9), dtype=int)

    for i in range (initial_board.shape[0]) :
        for j in range (initial_board.shape[1]) :
            if initial_board[i, j] == 0 :
                board[i, j] = np.random.randint (1, initial_board.shape[0] + 1)
            else :
                board[i, j] = initial_board[i, j]

    return board

def value (board) :
    score = 0

    for row in range (board.shape[0]) :
        for column in range (board.shape[1]) :
            if board[row][column] == 0 :
                return -1000

            if board[row][column] > 9 or board[row][column] < 0 :
                return -1000

            for i in range (board.shape[0]) :
                if board[i][column] == board[row][column] and i != row:
                    score += -1

            for j in range (board.shape[1]) :
                if board[row][j] == board[row][column] and j != column:
                    score += -1

            for i in range (3 * (row // 3), 3 * (row // 3) + 3) :
                for j in range (3 * (column // 3), 3 * (column // 3) + 3) :
                    if board[row][column] == board[i][j] and not (i == row and j == column):
                        score += -1

    return score

def board_clashes (board) :
    clashes = np.zeros (board.shape)

    for row in range (board.shape[0]) :
        for column in range (board.shape[1]) :
            if board[row][column] == 0 :
                continue

            if board[row][column] > 9 or board[row][column] < 0 :
                continue

            for i in range (board.shape[0]) :
                if board[i][column] == board[row][column] and i != row:
                    clashes[row, column] += 2

            for j in range (board.shape[1]) :
                if board[row][j] == board[row][column] and j != column:
                    clashes[row, column] += 2

            for i in range (3 * (row // 3), 3 * (row // 3) + 3) :
                for j in range (3 * (column // 3), 3 * (column // 3) + 3) :
                    if board[row][column] == board[i][j] and not (i == row and j == column):
                        clashes[row, column] += 2

    return clashes

def point_clashes (board, row, column) :
    clashes = 0
    
    for i in range (board.shape[0]) :
        if board[i][column] == board[row][column] and i != row:
            clashes += 2

    for j in range (board.shape[1]) :
        if board[row][j] == board[row][column] and j != column:
            clashes += 2

    for i in range (3 * (row // 3), 3 * (row // 3) + 3) :
        for j in range (3 * (column // 3), 3 * (column // 3) + 3) :
            if board[row][column] == board[i][j] and not (i == row and j == column):
                clashes += 2

    return clashes

def goal_test (board) :
    score = value (board) 
    if score == 0 :
        return True
    else :
        return False

def same_states (boardA, boardB) :
    for i in range (boardA.shape[0]) :
        for j in range (boardB.shape[1]) :
            if boardA[i, j] != boardB[i, j] :
                return False

    return True

if __name__ == '__main__' :
    starting_state = np.zeros ((9, 9), dtype=int)

    file = open ("input.txt", "r")
    for i, line in enumerate (file.readlines()) :
        starting_state[i, :] = np.array (list (map (int, line.split(" "))))

    if not is_valid_state (starting_state) :
        print ("NOT POSSIBLE")
        exit()

    variables = []

    for i in range (starting_state.shape[0]) :
        for j in range (starting_state.shape[1]) :
            if starting_state[i, j] == 0 :
                variables.append((i, j))

    MAXIMUM_ITERATIONS = 1000
    TOTAL_STATES = 5

    states = [random_board (starting_state) for i in range(TOTAL_STATES)]
    previous_states = [random_board (starting_state) for i in range (TOTAL_STATES)]

    for iteration in range (MAXIMUM_ITERATIONS) :
        print ([value(states[i]) for i in range(TOTAL_STATES)])
        for i in range (TOTAL_STATES) :
            if goal_test (states[i]) :
                print (states[i])
                exit()

            position = variables[np.random.randint(0, len(variables))]
            
            best_state = copy.deepcopy (states[i])
            best_state_value = value (states[i])
            for num in range(1, 10) :
                states[i][position] = num
                new_value = value(states[i])
                if best_state_value < new_value :
                    best_state = copy.deepcopy (states[i])
                    best_state_value = new_value
            
            states[i] = best_state

            if same_states (states[i], previous_states[i]) :
                states[i][position] = np.random.randint(1, 10)

            previous_states[i] = copy.deepcopy (states[i])