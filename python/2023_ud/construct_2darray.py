from typing import List

data_one = [1,2,3,4] # row=2, col=2
data_two = [1,2,3] # row=1, col=3
data_three = [1,2] # row=1, col=1
d_four = [3]

def construct2DArray(original: List[int], rows: int, cols: int) -> List[List[int]]:
    if len(original) > rows * cols:
        
        return []
    elif len(original) < rows * cols:
        
        return [] 
    counter = 0
    increment = cols
    new_arr = []
    while counter < len(original):
        # construct slice of original list
        
        new_arr.append(original[counter:cols])
        counter+=increment
        cols+=increment
    
    return new_arr


if __name__ == '__main__':
    construct2DArray(d_four, 1, 2)