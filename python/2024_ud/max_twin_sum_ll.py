from collections import deque

from data_structures import ListNode, ll_builder


def pair_sum_ll(head: ListNode) -> int:
    stack = deque()
    length = 0
    current = head
    while current:
        length += 1
        current = current.next_node
    pop_off_point = length // 2
    highest_sum = 0
    #breakpoint()
    current = head
    while current:
        if pop_off_point > 0:
            stack.append(current.val)
            pop_off_point -= 1
        else:
            current_sum = stack.pop() + current.val
            highest_sum = max(current_sum, highest_sum )
            
        current = current.next_node
    return highest_sum


def test_one():
    assert pair_sum_ll(ll_builder([5,4,2,1])) == 6


def test_two():
    assert pair_sum_ll(ll_builder([4,2,2,3])) ==  7