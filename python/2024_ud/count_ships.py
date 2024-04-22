'''
Write a function that counts of the number of ships in a 2D grid.

- Input: an array of arrays of strings, representing a 2D grid. 
The strings are either a `"."` for open water, or an `"S"` for part of 
a ship. Connected `"S"`es are part of the same ship.
- Output: an integer that is the count of the number of ships in the grid.

Facts about ships:

- Ships are only horizontal or vertical, not diagonal.
- Ships have a width of one or more and a height of one or more.
- Ships never touch each other.

The input will always be a well-formed grid (all rows are the same length).

Example function calls

    let ships = [
        [".", "S", ".", "S"],
        [".", ".", ".", "S"],
        ["S", "S", ".", "S"],
        [".", ".", ".", "S"]
    ]
    countShips(ships) -> 3

    let ships = [
        ["S", "S", ".", "S", "S", "S", ".", "."],
        ["S", "S", ".", "S", "S", "S", ".", "."],
        ["S", "S", ".", ".", ".", ".", "S", "S"]
    ]
    countShips(ships) -> 3
'''
from collections import deque

def count_ships(grid: list[list[str]]) -> int:
    # init queue using collections.deque, variable called counter
    counter = 0
    queue = deque()

    # search for our first "S" through through loop
    for i, outer in enumerate(grid):
        for j, inner in enumerate(outer):
        # once we have an S it's going to be pushed into queue
            if inner == "S":
                queue.append((i,j))
                # loop through queue
                while queue:
                    # pop off first item in queue # deconstruct the coords from queue row, col
                    row, col = queue.popleft()
                    # constraint on the coordinates are on the grid and coords are an "S"
                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == "S":
                        queue.append((row + 1, col))
                        queue.append((row -1, col))
                        queue.append((row, col + 1))
                        queue.append((row, col - 1))
                        grid[row][col] = "."
                        # add adjacent coords to queue

                        # set current coord to "."
                counter += 1
                # increment counter
    return counter




def test_one():
    assert count_ships([
        [".", "S", ".", "S"],
        [".", ".", ".", "S"],
        ["S", "S", ".", "S"],
        [".", ".", ".", "S"]
    ]) == 3
        

def test_two():
    assert count_ships([
        ["S", "S", ".", "S", "S", "S", ".", "."],
        ["S", "S", ".", "S", "S", "S", ".", "."],
        ["S", "S", ".", ".", ".", ".", "S", "S"]
    ]) == 3

def test_three():
    pass
test_two()