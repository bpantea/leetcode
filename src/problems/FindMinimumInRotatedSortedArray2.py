from typing import List
from unittest import TestCase


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
                left += 1
            else:
                right -= 1
        return nums[left]


class FindMinimumInRotatedSortedArray2Test(TestCase):
    def test_find_min(self):
        tests = [
            ([1, 3, 5], 1),
            ([2, 2, 2, 0, 1], 0),
            ([3, 5, 1], 1)
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[1], sol.findMin(test[0]))
