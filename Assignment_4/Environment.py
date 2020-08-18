import numpy as np
import copy

class Environment () :
    def __init__ (self, env_dimensions, env_start, env_end) :
        self.rows = env_dimensions[0]
        self.columns = env_dimensions[1]

        self.start_state = env_start
        self.end_state = env_end

        self.cliff = [[self.rows-1, i] for i in range (1, self.columns-1)]
        
        self.current_state = None
        self.reward = None

    def start (self) :
        self.current_state = copy.deepcopy (self.start_state)
        self.reward = 0.0

        return (self.current_state[0] * self.columns + self.current_state[1], self.reward)

    def take_action (self, action) :
        new_state = copy.deepcopy (self.current_state)

        if action == 0 :                                                        # UP
            new_state[0] = max (0, new_state[0] - 1)
        elif action == 1 :                                                      # LEFT
            new_state[1] = max (0, new_state[1] - 1)
        elif action == 2 :                                                      # DOWN
            new_state[0] = min (new_state[0] + 1, self.rows - 1)
        elif action == 3 :                                                      # RIGHT
            new_state[1] = min (new_state[1] + 1, self.columns - 1)

        self.current_state = copy.deepcopy (new_state)

        self.reward = -1.0
        if self.current_state in self.cliff :
            self.reward = -100.0
            self.current_state = copy.deepcopy (self.start_state)

        return (self.current_state[0] * self.columns + self.current_state[1], self.reward)

    def is_terminal_state (self, state) :
        if self.current_state == self.end_state :
            return True

        return False 