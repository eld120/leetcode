"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

# Definition for singly-linked list.
# class ListNode:
#     # lol not iterable
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"self.val = {self.val}"

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            do_recursive_stuff(self.head, node)

    def __str__(self) -> str:
        self.head.__str__


def do_recursive_stuff(head, new_node=None):
    if head.next is not None:
        do_recursive_stuff(head.next, new_node)
    else:
        head.next = new_node
        return head


def setup_ll(data):
    linked_list = LinkedList()
    for val in data:
        linked_list.add_node(Node(val))
    return linked_list.head


def do_reverse(linked_list, previous=None):
    if linked_list.next is None:
        # print(f"last:{linked_list.val}")
        linked_list.next = previous
        print(linked_list.next)
        print(linked_list)
        return linked_list
    else:
        new_node = linked_list.next
        linked_list.next = previous
        print(linked_list.next)
        # print(f"current:{linked_list.val}, next:{new_node.val}")
        # breakpoint()
        do_reverse(new_node, linked_list)


def reverse_ll(l_list):
    
    if l_list is not None:
        do_reverse(l_list)
    else:
        print("else clause")
        
        return l_list


test_data = [1, 2, 3, 4, 5]
# expected output =  [5,4,3,2,1]

test_data_two = [1, 2]
# expected output = [2, 1]

test_data_three = []
# expected output = []

def reversy(head):
    # 1st
    pointer = head
    final = None
    while head is not None:
        # 2nd / move 2nd to next
        next = pointer.next
        # set new LL 
        head.next = final
        # move pointer on new LL
        final = pointer
        #breakpoint()
        pointer = next
        head = next
        print(final)
        
    return final



if __name__ == "__main__":
    # reverse_ll(setup_ll(test_data))
    reversy(setup_ll(test_data))