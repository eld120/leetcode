class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val} -> {self.next}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, value):
        return self.__str__() == value.__str__()


def rotate_right(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head

    # Compute the length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Connect the tail to the head to form a circular linked list
    tail.next = head

    # Find the new tail and new head
    k %= length
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    new_head = new_tail.next

    # Break the circular linked list
    new_tail.next = None

    return new_head

def rotateRight( head: ListNode, k: int) -> ListNode:
        curr = head
        length = 0
        if k == 0 or head is None or head.next is None:
            return head
        while curr.next:
            length += 1
            curr = curr.next
        print(length)
        tail = curr
        tail.next = head
        rem = k % length
        print(rem)
        if rem == 0:
            return head
        r_head = None
        curr = head
        count = length - rem
        while count > 1:
            curr = curr.next
            count -=1

        r_head = curr.next
        curr.next = None
        return r_head
        


def linked_list_builder(array):
    if not array:
        return None

    head = ListNode(array[0])
    current = head
    for value in array[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def test_one():
    array = [1,2,3,4,5]
    k  = 2
    head = linked_list_builder(array)
    
    assert rotateRight(head, k) == linked_list_builder([4,5,1,2,3])


def test_two():
    assert rotateRight(linked_list_builder([1,2]), 1) == linked_list_builder([2,1])


def rotate_right_final(head, k):
    if k == 0 or head is None or head.next is None:
        return head
    curr = head
    length = 0
    tail = None
    while curr:
        if not curr.next:
            tail = curr
        curr = curr.next
        length += 1
    k =  k % length
    if k == 0:
        return head

    curr = head
    new_head = None
    while length > k + 1:
        curr = curr.next
        length -= 1
        
    new_head = curr.next
    curr.next = None
    tail.next = head
    return new_head
    