'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # search middle of the middle list for midpoint - Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    outer_low = 0
    outer_high = len(matrix)
    #breakpoint()
    while outer_low < outer_high:
        outer_midpoint = (outer_high + outer_low) // 2
        
        
        if matrix[outer_midpoint][0] <= target and target <= matrix[outer_midpoint][-1]:
            
            break
        elif target < matrix[outer_midpoint][0]:
            outer_high = outer_midpoint
        else:
            outer_low = outer_midpoint + 1
    inner_list = matrix[outer_midpoint]
    low = 0
    high = len(matrix[outer_midpoint]) -1
    while low < high:
        midpoint = (high + low) // 2
        if inner_list[midpoint] == target:
            return True
        elif inner_list[midpoint] < target: 
            low = midpoint + 1
        else:
            high = midpoint - 1
    return False


def search_matrix_recursive(matrix, target):
    
    lower = 0
    upper = len(matrix) -1
    #breakpoint()
    def recurse(matrix, lower, upper, target):
        #breakpoint()
        midpoint = (lower+upper) // 2
        if matrix[midpoint][0] <= target and target <= matrix[midpoint][-1]:
            left = 0
            right = len(matrix[midpoint]) -1
            
            while left < right:
                mid = (left + right) // 2
                if matrix[midpoint][mid] == target:
                    return True
                elif matrix[midpoint][mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return True if matrix[midpoint][(left + right) // 2] == target else False
        elif matrix[midpoint][-1] < target:
            lower = midpoint + 1
        else:
            upper = midpoint - 1
        if lower > upper:
            return False if target not in matrix[midpoint] else True
        return recurse(matrix, lower, upper, target)
        
    return recurse(matrix, lower, upper, target)


def test_one():
    assert search_matrix_recursive([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True

def test_two():
    assert search_matrix_recursive([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False

def test_three():
    assert search_matrix_recursive([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 5) == True

def test_len_two_false():
    assert search_matrix_recursive([[1], [3]], 0) == False

def test_len_two_true():
    assert search_matrix_recursive([[1], [3]], 1) == True

def test_tired():
    assert search_matrix_recursive([[1],[3],[5]], 3) == True