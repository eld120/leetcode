from data_structures import ListNode, ll_builder


def reorder_list(head: ListNode):
    # general pattern first, last, second, second last etc
    index_tracker = dict()
    current = head
    index = 0
    #breakpoint()
    while current:
        index_tracker[index] = current
        current = current.next
        index += 1

    length = len(index_tracker) -1
    forward_pointer = 1
    reverse_pointer = length
    current = head

    for index, node in enumerate(index_tracker.values()):
        if index == length:
            current.next = None
        elif index % 2 == 0:
            current.next = index_tracker[reverse_pointer]
            reverse_pointer -= 1
        else:
            current.next = index_tracker[forward_pointer]
            forward_pointer += 1
        current = current.next
    return head


def test_one():
    assert reorder_list(ll_builder([1,2,3,4])) == ll_builder([1,4,2,3])

test_one()