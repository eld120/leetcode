"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""
from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    # binary search on array checking num and num + index or num - index for an equivalent value, return the value that does not have a matching +- value
    # [1,2,2,4,4] vs [1,1,2,2,4]  example[1,1,2,3,3] and [1,1,2,2,3,4,4]
    # [1,2,2] vs [2,2,4]
    # [1,1,2]
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums)

    while len(nums[left:right]) > 3:
        breakpoint()
        midpoint = (left + right) // 2
        if nums[midpoint] == nums[midpoint - 1]:
            if midpoint % 2 == 0:
                right = midpoint
            else:
                left = midpoint + 1
        elif (
            nums[midpoint - 1] != nums[midpoint]
            and nums[midpoint + 1] != nums[midpoint]
        ):
            return nums[midpoint]
        else:
            if midpoint % 2 == 0:
                left = midpoint + 1
            else:
                right = midpoint

    if len(nums[left:right]) == 2:
        if nums[left - 1] == nums[left]:
            return nums[left + 1]
        else:
            return nums[left]
    elif len(nums[left:right]) == 1:
        return nums[left]
    if nums[left] == nums[left + 1]:
        return nums[left + 2]
    else:
        return nums[left]


"""



[1,1,2,2,3,3,4]
[1,1,2,3,3,4,4]
[1,1,2,2,3,4,4]
[1,1,2,2,3,3,4]

[1,1,2,3,3]
[1,2,2,3,3]
[1,1,2,2,3]
"""


def test_one():
    assert singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10


def test_two():
    assert singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2


def test_single_value():
    assert singleNonDuplicate([1]) == 1


def test_length_five():
    assert singleNonDuplicate([1, 1, 2, 2, 3]) == 3
    assert singleNonDuplicate([1, 2, 2, 3, 3]) == 1


def test_longer():
    assert singleNonDuplicate([1, 1, 2, 2, 4, 4, 5, 5, 9]) == 9


def test_wrong_answer():
    assert singleNonDuplicate([0, 1, 1, 2, 2, 5, 5]) == 0
