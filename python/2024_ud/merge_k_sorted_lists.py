from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        return self.__str__() == value.__str__()

def mergeKLists( lists: list[Optional[ListNode]]) -> Optional[ListNode]: # [1,1,2,3,4,4,5,6]
    if len(lists) < 2 and lists:
        return lists[0]
    def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
        #breakpoint()
        head = None
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        current = head
        while list2 or list1:
            if list2 and list1:
                if list2.val > list1.val:
                    current.next = list1
                    list1 = list1.next
                    current = current.next
                else:
                    current.next = list2
                    list2 = list2.next
                    current = current.next
            elif list1:
                current.next = list1
                break
            else:
                current.next = list2
                break
        #breakpoint()
        return head
    
    new_lists = []
    current_lists = lists
    while len(current_lists) > 1:
        for index in range(0, len(current_lists),2):
            try:
                new_lists.append( merge_two_lists(current_lists[index], current_lists[index + 1]))
                current_lists = current_lists[index+2:]
            except IndexError:
                
                new_lists.append(current_lists[-1])
    if len(new_lists) > 1:
        new_lists = [merge_two_lists(new_lists[0], new_lists[1])]
        
    
    if len(new_lists) > 0:
        return new_lists[0]
    return None



def ll_builder(array):
    head = ListNode()
    current = head
    for index, val in enumerate(array):
        current.val = val
        if index == len(array) -1:
            break
        
        current.next = ListNode()
        current = current.next
    return head


def test_one():
    ll = [ll_builder([1,4,5]),ll_builder([1,3,4]),ll_builder([2,6])]
    assert mergeKLists(ll) == ll_builder([1,1,2,3,4,4,5,6])




import heapq
def solution_two(lists):
    heapy = []
    heapq.heapify(heapy)
    for head in lists:
        current = head
        while current is not None:
            heapq.heappush(heapy, current.val)
            current = current.next
    head = ListNode()
    curr = head
    while heapy:
        curr.next = ListNode(heapq.heappop(heapy))
        curr = curr.next
    return head.next


def test_on2e():
    ll = [ll_builder([1,4,5]),ll_builder([1,3,4]),ll_builder([2,6])]
    assert mergeKLists(ll) == ll_builder([1,1,2,3,4,4,5,6])