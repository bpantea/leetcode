from typing import List
from unittest import TestCase


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        best = 0
        nr_lines = len(matrix)
        nr_columns = len(matrix[0]) if nr_lines > 0 else 0
        d = [[0] * (nr_columns + 1) for _ in range(2)]
        i0 = 1
        for i in range(nr_lines):
            if i0 == 0:
                i0 = 1
                i1 = 0
            else:
                i0 = 0
                i1 = 1
            for j in range(nr_columns):
                d[i0][j] = 0 if matrix[i][j] == '0' else min(d[i1][j - 1], min(d[i1][j], d[i0][j - 1])) + 1
                best = max(best, d[i0][j])
        return best * best


class MaximalSquareTest(TestCase):
    def test_maximal_square(self):
        tests = [
            ([["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]], 4),
            ([["0", "1"],
              ["1", "0"]], 1),
            ([["1", "1"],
              ["1", "1"]], 4),
            ([["0"]], 0),
            ([], 0)
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[1], sol.maximalSquare(test[0]))
