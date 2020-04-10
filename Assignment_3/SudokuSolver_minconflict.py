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

def exp_schedule(lam=0.02, limit=600):
    return lambda x : math.exp (- x * lam) if (x <= limit ) else 1e-8

if __name__ == '__main__' :
    starting_state = np.zeros ((9, 9), dtype=int)

    file = open ("input.txt", "r")
    for i, line in enumerate (file.readlines()) :
        starting_state[i, :] = np.array (list (map (int, line.split(" "))))

    if not is_valid_state (starting_state) :
        print ("NOT POSSIBLE")
        exit()

    sudoku = Sudoku (starting_state)

    MAXIMUM_ITERATIONS = 200
    TOTAL_STATES = 3
    STORED_STATES = 3

    scheldule = exp_schedule()

    states = [sudoku.initial() for i in range (TOTAL_STATES)]
    previous_states = np.array ([[sudoku.initial() for i in range (TOTAL_STATES)] for j in range (STORED_STATES)])
    
    current_storing_state = 0
    states_value = [sudoku.value(states[i]) for i in range (TOTAL_STATES)]

    for iteration in range (MAXIMUM_ITERATIONS) :
        temp = scheldule(iteration)

        print (states_value)

        best_state = states[states_value.index (max (states_value))]
        best_state_value = max(states_value)

        for i in range (TOTAL_STATES) :
            if np.random.randint (0, 10000) / 10000.0  > temp :
                states[i], states_value[i] = sudoku.best_child(states[i])
                if sudoku.same_states (states[i], previous_states[:, i]) :
                    states[i] = sudoku.random_child (states[i])
                    states_value[i] = sudoku.value (states[i])
                
                previous_states[current_storing_state, i] = copy.deepcopy(states[i])
            else :
                states[i] = sudoku.random_child(states[i])
                states_value[i] = sudoku.value (states[i])

                previous_states[current_storing_state, i] = copy.deepcopy (states[i])

            if sudoku.goal_test (states[i]) :
                print (states_value)
                print (states[i])
                print (sudoku.board_clashes (states[states_value.index (max (states_value))]))
                exit()

        current_storing_state += 1
        if current_storing_state == STORED_STATES :
            current_storing_state = 0

    print (states_value)
    print (states[states_value.index (max (states_value))])

    print (sudoku.board_clashes (states[states_value.index (max (states_value))]))
