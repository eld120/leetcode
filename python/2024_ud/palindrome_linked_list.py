'''
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'val: {self.val}, next: {self.next}'
    def __repr__(self) -> str:
        return f'val: {self.val}, next: {self.next}'

def isPalindrome( head: Optional[ListNode]) -> bool:
    if not head.next:
        return True
    
    numbers = []
    while head and head.next:
        
        numbers.append(head.val)
        head = head.next
    numbers.append(head.val)
    breakpoint()
    return numbers == [num for num in reversed(numbers)]


def test_one():
    assert isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))) == True

def test_two():
    assert isPalindrome(ListNode(1, ListNode(2, None))) == False