class ListNode:
    def __init__(self, val=None, nxt=None) -> None:
        self.val = val
        self.nxt = nxt

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"val:{self.val} next:{self.nxt}"

    def __eq__(self, __value: object) -> bool:
        return self.__repr__() == __value.__repr__()


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, new_val):
        """add item to end of queue"""
        if self.head:
            self.tail.nxt = ListNode(new_val, None)
            self.tail = self.tail.nxt
        else:
            self.head = ListNode(new_val, None)
            self.tail = self.head

    def remove(self):
        """remove first item from queue"""
        if self.head:
            temp = self.head.nxt
            self.head.nxt = None
            self.head = temp
        else:
            raise ValueError("Queue is Empty")

    def peek(self):
        """return the top of the queue"""
        return self.head.val

    def is_empty(self):
        """returns true if the queue is empty"""
        return True if self.head is None and self.head is None else False


def test_is_empty():
    new_queue = Queue()
    assert new_queue.is_empty() is True
    new_queue.add(1)
    assert new_queue.is_empty() is False


def test_peek_and_add():
    new_q = Queue()
    for val in range(1, 4):
        new_q.add(val)
        assert new_q.peek() == 1
    assert new_q.peek() == 1


def test_remove():
    new_q = Queue()
    for val in range(1, 4):
        new_q.add(val)
        assert new_q.peek() == 1
    new_q.remove()
    assert new_q.peek() == 2
    new_q.remove()
    assert new_q.peek() == 3
    assert new_q.is_empty() is False
    new_q.remove()
    assert new_q.is_empty() is True
