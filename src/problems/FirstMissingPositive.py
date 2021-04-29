from typing import List
from unittest import TestCase


class Solution:  # complexity: time: O(n), extra space: O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx = {}
        biggest_sol = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > biggest_sol:
                continue
            idx[nums[i]] = i
        possible_solution = 1
        while possible_solution in idx:
            possible_solution += 1
        return possible_solution


class FirstMissingPositiveTest(TestCase):
    def test_first_missing_positive(self):
        sol = Solution()
        self.assertEqual(3, sol.firstMissingPositive([1, 2, 0]))
        self.assertEqual(2, sol.firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, sol.firstMissingPositive([7, 8, 9, 11, 12]))
