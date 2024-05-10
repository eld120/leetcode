"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 105

"""
from typing import List


def trap(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    total_area = 0
    l_max = 0
    r_max = 0
    while left < right:
        # start counting as ssoon as we encounter a non zero integer
        # can't hold volume if integer

        # breakpoint()
        if height[left] > height[right]:
            if height[right] > r_max:
                r_max = height[right]

            total_area += r_max - height[right]
            right -= 1

        else:
            if height[left] > l_max:
                l_max = height[left]
            total_area += l_max - height[left]
            left += 1

    return total_area


# [0,2,1,2,0]
#


def test_single_value():
    assert trap([1]) == 0


def test_smallest_possible_pool():
    assert trap([1, 0, 1]) == 1


def test_also_smallest_pool():
    assert trap([3, 2, 3]) == 1


def test_small_but_long_pool():
    assert trap([0, 2, 1, 2, 0]) == 1


def test_uneven_walls():
    assert trap([3, 1, 2]) == 1


def test_leetcode_one():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_leetcode_two():
    assert trap([4, 2, 0, 3, 2, 5]) == 9
