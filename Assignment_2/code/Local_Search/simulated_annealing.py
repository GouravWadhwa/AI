import math
import random

def exp_schedule(k=1000, lam=0.1, limit=100):
    return lambda x : k * math.exp (- x * lam) if (x <= limit ) else 1e-8

def simulated_annealing(problem, schedule=exp_schedule()):
    MAXIMUM_TIME = 1000

    state = problem.initial ()
    state_value = problem.value (state)

    for time in range (MAXIMUM_TIME) :
        temp = schedule (time)
        child = problem.random_child(state)
        child_value = problem.value (child)

        if child_value > state_value :
            state = child
            state_value = child_value
        elif (random.randint (0, 10000)) / 10000.0 < math.exp ((child_value - state_value) / temp) :
            state = child
            state_value = child_value

        if problem.goal_test (state) :
            return state

    return state