# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]'


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