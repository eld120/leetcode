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
from typing import Optional, List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    ''' Linked List'''
    def __init__(self, val=0, nxt = None) -> None:
        self.val = val
        self.next = nxt

    def __repr__(self) -> str:
        return f'val:{self.val} - next:{self.next}'

    def __str__(self) -> str:
        return f'val:{self.val} - next:{self.next}'
    
    def __eq__(self, other):
        one = self.__repr__()
        two = other.__repr__()
        return one == two
        


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
    #breakpoint()
        
    
    result_tail = None # make the linter shut up
    while list1_pointer is not None and list2_pointer is not None:
        #breakpoint()
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




def build_linked_list(lst_input: List) -> ListNode:
    head = ListNode()
    current = head
    for index, val in enumerate(lst_input):
        current.val = val
        if index != len(lst_input) -1:
            current.next = ListNode()
            current = current.next
    #breakpoint()
    return head

def merge_ll_again(ll_one: ListNode, ll_two:  ListNode) -> ListNode:
    '''use recursion to merge two linked lists'''
    head = ListNode()
   
    current = head
    def merge(one: ListNode, two: ListNode, current: ListNode, head) -> None:
       # breakpoint()
        if not one and not two:
            return head.next
        current.next = ListNode()
        current = current.next
        if one and two:
            if one.val > two.val:
                current.val = two.val
                two = two.next
            else: 
                current.val = one.val
                one = one.next
        elif one:
            current.val = one.val
            one = one.next
        else:
            current.val = two.val
            two = two.next
        
        return merge(one, two, current, head)
    return merge(ll_one,ll_two, current, head)



def test_build_linked_list():
    ''' [] -> ListNode'''
    assert build_linked_list([1,2,3]) == ListNode(1, ListNode(2, ListNode(3, None)))
    assert build_linked_list([1,2,3]) != ListNode(1, ListNode(1, ListNode(3, None)))
    assert build_linked_list([]) == ListNode()

def test_one_second():
    assert merge_ll_again(build_linked_list([1,2,4]), build_linked_list([1,3,4])) == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None))))))
test_one_second()                                                  
def test_second_empty():
    assert merge_ll(None, None) is None

def test_unequal_length_second():
    assert merge_ll(None, build_linked_list([1,4])) == build_linked_list([1,4])

def test_single_value_ll():
    assert merge_ll(build_linked_list([1]), build_linked_list([3])) == ListNode(1, ListNode(3, None))

def test_single_and_empty():
    assert merge_ll(None, build_linked_list([1])) == build_linked_list([1])