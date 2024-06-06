


def can_i_jump_it(nums: list[int]) -> bool:
    # calc the prefix sums of everything?
    # track available jumps, distance_to_last_index
    # track zero indices in an array?

    '''
    ex 1: [2,3,1,1,4]
    ex 1 jumps needed: [4,3,2,1,0] -> at index 1 return True
    ex 2: [3,2,1,0,4]
    ex 2: jumps needed: [4,3,2,1,0] -> short of jumps needed at every step
    '''
    if len(nums) == 1:
        return True
    
    for index, val in enumerate(nums):
        if index == 0:
            max_available_jumps = val
        else:
            max_available_jumps -= 1
            max_available_jumps = max(max_available_jumps, val)
        if val == 0 and max_available_jumps == 0:
            return False
        elif max_available_jumps >= len(nums) -1 - index:
            return True
    


def test_one():
    assert can_i_jump_it([2,3,1,1,4]) == True

def test_two():
    assert can_i_jump_it([3,2,1,0,4]) == False