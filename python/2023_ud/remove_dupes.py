from typing import List
# test data
data_one = [1,1,2]
data_two = [0,0,1,1,1,2,2,3,3,4]
data_three = [1,1]
data_four = [1, 1, 1]
d_five = [1,1,2]

def removeDuplicates(nums: List[int]) -> int:
    # this works but it sucks
    remove_me = ()
    
    for index, num in enumerate(nums):
        if index == 0:
            continue
        else:
            if num == nums[index - 1]:
                remove_me += (num,)
    
    for val in remove_me:
         nums.remove(val)
        
        

    print(nums, remove_me)


        # works but sucks
        # dupe_tracker = set()
        # nums_to_remove = ()
        # for num in nums:
        #     if num in dupe_tracker:
        #         nums_to_remove += (num,)
        #     else:
        #         dupe_tracker.add(num)
        # for num in nums_to_remove:
        #     nums.remove(num)
        # return len(nums)
    
    
        # I was frustratingly close to this answer. never knew wtf [:] was
        # nums[:] = list(sorted(set(nums)))
        # return len(nums)


if __name__ == '__main__':
    removeDuplicates(d_five)