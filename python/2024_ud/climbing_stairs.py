def climb(n: int):
    """"""
    # 1 is 1

    # 2 is 1 + 1 and 2 - 2
    # 3 is 1+1 +1 and 1+2 and 2+1 = 3
    # 4 is 1,1,1,1, - 1,2,1 - 2,2 - 2,1,1 - 1,1,2 = 5
    # 5 is 1,1,1,1,1 - 1,2,1,1 - 2,2,1 - 1,2,2 - 2,1,2 - 2,1,1,1 - 1,1,2,1 - 1,1,1,2 = 8
    if n < 3:
        return n
    mem = [1, 2]
    left, right = 0, 1
    for val in range(1, n + 1):
        if val > 2:
            mem.append(mem[left] + mem[right])
            left += 1
            right += 1
    return mem[-1]


def test_one():
    assert climb(2) == 2


def test_two():
    assert climb(3) == 3
