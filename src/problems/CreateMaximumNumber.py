from typing import List
from unittest import TestCase


def concatenate(nums1: List[int], nums2: List[int]) -> List[int]:
    i, j = 0, 0
    sol = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            sol.append(nums1[i])
            i += 1
        else:
            sol.append(nums2[j])
            j += 1
    while i < len(nums1):
        sol.append(nums1[i])
        i += 1
    while j < len(nums2):
        sol.append(nums2[j])
        j += 1
    return sol


def initialize_d(nums: List[int], digits: int) -> List[List[List[int]]]:
    # d1(i, k) = the biggest number (with k digits) that I can make with the first i numbers
    # d1(i, k) = max(d(i - 1, k - 1) + nums1[i], d[i - 1][k])
    d = [[[] for k in range(min(digits - 1, i) + 2)] for i in range(len(nums) + 1)]
    for i in range(len(nums)):
        for k in range(min(digits, i) + 1):
            d[i][k] = d[i - 1][k - 1] + [nums[i]]
            if k < i and d[i - 1][k] > d[i][k]:
                d[i][k] = d[i - 1][k]
    return d


class Solution:

    def maxNumber(self, nums1: List[int], nums2: List[int], digits: int) -> List[int]:
        d1 = initialize_d(nums1, digits)
        d2 = initialize_d(nums2, digits)
        for line in d1:
            print(line)
        print()
        for line in d2:
            print(line)
        print()

        best = []
        for i in range(digits):
            if i > len(nums1) or digits - i > len(nums2):
                continue
            # i + 1 elements from nums1, digits - i - 1 elements from nums2
            sol = concatenate(d1[len(nums1) - 1][i - 1], d2[len(nums2) - 1][digits - i - 1])
            print('sol', d1[len(nums1) - 1][i - 1], d2[len(nums2) - 1][digits - i - 1], sol)
            if len(sol) == digits and sol > best:
                best = sol
        return best


class CreateMaximumNumberTest(TestCase):
    def test_max(self):
        tests = [
            (([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5), [9, 8, 6, 5, 3]),
            (([6, 7], [6, 0, 4], 5), [[6, 7, 6, 0, 4]])
        ]
        for test in tests:
            self.assertEqual(test[1], Solution().maxNumber(test[0][0], test[0][1], test[0][2]))
