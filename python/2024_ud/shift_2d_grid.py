from collections import deque


def shift_grid(grid: list[list[int]], k: int) -> list[list[int]]:
    if k == 0:
        return grid
    queue = deque()
    [queue.append(x) for arr in grid for x in arr]
    temp = []
    for _ in range(0, k):
        temp = queue.pop()
        queue.appendleft(temp)
    inx = len(grid[0])
    container = []
    while queue:
        temp = []
        for _ in range(0, inx):
            temp.append(queue.popleft())
        container.append(temp)
    return container


def test_one():
    assert shift_grid(
        [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4
    ) == [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]


def test_two():
    assert shift_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [
        [9, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
