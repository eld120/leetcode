def search(nums: list[int], target: int) -> int:
    """
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown
    pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k],
    nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        # if  sorted  and target in range
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test_part_one():
    assert search([4, 5, 6, 7, 0, 1, 2], 7) == 3


def test_part_two():
    assert search([4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 1, 2], 12) == 8


def test_part_three():
    assert search([4, 0, 1, 2], 7) == -1


def test_not_found():
    assert search([4, 5, 6, 7, 0, 1, 2], 10) == -1


def test_ex_one():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_ex_189():
    assert search([1, 3], 3) == 1
