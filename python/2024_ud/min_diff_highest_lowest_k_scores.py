import heapq


def min_difference(nums: list[int], k: int) -> int:
    nums.sort()
    if len(nums) == k:
        return nums[-1] - nums[0]
    left = 0
    right = 1
    diff = float("inf")
    min_diff = diff
    while right < len(nums):
        if right - left + 1 < k:
            right += 1
        else:
            diff = nums[right] - nums[left]
            left += 1

        min_diff = min(min_diff, diff)
    return min_diff


def test_one():
    assert min_difference([90], 1) == 0


def test_two():
    assert min_difference([9, 4, 1, 7], 2) == 2


def test_end():
    assert min_difference([9, 4, 1, 7, 11, 12], 2) == 1


def test_start():
    assert min_difference([9, 4, 1, 7, 12, 1], 2) == 0


def test_17():
    assert min_difference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6) == 74560
