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
'''

# this is really a recursive problem

def is_valid(s: str) -> bool:
    counter = 0
    while counter < len(s):
        #breakpoint()
        if s[counter] == "(" and s[counter + 1] == ")":
            counter += 1
            if counter + 1 == len(s):
                print(True)
                return True
            continue
        elif s[counter] == "[" and s[counter + 1] == "]":
            counter += 1
            if counter + 1 == len(s):
                print(True)
                return True
            continue
        elif s[counter] == "{" and s[counter + 1] == "}": 
            counter += 1
            if counter + 1 == len(s):
                print(True)
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
            print(False)
            return False
    


def try_again(s: str) -> bool:

    # if encounter an opening parentheses go recursive
    for val in s:
        if val == any('({['):
            recurse()
    # if encounter the correct closing parentheses happy base case


def recurse(iterab):
    if val == any('({['):
        pass

test_one = "()"
test_two = "{}"
test_three = "[]"
test_four = '()[]{}'
test_five = "{[]}"

if __name__ == '__main__':
    is_valid(test_five)