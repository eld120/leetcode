from collections import deque


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    """

    something = dict()
    for index, val in enumerate(nums):
        if val not in something:
            something[val] = deque()
        something[val].appendleft(index)
    for val in nums:
        diff = target - val

        if (
            diff in something
            and diff + val == target
            and len(something[val]) == 1
            and something[val][0] != something[diff][0]
        ):
            first = something[val].popleft()
            second = something[diff].popleft()
            return [first, second]
        elif diff in something and diff + val == target:
            temp1 = something[val][0]
            if len(something[val]) > 1:
                temp1 = something[val].popleft()
            temp2 = something[diff][0]
            if len(something[diff]) > 1:
                temp2 = something[diff].popleft()
            if temp1 != temp2:
                return [temp1, temp2]


def test_one():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_39():
    assert two_sum([3, 2, 3], 6) == [2, 0]


def test_48():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_49():
    assert two_sum([0, 3, -3, 4, -1], -1) == [0, 4]


def test_92():
    assert two_sum([3, 2, 95, 4, -3], 92) == [2, 4]
