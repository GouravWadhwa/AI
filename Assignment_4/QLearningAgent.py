import numpy as np
import copy

class QLearningAgent () :
    def __init__ (self, agent_info) :
        self.num_states = agent_info['num_states']
        self.num_actions = agent_info['num_actions']
        self.epsilon = agent_info['epsilon']
        self.discount = agent_info['discount']
        self.alpha = agent_info['alpha']
        self.epsilon_decay = agent_info['epsilon_decay']

        self.q_values = np.zeros ((self.num_states, self.num_actions))

    def intial_action (self, state) :
        if np.random.rand() < self.epsilon :
            action = np.random.randint(0, 4)
        else :
            action = self.best_action (self.q_values[state])

        self.prev_state = state
        self.prev_action = action

        return action
        

    def best_action (self, q_values) :
        best = float ("-inf")
        ties = []

        for i in range (len (q_values)) :
            if q_values[i] > best :
                best = q_values[i]
                ties = [i]
            elif q_values[i] == best :
                ties.append (i)

        return np.random.choice(ties)

    def update (self, reward, state, episode_number) :
        if np.random.rand() < self.epsilon :
            action = np.random.randint(0, 4)
        else :
            action = self.best_action (self.q_values[state])

        if self.epsilon_decay :
            self.epsilon = self.epsilon - (episode_number / 10000.0)

        self.q_values[self.prev_state, self.prev_action] += self.alpha * (reward + self.discount * max (self.q_values[state]) - self.q_values[self.prev_state, self.prev_action])

        self.prev_action = action
        self.prev_state = state

        return action

    def end (self, reward) :
        self.q_values[self.prev_state, self.prev_action] += self.alpha * (reward - self.q_values[self.prev_state, self.prev_action])
