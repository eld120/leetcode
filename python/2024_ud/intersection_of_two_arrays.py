


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    '''
    Given two integer arrays nums1 and nums2, return an array of their 
    intersection
    . Each element in the result must be unique and you may return the result in any order.
    '''
    return list(set(nums1) & set(nums2))

