from typing import List
from unittest import TestCase


class Node:
    def __init__(self):
        self.counter = 0  # the number of elements in the current segment
        self.left: Node = None
        self.right: Node = None


class Solution:

    def add_and_return_smaller_count(self, root: Node, left: int, right: int, val: int) -> int:
        root.counter += 1
        if left == right - 1:
            return 0
        mid = (left + right) // 2
        if val < mid:
            if root.left is None:
                root.left = Node()
            return self.add_and_return_smaller_count(root.left, left, mid, val)
        else:
            if root.right is None:
                root.right = Node()
            left_counter = root.left.counter if root.left is not None else 0
            return left_counter + self.add_and_return_smaller_count(root.right, mid, right, val)

    def countSmaller(self, nums: List[int]) -> List[int]:
        min_value = min(nums)
        max_value = max(nums) + 1
        root = Node()
        solution = []
        for x in reversed(nums):
            solution.append(self.add_and_return_smaller_count(root, min_value, max_value, x))
        return list(reversed(solution))


class CountSmallerTest(TestCase):
    def test_count(self):
        tests = [
            ([-1], [0]),
            ([5, 2, 6, 1], [2, 1, 1, 0]),
            ([-1, -1], [0, 0])
        ]
        for test in tests:
            self.assertEqual(test[1], Solution().countSmaller(test[0]))
