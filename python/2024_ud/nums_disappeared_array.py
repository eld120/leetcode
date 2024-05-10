from collections import Counter
from typing import List


def find_disappeared_num(nums: List[int]) -> List[int]:
    nums.sort()
    num = set(nums)

    # breakpoint()
    return [val for val in range(1, len(nums) + 1) if val not in num]


def find_disappeared(nums: List[int]) -> List[int]:
    n = set()
    highest = 0
    for num in nums:
        n.add(num)
        if num >= highest:
            highest = num
    return [num for num in range(1, len(nums) + 1) if num not in n]


def test_one_one():
    assert find_disappeared_num([1, 1]) == [2]
