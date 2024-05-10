"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""
from typing import List
from collections import Counter


def uncommonFromSentences(s1: str, s2: str) -> List[str]:
    s1_list = s1.split(" ")
    s2_list = s2.split(" ")
    count1 = Counter(s1_list)
    count2 = Counter(s2_list)
    s1_set = set(s1_list)
    s2_set = set(s2_list)
    ans = []
    for word in s1_list:
        if count1[word] < 2 and word not in s2_set:
            ans.append(word)
    for word in s2_list:
        if count2[word] < 2 and word not in s1_set:
            ans.append(word)

    return ans


def test_one():
    assert uncommonFromSentences("this apple is sweet", "this apple is sour") == [
        "sweet",
        "sour",
    ]
