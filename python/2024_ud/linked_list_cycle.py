'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None) -> None:
        self.val = val
        self.next = nxt

    # def __repr__(self) -> str:
    #     return f'val: {self.val}, next: {self.next}'
    
    # def __str__(self) -> str:
    #     return f'val: {self.val}, next: {self.next}'

    # def __eq__(self, other) -> bool:
    #     return self.__str__() == other.__str__()


def hasCycle( head: Optional[ListNode]) -> bool:
    if head and head.next is None:
            return False
        
    cyclical = False
    objects_found = set()
    while not cyclical:
        
        if id(head) not in objects_found:
            objects_found.add(id(head))
        else:
            return True
            
        if head is None or head.next is None:
            return False
        head = head.next


def has_cycle(head: ListNode) -> bool:
    fast = head
    slow = head
    iterations = 0
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        iterations += 1
        if slow == fast:
            return iterations
    return iterations


def build_ll(incoming) -> ListNode:
    head = ListNode()
    current = head
    for index, val in enumerate(incoming):
        current.val = val
        if index < len(incoming) -1:
            current.next = ListNode()
            current = current.next
    return head

def build_ll_cycle(inc, loop_size):
    '''
    generates link lists of 100 nodes in lenght  # TODO What is the starting size of the loop?
    all should have an loop
    on each iteration the loop should be one node larger

    find how many iterations does it take to find out that there is a loop
    '''

    head = ListNode()
    current = head
    loop_start = None
    for index, val in enumerate(inc):
        current.val = val

        if index == loop_size:
            loop_start = current
        if index == len(inc)-1:
            current.next = loop_start
            return head
        current.next = ListNode()
        current = current.next

#build_ll_cycle([1,2,3,4,5], 3)
has_cycle(build_ll_cycle([x for x in range(0,10)], 9))

def test_ll_builder():
    assert build_ll([1,2,1,3,5]) == ListNode(1,ListNode(2, ListNode(1,ListNode(3,ListNode(5)))))

def test_small_ll():
    assert has_cycle(build_ll([1,2,3,4,5])) == False

def test_ll_builder_cycle():
    assert has_cycle( build_ll_cycle([1,2,3,4,5], 3)) == 4


if __name__ == '__main__':
    for num in reversed(range(0,100)):
        
        print(f'{num} -- {has_cycle(build_ll_cycle([x for x in range(0,100)], num))} iterations to find the loop')
    #print(f'{99} -- {has_cycle(build_ll_cycle([x for x in range(0,100)], 99))} iterations to find the loop')