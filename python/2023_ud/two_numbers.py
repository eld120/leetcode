from typing import Iterable



# https://leetcode.com/problems/add-two-numbers-ii/description/

# sample data

l_one = [7, 2, 4, 3]
l_two = [5, 6, 4]
# [7, 8, 0, 7] is expected

l_three = [5,6,4]
l_four = [2,4,3]

l_five = [0]
l_six = [0]

def modulo_stuff(x: int, y: int) -> tuple[int, int]:
    larger: int = x if x > y else y
    smaller: int = x if x <= y else y
    index_minus_one: int = (larger + smaller) // 10
    remainder: int = (larger + smaller) % 10
    return (index_minus_one, remainder )

def add(x: int, y: int, iterable: Iterable , index: int):
    if x + y >= 10:
        index_minus_one = modulo_stuff(x, y)
        iterable[index-1] += index_minus_one[0]
        return index_minus_one[1]
    return x+y

def two_numbers(one, two):
    one.reverse()
    two.reverse()
    answer = []
    if len(one) > len(two):
        for index, num in enumerate(one):
            try:
                answer.append(add(num, two[index], answer, index)) 
            except IndexError:
                break
        print(answer) 
    else:
        for index, num in enumerate(two):
            try:
                answer.append(add(num, one[index], answer, index))
            except IndexError:
                break 
        print(answer)










if __name__ == '__main__':
   two_numbers(l_one, l_two)
  