from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    unsorted list, seeking longest consecutive sequence of ints
    """
    lookup = set(nums)
    largest = 0
    smallest = 999999999999999999999

    for val in lookup:
        if val > largest:
            largest = val
        if val < smallest:
            smallest = val

    longest = 0

    def find_longest(val: int, lookup: set, counter: int = 1) -> int:
        if val + 1 in lookup:
            counter += 1
            return find_longest(val + 1, lookup, counter)

        else:
            return counter

    for val in lookup:
        # breakpoint()
        current = find_longest(val, lookup)
        if current > longest:
            longest = current
    return longest


def longest_stuff_again(nums: List[int]) -> int:
    some_set = set(nums)
    if len(some_set) == 1:
        return 1
    elif len(some_set) == 0:
        return 0
    longest = 0
    for val in nums:
        if val - 1 not in some_set:
            starter = val
            counter = 0
            while starter in some_set:
                starter += 1
                counter += 1

            longest = max(counter, longest)
    return longest


def wtf_i_thought_i_couldnt_sort(fucking_input: List[int]) -> int:
    if len(fucking_input) < 10 and len(set(fucking_input)) == 1:
        return 1
    elif len(fucking_input) == 0:
        return 0
    some_shit = sorted(set(fucking_input))
    longest = 0
    count = 1
    for index, val in enumerate(some_shit):
        # breakpoint()
        if index == len(some_shit) - 1:
            break
        if val + 1 == some_shit[index + 1]:
            count += 1
        else:
            count = 1

        longest = max(count, longest)
    return longest


def test_gap_in_sequences():
    assert wtf_i_thought_i_couldnt_sort([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7


def test_idk():
    assert wtf_i_thought_i_couldnt_sort([100, 4, 200, 1, 3, 2]) == 4
