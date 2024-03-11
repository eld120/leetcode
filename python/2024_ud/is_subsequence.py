'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
'''

def isSubsequence(s: str, t: str) -> bool:
    if not t and s:
        return False

    is_subsequence = True
    fast = 0
    slow = 0
    while slow < len(s):
        if s[slow] == t[fast]:
            slow += 1
        elif fast == len(t) -1:
            is_subsequence = False
            break
        else:
            fast += 1
    return is_subsequence

from collections import Counter

def is_subsequence(sinput: str, tinput: str) -> bool:
    '''
    Input: s = "abc", t = "ahbgdc"
    Output: true

    Input: s = "axc", t = "ahbgdc"
    Output: false
    '''
    
    subsequence = True
    if not tinput and sinput:
        return False
    
    fast = 0
    slow = 0
    while slow < len(sinput):
       # breakpoint()
        if fast >= len(tinput):
            subsequence = False
            break
        if sinput[slow] == tinput[fast]:
            slow += 1
            

        
        fast += 1    
    return subsequence
        
   


def test_one():
    assert is_subsequence('abc', 'ahbgdc') == True

def test_two():
    assert is_subsequence('axc', 'ahbgdc') == False

def test_three():
    assert is_subsequence('ab', 'baab') == True

def test_four():
    assert is_subsequence('bb', 'ahbgdc') == False