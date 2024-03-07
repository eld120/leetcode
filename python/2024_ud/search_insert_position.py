'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    '''
    Input: nums = [1], target = 2
    Output: 2
    '''
    # if len(nums) == 1 and target > nums[0]:
    #     return 1
    # elif len(nums) == 1:
    #     return 0

    left = 0
    right = len(nums)

    while left < right:
        midpoint = (left + right) // 2
        # if nums[midpoint] == target:
        #     return midpoint
        if target > nums[midpoint]:
            left = midpoint + 1
        else:
            right = midpoint

    return left # something
    # if nums[midpoint] > target:
    #     return midpoint
    # else:
    #     return midpoint + 1
    

def test_number_within_list():
    assert searchInsert([1,3,5,6], 5) == 2

def test_number_not_within_list():
    assert searchInsert([1,3,4,6,7], 5) == 3

def test_number_not_within_list_2():
    assert searchInsert([1,3,5,7,9], 4) == 2

def test_list_of_length_one():
    assert searchInsert([2], 1) == 0
    assert searchInsert([1], 5) == 1

def test_case_two():
    assert searchInsert([1,3,5,6], 2) == 1