import numpy as np
import copy

class Variable (object) :
    def __init__(self, position, domain) :
        self.position = position
        self.domain = domain
    
    def remove_domain (self, num) :
        try : 
            self.domain.remove (num)
        except :
            pass

def update_constraints (state, variables) :
    for row in range(state.shape[0]) :
        for column in range (state.shape[1]) :
            if state[row][column] == 0 :
                continue

            for i in range (state.shape[0]) :
                if variables[i][column] == None :
                    continue

                variables[i][column].remove_domain (state[row][column])

            for j in range (state.shape[1]) :
                if variables[row][j] == None :
                    continue

                variables[row][j].remove_domain (state[row][column])

            for i in range (3 * (row // 3), 3 * (row // 3) + 3) :
                for j in range (3 * (column // 3), 3 * (column // 3) + 3) :
                    if variables[i][j] == None :
                        continue

                    variables[i][j].remove_domain (state[row][column])

def count_variables (variables) :
    count = 0
    for i in range (len (variables)) :
        for j in range (len (variables[i])) :
            if variables[i][j] != None :
                count += 1

    return count

def select_variable (variables) :
    best_variable_position = None
    minimum_domain_values = None

    for i in range (len (variables)) :
        for j in range (len (variables[i])) :
            if variables[i][j] == None :
                continue

            if minimum_domain_values == None or minimum_domain_values > len (variables[i][j].domain) :
                minimum_domain_values = len (variables[i][j].domain)
                best_variable_position = (i, j)

    return best_variable_position

def valid_variables (variables) :
    for i in range (len (variables)) :
        for j in range (len (variables[i])) :
            if variables[i][j] == None :
                continue
            if len (variables[i][j].domain) == 0 :
                return False

    return True

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

def backtrack (state, variables) :
    if count_variables (variables) == 0 :
        return state

    var_postion = select_variable (variables) 

    for value in variables[var_postion[0]][var_postion[1]].domain :
        new_variables = copy.deepcopy (variables)
        new_state = copy.deepcopy (state)

        new_state[var_postion[0]][var_postion[1]] = value
        new_variables[var_postion[0]][var_postion[1]] = None

        update_constraints (new_state, new_variables)

        if valid_variables (new_variables) :
            solution_state = backtrack (new_state, new_variables)
            if solution_state is None :
                continue
            elif is_valid_state (solution_state) :
                return solution_state

if __name__ == '__main__' :
    starting_state = np.zeros ((9, 9), dtype=int)

    file = open ("input.txt", "r")
    for i, line in enumerate (file.readlines()) :
        starting_state[i, :] = np.array (list (map (int, line.split(" "))))

    if not is_valid_state (starting_state) :
        print ("NOT POSSIBLE")
        exit()

    variables = [[None for i in range(9)] for j in range (9)]

    for i in range (starting_state.shape[0]) :
        for j in range (starting_state.shape[1]) :
            if starting_state[i, j] == 0 :
                variables[i][j] = (Variable ((i, j), [1, 2, 3, 4, 5, 6, 7, 8, 9]))
        
    update_constraints (starting_state, variables)
    solution_state = backtrack (starting_state, variables)

    print (solution_state)