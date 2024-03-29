



class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self) -> str:
        return f'val: {self.val} - next: {self.next}'
    
    def __eq__(self, __value: object) -> bool:
        return self.__repr__() == __value.__repr__()



def remove_nth(head: ListNode, n: int) -> ListNode:
    if not head.next and n == 1:
        return None
    counter = 0
    new_head = head
    current = new_head
    trailing = head
    while current:
        counter += 1
        if counter >= n +1 :
            if not current.next:
                trailing.next = trailing.next.next
                
            else:
                trailing = trailing.next        
        elif not current.next and counter  == n:
            return new_head.next
            
        current = current.next
    return new_head

def build_ll(something):
    head = ListNode()
    current = head
    for inx, val in enumerate(something):
        current.val = val
        if inx == len(something) -1:
            return head
        current.next = ListNode()
        current = current.next


def test_ll_builder():
    assert build_ll([1,2,3]) == ListNode(1, ListNode(2, ListNode(3,None)))

def test_one():
    assert remove_nth(build_ll([1,2]), 1) == build_ll([1])

def test_two():
    assert remove_nth(build_ll([1]), 1) == None

def test_three():
    assert remove_nth(build_ll([1,2,3,4,5]), 2) == build_ll([1,2,3,5])

def test_187():
    assert remove_nth(build_ll([1,2]), 2) == build_ll([2])