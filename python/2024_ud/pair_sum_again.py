from typing import List, Set



def pair_sum(array: List, k: int) -> List[Set[int]]:
    '''
    Mini interview question: pair sum
    Goal: solve this problem in < 30 minutes.
    Write a function that takes as input two arguments:
    An array of numbers
    An integer k
    and returns an array with all of the pairs of numbers from that array that sum to k. 
    You can’t use the same number twice. You can assume that there are no duplicate numbers in the array.
    
    Example
    Input array: [1, 9, 6, 3, 5, 4]
    k: 10
    Result: [[1, 9], [6, 4]] // Note that [5, 5] is not in the solution
    '''
    # init array to hold values, init pointers left/right
    valid_sums = []
    left = 0
    right = len(array) - 1
    # sort the array
    array.sort()
    # loop through array
    while left < right:
        current = array[left] + array[right]
        if current == k:
            valid_sums.append({array[left], array[right]})
            right -=1
            left += 1
    # if values at current == k

    # append to answer array
        elif current > k:
            right -= 1
        else:
            left += 1

    return valid_sums

    # if current > k
        # right -= 1
    
    # else
        # left += 1

def test_example():
    assert pair_sum([1, 9, 6, 3, 5, 4], 10) == [{1, 9}, {6, 4}]

def test_example_odd_length():
    assert pair_sum([1, 9, 6, 3, 5, 4,7], 10) == [{1, 9}, {3,7},{6, 4} ]

def test_empty():
    assert pair_sum([], 0) == []