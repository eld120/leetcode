import heapq

from collections import deque


def shortest_bridge(grid: list[list[int]]) -> int:
    """
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
    """
    island_one = set()
    # island_two = set()
    queue = deque()
    found_first_island = False
    for row, array in enumerate(grid):
        for col, cell in enumerate(array):
            if cell == 1:
                queue.append((row, col))
                island_one.add((row, col))
                found_first_island = True
                break
        if found_first_island:
            break

    # building island one
    while queue:
        row, col = queue.popleft()

        if row > 0 and grid[row - 1][col] == 1 and (row - 1, col) not in island_one:
            queue.append((row - 1, col))
            island_one.add((row - 1, col))
        if (
            row < len(grid) - 1
            and grid[row + 1][col] == 1
            and (row + 1, col) not in island_one
        ):
            queue.append((row + 1, col))
            island_one.add((row + 1, col))
        if col > 0 and grid[row][col - 1] == 1 and (row, col - 1) not in island_one:
            queue.append((row, col - 1))
            island_one.add((row, col - 1))
        if (
            col < len(grid[0]) - 1
            and grid[row][col + 1] == 1
            and (row, col + 1) not in island_one
        ):
            queue.append((row, col + 1))
            island_one.add((row, col + 1))
    queue = deque()

    island_two = set()
    found_second_island = False
    for row, array in enumerate(grid):
        for col, cell in enumerate(array):
            if cell == 1 and (row, col) not in island_one:
                queue.append((row, col))
                island_two.add((row, col))
                found_second_island = True
                break
        if found_second_island:
            break
    # building island two
    while queue:
        row, col = queue.popleft()

        if (
            row > 0
            and grid[row - 1][col] == 1
            and (row - 1, col) not in island_one
            and (row - 1, col) not in island_two
        ):
            queue.append((row - 1, col))
            island_two.add((row - 1, col))
        if (
            row < len(grid) - 1
            and grid[row + 1][col] == 1
            and (row + 1, col) not in island_one
            and (row + 1, col) not in island_two
        ):
            queue.append((row + 1, col))
            island_two.add((row + 1, col))
        if (
            col > 0
            and grid[row][col - 1] == 1
            and (row, col - 1) not in island_one
            and (row, col - 1) not in island_two
        ):
            queue.append((row, col - 1))
            island_two.add((row, col - 1))
        if (
            col < len(grid[0]) - 1
            and grid[row][col + 1] == 1
            and (row, col + 1) not in island_one
            and (row, col + 1) not in island_two
        ):
            queue.append((row, col + 1))
            island_two.add((row, col + 1))
    qu = deque()

    min_count = float("inf")
    for row, col in island_two:
        qu.append((row, col, 0))
        current_counts = []
        visited = set()
        heapq.heapify(current_counts)
        while qu:
            x, y, count = qu.popleft()
            
            if x > 0:
                if grid[x - 1][y] == 0 and (x - 1, y) not in visited:
                    qu.append((x - 1, y, count + 1))
                    visited.add((x - 1, y))
                elif (x - 1, y) in island_one:
                    heapq.heappush(current_counts, count)
            if x < len(grid) - 1:
                if grid[x + 1][y] == 0 and (x + 1, y) not in visited:
                    qu.append((x + 1, y, count + 1))
                    visited.add((x + 1, y))
                elif (x + 1, y) in island_one:
                    heapq.heappush(current_counts, count)
            if y > 0:
                if grid[x][y - 1] == 0 and (x, y - 1) not in visited:
                    qu.append((x, y - 1, count + 1))
                    visited.add((x, y - 1))
                elif (x, y - 1) in island_one:
                    heapq.heappush(current_counts, count)
            if y < len(grid[0]) - 1:
                if grid[x][y + 1] == 0 and (x, y + 1) not in visited:
                    qu.append((x, y + 1, count + 1))
                    visited.add((x, y + 1))
                elif (x, y + 1) in island_one:
                    heapq.heappush(current_counts, count)
        try:
            
            temp_count = heapq.heappop(current_counts)
        except IndexError:
            continue
        min_count = min(min_count, temp_count)

    return min_count


def shorter_bridge(grid: list[list[int]]) -> int:
    island_one = set()
    island_two = set()
    queue = deque()
    found_first_island = False
    for row, array in enumerate(grid):
        for col, cell in enumerate(array):
            if cell == 1:
                queue.append((row, col))
                island_one.add((row, col))
                found_first_island = True
                break
        if found_first_island:
            break

    # building island one
    while queue:
        row, col = queue.popleft()

        if row > 0 and grid[row - 1][col] == 1 and (row - 1, col) not in island_one:
            queue.append((row - 1, col))
            island_one.add((row - 1, col))
        if (
            row < len(grid) - 1
            and grid[row + 1][col] == 1
            and (row + 1, col) not in island_one
        ):
            queue.append((row + 1, col))
            island_one.add((row + 1, col))
        if col > 0 and grid[row][col - 1] == 1 and (row, col - 1) not in island_one:
            queue.append((row, col - 1))
            island_one.add((row, col - 1))
        if (
            col < len(grid[0]) - 1
            and grid[row][col + 1] == 1
            and (row, col + 1) not in island_one
        ):
            queue.append((row, col + 1))
            island_one.add((row, col + 1))

    queue = deque()
    found_second_island = False
    for row, array in enumerate(grid):
        for col, cell in enumerate(array):
            if cell == 1 and (row, col) not in island_one:
                queue.append((row, col))
                island_two.add((row, col))
                found_second_island = True
                break
        if found_second_island:
            break

    while queue:
        row, col = queue.popleft()

        if (
            row > 0
            and grid[row - 1][col] == 1
            and (row - 1, col) not in island_one
            and (row - 1, col) not in island_two
        ):
            queue.append((row - 1, col))
            island_two.add((row - 1, col))
        if (
            row < len(grid) - 1
            and grid[row + 1][col] == 1
            and (row + 1, col) not in island_one
            and (row + 1, col) not in island_two
        ):
            queue.append((row + 1, col))
            island_two.add((row + 1, col))
        if (
            col > 0
            and grid[row][col - 1] == 1
            and (row, col - 1) not in island_one
            and (row, col - 1) not in island_two
        ):
            queue.append((row, col - 1))
            island_two.add((row, col - 1))
        if (
            col < len(grid[0]) - 1
            and grid[row][col + 1] == 1
            and (row, col + 1) not in island_one
            and (row, col + 1) not in island_two
        ):
            queue.append((row, col + 1))
            island_two.add((row, col + 1))
    smallest = float("inf")
    for row_i1, col_i1 in island_one:
        for row_i2, col_i2 in island_two:
            smallest = min(smallest, abs(row_i2 - row_i1) + abs(col_i2 - col_i1) - 1)

    return smallest


# Stolen more concise BFS
# while bfs_queue:
#             new_bfs = []
#             for x, y in bfs_queue:
#                 for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
#                     if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
#                         new_bfs.append((cur_x, cur_y))
#                         second_bfs_queue.append((cur_x, cur_y))
#                         grid[cur_x][cur_y] = 2
#             bfs_queue = new_bfs


def recursive_bridge(grid: list[list[int]]) -> int:
    island_one = set()
    island_two = set()
    queue = deque()
    found_first_island = False
    for row, array in enumerate(grid):
        for col, cell in enumerate(array):
            if cell == 1:
                queue.append((row, col))
                island_one.add((row, col))
                found_first_island = True
                break
        if found_first_island:
            break

    # building island one
    while queue:
        row, col = queue.popleft()

        if row > 0 and grid[row - 1][col] == 1 and (row - 1, col) not in island_one:
            queue.append((row - 1, col))
            island_one.add((row - 1, col))
        if (
            row < len(grid) - 1
            and grid[row + 1][col] == 1
            and (row + 1, col) not in island_one
        ):
            queue.append((row + 1, col))
            island_one.add((row + 1, col))
        if col > 0 and grid[row][col - 1] == 1 and (row, col - 1) not in island_one:
            queue.append((row, col - 1))
            island_one.add((row, col - 1))
        if (
            col < len(grid[0]) - 1
            and grid[row][col + 1] == 1
            and (row, col + 1) not in island_one
        ):
            queue.append((row, col + 1))
            island_one.add((row, col + 1))
    queue = deque()

    found_second_island = False
    for row, array in enumerate(grid):
        for col, cell in enumerate(array):
            if cell == 1 and (row, col) not in island_one:
                queue.append((row, col))
                island_two.add((row, col))
                found_second_island = True
                break
        if found_second_island:
            break

    stack = deque()
    n = len(grid)

    for row, col in island_one:
        visited = set()
        stack.append((row, col, 0))
        while stack:
            x, y, count = stack.pop()
            if x > 0:
                if grid[x - 1][y] == 0 and (x - 1, y) not in visited:
                    visited.add((x - 1, y))
                    stack.append((x - 1, y, count + 1))

            if x < n - 1:
                if grid[x - 1][y] == 0 and (x - 1, y) not in visited:
                    visited.add((x - 1, y))
                    stack.append((x - 1, y, count + 1))

            if y > 0:
                pass
            if y < n - 1:
                pass


def test_example_one():
    assert (
        shortest_bridge(
            [
                [0, 1],
                [1, 0],
            ]
        )
        == 1
    )


def test_exmaple_two():
    assert (
        shortest_bridge(
            [
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 1],
            ]
        )
        == 2
    )


def test_example_three():
    assert (
        shortest_bridge(
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ]
        )
        == 1
    )


def test_three():
    assert (
        shortest_bridge(
            [
                [0, 1, 0, 0, 0],
                [0, 1, 0, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        == 1
    )


def test_is_slow():
    assert (
        shortest_bridge(
            [
                [0, 0, 1, 0, 1],
                [0, 1, 1, 0, 1],
                [0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        == 1
    )


def test_2nd_slow_test():
    assert (
        shortest_bridge(
            [
                [0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
            ]
        )
        == 3
    )
