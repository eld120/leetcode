'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
from typing import Optional

class ListNode:
    def __init__(self, val, next) -> None:
        self._val = val
        self._next = next


def middleNode( head: Optional[ListNode]) -> Optional[ListNode]:
    fast = head
    slow = head
    while fast:
        
        if fast.next:    
            fast = fast.next.next
        else:
            return slow
        slow = slow.next
    return slow

