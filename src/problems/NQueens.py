from typing import List
from unittest import TestCase


def intersect(first: tuple, second: tuple) -> bool:
    if first[0] == second[0] or first[1] == second[1]:
        return True
    if first[0] - first[1] == second[0] - second[1]:
        return True
    if first[0] + first[1] == second[0] + second[1]:
        return True
    return False


class Solution:
    def __init__(self):
        self.n = -1
        self.queen_column = []
        self.available_columns = []
        self.available_diagonals = []
        self.available_second_diagonals = []
        self.solutions = []

    def get_possibilities(self, line) -> List[int]:
        possibilities = []
        for i in range(self.n):
            add_i = True
            for j in range(line):
                col = self.queen_column[j]
                assert col is not None
                if intersect((line, i), (j, col)):
                    add_i = False
                    break
            if add_i:
                possibilities.append(i)
        return possibilities

    def solve_line(self, line):
        if line == self.n:
            self.solutions.append([x for x in self.queen_column])
            return
        assert self.queen_column[line] is None
        possibilities = self.get_possibilities(line)
        for pos in possibilities:
            self.queen_column[line] = pos
            self.solve_line(line + 1)
        self.queen_column[line] = None

    def solve(self, n: int):
        self.n = n
        self.queen_column = [None] * n
        self.solutions = []
        self.available_columns = [x for x in range(n)]
        self.available_diagonals = [x for x in range(-n, n)]
        self.solve_line(0)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solve(n)
        parsed_solutions = []
        for s in self.solutions:
            lines = []
            for i in range(self.n):
                col = s[i]
                current_line = '.' * col + 'Q' + '.' * (self.n - col - 1)
                lines.append(current_line)
            parsed_solutions.append(lines)
        return parsed_solutions


class NQueensTest(TestCase):
    def test_n_queens(self):
        sol = Solution()
        print(sol.solveNQueens(4))
        self.assertTrue(True)
