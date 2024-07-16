

def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    
    winners = set()
    for index, val in enumerate(nums):
        left = 0
        right = len(nums) -1
        while left < right:
            total = nums[left] + nums[index] + nums[right]
           #breakpoint()
            if  total == 0 and left != right and left != index and index != right:
                winners.add(tuple(sorted([nums[left],nums[right], nums[index]])))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
                
            else:
                right -= 1
    
    return [list(tup) for tup in winners]

def test_one():
    assert three_sum([-1,0,1,2,-1,-4]) == [[-1,0,1],[-1,-1,2]]