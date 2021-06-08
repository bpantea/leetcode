from typing import List
from unittest import TestCase


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_num, max_num = min(nums), max(nums)
        if max_num == min_num:
            return 0
        intervals = [None] * len(nums)
        interval = (max_num - min_num) / (len(nums) - 1)
        for num in nums:
            index = int((num - min_num) // interval)
            if intervals[index] is None:
                intervals[index] = (num, num)
            else:
                intervals[index] = min(intervals[index][0], num), max(intervals[index][1], num)
        best = 0
        prev_max = intervals[0][0]
        for interval in intervals:
            if interval is None:
                continue
            best = max(best, interval[0] - prev_max)
            prev_max = interval[1]
        return best


class MaximumGapTest(TestCase):
    def test_gap(self):
        tests = [
            ([3, 6, 9, 1], 3),
            ([10], 0)
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[1], sol.maximumGap(test[0]))
