from typing import List


def find_diff(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    """
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
    Note that the integers in the lists may be returned in any order.

    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]
    Explanation:
    For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
    For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

    Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    Output: [[3],[]]
    Explanation:
    For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
    Every integer in nums2 is present in nums1. Therefore, answer[1] = [].


    Constraints:

    1 <= nums1.length, nums2.length <= 1000
    -1000 <= nums1[i], nums2[i] <= 1000
    """

    return [
        list({val for val in nums1 if val not in set(nums2)}),
        list({val for val in nums2 if val not in set(nums1)}),
    ]


def find_diff_faster(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    """
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
    Note that the integers in the lists may be returned in any order.
    """
    num1 = set(nums1)
    num2 = set(nums2)
    dup = set()
    dup2 = set()
    ans = []
    for val in nums1:
        if val not in num2 and val not in dup:
            ans.append(val)
            dup.add(val)

    ans2 = []
    for val in nums2:
        if val not in num1 and val not in dup2:
            ans2.append(val)
            dup2.add(val)

    return [ans, ans2]
