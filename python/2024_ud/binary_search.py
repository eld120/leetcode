"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)

    while low < high:
        midpoint = (high + low) // 2
        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            high = midpoint
        else:
            low = midpoint + 1
    return -1


def test_one():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4


test_one()


def test_two():
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_single_val_list():
    assert search([1], 1) == 0


def test_empty():
    assert search([], 1) == -1


def test_last_index():
    assert search([-1, 0, 3, 5, 9, 12, 15], 15) == 6
    assert search([-5, -3, -1, 0, 3, 5, 9, 12, 15, 20], 20) == 9
    assert search([-5, -3, -1, 0, 3, 5, 9, 12, 15], 15) == 8


def test_first_index():
    assert search([-1, 0, 3, 5, 9, 12, 15], -1) == 0
    assert search([-5, -3, -1, 0, 3, 5, 9, 12, 15, 20], -5) == 0


def test_second_index():
    assert search([-5, -3, -1, 0, 3, 5, 9, 12, 15, 20], -3) == 1
    assert search([1, 2, 3], 2) == 1
    assert search([2, 4], 4) == 1
