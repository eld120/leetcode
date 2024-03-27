from typing import List



def sorted_squares(nums: List[int]) -> List[int]:
    for inx, val in enumerate(nums):
        nums[inx] = val * val
    nums.sort()
    return nums #should've been sorted([x*x for x in nums])
    