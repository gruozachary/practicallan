import unittest
import pathlib
from src import solver

class ModuleTest(unittest.TestCase):
    def test_yeah(self):
        word_list = pathlib.Path("/Users/tomzachary/Desktop/wordlist.txt").read_text().split('\n')
        board = [["R", "S", "P", "E"],
                 ["H", "Y", "P", "N"],
                 ["A", "U", "T", "O"],
                 ["Y", "E", "R", "O"]]
        solver_ins = solver.Solver(word_list, board)
        for v in solver_ins.solve():
            print(v.word)

