from collections import deque
from typing import List
from unittest import TestCase


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        solution = []
        assert 1 <= k <= len(nums)
        for i in range(k):
            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        solution.append(nums[queue[0]])
        for i in range(k, len(nums)):
            while len(queue) > 0 and queue[0] <= i - k:
                queue.popleft()
            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            solution.append(nums[queue[0]])
        return solution


class SlidingWindowMaximumTest(TestCase):
    def test_sliding(self):
        tests = [
            ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
            ([1], 1, [1]),
            ([1, -1], 1, [1, -1]),
            ([9, 11], 2, [11]),
            ([4, -2], 2, [4])
        ]
        for test in tests:
            self.assertEqual(test[2], Solution().maxSlidingWindow(test[0], test[1]))
