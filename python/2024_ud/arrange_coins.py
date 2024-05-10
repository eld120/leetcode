"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1
"""


def arrangeCoins(n: int) -> int:
    increment = 1
    while n > increment:
        n -= increment
        increment += 1
    return increment - 1


def test_five():
    assert arrangeCoins(5) == 2


def test_eight():
    assert arrangeCoins(8) == 3
