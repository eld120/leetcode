'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

example 4:
input: list1 = [1,4], list2 = [3,5,6]
# result_list -> head
# result_tail -> 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'val:{self.val} - next:{self.next}'

    def __str__(self) -> str:
        return f'val:{self.val} - next:{self.next}'
    
    
        


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    example 4:
    input: list1 = [1,4], list2 = [3,5,6]
    # result_list -> head
    # result_tail -> 

    # edge cases to handle
    # if one or both LLs are None
    # while iterating through each LL
        # if one or both LL.next are None
    '''
    list1_pointer = list1
    list2_pointer = list2
    result_list = None
    # handle empty linked lists as input
    if list1_pointer and not list2_pointer:
        result_list = list1_pointer
    elif list2_pointer and not list1_pointer:
        result_list = list2_pointer
    elif list1_pointer and list2_pointer:
        if list1_pointer.val > list2_pointer.val:
            result_list = list2_pointer
        elif list2_pointer.val >= list1_pointer.val:
            result_list = list1_pointer
    else:
        return result_list
    breakpoint()
        
    

    while list1_pointer is not None and list2_pointer is not None:
        breakpoint()
        # handle LLs of unequal lengths
        if list1_pointer.next is None:
            result_tail.next = list2_pointer
            return result_list
        elif list2_pointer.next is None:
            result_tail.next = list1_pointer
            return result_list
        elif list1_pointer.val > list2_pointer.val and list2_pointer.next is not None:
           
            result_tail = list2_pointer
            list2_pointer = list2_pointer.next
        elif list1_pointer.val <= list2_pointer.val and list1_pointer.next is not None:
            
            result_tail = list1_pointer
            list1_pointer = list1_pointer.next
    return result_list
        

    


# def test_one():
#     assert mergeTwoLists(list_one, list_two) == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None))))))

# def test_empty():
#     assert mergeTwoLists(list_three, list_four) is None

# def test_unequal_length():
#     assert mergeTwoLists(list_four, list_five) == ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))



# 2nd implementation
    

def merge_ll(list1: ListNode, list2: ListNode) -> ListNode:
    '''
    ex 3
    input list1 = [], list2 = []
    output = []
    
    example 4:
    input: list1 = [1,4], list2 = [3,5,6]
    output = [1,3,4,5,6]
    '''
     
     
    head = None
    #breakpoint()
    if list1 and list2:
        # if both LLs are not empty
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
    elif list1 and not list2:
        head = list1
        list1 = list1.next
    elif list2 and not list1:
        head = list2
        list2 = list2.next
    else:
        return head
    
    tail = head
    

    # choosing to terminate when we're at the last element in both LLs
    while list1 or list2:
        #breakpoint()
        # handle when we get to the end
        # list1 = [2], list2 = [1]
        # set tail next, set tail to current, increment ll pointer
        if list1 is None:
            tail.next = list2
            return head
        elif list2 is None:
            tail.next = list1
            return head
        
        
        elif list1.next is None and list2.next is None:
           if list1.val > list2.val:
               tail.next = list2
               tail = list2
               list2.next = list1
               return head
           else:
               tail.next = list1
               tail = list1
               list1.next = list2
               return head
        
        elif list1.next is None:
            if list1.val > list2.val:
                tail.next = list2
                tail = list2
                list2 = list2.next
            else:
                tail.next = list1
                tail = list1
                tail.next = list2
                return head
        elif list2.next is None:
            if list2.val > list1.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                tail.next = list1
                return head 
        
        # if one LL is greater than the other, choosing to peek
        elif list1.val > list2.val:
            tail.next = list2
            tail = list2
            list2 = list2.next
        else:
            tail.next = list1
            tail = list1
            list1 = list1.next
    return head

list_one_two_four = ListNode(1, ListNode(2, ListNode(4, None)))
list_one_three_four = ListNode(1, ListNode(3, ListNode(4, None)))

list_also_empty = None
list_empty =  None

list_one_four = ListNode(1, ListNode(4, None))
list_three_five_six  = ListNode(3, ListNode(5, ListNode(6, None)))

single_one = ListNode(1, None)
single_copy = ListNode(1, None)
single_three = ListNode(3, None)

def test_one_second():
    assert str(merge_ll(list_one_two_four, list_one_three_four)) == str(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None)))))))

def test_second_empty():
    assert merge_ll(list_also_empty, list_empty) is None

def test_unequal_length_second():
    assert str(merge_ll(list_empty, list_one_four)) == str(ListNode(1,  ListNode(4,  None)))

def test_single_value_ll():
    assert str(merge_ll(single_one, single_three)) == str(ListNode(1, ListNode(3, None)))

def test_single_and_empty():
    assert str(merge_ll(list_empty, single_copy)) == str(ListNode(1, None) )