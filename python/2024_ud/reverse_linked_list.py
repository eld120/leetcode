'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'val: {self.val}, next: {self.next}'

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    
    #init three pointers:current next, future
    if not head or not head.next:
        return head
    elif head.next:
        current = head
        second = current.next
        current.next = None
    
    # iterate through the linked list
    while second.next:
    # base case is when future is None
        # starting to mutate each node
        # starting at current, then second, then third

        third = second.next
        second.next = current
        current = second
        second = third
        third = third.next
    second.next = current
    return second

def build_it(lst):
    nodes = [ListNode(x, None) for x in lst]
    for i in range(0, len(lst) -1):
        nodes[i].next = nodes[i+1]
    return nodes[0]
       



def test_base_case():
    assert print(reverseList(build_it([1,2]))) == print(ListNode(2,ListNode(1, None)))

def test_longer_example():
    assert print(reverseList(build_it([1,2,3,4]))) == print(ListNode(4,ListNode(3, ListNode(2,ListNode(1, None)))))

def test_empty_list():
    assert print(reverseList(build_it([]))) == print(ListNode(None, None))

def test_single_value():
    assert print(reverseList(build_it([1]))) == print(ListNode(1, None))