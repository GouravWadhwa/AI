from TicTacToe import Tic_Tac_Toe
import time

def max_value (problem, board, alpha, beta, next_turn, depth) :
    if depth == 4 or problem.goal_test (board) != None :
        return problem.heuristic_value (board)

    v = float ('-inf')
    
    childs = problem.children (board, next_turn)
    
    if next_turn == 'O' :
        next_turn = 'X'
    else :
        next_turn = 'O'
    
    for child in childs :
        v = max (v, min_value (problem, child, alpha, beta, next_turn, depth+1))
        if v >= beta :
            return v
        alpha = max (alpha, v)
    
    return v

def min_value (problem, board, alpha, beta, next_turn, depth) :
    if depth == 4 or problem.goal_test (board) != None :
        return problem.heuristic_value (board)

    v = float ('inf')
    
    childs = problem.children (board, next_turn)
    
    if next_turn == 'O' :
        next_turn = 'X'
    else :
        next_turn = 'O'
    
    for child in childs :
        v = min (v, max_value (problem, child, alpha, beta, next_turn, depth+1))
        if v <= alpha :
            return v
        beta = min (beta, v)
    
    return v

if __name__ == '__main__' :
    size = int (input("Size of the Tic Tac Toe : "))
    problem = Tic_Tac_Toe (size = size)
    board = problem.initial_board ()

    start = time.time ()

    while (True) :
        childs = problem.children (board, 'O')
        value = float ('inf')
        for child in childs :
            new_value = max_value (problem, child, float('-inf'), float ('inf'), next_turn='X', depth=0)
            if new_value < value :
                board = child
                value = new_value

        problem.print_board (board)
        print ()

        if problem.goal_test (board) == -1 :
            print ("Agent O Won the game")
            break
        elif problem.goal_test (board) == 0 :
            print ("Game Tied")
            break

        childs = problem.children (board, 'X')
        value = float ('-inf')
        for child in childs :
            new_value = min_value (problem, child, float('-inf'), float ('inf'), next_turn='O', depth=0)
            if new_value > value :
                board = child
                value = new_value

        problem.print_board (board)
        print ()

        if problem.goal_test (board) == 1 :
            print ("Agent X Won the game")
            break
        elif problem.goal_test (board) == 0 :
            print ("Game Tied")
            break

    print ("Time Consumed : ", time.time () - start, " seconds")