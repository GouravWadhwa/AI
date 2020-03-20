import random
from NQueens import NQueensSearch
from hill_climbing import hill_climbing

def GA(problem):
    POPULATION_SIZE = 100
    CROSSOVER_PROBABILITY = 0.6
    MUTATION_PROBABILITY = 0.09
    ELITISM = 0.2
    MAXIMUM_ITERATIONS = 1000

    states = [problem.initial() for i in range (POPULATION_SIZE)]
    states_value = [problem.value(state) for state in states]

    for i in range (MAXIMUM_ITERATIONS) :
        probs = [state_value / sum (states_value) for state_value in states_value]
        state_1 = random.uniform (0, 1)
        state_2 = random.uniform (0, 1)
        
        for j in range (POPULATION_SIZE) :
            state_1 = state_1 - probs[j]
            if state_1 <= 0 :
                state_index_1 = j
                state_1 = list (states[j])
                break

        for j in range (POPULATION_SIZE) :
            state_2 = state_2 - probs[j]
            if state_2 <= 0 :
                state_2 = list (states[j])
                state_index_2 = j
                break
        
        if (random.randint (0, 10000)) / 10000.0 <= CROSSOVER_PROBABILITY :
            cut = random.randint (0, len(state_1) - 1)

            state_1 = state_1[:cut] + state_2[cut:]
            state_2 = state_2[:cut] + state_1[cut:]

        if (random.randint (0, 10000)) / 10000.0 <= MUTATION_PROBABILITY :
            index_1 = random.randint (0, len (state_1) - 1)
            state_1[index_1] = random.randint (0, len(state_1) - 1)

        if (random.randint (0, 10000)) / 10000.0 <= MUTATION_PROBABILITY :
            index_2 = random.randint (0, len (state_2) - 1)
            state_2[index_2] = random.randint (0, len(state_2) - 1)
        
        best_state = states[states_value.index (max (states_value))]

        if random.randint (0, int (1.0 / ELITISM) - 1) == 0 :
            index = random.randint (0, POPULATION_SIZE-1)
        else :
            index = states_value.index (min(states_value))
        
        states[index] = tuple (state_1)
        states_value[index] = problem.value (state_1)

        if random.randint (0, int (1.0 / ELITISM) - 1) == 0 :
            index = random.randint (0, POPULATION_SIZE-1)
        else :
            index = states_value.index (min(states_value))
            
        states[index] = tuple (state_2)        
        states_value[index] = problem.value (state_2)

        if problem.value (best_state) > max(states_value) :
            index = random.randint (0, POPULATION_SIZE-1)
            states[index] = best_state
            states_value[index] = problem.value (best_state)

        for j in range (POPULATION_SIZE) :
            if problem.goal_test (states[j]) :
                return states[j]
    return states[states_value.index(max (states_value))]