from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list_node(lst: list) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def to_list(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = ListNode()
        cur: ListNode = result

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        cur.next = list1 if list1 else list2
        return result.next


if __name__ == "__main__":
    examples = [
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([], []), []),
        (([], [0]), [0]),
    ]
    solution = Solution()
    for example_input, example_output in examples:
        l1, l2 = to_list_node(example_input[0]), to_list_node(example_input[1])
        result = to_list(solution.mergeTwoLists(l1, l2))
        status = "PASS" if result == example_output else "FAIL"
        print(f"[{status}] expected {example_output}, got {result}")
