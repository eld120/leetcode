"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
from collections import Counter


def firstUniqChar(s: str) -> int:
    char_count = Counter(s)

    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1


def first_unique_char(s: str):
    # if len(s) == 1:
    #     return 0
    for index, char in enumerate(s):
        for inner_index, inner_char in enumerate(s):
            if inner_index == index:
                if inner_index == len(s) - 1 and index == len(s) - 1:
                    return index
                continue
            elif char == inner_char:
                break
            elif inner_index == len(s) - 1:
                return index
    return -1


def test_one():
    assert firstUniqChar("leetcode") == 0


def test_two():
    assert firstUniqChar("loveleetcode") == 2


def test_three():
    assert firstUniqChar("aabb") == -1
