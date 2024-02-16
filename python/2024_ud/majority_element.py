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


def test_majority_element_one():
    assert majorityElement([3, 2, 3]) == 3


def test_majority_element_two():
    assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element_three():
    assert majorityElement([1]) == 1


# def test_majority_element_four():
#     assert majorityElement()
