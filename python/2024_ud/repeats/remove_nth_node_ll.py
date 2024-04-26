class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f'val: {self.val} - next: {self.next}'

    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()


def remove_node(head: ListNode, n: int) -> ListNode:
    ll_length = 0
    current = head
    while current: # 123
        ll_length += 1
        current = current.next
    #breakpoint()
    remove = ll_length - n -1
    current = head
    while current:
        
        if remove == 0:
            current.next = current.next.next
            return head
        elif remove < 0 and current is head:
            
            current = current.next
            head = current
            if not current:
                return head
        remove -= 1
        current = current.next
    return head

def ll_builder(array: list[int]) -> ListNode:
    
    head = ListNode()
    if not array:
        return head
    current = head
    for index, val in enumerate(array):
        current.val = val
        if index == len(array) -1:
            return head
        current.next = ListNode()
        current = current.next

def test_ll_builder():
    assert ll_builder([1,3,5]) == ListNode(1, ListNode(3, ListNode(5)))

def test_187():
    assert remove_node(ll_builder([1,2]), 2) == ll_builder([2])

def test_one():
    assert remove_node(ll_builder([1,2,3,4,5]), 2) == ll_builder([1,2,3,5])

def test_two():
    assert remove_node(ll_builder([1]), 1) == None

def test_three():
    assert remove_node(ll_builder([1,2]), 1) == ll_builder([1])