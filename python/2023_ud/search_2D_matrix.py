'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

from typing import List

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 1

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    pass
    # lower = 0
    # upper = len(matrix)-1
    # while lower < upper:
        
    #     midpoint = (upper + lower//2)
    #     if matrix[midpoint][0] == target:
    #         print(True)
    #         return True
    #     if matrix[midpoint][0] > target:
    #         upper = midpoint
    #     else:
    #         lower = midpoint 
    # left = 0
    # right = len(matrix[upper])-1
    # while left <= right:
    #     midpoint = (left + right)//2
    #     if matrix[upper][midpoint] == target:
    #         print(True)
    #         return True
    #     if matrix[upper][midpoint] > target:
    #         right = midpoint
    #     else:
    #         left = midpoint 
        
    # print(False)
    # return False

            
def whatever(matrix, target):
    # fails time complexity requirement 
    lower = 0
    upper = len(matrix)
    while lower < upper:
        #breakpoint()
        
        mid = (upper + lower)//2
        if matrix[mid][0] <= target and target <= matrix[mid][-1]:
            
            break
        elif matrix[mid][0] > target:
            upper = mid 
        else:
            lower = mid + 1
    left = 0
    right = len(matrix[mid]) 
    inner_list = matrix[mid]
    while left < right:
        #breakpoint()
        middle = (left + right)//2
        if inner_list[middle] == target:
            
            return True
        elif inner_list[middle] > target:
            right = middle 
        else:
            left = middle + 1
    
    return False




def test_one():
    assert whatever([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True