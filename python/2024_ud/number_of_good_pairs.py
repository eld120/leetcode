from collections import Counter


def num_identical_pairs(nums: list[int]) -> int:
    # 3 -> 3, 4-> 6 5 -> 10
    # count = Counter(nums)
    # ans = 0
    # for val in count:
    #     if val > 1:
    #         ans += val 

    # return ans
    counter = Counter()
    ans = 0
    for val in nums:
        # if val in counter:
        counter[val] += 1
        # else:
            #counter[val] = 1
        length = counter[val] -1
        ans += length

    return ans

def brute_force(nums: list[int]) -> int:
    count = 0
    for index, num in enumerate(nums):
        for val in nums[index+1:]:
            if num == val:
                count += 1

    return count



def test_four():
    assert num_identical_pairs([1,1,1,1]) == 6
    # 3 -> 3,  6, 10, 15    count
    #  4 -> 6
    # 5 -> 10

def test_five():
    assert num_identical_pairs([1,1,1,1,1,1]) == 15
