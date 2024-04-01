from typing import List


def merge_sort(thingy: List[int]) -> List[int]:
    def merge(left, right):
        answer = []
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                answer.append(right[r])
                r += 1
            else:
                answer.append(left[l])
                l += 1

        answer += right[r:]
        answer += left[l:]
        return answer
    
    if len(thingy)> 1:
        middle = len(thingy)//2
        left = thingy[:middle]
        right = thingy[middle:]
        l = merge_sort(left)
        r = merge_sort(right)
        return merge(l,r)
        
    else:
        return thingy

    

def test_one():
    assert merge_sort([5,4,3,2,1]) == [1,2,3,4,5]