from typing import Optional, List, Tuple

class ListNode:
    def __init__(self, x=0, nxt=None):
        self.val = x
        self.next = nxt
        

    def __str__(self) -> str:
        return f'val: {self.val}, next:{self.next}'

    def __repr__(self) -> str:
        return f'val: {self.val}, next:{self.next}'
    
    def __eq__(self, other) ->  bool:
        return self.__repr__() == other.__repr__()

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    '''
    Constraints:

    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 104
    1 <= Node.val <= 105
    0 <= skipA < m
    0 <= skipB < n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
    '''
    
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
    return 0


def build_ll(linput : List[int]) -> ListNode:
    '''a crappy list -> Linked List factory'''
    head = ListNode()
    prev = head
    for index, val in enumerate(linput):
        if index == len(linput) -1:
            prev.val = val
        else:
            prev.val= val
            prev.next = ListNode()
            prev = prev.next
    return head


def build_ll_intersection(incoming: List[int]) -> Tuple[ListNode, ListNode]:
    '''
    incoming list object must be > 1
    returns Tuple(head, tail) of Linked List w/ intersection
    '''
    if len(incoming) < 2:
        raise IndexError('Must be: len(incoming) > 1 ')
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



def test_build_ll():
    '''validate that build_ll creates a linked list'''
    assert build_ll([1,2,3]) == ListNode(1, ListNode(2, ListNode(3, None)))

def test_build_ll_tail():
    '''
    tests the building of a linked list w/ an intersection at the end
    returns the head and tail in a tuple
    '''
    assert build_ll_intersection([1,2,3,4]) == (build_ll([1,2,3]), build_ll([4,3]))
    


def test_intersecting_linked_lists():
    '''
    building one linked list and traversing through the head/tail
    '''
    head, tail = build_ll_intersection([1,2,3,4])
    assert getIntersectionNode(head, tail) == ListNode(3, None)