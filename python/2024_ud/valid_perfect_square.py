def is_perfect_square(num: int) -> bool:
    """
    Given a positive integer num, return true if num is a perfect square or false otherwise.

    A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

    You must not use any built-in library function, such as sqrt.
    """
    if num == 1:
        return True
    left, right = 0, num * 3 - 1
    while left < right:
        # breakpoint()
        mid = (left + right) // 2
        ans = mid * mid
        if ans > num:
            right = mid - 1
        elif ans < num:
            left = mid + 1
        else:
            break

    if left * right == num or mid * mid == num and isinstance(left, int):
        return True
    return False


def test_one():
    assert is_perfect_square(16) == True


def test_two():
    assert is_perfect_square(14) == False


def test_is_one():
    assert is_perfect_square(1) == True


def test_nine():
    assert is_perfect_square(9) == True


def test_four():
    assert is_perfect_square(4) == True
