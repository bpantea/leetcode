from typing import List
from unittest import TestCase


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        d = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for left in range(n - k):
                right = left + k
                for i in range(left + 1, right):
                    val = nums[left] * nums[i] * nums[right] + d[left][i] + d[i][right]
                    d[left][right] = max(d[left][right], val)
        return d[0][n - 1]


class BurstBalloonsTest(TestCase):
    def test_burst(self):
        tests = [
            ([2, 3, 2], 18),
            ([9, 76, 64], 44416),
            ([3, 1, 5, 8], 167),
            ([2, 4, 8], 88)
        ]
        for test in tests:
            self.assertEqual(test[1], Solution().maxCoins(test[0]))
