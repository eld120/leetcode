from typing import Optional, List, Tuple


class ListNode:
    """Linked List boilerplate"""

    def __init__(self, x=0, nxt=None):
        self.val = x
        self.next = nxt

    def __str__(self) -> str:
        return f"val: {self.val}, next:{self.next}"

    def __repr__(self) -> str:
        return f"val: {self.val}, next:{self.next}"

    def __eq__(self, other) -> bool:
        return self.__repr__() == other.__repr__()


def get_intersection_node(
    headA: ListNode, headB: ListNode
) -> Optional[ListNode]:  # pylint: disable=C0103
    """
    Constraints:

    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 104
    1 <= Node.val <= 105
    0 <= skipA < m
    0 <= skipB
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
    """
    nodes = set()
    while headA is not None:
        ida = id(headA)

        if ida not in nodes:
            nodes.add(ida)
        headA = headA.next

    while headB is not None:
        idb = id(headB)

        if idb in nodes:
            return headB
        headB = headB.next
    return None


def get_intersection_again(headA, headB):
    """[1,2,3], [4,3]"""
    a = headA
    b = headB
    ll_a_len = 0
    ll_b_len = 0
    # traverse the entirety of head_a + record the length
    while a is not None:
        ll_a_len += 1
        a = a.next
    # traverse the entirety of head_b + record the length
    while b is not None:
        ll_b_len += 1
        b = b.next
    # take the diff between head_a and head_b - below
    diff = abs(ll_b_len - ll_a_len)
    # advance the pointer of the longer LL by the diff between a + b
    longer = headA if ll_a_len > ll_b_len else headB
    shorter = headB if ll_a_len > ll_b_len else headA
    # breakpoint()
    while diff > 0:
        longer = longer.next
        diff -= 1
    while longer is not None:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next

    return None

    # move each pointer (head_a/head_b) one node at a time until they are both pointing to the same node


def build_ll(linput: List[int]) -> ListNode:
    """a crappy list -> Linked List factory"""
    head = ListNode()
    prev = head
    for index, val in enumerate(linput):
        if index == len(linput) - 1:
            prev.val = val
        else:
            prev.val = val
            prev.next = ListNode()
            prev = prev.next
    return head


def build_ll_intersection(incoming: List[int]) -> Tuple[ListNode, ListNode]:
    """
    incoming list object must be > 1
    returns Tuple(head, tail) of Linked List w/ intersection
    """
    if len(incoming) < 2:
        raise IndexError("Must be: len(incoming) > 1 ")
    head = build_ll(incoming)
    current = head

    while current is not None:
        if current.next is not None:
            nxt = current.next
            if nxt.next is None:
                nxt.next = current
                current.next = None

            current = current.next
    return head, nxt


# def build_second_intersection(incoming: List[int], second: List[int], incoming_intersection: int, second_intersection: int) -> Tuple[ListNode, ListNode]:
#     head = build_ll(incoming)
#     current = head
#     second = ListNode()
#     index = 0
#     sec_inx = 0
#     while
#     while current is not None:
#         if index ==


def test_build_ll():
    """validate that build_ll creates a linked list"""
    assert build_ll([1, 2, 3]) == ListNode(1, ListNode(2, ListNode(3, None)))


def test_build_ll_tail():
    """
    tests the building of a linked list w/ an intersection at the end
    returns the head and tail in a tuple
    """
    assert build_ll_intersection([1, 2, 3, 4]) == (
        build_ll([1, 2, 3]),
        build_ll([4, 3]),
    )


def test_intersecting_linked_lists():
    """
    building one linked list and traversing through the head/tail
    """
    head, tail = build_ll_intersection([1, 2, 3, 4])
    assert get_intersection_again(head, tail) == ListNode(3, None)


def test_single_ll():
    head = build_ll([1])
    assert get_intersection_again(head, head) == ListNode(1, None)
