from collections import Counter

def contains_dup(nums: list[int], k: int) -> bool:
    '''
    Given an integer array nums and an integer k, return true 
    if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
    Input: nums = [1,2,3,1], k = 3
    Output: true
    '''
    if len(nums) < 2:
        return False
    indices = dict()

    for index, val in enumerate(nums):
        if val not in indices:
            indices[val] = [index]
        else:
            if abs(indices[val][-1] - index) <= k:
                return True
            indices[val] += [index]
    return False
