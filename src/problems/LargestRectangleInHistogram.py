from typing import List
from unittest import TestCase


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        best_rectangle = heights[0]
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                rect = h * w
                if rect > best_rectangle:
                    best_rectangle = rect
            stack.append(i)
        return best_rectangle


class LargestRectangleInHistogramTest(TestCase):
    def test_largest_rectangle_area(self):
        tests = [
            ([2, 1, 5, 6, 2, 3], 10),
            ([2, 4], 4),
            ([999, 999, 999, 999], 3996),
            ([3, 6, 5, 7, 4, 8, 1, 0], 20),
            ([3, 2, 4], 6),
            ([0], 0)
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[1], sol.largestRectangleArea(test[0]))

# stack = [
# (2, 0)
# ]

# stack = [
# (1, 0)
# ]

# stack = [
# (1, 0),
# (5, 2)
# ]

# stack = [
# (1, 0),
# (5, 2),
# (6, 3)
# ]

# stack = [
# (1, 0),
# (5, 2), -- removed and (2, 2) is added
# ]

# stack = [
# (1, 0),
# (2, 2),
# (3, 5)
# ]
