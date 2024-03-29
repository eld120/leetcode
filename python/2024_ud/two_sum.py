"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    counter = 0
    while counter < len(nums):
        temp = counter + 1
        while temp < len(nums):
            try:
                if nums[counter] + nums[temp] == target:
                    return [counter, temp]
            except IndexError:
                break
            temp += 1
        counter += 1
    return []


def two_sum(nums: List[int], target: int) -> List[int]:
    number_dict = dict()
    # iterate through nums
    # add elements to nums
    # whether result is the value
    for index, val in enumerate(nums):
        result = target - val
        if result in number_dict:
            return [number_dict[result], index]
        number_dict[val] = index
