from typing import List
from collections import Counter


def least_brick(wall: List[List[int]]):
    """
    There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

    Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

    Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

    Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    inp = [1,3,5,6], [3,4,6], [1,4,6], [2,6], [3,4,6], [1,4,5,6]
    Output: 2

    Input: wall = [[1],[1],[1]]
    Output: 3
    Constraints:
    n == wall.length
    1 <= n <= 104
    1 <= wall[i].length <= 104
    1 <= sum(wall[i].length) <= 2 * 104
    sum(wall[i]) is the same for each row i.
    1 <= wall[i][j] <= 231 - 1

    """

    values = []
    for inner in wall:
        current = 0
        temp = []
        for val in inner:
            current += val
            temp.append(current)
        values.append(temp)

    count = Counter()
    for row in values:
        for val in row:
            try:
                count[val] += 1
            except KeyError:
                count[val] = 1
    if len(count) == 1:
        return len(wall)
    elif len(count) > 1:
        # breakpoint()
        most_common = count.most_common(2)[-1][-1]
    else:
        most_common = 0

    return len(wall) - most_common


def test_one():
    assert (
        least_brick(
            [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
        )
        == 2
    )


def test_two():
    assert least_brick([[1], [1], [1]]) == 3


def test_three():
    assert least_brick([[1, 1], [2], [1, 1]]) == 1


test_three()
