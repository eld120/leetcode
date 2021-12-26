#!/bin/python3

import math, os, random, re, sys




def solve(s):
    print(len(s))
    ans = s.split()
    b = [a.capitalize() for a in ans]
    string  = ""
    for ele in b:
        string = string + ele + " "
    string = string[:-1]
    print(string)
    print(len(string))


if __name__ == '__main__':
    a = 'a string of characters'
    solve(a)