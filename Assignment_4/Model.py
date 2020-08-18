import numpy as np
import copy
import matplotlib.pyplot as plt

from tqdm import tqdm

from Environment import Environment
from QLearningAgent import QLearningAgent
from SarsaAgent import SarsaAgent

EPSILON = 0.1
ALPHA = 0.5
DISCOUNT = 1.0
RUNS = 500
EPISODES = 500
EPSILON_DECAY = False

agent_info = {
    'num_actions' : 4,
    'num_states' : 48,
    'epsilon' : EPSILON,
    'alpha' : ALPHA,
    'discount' : DISCOUNT,
    'epsilon_decay' : EPSILON_DECAY
}

gridworld = Environment ((4, 12), [3, 0], [3, 11])

agents = []

agents.append (QLearningAgent (agent_info))
agents.append (SarsaAgent (agent_info))

k = 0
for agent in agents :
    if k == 0 :
        print ('Q-Learning Agent')
    else :
        print ('SARSA Agent')
    averaged_rewards_sum = []
    for run in tqdm (range (RUNS)) :
        rewards_sum = []

        agent.__init__ (agent_info)

        for episode in range (EPISODES) :
            episode_reward_sum = 0
            
            state, reward = gridworld.start()
            action = agent.intial_action (state)
            
            count = 0

            while (not gridworld.is_terminal_state(state)) :
                count += 1
                
                state, reward = gridworld.take_action (action)
                if gridworld.is_terminal_state (state) :
                    action = agent.end (reward)
                else :
                    action = agent.update (reward, state, episode)
                
                episode_reward_sum += reward

                if count > 2000 :
                    break

            rewards_sum.append (episode_reward_sum)

        averaged_rewards_sum.append (rewards_sum)
    
    print ('GRIDWORLD GREEDY ACTION SELECTION OF THE LAST RUN')
    for i in range (4) :
        for j in range (12) :
            action = np.argmax(agent.q_values[i*12+j])

            if action == 0 :
                print ('U', end='  ')
            elif action == 1 :
                print ('L', end='  ')
            elif action == 2 :
                print ('D', end='  ')
            else :
                print ('R', end='  ')
        
        print ()
    
    plt.plot (np.mean (averaged_rewards_sum, axis=0), label='QLearning' if k == 0 else 'SARSA')
    k += 1

plt.xlabel ("EPISODES")
plt.ylabel ("SUM OF REWARDS")
plt.xlim (0, 500)
plt.ylim (-100, 0)
plt.legend ()
plt.show ()