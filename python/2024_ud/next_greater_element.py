



def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    ans = []
    n2 = {val: index for index, val in enumerate(nums2)}
    for val in nums1:
        found = False
        start = n2[val]
        while start < len(nums2):
            if nums2[start] > val:
                ans.append(nums2[start])
                found = True
                break
            start += 1
        if not found:
            ans.append(-1)
    return ans    

def test_one():
    assert next_greater_element([4,1,2], [1,3,4,2]) == [-1,3,-1]

def test_two():
    assert next_greater_element([3,1,5,7,9,2,6], [1,2,3,5,6,7,9,11]) == [5,2,6,9,11,3,7]