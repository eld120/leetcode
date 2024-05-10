"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

from typing import List


def jump_game(nums) -> bool:
    """
    need to figure out if we can jump to the end quickly

    """
    can_jump = True
    if 0 not in set(nums) or len(nums) == 1:
        return can_jump
    zero_list = []

    index = 0
    # iterate through nums
    for val in nums:
        # breakpoint()
        # when we come to a zero in nums start to backtrack

        if val == 0 and index < len(nums) - 1:
            can_jump = False
            zero_list.append(index)
            if len(zero_list) > 1:
                backtrack_index = zero_list[-2] + 1
            else:
                backtrack_index = 0
            steps_to_zero = index
            # breakpoint()

            while steps_to_zero > backtrack_index:
                # breakpoint()
                # want to compare steps to zero with value at a specific index
                if nums[backtrack_index] > steps_to_zero and index < len(nums) - 1:
                    can_jump = True
                elif nums[backtrack_index] >= steps_to_zero and index == len(nums) - 1:
                    can_jump = True
                if nums[backtrack_index] >= len(nums) - 1 - backtrack_index:
                    return True
                steps_to_zero -= 1
                backtrack_index += 1
                # breakpoint()
                if not can_jump:
                    return can_jump

        index += 1

    return can_jump


def jump_two(rando_list: List[int]) -> bool:
    """
    need to determine if there's a way to jump to the last index based on the values within the list
    ex:
    [3, 2, 1, 0, 4] -> False
    [0] -> True
    [1,0] -> True
    [2,0,0] -> True
    """
    jumps = 0
    index = 0
    for val in rando_list:
        if jumps < val:
            jumps = val
        if val == 0 and jumps < 1 and len(rando_list) - 1 > index:
            return False

        jumps -= 1
        index += 1
    return True


def test_one():
    assert jump_two([2, 3, 1, 1, 4]) == True


def test_two():
    assert jump_two([3, 2, 1, 0, 4]) == False


def test_three():
    assert jump_two([2, 0]) == True


def test_four():
    assert jump_two([2, 5, 0, 0]) == True


def test_five():
    assert jump_two([0]) == True


def test_six():
    assert jump_two([1, 1, 1, 0]) == True


def test_seven():
    assert jump_two([1, 0, 1, 0]) == False


def test_eight():
    assert jump_two([2, 0, 1, 0, 1]) == False


def test_nine():
    # not handled
    assert jump_two([1, 2, 0, 1]) == True


def test_not_handled():
    # not handled
    assert jump_two([3, 0, 0, 0]) == True
