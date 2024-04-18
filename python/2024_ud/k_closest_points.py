
import heapq
from math import sqrt

def k_closest(points: list[list[int]], k:int) -> list[list[int]]:
    '''
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
    return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
    '''
    numbers = []
    somethign = dict()
    
    for index, num in enumerate(points):
        key = sqrt((num[0]**2 + (num[1])**2))
        numbers.append(key)
        if key in somethign:
            somethign[key] += [index]
        else:
            somethign[key] = [index]

    heapq.heapify(numbers)
    small =  heapq.nsmallest(k, numbers)
    ans = []
    for val in set(small):
        #breakpoint()
        l = somethign[val]
        for index in l:
            ans.append(points[index])
    return ans


def test_one():
    assert k_closest([[1,3],[-2,2]], 1) == [[-2,2]]

def test_same_distance():
    assert k_closest([[0,1],[1,0]], 2) == [[0,1],[1,0]]
