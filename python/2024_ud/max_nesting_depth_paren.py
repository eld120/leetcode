


def max_depth( s: str) -> int:

    def recurse(string: str, counter: int = 0, max_count: int = 0) -> int:
        # if ( counter = 0
        # if ) counter += 1  max_count = max(counter, max_count)
        if len(string) == 0:
            return max_count
        char = string[0]
        if char == '(':
            counter = 0
        elif char == ')':
            counter += 1
            max_count = max(counter, max_count)
        
        return recurse(string[1:], counter, max_count)
    return recurse(s)

from collections import deque
def m_depth(s: str) -> int:
    stack = deque()
    max_length = 0
    for char in s:
        if char == '(':
            stack.appendleft(char)
        elif char == ')':
            stack.popleft()
        max_length = max(max_length, len(stack))
    return max_length

def no_new_ds(s):
    ''' same shit as above but creating a stack is a lot slower than just incrementing/decrementing a pointer by a lot '''
    longest = 0
    max_length = 0
    for char in s:
        if char == '(':
            longest += 1
        elif char == ')':
            longest -= 1
        max_length = max(max_length, longest)
    return max_length



def test_one():
    assert no_new_ds("(1+(2*3)+((8)/4))+1") ==3

def test_nested_parens():
    assert no_new_ds("8*((1*(5+6))*(8/6))") == 3