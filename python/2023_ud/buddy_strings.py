"""
Given two strings s and goal, return true if you can swap two letters in s so the 
result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j 
and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Constraints:
1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
"""



def budd_strings(s: str, goal: str) -> bool:
    if s == goal:
        return len(set(s)) < len(s)
    elif len(s) != len(goal):
        return False
    s = [char for char in s]
    goal = [char for char in goal]
    
    left, right = 0, len(s)-1
    for _ in range(0, len(s)):
        if s[left] == goal[left]:
            left += 1
        if s[right] == goal[right]:
            right -= 1 
    
    l,r = s[left], s[right]
    
    s[left],s[right] = r,l
    
    return s == goal

def test_reversed_strings():
    assert budd_strings('ab', 'ba') is True

def test_same_string_len_two():
    assert budd_strings('ab', 'ab') is False

def test_same_char_twice():
    assert budd_strings('aa', 'aa') is True

def test_34():
    assert budd_strings("aaaaaaabc", "aaaaaaacb") is True

def test_same_string_still_pass():
    assert budd_strings('abab', 'abab') is True

def test_abcd():
    assert budd_strings('abcd', 'abcd') is False

def test_ab():
    assert budd_strings('ab', 'ab') is False

def test_strings_unequal_len():
    assert budd_strings('aab', 'aa') is False