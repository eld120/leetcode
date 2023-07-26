from typing import List


test_one = [1, 1, 1, 2, 2, 3]
test_two = [0, 0, 1, 1, 1, 1, 2, 3]
test_three = []
test_four = [1, 1]
test_five = [1]
test_six = [1, 1, 1, 1]

# def last_index(arr, index):
#     '''returns the last index of a given value within a List'''
#     if index + 1 == len(arr):
#         return index
#     elif arr[index] == arr[index + 1]:
#         return last_index(arr, index + 1)
#     else:
#         return index


def last_index(arr, value):
    """returns the last index of a given value within a List"""
    for index, val in enumerate(arr):
        if val > value:
            return index - 1
        elif index == len(arr) - 1:
            return index
        else:
            continue


def value_swap(arr, value):
    # find last value
    index = last_index(arr, value)
    temp = arr[index]
    # shift values around
    while index < len(arr):
        if index == len(arr) - 1:
            arr[index] = temp
            break
        else:
            arr[index] = arr[index + 1]
        index += 1


def value_count(arr: List, value: int, index=0, count=0):
    """returns the count of a given value in a List
    used recursion because why not
    """
    while True:
        if index + 1 == len(arr):
            return count + 1
        if value == arr[index]:
            count += 1
            return value_count(arr, value, index + 1, count)

        elif value > arr[index]:
            return value_count(arr, value, index + 1, count)
        else:
            return count


def removeDuplicates(nums: List[int]) -> int:
    for val in nums:
        # count how many values are in the array
        values = value_count(nums, val)
        # if we have more than two values swap any beyond the first two
        if values > 2:
            for _ in range(values - 2):
                value_swap(nums, val)
    print(nums)
    return nums


if __name__ == "__main__":
    removeDuplicates(test_six)
