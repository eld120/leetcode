# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# def hasCycle(self, head: Optional[ListNode]) -> bool:



def detectCycle(head):
    # hilariously slow compared to the majority of implementations but still O(1)
    library = tuple()
    while head is not None:
        if id(head) in library:
            return True
        if head.next is None:
            return False
        library += (id(head),)
        head = head.next
    return False    

def detectCycle(head):
    # way faster but a little more memory allocation (not much)
    library = set()
    while head is not None:
        if id(head) in library:
            return True
        if head.next is None:
            return False
        library |= {id(head),}
        head = head.next
    return False    