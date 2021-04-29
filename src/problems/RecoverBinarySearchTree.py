from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):  # this is used only for testing purposes
        if (other is None and self is not None) or (self is None and other is not None):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right


def print_node(node: TreeNode, level=0):
    spaces = ' ' * (level * 3)
    if node is None:
        return
    print(spaces, node.val)
    if node.left is not None:
        print(spaces, 'Left =')
        print_node(node.left, level + 1)
    if node.right is not None:
        print(spaces, 'Right =')
        print_node(node.right, level + 1)


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        first = None
        second = None
        prev = None

        for node in self.morris_traversal(root):
            if first is None and prev is not None and prev.val >= node.val:
                first = prev
            if first is not None and prev is not None and prev.val >= node.val:
                second = node
            prev = node
        first.val, second.val = second.val, first.val

    def morris_traversal(self, root: TreeNode):
        current = root
        while current is not None:
            if current.left is None:
                yield current
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right is not current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    yield current
                    current = current.right


class RecoverBinarySearchTree(TestCase):

    def test_recover_tree(self):
        sol = Solution()
        expected = TreeNode(
            3, left=TreeNode(
                1, left=None, right=TreeNode(2)
            )
        )
        test = TreeNode(
            1,
            left=TreeNode(
                3,
                left=None,
                right=TreeNode(2)
            ),
        )
        sol.recoverTree(test)
        self.assertEqual(expected, test)


        test2 = TreeNode(
            3, left=TreeNode(1), right=TreeNode(4, left=TreeNode(2))
        )
        expected2 = TreeNode(
            2, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3))
        )
        sol.recoverTree(test2)
        print_node(test2)
        self.assertEqual(expected2, test2)
