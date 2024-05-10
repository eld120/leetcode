def pair_sum(array, k):
    # sort the array
    array.sort()
    # init one pointer,  right, one list = answers
    right = len(array) - 1
    left = 0
    answers = []
    # iterate through for loop
    while left < right:
        if array[left] + array[right] == k:
            answers.append([array[left], array[right]])
            left += 1
            right -= 1
        elif array[left] + array[right] < k:
            left += 1
        else:
            right -= 1
    return answers


def test_one():
    assert pair_sum([1, 9, 6, 3, 5, 4], 10) == [[1, 9], [6, 4]]


def test_empty():
    assert pair_sum([], 0) == []


def test_negative_nums():
    assert pair_sum([-1, 1, 9, 6, 3, 5, 4, 11], 10) == [[1, 9], [6, 4], [-1, 11]]
