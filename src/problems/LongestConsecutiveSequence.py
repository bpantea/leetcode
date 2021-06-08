from typing import List
from unittest import TestCase


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sizes = {}
        best = 0
        for x in nums:
            if x not in sizes:
                left_cnt = sizes.get(x - 1, 0)
                right_cnt = sizes.get(x + 1, 0)
                current_sequence = left_cnt + right_cnt + 1
                sizes[x] = current_sequence
                sizes[x - left_cnt] = current_sequence
                sizes[x + right_cnt] = current_sequence
                best = max(best, current_sequence)
        return best


class LongestConsecutiveSequenceTest(TestCase):
    def test_longest_consecutive(self):
        tests = [
            ([100, 4, 200, 1, 3, 2], 4),
            ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[1], sol.longestConsecutive(test[0]))
