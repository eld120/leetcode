'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

Seen this question in a real interview before?
1/4
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f'val: {self.val}, next: {self.next}'

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    '''
    initialize the set with head.val
    check if the next value is in the set
    vars
        head
        current
        next
    continue until next is None
    return head
    [1,1,2]
    '''
    
    duplicates = set()
    if not head:
        return head
    else:
        duplicates.add(head.val)
    #breakpoint()
    current = head
    while current:
        # [1,1,2]
        if current.next:
            if current.next.val not in duplicates:
                duplicates.add(current.next.val)
                current = current.next
            else:
                second = current.next
                if current.next.next:
                    current.next = second.next
                    second = None
                else:
                    current.next = None
        else:
            break
        
    return head




