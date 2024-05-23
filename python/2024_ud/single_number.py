from collections import Counter

def single_num(nums: list[int]) -> int:
    tracker = set()
    for val in nums:
        if val not in tracker:
            tracker.add(val)
        else:
            tracker.remove(val)
    return tracker.pop()

def single_number_On_space(nums):
    tracker = Counter(nums)
    for val, count in tracker.items():
        if count == 1:
            return val


def test_one():
    assert single_num([3,3,2,3]) == 2