

def move_zeros(nums: list[int]) -> list:
    
    temp = []
    for val in nums:
        if val != 0:
            temp.append(val)
    diff = len(nums) - len(temp)
    index = 0
    while index < len(nums):
        if index < len(temp):
            nums[index] = temp[index]
        else:
            nums[index] = 0
        index += 1
    return nums


def test_one():
    assert move_zeros([0,1,0,3,12]) == [1,3,12,0,0]

def test_two():
    assert move_zeros([0]) == [0]

def test_28():
    assert move_zeros([0,0,1]) == [1,0,0]