from typing import List




def k_largest_elements(array: List[int], k: int) -> List[int]:
    '''
    int/float array, input array fits in memory
    Example

    - Input array: `[7, 16, 5, 9, -1, 4, 3, 11, 2]`
    top_nums = [9,16,5]
    - `k`: 3
    - Result: `[16, 9, 11]`
    '''
    array.sort()
    return array[-k:]

def k_largets_ele_no_sorting(array: List[int], k: int) -> List[int]:
    top_nums = []
    for num in array:
        top_nums.append(num)
        top_nums = sorted(top_nums)
        top_nums = top_nums[-k:]

    return top_nums

# Leetcode problem here
class KthLargest:
    def __init__(self, k: int, nums: List[int]) -> None:
        self._array = nums
        self._k = k

    def add(self,val: int) -> int:
        self._array.append(val)
        self._array.sort()
        self._array = self._array[-self._k:]
        return self._array[-self._k]



def test_ints_duplicates():
    assert k_largets_ele_no_sorting([7,16,5,16,-1,-1,3,11,2],3) == [11,16,16]

def test_empty_array():
    assert k_largets_ele_no_sorting([], 0) == []

def test_k_larger_than_array():
    assert k_largets_ele_no_sorting([1,2,3], 4) == [1,2,3]