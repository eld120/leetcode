from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    '''
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
    Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

    Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

    Constraints:
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
    '''
    if n == 0:
        return True
    index = 0
    #breakpoint()
    while index < len(flowerbed):
        if index == 0 or index == len(flowerbed) -1:
            if flowerbed[0:2] == [0,0]:
                n -= 1
                flowerbed[0] = 1
                index += 1
            elif index == len(flowerbed) -1:
                if flowerbed[-2:] == [0,0]:
                    n -= 1
                    flowerbed[-1] = 1
                    index += 1
            else:
                index += 1
        else:
            if flowerbed[index-1:index+2] == [0,0,0]:
                flowerbed[index] = 1
                n -= 1
            index += 1

        if n <= 0:
            break
    if n <= 0:
        return True
    else: 
        return False
            

def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    if len(flowerbed) == 1 and n <= 1:
        if n == 1 and flowerbed[0] == 0:
            return True
        elif n == 0:
            return True
    #beds = 0
    
    for index, val in enumerate(flowerbed):
        if val == 1 and index > 0 and index < len(flowerbed) -1:
            if flowerbed[index -1] != 0 or flowerbed[index + 1] != 0:
                return False
        if val == 0:
            if index > 0 and index < len(flowerbed) -1:
                if flowerbed[index + 1] == 0  and flowerbed[index - 1] == 0:
                    flowerbed[index] = 1
                    n -= 1
            elif index == 0 and flowerbed[1] == 0:
                flowerbed[index] = 1
                n -= 1
            elif index == len(flowerbed) -1 and flowerbed[-2] == 0:
                flowerbed[index] = 1
                n -= 1
    if n > 0:
        return False
    return True

    #     beds += val
    # if len(flowerbed) % 2 == 1:
    #     if (beds + n)/len(flowerbed) <= .67:
    #         return True
    #     else:
    #         return False
    # else:
    #     if (beds + n)/len(flowerbed) <= .5:
    #         return True
    #     else:
    #         return False


            
def test_even():
    assert can_place_flowers([1,0,0,0], 1) == True
    assert can_place_flowers([0,1,0,0], 1) == True
    assert can_place_flowers([0,0], 1) == True
    assert can_place_flowers([1,0], 1) == False
    assert can_place_flowers([1,0,1,0], 1) == False

def test_single_val():
    assert can_place_flowers([1], 0) == True
    assert can_place_flowers([0], 1) == True
    assert can_place_flowers([1], 1) == False

def test_huh():
    assert can_place_flowers([1,0,0], 1) == True

def test_huh_two():
    assert can_place_flowers([0,1,0], 1) == False

def test_leetcode_one():
    assert can_place_flowers([1,0,0,0,1], 1) == True