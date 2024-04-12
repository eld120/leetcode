class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'val:{self.val} next:{self.next}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()
    


def rotate_right(head: ListNode, k: int) -> ListNode:
    '''[1,2,3,4,5]'''
    # iterate through the ll by k

    # start changing next pointer at len(head) - k
    #breakpoint()
    if not head or not head.next or k == 0:
        return head
    current = head
    ll_length = 0
    while current:
        ll_length += 1
        current = current.next
    if k % ll_length == 0:
        return head

    #if length == 1 then leave

    end_of_new_ll = ll_length - (k % ll_length)
    #breakpoint()
    current = head
    new_head = None
    new_tail = None
    counter = 1
    while current:
        if counter  == end_of_new_ll:
            new_head = current.next
            new_tail = current
            break
        
        current = current.next
        counter += 1
    current = new_head
    while current:
        if current.next is None:
            current.next = head
            new_tail.next = None
            return new_head
        current = current.next

def setup_ll(array : list) -> ListNode:
    head = ListNode()

    current = head
    for index, val in enumerate(array):
        current.val = val
        if index == len(array)-1:
            break
        current.next = ListNode()
        current = current.next
    return head



def test_setup_ll():
    assert setup_ll([1,2]) == ListNode(1,ListNode(2, None))

def test_one():
    assert rotate_right(setup_ll([1,2,3,4,5]), 2) == setup_ll([4,5,1,2,3])


def test_k_longer_than_ll_len():
    assert rotate_right(setup_ll([0,1,2]), 4) == setup_ll([2,0,1])

def test_empty_ll():
    assert rotate_right(None, 0) is None


def test_k_eq_len_ll():
    assert rotate_right(setup_ll([1,2,3]), 3) == setup_ll([1,2,3])

def test_k_eq_zero():
    assert rotate_right(setup_ll([1,2,3]), 0) == setup_ll([1,2,3])

def test_ll_of_len_one():
    assert rotate_right(setup_ll([1]), 1) == setup_ll([1])

def test_ll_len_two():
    assert rotate_right(setup_ll([1,2]), 1) == setup_ll([2,1])

def test_226():
    assert rotate_right(setup_ll([1,2,3,4,5]), 10) == setup_ll([1,2,3,4,5])