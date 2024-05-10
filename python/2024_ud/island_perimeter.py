from collections import deque


def island_perimeter(grid: list[list[int]]) -> int:
    deck = deque()
    # add indices of all nieghbors once we find land
    counter = 0
    dups = set()
    for arr_inx, arr in enumerate(grid):
        found = False
        for inx, val in enumerate(arr):
            if val == 1:
                # loop through left, right , next arr same index, whatever above same index
                deck.append((arr_inx, inx))
                found = True
                break
        if found:
            break

    while len(deck) > 0:
        inx = deck.popleft()
        if inx[0] not in range(0, len(grid)) or inx[1] not in range(0, len(grid[0])):
            counter += 1
        elif grid[inx[0]][inx[1]] == 1 and (inx[0], inx[1]) not in dups:
            deck.append((inx[0], inx[1] - 1))
            deck.append((inx[0], inx[1] + 1))
            deck.append((inx[0] + 1, inx[1]))
            deck.append((inx[0] - 1, inx[1]))
            dups.add(inx)
        elif grid[inx[0]][inx[1]] == 0:
            counter += 1

    return counter


def test_one():
    assert (
        island_perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    )


test_one()
