import pytest
from collections import deque

def add(one, two):
    return one + two

def subtract(one, two):
    return one - two

def multiply(one, two):
    return one * two

def divide(one, two):
    return one/two

def postfix_calculator(expression: str) -> float:
    
    # we'll want a stack import deque, stack = deque()
    operator_dict = {
        '+' : add,
        '-' : subtract,
        '*' : multiply,
        '/' : divide
    }
    operators = set(['+', '-', '/', '*'])
    stack = deque()
    # for term in expression.split(' ')
    for term in expression.split(' '):
        # if term == '+'
        if term in operators:
            #  pop two values off the stack
            number_two = stack.pop()
            # number_one/two = stack.pop()
            number_one = stack.pop()
            # funct = map[term]
            # stack.append(funct(number_one, number_two))
            operator = operator_dict[term]
            stack.append(operator(number_one, number_two))
            # if term == '+':
            #    stack.append(number_one + number_two)
            # elif term == '-':
            #    stack.append(number_one - number_two)
            # elif term == '*':
            #     stack.append(number_one * number_two)
            # elif term == '/':
            #     stack.append(number_one / number_two)
        else:
            # elif float(term) is a number
            # push onto the stack
            number = float(term)
            stack.append(number)
    return stack.pop()
        
       
        

def test_two_numbers_addition():
    assert postfix_calculator('24 2 +') == 26


def test_ints_multiple_operations():
    assert postfix_calculator('3 2 1 + + 2 /') == 3

def test_raises_error_invalid_input():
    with pytest.raises(IndexError):
        postfix_calculator('2 +') 

def test_floats_multiple_operations():
    assert postfix_calculator('6.9 3 / 3.2 + 7 -') == -1.5