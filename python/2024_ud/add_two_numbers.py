'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class ListNode:
    '''shitty listnode class'''
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt
    
    def __str__(self):
        return f'val: {self.val}, next: {self.next}'
    
    def __repr__(self):
        return f'val: {self.val}, next: {self.next}'


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.



    '''
   
    head = ListNode()
    tail = head
    while l1 and l2:
        if not l1.next and not l2.next:
            if l1.val + l2.val > 9:
                tail.val = l1.val + l2.val -10
                temp = ListNode(1, None)
                tail.next = temp
                
                return tail
            return ListNode(l1.val + l2.val, None) 
        elif not l1.next:
            if l1.val + l2.val > 9:
                tail.val = l1.val + l2.val - 10
                l1.val = 1
                tail.next = ListNode(0, None)
                tail = tail.next
            else:
                tail.val = l1.val + l2.val
                l2 = l2.next
                tail.next = l2
                return head
        elif not l2.next:
            if l1.val + l2.val > 9:
                tail.val = l1.val + l2.val - 10
                l2.val = 1
                tail.next = ListNode(0, None)
                tail = tail.next
            else:
                tail.val = l1.val + l2.val
                l1 = l1.next
                tail.next = l1
                return head
            

def add_two_linked_lists(l1: ListNode, l2: ListNode) -> ListNode:
    '''
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

    Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
    '''
    if l1 is None and l2 is None:
        return l1
    elif l1 is  None :
        return l2
    elif l2 is None :
        return l1
    
    previous = ListNode()
    ret = previous
    while l1 is not None or l2 is not None:
        # try to create the new node then attach to LL rather than in place mutation
        current = ListNode()
        if l1 is None:
            if previous.val + l2.val > 9:
                previous.val += l2.val - 10
                current.val = 1
            else:
                previous.val += l2.val
                
            if l2.next is not None or current.val > 0:
                l2 = l2.next
                previous.next = current
                previous = previous.next
            else:
                return ret
        elif l2 is None:
            if previous.val + l1.val > 9:
                previous.val += l1.val - 10
                current.val = 1
            else:
                previous.val += l1.val 

            if l1.next is not None or current.val > 0:
                l1 = l1.next
                previous.next = current
                previous = previous.next
            else:
                return ret
        else:
            previous.val += l1.val + l2.val
            if previous.val > 9:
                previous.val -= 10
                current.val = 1
            if l1.next is not None or l2.next is not None or current.val > 0:
                previous.next = current
                previous = previous.next
            l1 = l1.next
            l2 = l2.next
    return ret

def listnode_builder(list_of_ints: List) -> ListNode:
    '''
    creates a linked list/listnode from a list of values
    '''
    head = ListNode()
    current = head
    for index, val in enumerate(list_of_ints):
        if index < len(list_of_ints) -1:
            current.val = val
            current.next = ListNode()
            current = current.next
        else:
            current.val = val
            current.next = None
    return head



def test_one():
    ''' 
    l1 = [2,4,3], l2 = [5,6,4]
    expected = [7,0,8]
    
    '''
    assert add_two_linked_lists(listnode_builder([2,4,3]), listnode_builder([5,6,4])) == listnode_builder([7,0,8])

def test_nine_nine_one():
    ''' 
    l1 = [9,9,1], l2 = [1]
    expected = [0, 0, 2]
    '''
    assert add_two_linked_lists(listnode_builder([9,9,1]), listnode_builder([1])) == listnode_builder([0, 0, 2])

def test_list_of_nines():
    '''
    l1 = [9], l2 = [1,9,9,9,9,9,8,9,9,9]
    expected  = [0,0,0,0,0,0,9,9,9]
    '''
    assert add_two_linked_lists(listnode_builder([9]), listnode_builder([1,9,9,9,9,9,8,9,9,9])) == listnode_builder([0,0,0,0,0,0,9,9,9])

def test_long_things():
    '''
    l1 = [0,8,6,5,6,8,3,5,7], l2 = [6,7,8,0,8,5,8,9,7]
    expected = [6,5,5,6,4,4,2,5,5,1]
    '''
    assert add_two_linked_lists(listnode_builder([0,8,6,5,6,8,3,5,7]), listnode_builder([6,7,8,0,8,5,8,9,7])) == listnode_builder([6,5,5,6,4,4,2,5,5,1])

# def adding_lls(l1: ListNode, l2: ListNode) -> ListNode:
#     '''
#     more shitty LL stuff
#     '''
#     if not l1 and not l2:
#         return l1
#     elif not l1:
#         return l2
#     elif not l2:
#         return l1
    
#     current = ListNode()
#     head = current
    
#     while l1 or l2:
#         if not l1.next and l2.next:
#             current.val = l1.val + l2.val
#             if current.val > 9:
#                 current.val -= 10
#                 current.next = ListNode(1, None)
#             return head
#         elif not l1.next:
#             current.val = l1.val + l2.val 
#             if current.val > 9:
#                 current.val -= 10
#                 current.next = ListNode(1, None)
#                 prev = current
#                 current = current.next
#             else:
#                 current.next = l2.next
#                 return head
#         elif not l2.next:
#             current.val = l1.val + l2.val 
#             if current.val > 9:
#                 current.val -= 10
#                 current.next = ListNode(1, None)
#                 current = current.next
#             else:
#                 current.next = l1.next
#                 return head
#         else:
#             temp = ListNode(l1.val + l2.val, None)
#             if temp.val > 9:
#                 temp.val -= 10
#                 temp.next = ListNode(1, None)
#             prev = current

#             current = current.next
test_long_things()

# def test_one():
#     ''' something'''
#     assert adding_lls(ListNode(2, ListNode(4, ListNode(3, None))), ListNode(5, ListNode(6, ListNode(4, None)))) == ListNode(7, ListNode(0, ListNode(8, None)))

#test_one()

# def test_single_value_nodes():
#     assert print(addTwoNumbers(ListNode(3, None), ListNode(5, None))) == print(ListNode(8, None))
#     assert print(addTwoNumbers(ListNode(6, None), ListNode(6, None))) == print(ListNode(2, ListNode(1, None)))

# def test_empty_nodes():
#     assert print(addTwoNumbers(ListNode(), ListNode())) == print(ListNode())
#     assert print(addTwoNumbers(ListNode(), ListNode(1, None))) == print(ListNode(1, None))
#     assert print(addTwoNumbers(ListNode(3, None), ListNode())) == print(ListNode(3, None))

# def test_nodes_of_uneven_length():
#     assert print(addTwoNumbers(ListNode(1, ListNode(2, ListNode(3, None))), ListNode(4, ListNode(5, None)))) == print(ListNode(5, ListNode(7, ListNode(3, None))))


# if __name__ == '__main__':
#     if print(addTwoNumbers(ListNode(), ListNode(2, None))) == print(ListNode(1, None)):
#         print('sure')