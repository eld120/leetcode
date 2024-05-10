"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:
        cost = [1,100,1,1,1,100,1,1,100,1]
            1, 100, 1001, 101, 102, 201, 103, 104, 203, 105
Input: cost = [1,100,1000,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
ex 3
    []
Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999

"""


def min_cost_climbing_stairs(cost: list[int]) -> int:
    cost_tracker = [cost[0], cost[1]]
    lowest = float("inf")
    for index, val in enumerate(cost):
        if index > 1:
            lowest = min(cost_tracker[-1], cost_tracker[-2])
            cost_tracker.append(val + lowest)
    return cost_tracker[-2] if cost_tracker[-2] < cost_tracker[-1] else cost_tracker[-1]


def test_one():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15


def test_two():
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
