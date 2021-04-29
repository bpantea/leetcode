from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.best = 0

    def max_path_sum_one_branch(self, root: TreeNode) -> int:
        best_left = self.max_path_sum_one_branch(root.left) if root.left is not None else 0
        best_right = self.max_path_sum_one_branch(root.right) if root.right is not None else 0

        self.best = max(self.best, best_left + root.val + best_right)

        return max(max(root.val, 0), max(root.val + best_left, root.val + best_right))

    def maxPathSum(self, root: TreeNode) -> int:
        self.best = root.val
        self.max_path_sum_one_branch(root)
        return self.best


class BinaryTreeMaximumPathSum(TestCase):
    def test_max_path_sum(self):
        tests = [
            (TreeNode(1, left=TreeNode(2), right=TreeNode(3)), 6),
            (TreeNode(-10, left=TreeNode(9), right=
                      TreeNode(20, left=TreeNode(15), right=TreeNode(7))), 42),
            (TreeNode(-4, left=TreeNode(-5, right=TreeNode(-3))), -3)
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[1], sol.maxPathSum(test[0]))
