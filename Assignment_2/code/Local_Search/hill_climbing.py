def hill_climbing(problem, starting_state = None):
    TOTAL_STATES = 1
    MAXIMUM_ITERATIONS = 20

    states = [problem.initial() for i in range (TOTAL_STATES)]
    states_value = [problem.value(state) for state in states]

    for iteration in range (MAXIMUM_ITERATIONS) :
        for i in range (TOTAL_STATES) :
            state_value = states_value[i]
            state = states[i]
            new_state = None
            new_state_value = None
            
            for child in problem.children (state) :
                child_value = problem.value (child) 
                
                if (new_state is not None and new_state_value < child_value) or (new_state is None and child_value > state_value) :
                    new_state = child
                    new_state_value = child_value
            
            if new_state is not None :
                states[i] = new_state
                states_value[i] = new_state_value

            if problem.goal_test (states[i]) :
                return states[i]

    return states[states_value.index (max (states_value))]