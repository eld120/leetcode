from typing import List


test_one = [1, 1, 1, 2, 2, 3]
test_two = [0, 0, 1, 1, 1, 1, 2, 3]
test_three = []
test_four = [1, 1]
test_five = [1]
test_six = [1, 1, 1, 1]
test_seven = [0, 0, 1, 1, 1, 1, 2, 3, 3]


def value_count(arr, value: int, index=0, count=0):
    """returns the count of a given value in a List
    used recursion because why not
    """
    if len(arr) == 0:
        return 0
    while True:
        if index + 1 == len(arr):
            if arr[index] == value:
                return count + 1
            else:
                return count
        if value == arr[index]:
            count += 1
            return value_count(arr, value, index + 1, count)
        elif value > arr[index]:
            return value_count(arr, value, index + 1, count)
        else:
            return count


def removeDuplicates(nums) -> int:
    for val in nums:
        count = value_count(nums, val)
        while count > 2:
            nums.remove(val)
            count = value_count(nums, val)

    return len(nums)


def test_value_counts():
    # test_one = [1, 1, 1, 2, 2, 3]
    # test_two = [0, 0, 1, 1, 1, 1, 2, 3]
    # test_three = []
    # test_four = [1, 1]
    # test_five = [1]
    # test_six = [1, 1, 1, 1]
    # test_seven = [0,0,1,1,1,1,2,3,3]

    assert value_count(test_one, 1) == 3
    assert value_count(test_one, 2) == 2
    assert value_count(test_one, 3) == 1
    assert value_count(test_two, 0) == 2
    assert value_count(test_two, 1) == 4
    assert value_count(test_two, 2) == 1
    assert value_count(test_two, 3) == 1
    assert value_count(test_three, 1) == 0
    assert value_count(test_four, 1) == 2
    assert value_count(test_five, 1) == 1


def test_remove_duplicates():
    assert removeDuplicates(test_one) == 5
    assert removeDuplicates(test_two) == 6
    assert removeDuplicates(test_three) == 0
    assert removeDuplicates(test_four) == 2
    assert removeDuplicates(test_five) == 1
    assert removeDuplicates(test_six) == 2
    assert removeDuplicates(test_seven) == 7


if __name__ == "__main__":
    removeDuplicates(test_one)  # [1, 1, 2, 2, 3]
    # value_count(test_one, 2)
