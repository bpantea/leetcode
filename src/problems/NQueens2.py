from unittest import TestCase

from src.problems import NQueens


class Solution(NQueens.Solution):
    def __init__(self):
        super()

    def totalNQueens(self, n: int) -> int:
        self.solve(n)
        return len(self.solutions)


class NQueens2Test(TestCase):
    def test_total_queens(self):
        solution = Solution()
        self.assertEqual(2, solution.totalNQueens(4))
