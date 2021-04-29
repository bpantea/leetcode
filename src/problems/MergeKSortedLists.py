import heapq
from typing import List
from unittest import TestCase

from src.utils.linked_lists.ListNode import list_to_list_node, list_node_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode2:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:  # complexity: O(log k * N)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for x in lists:
            if x is not None:
                node = ListNode2(x)
                heap.append(node)
        heapq.heapify(heap)
        last_node = None
        first_node = None
        while len(heap) > 0:
            smallest = heapq.heappop(heap)
            if last_node is not None:
                last_node.next = smallest.node
            else:
                first_node = smallest.node
            last_node = smallest.node
            if last_node is not None and last_node.next is not None:
                smallest.node = last_node.next
                heapq.heappush(heap, smallest)
        return first_node


class MergeKSortedListsTest(TestCase):
    def test_merge_klists(self):
        solution = Solution()
        lists = [
            list_to_list_node([1, 3, 5, 7]),
            list_to_list_node([4, 6]),
            list_to_list_node([2, 4, 6]),
        ]
        expected = [1, 2, 3, 4, 4, 5, 6, 6, 7]
        self.assertEqual(expected, list_node_to_list(solution.mergeKLists(lists)))
        self.assertEqual([], list_node_to_list(solution.mergeKLists([list_to_list_node([])])))
        self.assertEqual([], list_node_to_list(solution.mergeKLists([list_to_list_node([]), list_to_list_node([])])))
