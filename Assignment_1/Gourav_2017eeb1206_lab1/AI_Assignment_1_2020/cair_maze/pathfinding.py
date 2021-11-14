from collections import deque
from queue import PriorityQueue
import numpy as np
import time

def search_DFS(maze_game, start, goal):
    """
    ***************************************
    YOUR CODE HERE
    **************************************
    search-algorithm
    :param maze_game: the GameMaze instance
    :param start: tuple (x,y) of start position
    :param goal: tuple (x,y) of the goal position
    :A sequential loop to take 1 step then again check for environment legal actions
     and then take 2 step or backtrack if no options possible
    :return: list containing the path [number of coordinates, sequence of coordinates from source to destination, comma separated] if possible

    """

    memory = 1
    start_time = time.process_time ()
    stack = []
    stack.append (start)

    valid_moves = []
    visited = np.zeros ((maze_game.height, maze_game.width))
    not_possible = 0
    possible = 0

    visited[start[0], start[1]] = 1

    while (True) :
        if len (stack) == 0 :
            not_possible = 1
            break 

        current_position = stack.pop ()
        valid_moves.append (current_position)
        valid_direction = maze_game.legal_directions (current_position[0], current_position[1])

        for direction in valid_direction :
            if goal == direction :
                valid_moves.append (goal)
                possible = 1
                break
            if visited [direction[0], direction[1]] == 0 :
                stack.append (direction)
                visited[direction[0], direction[1]] = 1

        if len (stack) > memory :
            memory = len (stack)
        if possible == 1 :
            break
    
    if not_possible == 1 :
        print ("It is not possible to reach the goal")
        return [1, [goal]]

    final_moves = []
    last_move = goal
    for move in reversed (valid_moves) :
        if move == goal :
            final_moves.append (goal)
        else :
            current_pos_x, current_pos_y = last_move
            next_pos_x, next_pos_y = move

            diff_x = abs (current_pos_x - next_pos_x)
            diff_y = abs (current_pos_y - next_pos_y)

            if diff_x + diff_y <= 1 :
                final_moves.append (move)
                last_move = move

    print ("Time Taken = ", time.process_time() - start_time)
    print ("Memory Taken By Stack = " + str (memory))
    print ("Total Nodes Expanded inorder to reach the goal = " + str (len (valid_moves)))
    print ("Total Cost Till Goal =", len (final_moves) * 2)
    return [len (valid_moves), final_moves[::-1]]

def search_BFS (maze_game, start, goal) :
    memory = 1
    start_time = time.process_time ()
    stack = deque ()
    stack.append (start)

    valid_moves = []
    visited = np.zeros ((maze_game.height, maze_game.width))
    not_possible = 0
    possible = 0

    visited[start[0], start[1]] = 1

    while (True) :
        if len (stack) == 0 :
            not_possible = 1
            break 

        current_position = stack.popleft ()
        valid_moves.append (current_position)
        valid_direction = maze_game.legal_directions (current_position[0], current_position[1])

        for direction in valid_direction :
            if goal == direction :
                valid_moves.append (goal)
                possible = 1
                break
            if visited [direction[0], direction[1]] == 0 :
                stack.append (direction)
                visited[direction[0], direction[1]] = 1

        if len (stack) > memory :
            memory = len (stack)
        if possible == 1 :
            break
    
    if not_possible == 1 :
        print ("It is not possible to reach the goal")
        return [1, [goal]]

    final_moves = []
    last_move = goal
    for move in reversed (valid_moves) :
        if move == goal :
            final_moves.append (goal)
        else :
            current_pos_x, current_pos_y = last_move
            next_pos_x, next_pos_y = move

            diff_x = abs (current_pos_x - next_pos_x)
            diff_y = abs (current_pos_y - next_pos_y)

            if diff_x + diff_y <= 1 :
                final_moves.append (move)
                last_move = move

    print ("Time Taken = ", time.process_time() - start_time)
    print ("Memory Taken By Queue = " + str (memory))
    print ("Total Nodes Expanded inorder to reach the goal = " + str (len (valid_moves)))
    print ("Total Cost Till Goal =", len (final_moves) * 2)
    return [len (valid_moves), final_moves[::-1]]

def search_UCS (maze_game, start, goal) :
    memory = 1
    start_time = time.process_time ()
    stack = PriorityQueue()
    stack.put ((0, start))

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
        valid_moves.append (current_position)
        valid_direction = maze_game.legal_directions (current_position[0], current_position[1])

        for direction in valid_direction :
            if goal == direction :
                valid_moves.append (goal)
                possible = 1
                break
            if visited [direction[0], direction[1]] == 0 :
                if direction[1] - current_position[1] == 1 :
                    stack.put ((current_cost + 1, direction))
                else :
                    stack.put ((current_cost + 2, direction))
                visited[direction[0], direction[1]] = 1

        if stack.qsize() > memory :
            memory = stack.qsize()
        if possible == 1 :
            break
    
    if not_possible == 1 :
        print ("It is not possible to reach the goal")
        return [1, [goal]]

    final_moves = []
    last_move = goal
    total_cost = 0
    for move in reversed (valid_moves) :
        if move == goal :
            final_moves.append (goal)
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
    return [len (valid_moves), final_moves[::-1]]

def manhattan_distance (pos_1, pos_2) :
    return abs (pos_1[0] - pos_2[0]) + abs (pos_1[1] - pos_2[1])

def search_A_star (maze_game, start, goal) :
    memory = 1
    start_time = time.process_time ()
    stack = PriorityQueue()
    stack.put ((0 + manhattan_distance (start, goal), start))

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
        current_cost = current_cost - manhattan_distance (goal, current_position)
        valid_moves.append (current_position)
        valid_direction = maze_game.legal_directions (current_position[0], current_position[1])

        for direction in valid_direction :
            if goal == direction :
                valid_moves.append (goal)
                possible = 1
                break
            if visited [direction[0], direction[1]] == 0 :
                if direction[1] - current_position[1] == 1 :
                    stack.put ((current_cost + 1 + manhattan_distance (direction, goal), direction))
                else :
                    stack.put ((current_cost + 2 + manhattan_distance (direction, goal), direction))
                visited[direction[0], direction[1]] = 1

        if stack.qsize() > memory :
            memory = stack.qsize()
        if possible == 1 :
            break
    
    if not_possible == 1 :
        print ("It is not possible to reach the goal")
        return [1, [goal]]

    final_moves = []
    last_move = goal
    total_cost = 0
    for move in reversed (valid_moves) :
        if move == goal :
            final_moves.append (goal)
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
    return [len (valid_moves), final_moves[::-1]]