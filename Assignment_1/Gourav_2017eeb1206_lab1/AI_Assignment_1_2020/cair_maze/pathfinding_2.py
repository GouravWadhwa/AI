from collections import deque
from queue import PriorityQueue
import numpy as np
import time

def manhattan_distance (pos_1, pos_2) :
    return abs (pos_1[0] - pos_2[0]) + abs (pos_1[1] - pos_2[1])

def search_A_star (maze_game, start, goal_1, goal_2) :
    memory = 1
    start_time = time.process_time ()
    stack = PriorityQueue()
    stack.put ((0 +  min (manhattan_distance (goal_1, start), manhattan_distance (goal_2, start)), start))

    valid_moves = []
    visited = np.zeros ((maze_game.height, maze_game.width))
    not_possible = 0
    possible = 0

    visited[start[0], start[1]] = 1

    while (True) :
        if stack.qsize() == 0 :
            not_possible = 1
            break 

        current_cost , current_position = stack.get ()
        current_cost = current_cost - min (manhattan_distance (goal_1, current_position), manhattan_distance (goal_2, current_position))
        valid_moves.append (current_position)
        valid_direction = maze_game.legal_directions (current_position[0], current_position[1])

        for direction in valid_direction :
            if goal_1 == direction :
                valid_moves.append (goal_1)
                possible = 1
                break
            elif goal_2 == direction :
                valid_moves.append (goal_2)
                possible = 2
                break
            if visited [direction[0], direction[1]] == 0 :
                if direction[1] - current_position[1] == 1 :
                    stack.put ((current_cost + 1 + min (manhattan_distance (goal_1, current_position), manhattan_distance (goal_2, current_position)), direction))
                else :
                    stack.put ((current_cost + 2 + min (manhattan_distance (goal_1, current_position), manhattan_distance (goal_2, current_position)), direction))
                visited[direction[0], direction[1]] = 1

        if stack.qsize() > memory :
            memory = stack.qsize()
        if possible == 1 or possible ==2 :
            break
    
    final_moves = []
    last_move = None
    goal_targeted = None
    if possible == 1 :
        last_move = goal_1
        goal_targeted = goal_1
    elif possible == 2 :
        last_move = goal_2
        goal_targeted = goal_2

    total_cost = 0
    for move in reversed (valid_moves) :
        if move == goal_1 :
            final_moves.append (goal_1)
        elif move == goal_2 :
            final_moves.append (goal_2)
        else :
            current_pos_x, current_pos_y = last_move
            next_pos_x, next_pos_y = move

            diff_x = abs (current_pos_x - next_pos_x)
            diff_y = abs (current_pos_y - next_pos_y)

            if diff_x + diff_y <= 1 :
                final_moves.append (move)
                last_move = move

                if current_pos_y - next_pos_y == 1 :
                    total_cost += 1
                else : 
                    total_cost += 2

            

    print ("Time Taken = ", time.process_time() - start_time)
    print ("Memory Taken By Queue = " + str (memory))
    print ("Total Nodes Expanded inorder to reach the goal = " + str (len (valid_moves)))
    print ("Total Cost Till Goal =", total_cost)
    print ("Goal State Reached =", goal_targeted)
    return [len (valid_moves), final_moves[::-1]]