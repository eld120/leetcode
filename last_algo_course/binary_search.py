from typing import List


def binary_find_stuff(searchable: List[int], hopefully_findable: int) -> int:
    '''
    now returns the index of the value of hopefully_findable or -1 if not found
    '''
    high = len(searchable)
    low = 0
    
    while low <= high:
        midpoint = (high + low)//2
        if hopefully_findable == searchable[midpoint]:
            return midpoint
        elif hopefully_findable < searchable[midpoint] :
            
            high = midpoint 
        else:
            low = midpoint + 1
    return -1

def test_lower_bound():
    assert binary_find_stuff([1,2,3,4,5,6,7], 2) == 1

def test_one():
    assert binary_find_stuff([num for num in range(1,101)], 12) == 11
    assert binary_find_stuff([1,2,3], 2) == 1

def test_two():
    assert binary_find_stuff([num for num in range(1,101)], 22) == 21

def test_odd_number():
    assert binary_find_stuff([1,2,3,4,5,6,7], 7) == 6


def test_three():
    assert binary_find_stuff([num for num in range(1,1000001)], 954126) == 954125

def test_four():
    assert binary_find_stuff([num for num in range(1,1000001)], 54376) == 54375