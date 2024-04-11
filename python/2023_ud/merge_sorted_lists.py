'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

class ListNode:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        return f"self.val = {self.val}"

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other) -> bool:
        return self.__repr__() == other.__repr__()



def merge(list1: ListNode, list2: ListNode) -> ListNode:
    head = ListNode()
    current = head
    def do_recursive_stuff(l1, l2, curr, head):
       # breakpoint()
        if l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
        elif l1:
            curr.next = l1
            l1 = l1.next
        elif l2:
            curr.next = l2
            l2 = l2.next
        else:
            return head.next
        curr = curr.next
        return do_recursive_stuff(l1, l2, curr, head)

    return do_recursive_stuff(list1, list2, current, head)


def setup_ll(arr: list) -> ListNode:
    head = ListNode()
    current = head
    for i, val in enumerate(arr):
        current.val = val
        if i == len(arr) -1:
            break
        current.next = ListNode()
        current = current.next
    return head


def test_ll_setup():
    assert setup_ll([1,2,3]) == ListNode(1, ListNode(2, ListNode(3, None)))

def test_one():
    assert merge(setup_ll([1,2,4]), setup_ll([1,3,4])) == setup_ll([1,1,2,3,4,4])