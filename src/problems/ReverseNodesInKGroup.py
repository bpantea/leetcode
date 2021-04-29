from unittest import TestCase

from src.problems.MergeKSortedLists import ListNode
from src.utils.linked_lists.ListNode import list_to_list_node, list_node_to_list


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        FIRST = None
        LAST = None
        while head is not None:
            tmp_head = head
            cnt = 0
            while tmp_head is not None:
                cnt += 1
                tmp_head = tmp_head.next
                if cnt >= k:
                    break
            if cnt < k:
                if LAST is not None:
                    LAST.next = head
                if FIRST is None:
                    FIRST = head
                break
            if k == 1:
                if LAST is not None:
                    LAST.next = head
                if FIRST is None:
                    FIRST = head
                break
            first = head
            prev = first
            middle = first.next
            last = middle.next
            first.next = None
            for i in range(k - 1):
                middle.next = prev
                prev = middle
                middle = last
                last = last.next if middle is not None else None
            if LAST is not None:
                LAST.next = prev
            if FIRST is None:
                FIRST = prev
            LAST = first
            head = middle
        return FIRST


class ReverseNodesInKGroupTest(TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(
            [2, 1, 4, 3, 6, 5, 7],
            list_node_to_list(solution.reverseKGroup(list_to_list_node([1, 2, 3, 4, 5, 6, 7]), 2))
        )
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7],
            list_node_to_list(solution.reverseKGroup(list_to_list_node([1, 2, 3, 4, 5, 6, 7]), 1))
        )
        self.assertEqual(
            [],
            list_node_to_list(solution.reverseKGroup(list_to_list_node([]), 2))
        )
        self.assertEqual(
            [3, 2, 1, 4, 5],
            list_node_to_list(solution.reverseKGroup(list_to_list_node([1, 2, 3, 4, 5]), 3))
        )

