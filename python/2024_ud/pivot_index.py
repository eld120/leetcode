def pivot_index(nums: list[int]) -> int:
    # breakpoint()
    left, right = 0, len(nums) - 1
    left_sum, right_sum = nums[left], nums[right]

    while left < right:
        if left_sum > right_sum:
            if left_sum == right_sum:
                return right
            right -= 1
            right_sum += nums[right]
        elif left_sum < right_sum:
            if left_sum == right_sum:
                return left
            left += 1
            left_sum += nums[left]
        else:
            left += 1
            right -= 1

    return left if left_sum == right_sum else -1


def piv_inx(nums: list[int]) -> int:
    """
    The pivot index is the index where the sum of all the numbers strictly
    to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    """
    left, right = 0, len(nums) - 1
    totals = []

    left_sum = 0
    right_sum = 0
    while left < len(nums):
        # right_sum += nums[right]
        left_sum += nums[left]
        left += 1
        # right -= 1
        totals.append(left_sum)
        # totals.append(right_sum)
    while right > 0:
        right_sum += nums[right]

    breakpoint()

    return -1


def pivot_again(nums: list[int]) -> int:
    prefixes = []
    for index, val in enumerate(nums):
        if index > 0:
            val += prefixes[index - 1][0]
        prefixes.append([val])
    right = len(nums) - 1
    while right >= 0:
        # breakpoint()
        val = nums[right]
        if right < len(nums) - 1:
            val += prefixes[right + 1][1]
        prefixes[right].append(val)
        right -= 1
    for index, tup in enumerate(prefixes):
        if tup[0] == tup[1]:
            return index
    return -1


def test_one():
    # 1,28  8,27  11,20  17,17  22,11  28,6
    assert pivot_again([1, 7, 3, 6, 5, 6]) == 3


def test_two():
    assert pivot_again([1, 2, 3]) == -1


def test_three():
    assert pivot_again([2, 1, -1]) == 0
