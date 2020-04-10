import numpy as np
import copy

class Sudoku(object) :
    def __init__ (self, initial_board) :
        self.initial_board = initial_board
        
    def initial (self) :
        board = np.zeros ((9, 9), dtype=int)

        for i in range (self.initial_board.shape[0]) :
            for j in range (self.initial_board.shape[1]) :
                if self.initial_board[i, j] == 0 :
                    board[i, j] = np.random.randint (1, self.initial_board.shape[0] + 1)
                else :
                    board[i, j] = self.initial_board[i, j]

        return board

    def value (self, board) :
        score = 0

        for row in range (board.shape[0]) :
            for column in range (board.shape[1]) :
                if board[row][column] == 0 :
                    return -1000

                if board[row][column] > 9 or board[row][column] < 0 :
                    return -1000

                for i in range (board.shape[0]) :
                    if board[i][column] == board[row][column] and i != row:
                        score += -1

                for j in range (board.shape[1]) :
                    if board[row][j] == board[row][column] and j != column:
                        score += -1

                for i in range (3 * (row // 3), 3 * (row // 3) + 3) :
                    for j in range (3 * (column // 3), 3 * (column // 3) + 3) :
                        if board[row][column] == board[i][j] and not (i == row and j == column):
                            score += -1

        return score

    def board_clashes (self, board) :
        clashes = np.zeros (board.shape)

        for row in range (board.shape[0]) :
            for column in range (board.shape[1]) :
                if board[row][column] == 0 :
                    continue

                if board[row][column] > 9 or board[row][column] < 0 :
                    continue

                for i in range (board.shape[0]) :
                    if board[i][column] == board[row][column] and i != row:
                        clashes[row, column] += 2

                for j in range (board.shape[1]) :
                    if board[row][j] == board[row][column] and j != column:
                        clashes[row, column] += 2

                for i in range (3 * (row // 3), 3 * (row // 3) + 3) :
                    for j in range (3 * (column // 3), 3 * (column // 3) + 3) :
                        if board[row][column] == board[i][j] and not (i == row and j == column):
                            clashes[row, column] += 2
        
        return clashes

    def point_clashes (self, board, row, column) :
        clashes = 0
        
        for i in range (board.shape[0]) :
            if board[i][column] == board[row][column] and i != row:
                clashes += 2

        for j in range (board.shape[1]) :
            if board[row][j] == board[row][column] and j != column:
                clashes += 2

        for i in range (3 * (row // 3), 3 * (row // 3) + 3) :
            for j in range (3 * (column // 3), 3 * (column // 3) + 3) :
                if board[row][column] == board[i][j] and not (i == row and j == column):
                    clashes += 2

        return clashes

    def best_child (self, board) :
        children = []
        best_value = None
        clashes = self.board_clashes (board)
        board_value = self.value (board)

        for i in range (self.initial_board.shape[0]) :
            for j in range (self.initial_board.shape[1]) :
                if self.initial_board[i, j] != 0 :
                    continue

                current = board[i, j]
                for num in range (1, board.shape[0]+1) :
                    if current == num :
                        continue
                    
                    board[i, j] = num
                    value_board = board_value + clashes[i, j] - self.point_clashes(board, i, j)
                    if best_value == None or best_value < value_board :
                        children = []
                        children.append (copy.deepcopy(board))
                        best_value = value_board
                    elif best_value == value_board :
                        children.append (copy.deepcopy(board))

                board[i, j] = current
        return children[np.random.randint(0, len(children))], int (best_value)

    def same_states (self, boardA, boards) :
        for boardB in boards :
            a = 0
            for i in range (boardA.shape[0]) :
                for j in range (boardB.shape[1]) :
                    if boardA[i, j] != boardB[i, j] :
                        a = 1
                        break
                if a == 1 :
                    break
            if a == 0 :
                return True
            
        return False

    def random_child (self, board) :
        variables = []

        for i in range (self.initial_board.shape[0]) :
            for j in range (self.initial_board.shape[1]) :
                if self.initial_board[i, j] != 0 :
                    continue

                variables.append ((i, j))


        rand_pos = variables[np.random.randint(0, len(variables))]

        if np.random.randint(0, 10) < 5 :
            min_clashes = self.point_clashes (board, rand_pos[0], rand_pos[1])
            min_clashes_num = board[rand_pos]
            for num in range(1, 10) :
                if num == min_clashes_num :
                    continue

                board[rand_pos] = num
                
                new_clashes = self.point_clashes (board, rand_pos[0], rand_pos[1])
                if new_clashes < min_clashes :
                    min_clashes = new_clashes
                    min_clashes_num = num

            board[rand_pos] = min_clashes_num
        else :
            board[rand_pos] = np.random.randint(1, 10)
        return board

    def goal_test (self, board) :
        score = self.value (board) 
        if score == 0 :
            return True
        else :
            return False