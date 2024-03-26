from typing import List

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f'val:{self.val}, next:{self.next}'
    
    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()
    
def remove_elements(head: ListNode, val: int) -> ListNode:
    '''
    [1,1,1,2,2] k = 1
    [1,1,1,2,2] k = 2
    [1,3] k = 3
    [1,1,2,3,3] k = 3
    [1,1,2,2,3,3] k = 2 -> [1,1]
    '''
    if head is None:
        return None
    original = head
    new_head = ListNode()
    current = new_head
    while original:
        if original.val != val:
            prev = current
            current.val = original.val
            if original.next is not None:
                current.next = ListNode()
                current = current.next
        else:
            if original.next is None:
                try:
                    prev.next = None
                except UnboundLocalError:
                    pass
        original = original.next
    if new_head.val == 0 and new_head.next is None:
        return None
    return new_head


def kick_ll_elements_out(head:ListNode, val: int)-> ListNode:
    '''
    [0,1,1,1] k = 1
    0,
    [1,1,1,2,2] k = 2
    [1,3] k = 3
    [1,1,2,3,3] k = 3
    [1,1,2,2,3,3] k = 2 -> [1,1]
    '''

    # new_ll : ListNode
    new_ll_head = ListNode()
    new_ll_tail = new_ll_head
    # iterate through head with a pointer: current
    current = head
    while current is not None:
        if current.val != val:
            new_ll_tail.next = current
            new_ll_tail = current
        else:
            new_ll_tail.next = None
        current = current.next
        
    return new_ll_head.next
        # if current.next:
        # if current.val is not val
            # append val to new ll
        # else:
            # current = current.next



def ll_builder(incoming: List[int]) -> ListNode:
    '''builds crappy linked lists'''
    head = ListNode()
    current = head
    for index, val in enumerate(incoming):
        current.val = val
        
        if index == len(incoming)-1:
            return head
        
        current.next = ListNode()
        current = current.next


def test_builder():
    assert ll_builder([1,2]) == ListNode(1, ListNode(2, None))

def test_one():
    assert kick_ll_elements_out(ll_builder([1,3]), 3) == ll_builder([1])

def test_remove_duplicates():
    assert kick_ll_elements_out(ll_builder([1,2,2,3]), 2) == ll_builder([1,3])

def test_remove_at_end():
    assert kick_ll_elements_out(ll_builder([1,1,2,3,3]), 3) == ll_builder([1,1,2])

def test_remove_at_beginning():
    assert kick_ll_elements_out(ll_builder([1,1,2,3,4]), 1) == ll_builder([2,3,4])

def test_two():
    assert kick_ll_elements_out(ll_builder([1,2,6,3,4,5,6]), 6) == ll_builder([1,2,3,4,5])

def test_empty():
    assert kick_ll_elements_out(ll_builder([]), 1) == ll_builder([])

def test_remove_all():
    assert kick_ll_elements_out(ll_builder([7,7,7,7]), 7) == ll_builder([])