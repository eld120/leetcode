from typing import List




def find_peak(nums: List[int])-> int:
    if len(nums) < 4:
        peak = -float('inf')
        ret = 0
        for inx, val in enumerate(nums):
            if val > peak:
                peak = val
                ret = inx
        return ret
    left = 0
    right = len(nums) -1
    midpoint = (left + right) //2
    
    while left< right:
        midpoint = (left + right) //2
        #breakpoint()
        if nums[midpoint] < nums[midpoint + 1]:
            # if peak < nums[midpoint + 1]:
            #     peak =  nums[midpoint + 1]
            left = midpoint + 1
        elif nums[midpoint] < nums[midpoint - 1]:
            #peak =  nums[midpoint - 1]
            right = midpoint - 1
        else:
            break
    if nums[left] > nums[midpoint]:
        if nums[left] > nums[right]:
            return left
        else:
            return right
    elif nums[right] > nums[midpoint] and nums[midpoint] > nums[left]:
        return right
    else:
        return midpoint




def test_one():
    assert find_peak([1,2,1,3,5,6,4]) == 1 or find_peak([1,2,1,3,5,6,4]) == 5

def test_36():
    assert find_peak([6,5,4,3,2,3,2]) == 0

def test_27():
    assert find_peak([1,2,3,1,]) == 2