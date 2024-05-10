from collections import deque


def remove_stars(s: str) -> str:
    stack = deque()
    for char in s:
        if char == "*":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


def test_one():
    assert remove_stars("leet**cod*e") == "lecoe"


def test_two():
    assert remove_stars("erase*****") == ""
