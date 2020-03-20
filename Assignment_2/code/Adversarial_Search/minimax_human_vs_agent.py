from TicTacToe import Tic_Tac_Toe

def max_value (problem, board) :
    if problem.goal_test (board) != None :
        return problem.goal_test (board)

    v = -2
    
    childs = problem.children (board, 'X')
    for child in childs :
        v = max (v, min_value (problem, child))
    
    return v

def min_value (problem, board) :
    if problem.goal_test (board) != None :
        return problem.goal_test (board)

    v = 2
    
    childs = problem.children (board, 'O')
    for child in childs :
        v = min (v, max_value (problem, child))
    
    return v

if __name__ == '__main__' :
    size = int (input("Size of the Tic Tac Toe : "))
    problem = Tic_Tac_Toe (size = size)
    board = problem.initial_board ()

    print ("First move will be taken by the human")
    print ("The board positions are from (1, 1) to (%d, %d) where (1, 1) is the top left corner" %  (size, size))
    
    while (True) :
        while (True) :
            position_x = int (input ("Give the x position : "))
            position_y = int (input ("Give the y position : "))

            if problem.is_valid_move (board, (position_x - 1, position_y - 1)) :
                break
            else :
                print ("Invalid Move !!")
                print ("Please Try Again")
                print ()
                problem.print_board (board)

        problem.move (board, (position_x - 1, position_y - 1), 'O')

        problem.print_board (board)

        if problem.goal_test (board) == -1 :
            print ("You Won the game")
            break
        elif problem.goal_test (board) == 0 :
            print ("Game Tied")
            break

        childs = problem.children (board, 'X')
        value = -2
        for child in childs :
            new_value = min_value (problem, child)
            if new_value > value :
                board = child
                value = new_value

        print ()
        problem.print_board (board)

        if problem.goal_test (board) == 1 :
            print ("Agent Won the game")
            break
        elif problem.goal_test (board) == 0 :
            print ("Game Tied")
            break
        
        