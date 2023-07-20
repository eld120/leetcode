import math
import os
import random
import re
import sys


def plus_minus(arr):
    # num of positive values
    positives = 0
    negatives = 0
    zeroes = 0

    for line in arr:
        if line > 0:
            positives += 1
        elif line < 0:
            negatives += 1
        else:
            zeroes += 1

    print(positives / n)
    print(negatives / n)
    print(zeroes / n)


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)
