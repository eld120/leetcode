#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    print(arr)
    iterator = 0
    decrementor = -1
    answer = 0
    ans2 = 0
    for length in arr:
        answer = answer + length[iterator]
        ans2 = ans2 + length[decrementor]
        iterator += 1
        decrementor -= 1

    return answer - ans2


if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
