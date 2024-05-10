from data_structures import ListNode, ll_builder


def reorder_list(head: ListNode):
    # general pattern first, last, second, second last etc
    index_tracker = dict()
    current = head
    index = 0
    # breakpoint()
    while current:
        index_tracker[index] = current
        current = current.next
        index += 1

    length = len(index_tracker) - 1
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


def reorder_faster(head: ListNode):
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    forward_pointer = 1
    reverse_pointer = len(nodes) - 1
    index = 0
    current = head
    for _ in nodes:
        if index == len(nodes) - 1:
            current.next = None
        elif index % 2 == 0:
            current.next = nodes[reverse_pointer]
            reverse_pointer -= 1
        else:
            current.next = nodes[forward_pointer]
            forward_pointer += 1
        current = current.next
        index += 1
    return head


def test_one():
    assert reorder_faster(ll_builder([1, 2, 3, 4])) == ll_builder([1, 4, 2, 3])
