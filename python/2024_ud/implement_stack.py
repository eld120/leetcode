class ListNode:
    def __init__(self, val=None, nxt=None) -> None:
        self.val = val
        self.nxt = nxt

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"val:{self.val} - next:{self.nxt}"

    def __eq__(self, __value: object) -> bool:
        return self.__repr__() == __value.__repr__()


class Stack:
    def __init__(self) -> None:
        self.head = ListNode()

    def pop(self) -> None:
        """removes/returns val at the top of the stack"""
        nxt = self.head.nxt
        self.head.nxt = None
        val = self.head.val
        self.head = nxt
        return val

    def push(self, incoming) -> None:
        """pushes a new value to the top of the stack"""
        nxt = self.head
        self.head = ListNode(incoming, nxt)

    def peek(self):
        """returns the value at the top of the stack"""
        return self.head.val

    def is_empty(self) -> bool:
        """returns true if the stack is empty"""
        return True if self.head.val is None and self.head.nxt is None else False


def test_is_empty_happy_path():
    assert Stack().is_empty() is True


def test_push():
    new_stack = Stack()
    for val in range(1, 4):
        new_stack.push(val)
    assert new_stack.peek() == 3


def test_pop():
    new_stack = Stack()
    for val in range(1, 4):
        new_stack.push(val)
    assert new_stack.pop() == 3
    assert new_stack.pop() == 2
    assert new_stack.pop() == 1
    assert new_stack.is_empty() is True


def test_peek():
    new_stack = Stack()
    for val in range(0, 5):
        new_stack.push(val)
        assert new_stack.peek() == val
    assert new_stack.peek() == 4
