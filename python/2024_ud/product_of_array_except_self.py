"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
"""

def divide_py(a, b):
    return a * b ** -1







def product_except(nums: list[int]) -> list[int]:
    total = 1
    ans = []
    contains_zeros = False
    zero_count = 0
    for val in nums:
        if val != 0:
            total *= val
        else:
            contains_zeros = True
            zero_count += 1
    for num in nums:
        if contains_zeros and num == 0 and zero_count == 1 :
            ans.append(total)
        elif not contains_zeros:
            ans.append(int(total * num ** -1))
        else:
            ans.append(0)
    return ans
        


def test_one():
    assert product_except([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_two():
    assert product_except([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_twelve():
    assert product_except([1,-1]) == [-1, 1]

