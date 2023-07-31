from typing import Iterable

# https://leetcode.com/problems/add-two-numbers-ii/description/

# sample data

l_one = [7, 2, 4, 3]
l_two = [5, 6, 4]
# [7, 8, 0, 7] is expected

l_three = [5, 6, 4]
l_four = [2, 4, 3]

l_five = [0]
l_six = [0]


def do_math_stuff(val_one: int, val_two: int) -> tuple[int, int]:
    index_minus_one: int = (val_one + val_two) // 10
    remainder: int = (val_one + val_two) % 10
    return (index_minus_one, remainder)


def add_numbers(val_one: int, val_two: int, iterable: Iterable, index: int):
    if val_one + val_two >= 10:
        index_minus_one = do_math_stuff(val_one, val_two)
        iterable[index - 1] += index_minus_one[0]
        return index_minus_one[1]
    return val_one + val_two


def two_numbers(one: Iterable, two: Iterable):
    # none of this works because the incoming datatype is a linked list
    # one.reverse()
    # two.reverse()
    # answer: list = []
    # if len(one) > len(two):
    #     for index, num in enumerate(one):
    #         try:
    #             answer.append(add_numbers(num, two[index], answer, index))
    #         except IndexError:
    #             break
    #     print(answer)
    # else:
    #     for index, num in enumerate(two):
    #         try:
    #             answer.append(add_numbers(num, one[index], answer, index))
    #         except IndexError:
    #             break
    #     print(answer)
    pass


if __name__ == "__main__":
    two_numbers(l_one, l_two)
