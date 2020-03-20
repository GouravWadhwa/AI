from TicTacToe import Tic_Tac_Toe
import time

def max_value (problem, board, next_turn) :
    if problem.goal_test (board) != None :
        return problem.goal_test (board)

    v = -2
    
    childs = problem.children (board, next_turn)
    
    if next_turn == 'O' :
        next_turn = 'X'
    else :
        next_turn = 'O'
    
    for child in childs :
        v = max (v, min_value (problem, child, next_turn))
    
    return v

def min_value (problem, board, next_turn) :
    if problem.goal_test (board) != None :
        return problem.goal_test (board)

    v = 2
    
    childs = problem.children (board, next_turn)
    
    if next_turn == 'O' :
        next_turn = 'X'
    else :
        next_turn = 'O'
    
    for child in childs :
        v = min (v, max_value (problem, child, next_turn))
    
    return v

if __name__ == '__main__' :
    size = int (input("Size of the Tic Tac Toe : "))
    problem = Tic_Tac_Toe (size = size)
    board = problem.initial_board ()
    
    start = time.time()

    while (True) :
        childs = problem.children (board, 'O')
        value = 2
        for child in childs :
            new_value = max_value (problem, child, next_turn='X')
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
        value = -2
        for child in childs :
            new_value = min_value (problem, child, next_turn='O')
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