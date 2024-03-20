from typing import List

def replace_elements(arr: List[int]) -> List[int]:
    highest = 0
    highest_index = 0
    
    for index, _ in enumerate(arr):
        if index >= highest_index and index < len(arr)-1:
            fast = index +1
            highest = 0
            while fast < len(arr):
                if arr[fast] > highest:
                    highest = arr[fast]
                    highest_index = fast
                fast += 1
        if index == len(arr) -1:
            arr[index] = -1
        else:
            arr[index] = highest
    return arr



def test_one():
    assert replace_elements([17,18,5,4,6,1]) == [18,6,6,6,1,-1]


def test_two():
    assert replace_elements([400]) == [-1]