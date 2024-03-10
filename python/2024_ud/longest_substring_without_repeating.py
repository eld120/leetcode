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
    '''
    string as input - 'abcdd' - 'adbdwlerkjwlrjq'
    look for longest substring w/o repeating chars
    use a window, initialized at size 1
    current_substring, longest_substring

    using a set to track unique chars
    within loop
        if char is not in set - add, we'll be peeking at sinput[right] for our next char
            
        if char is found in set -> not add - record length of the current substring
            remove/increment left char/pointer

    '''
    if len(sinput) <= 1:
        return len(sinput)
    
    longest_substring = 0
    left = 0
    right = 0
    unique_characters = set()
    while right < len(sinput):
        
        if sinput[right] not in unique_characters:
            unique_characters.add(sinput[right])
            if right - left + 1 > longest_substring:
                longest_substring = right - left + 1
            right += 1
        else:
            
            unique_characters.remove(sinput[left])
            left += 1

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

def test_empty_str():
    assert length_longest_substring('') == 0

def test_sol_at_start():
    assert length_longest_substring('abcddddddq') == 4

def test_sol_at_end():
    assert length_longest_substring('abcababddddddlwiroqpuzyx') == 12