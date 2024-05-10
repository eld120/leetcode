from typing import List
from collections import Counter


def contains_nearby_dup(nums: List[int], k: int) -> bool:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

    Input: nums = [1,2,3,1], k = 3
    Output: true
    Input: nums = [1,0,1,1], k = 1
    Output: true
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

    Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105
    """
    left = 0
    right = 0
    count = Counter()
    count[nums[right]] += 1
    while right < len(nums) - 1:
        # breakpoint()
        if right - left < k:
            right += 1
            count[nums[right]] += 1
            if count[nums[right]] > 1:
                return True
        else:
            count[nums[left]] -= 1
            left += 1
    return False


def test_one():
    assert contains_nearby_dup([1, 2, 3, 1, 2, 3], 2) == False
