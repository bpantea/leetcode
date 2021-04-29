from typing import List
from unittest import TestCase


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # this will store tuples: (height, position)
        rain_trapped = 0
        for i in range(len(height)):
            current_height = height[i]
            while len(stack) > 0 and stack[-1][0] <= current_height:
                last = stack.pop()
                if len(stack) > 0:
                    prev_last = stack[-1]
                    dh = min(current_height, prev_last[0])
                    rain_trapped += (dh - last[0]) * (i - prev_last[1] - 1)
            stack.append((current_height, i))
        return rain_trapped


class TrappingRainWaterTest(TestCase):
    def test_trap(self):
        sol = Solution()
        self.assertEqual(6, sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(9, sol.trap([4, 2, 0, 3, 2, 5]))
