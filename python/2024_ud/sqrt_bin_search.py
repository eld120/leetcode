'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
'''
import math, decimal

def mySqrt(x: int) -> int:
    # binary search boilerplate: low = 0, high = x 
    if x == 1 or x == 0:
        return x
    low = 1
    high = x - .001
    # looping condition low <= high
    midpoint = (low + high) / 2
    while low <= high:
        # midpoint = low + high / 2
        midpoint = (low + high) /2
        # midpoint * midpoint == x?
        square = midpoint * midpoint
        # if square == x:
        #     return math.floor(midpoint)
        # measuring whether our midpoint higher or lower than target
        if x < square:
            high = midpoint - .00000000001
        else:
            low = midpoint + .0000001
    #return midpoint
    return math.floor(low)


def test_four():
    assert mySqrt(4) == 2

def test_eight():
    assert mySqrt(8) == 2

def test_big():
    assert mySqrt(54721) == 233

def test_two():
    assert mySqrt(2) == 1

def test_zero():
    assert mySqrt(0) == 0

def test_nine():
    assert mySqrt(9) == 3

def test_bigger_num():
    assert mySqrt(2147395599) == 46339

def test_thirty_six():
    assert mySqrt(36) == 6

def test_1024():
    assert mySqrt(1024) == 32