import unittest
from typing import List


# link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# difficulty: hard

# wtf? the bad solution was better than the optimized one :) gg

class OptimizedList:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.left = 0
        self.right = len(nums)

    # complexity: O(1)
    def __len__(self):
        return self.right - self.left

    # complexity: O(1)
    def __getitem__(self, item):
        if item >= len(self):
            raise Exception('Wrong state')
        return self.nums[self.left + item]

    # complexity: O(1)
    def cut_left_side(self, cut_size):
        self.left += cut_size

    # complexity: O(1)
    def cut_right_side(self, cut_size):
        self.right -= cut_size

    # complexity: O(1)
    def median_value(self) -> float:
        size = len(self)
        if size == 0:
            raise Exception('No value')
        if size % 2 == 0:
            return (self[size // 2 - 1] + self[size // 2]) / 2
        else:
            return self[size // 2]

    # complexity: O(1) -> note, with a higher constant, but still 1
    def median_with_number(self, value: int) -> float:
        size = len(self)
        if size == 1:
            return (self[0] + value) / 2
        if size % 2 == 0:
            left_mid = size // 2 - 1
            if self[left_mid] <= value <= self[left_mid + 1]:
                return value
            if value < self[left_mid]:
                return self[left_mid]
            else:
                return self[left_mid + 1]
        else:
            mid = size // 2
            left_mid = mid - 1
            right_mid = mid + 1
            if value <= self[left_mid]:
                return (self[mid] + self[left_mid]) / 2
            elif value >= self[right_mid]:
                return (self[mid] + self[right_mid]) / 2
            return (self[mid] + value) / 2

    # complexity: O(1) -> with a higher constant
    def median_with_two_numbers(self, value1: int, value2: int) -> float:
        size = len(self)
        # trivial cases
        if size == 1:
            if value1 <= self[0] <= value2:
                return self[0]
            elif value1 > self[0]:
                return value1
            else:
                return value2
        if size == 2:
            return trivial_two(self, OptimizedList([value1, value2]))

        if size % 2 == 0:  # i have at least 4
            left = size // 2 - 1
            right = left + 1
            if value2 <= self[left - 1]:
                return (self[left - 1] + self[left]) / 2
            elif value1 >= self[right + 1]:
                return (self[right] + self[right + 1]) / 2
            return trivial_two(OptimizedList([self[left], self[right]]), OptimizedList([value1, value2]))
        else:  # at least 3
            mid = size // 2

            if value2 <= self[mid - 1]:
                return self[mid - 1]
            elif value1 >= self[mid + 1]:
                return self[mid + 1]

            if value2 <= self[mid]:
                return value2
            elif value1 >= self[mid]:
                return value1
            return self[mid]


# complexity: O(n log2(n) - because of sorting, but this is called just for the trivial task of n=2 + 2)
# O(n) extra memory
def trivial_two(nums1: OptimizedList, nums2: OptimizedList) -> float:
    lst = [nums1[0], nums1[1], nums2[0], nums2[1]]
    lst.sort()
    return (lst[1] + lst[2]) / 2


def median_arrays_optimized(nums1: OptimizedList, nums2: OptimizedList) -> float:
    while True:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        if len_nums1 == 0:
            return nums2.median_value()
        elif len_nums2 == 0:
            return nums1.median_value()
        if len_nums1 == 1:
            return nums2.median_with_number(nums1[0])
        elif len_nums2 == 1:
            return nums1.median_with_number(nums2[0])

        if len_nums1 == 2 and len_nums2 == 2:
            return trivial_two(nums1, nums2)
        if len_nums1 == 2:
            return nums2.median_with_two_numbers(nums1[0], nums1[1])
        elif len_nums2 == 2:
            return nums1.median_with_two_numbers(nums2[0], nums2[1])

        # note: time complexity should be log2(min(n, m) here. what am I doing wrong?
        median_l1 = nums1.median_value()
        median_l2 = nums2.median_value()
        if median_l1 == median_l2:
            return median_l1
        cross_out_nr = min(len_nums1 - 1, len_nums2 - 1) // 2
        if median_l1 < median_l2:
            nums1.cut_left_side(cross_out_nr)
            nums2.cut_right_side(cross_out_nr)
        else:
            nums1.cut_right_side(cross_out_nr)
            nums2.cut_left_side(cross_out_nr)


def median_arrays(nums1: List[int], nums2: List[int]) -> float:
    return median_arrays_optimized(OptimizedList(nums1), OptimizedList(nums2))


# time complexity: O(n + m)
def median_arrays_merging(nums1: List[int], nums2: List[int]) -> float:
    i = 0
    len1 = len(nums1)
    j = 0
    len2 = len(nums2)
    k = 0
    last = -1
    prevLast = -1
    total_elements = len(nums1) + len(nums2)
    median1 = (total_elements - 1) // 2
    if total_elements % 2 == 0:
        median2 = median1 + 1
    else:
        median2 = median1
    while k <= median2:
        prevLast = last
        if j >= len2 or (i < len1 and nums1[i] <= nums2[j]):
            last = nums1[i]
            i += 1
        else:
            last = nums2[j]
            j += 1
        k += 1
    if median1 == median2:
        return last
    else:
        return (prevLast + last) / 2


def get_list(nums) -> List[int]:
    if isinstance(nums, int):
        return [nums]
    return list(nums)


class MyTestCase(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.test_data = {
            ((1, 2, 3), (2, 3, 4)): 2.5,
            ((1, 2), (2, 3, 4)): 2,
            (1, (3, 4)): 3,
            ((1, 3), 4): 3,
            (1, 4): 2.5,
            (1, 3): 2,
            ((1, 3, 5), (3, 5, 6)): 4,
            ((1, 3, 5), (3, 5, 6, 7)): 5,
            ((1, 2), (-1, 3)): 1.5
        }

    def test_median_value(self):
        self.assertEqual(1, OptimizedList([-3, -2, 1, 5, 10]).median_value())
        self.assertEqual(1.5, OptimizedList([-3, -2, 1, 2, 5, 10]).median_value())

    def test_median_with_nr(self):
        self.assertEqual(2.5, OptimizedList([1, 3, 5]).median_with_number(2))
        self.assertEqual(3, OptimizedList([1, 3, 5]).median_with_number(3))
        self.assertEqual(3, OptimizedList([1, 3]).median_with_number(3))
        self.assertEqual(2, OptimizedList([1, 3]).median_with_number(2))
        self.assertEqual(1.5, OptimizedList([1]).median_with_number(2))

    def test_final_optimized(self):
        # median_arrays([1, 2], [-1, 3])

        for test in self.test_data:
            sol = median_arrays(get_list(test[0]), get_list(test[1]))
            self.assertEqual(self.test_data[test], sol)


if __name__ == '__main__':
    unittest.main()
