"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
import heapq


def last_weight(stones: list[int]) -> int:
    while len(stones) > 1:
        temp = heapq.nlargest(2, stones)
        largest = temp[0]
        second_largest = temp[1]

        if largest != second_largest:
            remains = largest - second_largest
            heapq.heappush(stones, remains)
        stones.remove(largest)
        stones.remove(second_largest)
    try:
        last_one = heapq.heappop(stones)
    except:
        last_one = 0
    return last_one


def test_one():
    assert last_weight([2, 7, 4, 1, 8, 1]) == 1
