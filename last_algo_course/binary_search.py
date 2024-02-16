from typing import List


def binary_find_stuff(searchable: List, hopefully_findable: int) -> int:

    high = len(searchable)
    low = 0
    while low < high:
        midpoint = (high + low)//2
        #breakpoint()
        if hopefully_findable == midpoint:
            
            return midpoint
        elif hopefully_findable < midpoint :
            high = midpoint
        else:
            low = midpoint
        

def test_one():
    assert binary_find_stuff([num for num in range(1,101)], 23) == 23

def test_two():
    assert binary_find_stuff([num for num in range(1,101)], 22) == 22


def test_three():
    assert binary_find_stuff([num for num in range(1,1000001)], 954126) == 954126

def test_four():
    assert binary_find_stuff([num for num in range(1,1000001)], 54376) == 54376