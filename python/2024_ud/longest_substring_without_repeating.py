'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
from collections import Counter


def lengthOfLongestSubstring(sinput: str) -> int:
    # sliding window compares substring within string
    # conditional to determine if/when there's a repeating 
    if len(sinput) == 1:
        return 1
    
    longest_substring = 0

    #breakpoint()
    
    for slow in range(0, len(sinput)):
        for fast in range(slow + 1, len(sinput)+1):
            current = sinput[slow:fast]
            if len(current) != len(set(current)):
                break
            
            elif len(current) > longest_substring:
                longest_substring = len(current)
        
    return longest_substring
            

def length_longest_substring(sinput: str) -> int:
    if len(sinput) == 1:
        return 1
    longest_substring = 0
    slow = 0
    fast = slow +1
    while slow < len(sinput) and longest_substring < len(sinput) - slow:
        current = sinput[slow:fast]
        if len(current) != len(set(current)):
            slow +=1
            fast = slow + 1
        elif len(current) > longest_substring:
            longest_substring = len(current)
        
        if fast >= len(sinput):
            slow += 1
            fast = slow + 1
        else:
            fast += 1
    return longest_substring


def test_abc_pattern():
    assert length_longest_substring('abcabcbb') == 3

def test_bbbbbbbbb():
    assert length_longest_substring('bbbbbbb') ==  1

def test_longest_substring_in_middle():
    assert length_longest_substring('pwwkew') == 3

def test_empty_string():
    assert length_longest_substring(' ') == 1

def test_str_of_len_two():
    assert length_longest_substring('au') == 2