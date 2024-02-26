'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.


[1,2,3]
[2,3,1]

# [3,4,5,6,1,2]


# how does a comparison inform which direction to move in binary search, how is this different here.

# we would need to compare the min/max of the parent array and each sub-array of the parent

'''


    

def min_array(rotated_array):
    if len(rotated_array) == 1:
        return rotated_array[0]
    
    
    midpoint = len(rotated_array) // 2
    left_subarray = rotated_array[midpoint:]
    right_subarray = rotated_array[:midpoint]

    while True:
        if left_subarray[-1] > right_subarray[-1] and  len(right_subarray) == 1:
            return right_subarray[0]
        elif left_subarray[-1] < right_subarray[-1] and  len(left_subarray) == 1:
            return left_subarray[0]
        
        if left_subarray[-1] > right_subarray[-1]:
            
            midpoint = len(right_subarray) // 2
            left_subarray = right_subarray[midpoint:]
            right_subarray = right_subarray[:midpoint]
            
            
        elif  left_subarray[-1] < right_subarray[-1]:
            
            midpoint = len(left_subarray) // 2
            right_subarray = left_subarray[:midpoint]
            left_subarray = left_subarray[midpoint:]
            
        
    
def test_one():
    assert min_array([3,4,5,1,2]) == 1

def test_two():
    assert min_array([4,5,6,7,0,1,2]) == 0

def test_three():
    assert min_array([11,13,15,17]) == 11

def test_single_length_list():
    assert min_array([1]) == 1

def test_two_length_list():
    assert min_array([1,2]) == 1

def test_slightly_longer_list():
    assert min_array([1,2,3]) == 1

def test_rotated_one():
    assert min_array([2,3,1]) == 1