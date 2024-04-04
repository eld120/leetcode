from typing import List

import heapq


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

def k_largest_ele_no_sorting(array: List[int], k: int) -> List[int]:
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


def k_largest_element(array: List[int], k: int) -> List[int]:
    smallest_nums = []
    heapq.heapify(smallest_nums)
    for num in array:
        heapq.heappush(smallest_nums, num)
        if len(smallest_nums) > k:
            heapq.heappop(smallest_nums)
        
    return smallest_nums
        

def k_elements_again(array: List[int], k: int) -> List[int]:
    

    smallest_nums = array[:k]
    heapq.heapify(smallest_nums)

    for index in range(k, len(array)):
        heapq.heappushpop(smallest_nums, array[index])
    
    return smallest_nums


def test_ints_duplicates():
    assert k_elements_again([7,16,5,16,-1,-1,3,11,2],3) == [11,16,16]

def test_empty_array():
    assert k_elements_again([], 0) == []

def test_k_larger_than_array():
    assert k_elements_again([1,2,3], 4) == [1,2,3]


