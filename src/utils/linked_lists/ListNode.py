from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_list_node(lst: List[int]) -> ListNode:
    if len(lst) == 0:
        return None
    first = ListNode(lst[0])
    last = first
    for i in lst:
        last.next = ListNode(i)
        last = last.next
    return first.next


def list_node_to_list(node: ListNode) -> List[int]:
    lst = []
    while node is not None:
        lst.append(node.val)
        node = node.next
    return lst
