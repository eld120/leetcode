

def single_num(nums: list[int]) -> int:
    tracker = set()
    for val in nums:
        if val not in tracker:
            tracker.add(val)
        else:
            tracker.remove(val)
    return tracker.pop()

def test_one():
    assert single_num([3,3,2,3]) == 2