#!/bin/python3

import math, os, random, re, sys



# Complete the solve function below.
def solve(s):
    ans = s.split(" ")
    capitalize  = [_.capitalize() for _ in ans]
    answer = ""
    for ele in capitalize:
        answer = answer + ele + " "
    answer = answer[:-1]
    return answer
    
    
if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)