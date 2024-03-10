from typing import List


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    even slower than the original due to the extra list/enumerate generation plus On**2 time complexity
    """
    result = None
    slow = 0
    fast = 1
    index = 0
    value = 1
    nums = sorted(enumerate(nums))
    while result != target:
        try:
            result = nums[slow][value] + nums[fast][value]
            if target > 1:
                if result == target:
                    return [nums[slow][index], nums[fast][index]]
                # elif result < target:
                #    fast += 1
                else:
                    # slow += 1
                    # fast = slow + 1
                    fast += 1
            else:
                if result == target:
                    return [nums[slow][index], nums[fast][index]]
                # elif result > target or nums[slow][value] + nums[fast][value] > target:
                #     fast += 1
                else:
                    # slow += 1
                    # fast = slow + 1
                    fast += 1
        except IndexError:
            slow += 1
            fast = slow + 1
        if slow >= len(nums):
            break


def test_one():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_two():
    assert twoSum([3, 2, 4], 6) == [1, 2]


def test_three():
    assert twoSum([3, 3], 6) == [0, 1]


def test_four():
    assert twoSum([3, 2, 3], 6) == [0, 2]


def test_five():
    assert twoSum([0, 4, 3, 0], 0) == [0, 3]


def test_six():
    assert twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_seven():
    assert twoSum([0, 3, -3, 4, -1], -1) == [0, 4]


def test_eight():
    assert twoSum([3, 2, 95, 4, -3], 92) == [2, 4]


def test_nine():
    assert twoSum([0, 3, -3, 4, -1], -1) == [0, 4]


if __name__ == "__main__":
    twoSum([-1, -2, -3, -4, -5], -8)
