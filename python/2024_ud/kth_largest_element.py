import heapq


def find_kth_largest_element(nums: list[int], k) -> int:
    heapq.heapify(nums)
    largest = heapq.nlargest(k, nums)
    return largest[-1]


def test_one():
    assert find_kth_largest_element([3, 2, 1, 5, 6, 4], 2) == 5


def test_two():
    assert find_kth_largest_element([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
