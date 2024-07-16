class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.val} -> {self.next} '
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()


def ll_builder(array):
    head = ListNode()
    current = head
    for index, val in enumerate(array):
        current.next = ListNode(val)
        if index == len(array)-1:
            return head.next
        
        current = current.next

def merge_ll(list1: ListNode, list2: ListNode) -> ListNode:
    head = ListNode()
    if list1 and list2 and list1.val > list2.val:
        head.val = list2.val
        list2 = list2.next
    elif list1 and list2 and list2.val <= list1.val:
        head.val = list1.val
        list1 = list1.next
    tail= head
    
    while list1 or list2:
        if list1 and list2 and list1.val > list2.val:
            tail.next = list2
            list2 = list2.next
            tail = tail.next
            
        elif list1 and list2 and list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
            
        elif list1:
            
            tail.next = list1
            list1 = None
            
        elif list2:
            if tail and tail.next:
                tail = tail.next
            
            tail.next = list2
            list2 = None
    if head.val is None or head.val == 0:
        return head.next
    return head
            

def test_builder():
    assert ll_builder([1,2,3,4]) == ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

def test_one():
    assert merge_ll(ll_builder([1,2,4]), ll_builder([1,3,5])) == ll_builder([1,1,2,3,4,5])

def test_two():
    assert merge_ll(ll_builder([]), ll_builder([1,2])) == ll_builder([1,2])

def test_three():
    assert merge_ll(ll_builder([]), ll_builder([])) == None

def test_four():
    assert merge_ll(ll_builder([2]), ll_builder([1])) == ll_builder([1,2])

def test_five():
    assert merge_ll(ll_builder([5]), ll_builder([1,2,4])) == ll_builder([1,2,4,5])