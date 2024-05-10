from typing import List

from collections import Counter


def majorityElement(nums: List[int]) -> int:
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

    Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    """

    return Counter(nums).most_common(1)[0][0]


def majority_element(nums: List[int]) -> int:
    # O(1) space because the allocation of a tuple of 2 ints is constant regardless of the size of the input
    if len(nums) == 1:
        return nums[0]
    nums.sort()
    fast = 1
    most_common = [0, 0]
    for index, num in enumerate(nums):
        if index < len(nums) - 1 and num != nums[fast]:
            backtrack = index
            current_count = 0
            while nums[index] == nums[backtrack]:
                current_count += 1
                backtrack -= 1
            if current_count >= most_common[1]:
                most_common = [nums[index], current_count]
        elif index == len(nums) - 1:
            # breakpoint()
            backtrack = index
            current_count = 0
            while backtrack > -1 and nums[index] == nums[backtrack]:
                current_count += 1
                backtrack -= 1
            if current_count >= most_common[1]:
                most_common = [nums[index], current_count]
        fast += 1
    return most_common[0]


def test_majority_element_one():
    assert majority_element([3, 2, 3]) == 3


def test_majority_element_two():
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element_three():
    assert majority_element([1]) == 1


def test_two_length():
    assert majority_element([2, 2]) == 2


# def test_majority_element_four():
#     assert majorityElement()
