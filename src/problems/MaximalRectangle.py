from typing import List
from unittest import TestCase


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        lines = len(matrix)
        columns = len(matrix[0]) if lines > 0 else 0
        height = [0] * columns
        left = [0] * columns
        right = [columns] * columns
        best = 0
        for i in range(lines):
            curr_left = 0
            curr_right = columns
            for j in reversed(range(columns)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = columns
                    curr_right = j
            for j in range(columns):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], curr_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    curr_left = j + 1
                best = max(best, (right[j] - left[j]) * height[j])
        return best


class MaximalRectangleTest(TestCase):
    def test_maximal_rectangle(self):
        sol = Solution()
        tests = [
            ([["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]], 6),
            ([], 0),
            ([['0']], 0),
            (['0', '0'], 0)
        ]
        for test in tests:
            self.assertEqual(test[1], sol.maximalRectangle(test[0]))
