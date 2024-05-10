def num_of_subarrays(arr: list[int], size: int, threshold: int) -> int:
    """
    Given an array of integers arr and two integers k and threshold,
    return the number of sub-arrays of size k and average greater than or equal to threshold.
    """

    # init variables: num_of_subarrays: int, subtotal, left, right
    subarrays = 0
    index = 0
    subtotal = arr[index]
    while index < len(arr):
        if index - size + 1 < 0:
            index += 1
            subtotal += arr[index]
        else:
            if subtotal / size >= threshold:
                subarrays += 1
            if index == len(arr) - 1:
                break
            subtotal -= arr[index - size + 1]
            index += 1
            subtotal += arr[index]

    return subarrays


def test_one():
    assert num_of_subarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3


def test_two():
    assert num_of_subarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6


def test_three():
    assert num_of_subarrays([1, 1, 1, 1, 1], 1, 0) == 5


def t_all():
    test_one()
    test_two()
    test_three()


t_all()
