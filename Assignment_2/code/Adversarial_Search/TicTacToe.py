import numpy as np

class Tic_Tac_Toe :
    def __init__ (self, size=4) :
        self.size = size

    def initial_board (self) :
        return np.zeros ((self.size, self.size))

    def move (self, board, position, turn) :
        if turn == 'X' :
            board[position[0], position[1]] = 1
        else :
            board[position[0], position[1]] = 2

    def goal_test (self, board) :
        for i in range (self.size) :
            if np.all (board[:, i] == np.ones (self.size)) :
                return 1
            if np.all (board[:, i] == np.ones (self.size) * 2) :
                return -1
            if np.all (board[i, :] == np.ones (self.size)) :
                return 1
            if np.all (board[i, :] == np.ones (self.size) * 2) :
                return -1

        if np.all (board.diagonal() == np.ones (self.size)) :
            return 1
        if np.all (board.diagonal() == np.ones (self.size) * 2) :
            return -1
        if np.all (np.fliplr(board).diagonal() == np.ones (self.size)) :
            return 1
        if np.all (np.fliplr(board).diagonal() == np.ones (self.size) * 2) :
            return -1
        if not 0 in board :
            return 0

    def print_board (self, board) :
        for i in range (self.size) :
            for j in range (self.size) :
                if board[i, j] == 0 :
                    print ("|_ _|", end='')
                elif board[i, j] == 1 :
                    print ("|_X_|", end='') 
                else :
                    print ("|_O_|", end='')    
            print ()

    def children (self, board, turn) :
        child = []
        if turn == 'X' :
            for i in range (self.size) :
                for j in range (self.size) :
                    if board[i, j] == 0 :
                        board[i, j] = 1
                        child.append (board.copy())
                        board[i, j] = 0
        if turn == 'O' :
            for i in range (self.size) :
                for j in range (self.size) :
                    if board[i, j] == 0 :
                        board[i, j] = 2
                        child.append (board.copy())
                        board[i, j] = 0

        return child

    def heuristic_value (self, board) :
        value = 0

        goal = self.goal_test (board)
        if goal != None :
            if goal == 1 :
                return 1000
            elif goal == 0 :
                return 0
            else :
                return -1000

        for i in range (self.size) :
            for j in range (self.size) :
                if board[i, j] == 1 :
                    if i < self.size - 2 and board[i+1, j] == 1 and board[i+2, j] == 1 :
                        value = value + 100
                    if i < self.size - 2 and board[i+1, j] == 1 and board[i+2, j] == 0 :
                        value = value + 10
                    if i < self.size - 2 and board[i+1, j] == 0 and board[i+2, j] == 1 :
                        value = value + 10
                    if i < self.size - 2 and board[i+1, j] == 0 and board[i+2, j] == 0 :
                        value = value + 1

                    if j < self.size - 2 and board[i, j+1] == 1 and board[i, j+2] == 1 :
                        value = value + 100
                    if j < self.size - 2 and board[i, j+1] == 1 and board[i, j+2] == 0 :
                        value = value + 10
                    if j < self.size - 2 and board[i, j+1] == 0 and board[i, j+2] == 1 :
                        value = value + 10
                    if j < self.size - 2 and board[i, j+1] == 0 and board[i, j+2] == 0 :
                        value = value + 1                

                    if i < self.size - 2 and j < self.size - 2 and board[i+1, j+1] == 1 and board[i+2, j+2] == 1 :
                        value = value + 100
                    if i < self.size - 2 and j < self.size - 2 and board[i+1, j+1] == 1 and board[i+2, j+2] == 0 :
                        value = value + 10
                    if i < self.size - 2 and j < self.size - 2 and board[i+1, j+1] == 0 and board[i+2, j+2] == 1 :
                        value = value + 10
                    if i < self.size - 2 and j < self.size - 2 and board[i+1, j+1] == 0 and board[i+2, j+2] == 0 :
                        value = value + 1
                    
                    if i < self.size - 2 and j > 1 and board[i+1, j-1] == 1 and board[i+2, j-2] == 1 :
                        value = value + 100
                    if i < self.size - 2 and j > 1 and board[i+1, j-1] == 1 and board[i+2, j-2] == 0 :
                        value = value + 10
                    if i < self.size - 2 and j > 1 and board[i+1, j-1] == 0 and board[i+2, j-2] == 1 :
                        value = value + 10
                    if i < self.size - 2 and j > 1 and board[i+1, j-1] == 0 and board[i+2, j-2] == 0 :
                        value = value + 1

                if board[i, j] == 2 :
                    if i < self.size - 2 and board[i+1, j] == 2 and board[i+2, j] == 2 :
                        value = value - 100
                    if i < self.size - 2 and board[i+1, j] == 2 and board[i+2, j] == 0 :
                        value = value - 10
                    if i < self.size - 2 and board[i+1, j] == 0 and board[i+2, j] == 2 :
                        value = value - 10
                    if i < self.size - 2 and board[i+1, j] == 0 and board[i+2, j] == 0 :
                        value = value - 1

                    if j < self.size - 2 and board[i, j+1] == 2 and board[i, j+2] == 2 :
                        value = value - 100
                    if j < self.size - 2 and board[i, j+1] == 2 and board[i, j+2] == 0 :
                        value = value - 10
                    if j < self.size - 2 and board[i, j+1] == 0 and board[i, j+2] == 2 :
                        value = value - 10
                    if j < self.size - 2 and board[i, j+1] == 0 and board[i, j+2] == 0 :
                        value = value - 1                

                    if i < self.size - 2 and j < self.size - 2 and board[i+1, j+1] == 2 and board[i+2, j+2] == 2 :
                        value = value - 100
                    if i < self.size - 2 and j < self.size - 2 and board[i+1, j+1] == 2 and board[i+2, j+2] == 0 :
                        value = value - 10
                    if i < self.size - 2 and j < self.size - 2 and board[i+1, j+1] == 0 and board[i+2, j+2] == 2 :
                        value = value - 10
                    if i < self.size - 2 and j < self.size - 2 and board[i+1, j+1] == 0 and board[i+2, j+2] == 0 :
                        value = value - 1

                    if i < self.size - 2 and j > 1 and board[i+1, j-1] == 2 and board[i+2, j-2] == 2 :
                        value = value - 100
                    if i < self.size - 2 and j > 1 and board[i+1, j-1] == 2 and board[i+2, j-2] == 0 :
                        value = value - 10
                    if i < self.size - 2 and j > 1 and board[i+1, j-1] == 0 and board[i+2, j-2] == 2 :
                        value = value - 10
                    if i < self.size - 2 and j > 1 and board[i+1, j-1] == 0 and board[i+2, j-2] == 0 :
                        value = value - 1

        return value

    def is_valid_move (self, board, position) :
        if position[0] >= self.size or position[1] >= self.size or position[0] < 0 or position[1] < 0 :
            return False

        if board[position[0], position[1]] == 0 :
            return True
        else :
            return False 