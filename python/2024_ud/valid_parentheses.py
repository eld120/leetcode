'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


previous ans:
 counter = 0
        while counter < len(s):
            if s[counter] == "(" and s[counter + 1] == ")":
                counter += 1
                if counter + 1 == len(s):
                    return True
                continue
            elif s[counter] == "[" and s[counter + 1] == "]":
                counter += 1
                if counter + 1 == len(s):
                    return True
                continue
            elif s[counter] == "{" and s[counter + 1] == "}": 
                counter += 1
                if counter + 1 == len(s):
                    return True
                continue
            elif s[counter] == ")" and s[counter - 1] == "(":
                counter += 1
                continue
            elif s[counter] == "}" and s[counter - 1] == "{":
                counter += 1
                continue
            elif s[counter] == "]" and s[counter - 1] == "[":
                counter += 1
                continue
            else:
                return False
        return True
'''

from collections import deque, Counter


def is_valid(s: str) -> bool:
    # reasons to return False
    # if we don't have an even number of chars 
    count = Counter(s)
    if count['{'] != count['}'] or count['['] != count[']'] or count['('] != count[')']:
        return False


    lst = deque()
    allowed_pairs = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    index = 0
    for val in s:
        if val in '({[':
            lst.append(val)
        elif index == 0:
            return False
        else:
            try:
                last = lst.pop()
                if val != allowed_pairs[last]:
                    return False
            except IndexError:
                return False
        index += 1
    return True


    
        



def test_one():
    assert is_valid('()') == True


def test_two():
    assert is_valid("()[]{}") == True

def test_three():
    assert is_valid("(]") == False

def test_four():
    assert is_valid("([)]") == False

def test_five():
    assert is_valid('[{()]}') == False

def test_six():
    assert is_valid("(){}}{") == False