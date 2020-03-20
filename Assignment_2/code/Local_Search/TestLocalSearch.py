from time import time

size = 0
test = 0
class TestLocalSearch(object):
    def make_board(self, n, result):
        board = []
        for col in result:
            line = ['.'] * n
            line[col] = 'Q'
            board.append(str().join(line))
        return board

    def printBoard(self, board):
        charlist = list(map(list, board))
        for line in charlist:
            print(" ".join(line))

    def testLocalSearch(self, problem, local_search):
        times = 1
        cnt = 0
        start = time()
        for i in range(times):
            result = local_search(problem)
        
        build = test.make_board(size, result)
        test.printBoard(build)        
        

from hill_climbing import hill_climbing
from GA import GA
from simulated_annealing import simulated_annealing
from NQueens import NQueensSearch


if __name__ == "__main__":
    test = TestLocalSearch()
    print("Running local search for N Queens Problem")
    size = eval(input(" - Please input the size of the board: "))
    print()
    problem = NQueensSearch(size)
    algorithms = [ hill_climbing, simulated_annealing, GA]
    names = ["hill_climbing","simulated_annealing", "GA"]
    problems = [problem, problem, problem]
    for i in range(len(algorithms)):
        print(names[i])
        board = test.testLocalSearch(problems[i], algorithms[i])

