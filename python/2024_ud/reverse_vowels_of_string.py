"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 
input s = ' '

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
from collections import deque


def reverseVowels(s: str) -> str:
    # iterate through the string once, noting vowels and their indices
    # going through the string
    #
    vowels = {"a", "e", "i", "o", "u"}
    vowels_and_indices = []
    for index, char in enumerate(s):  # O(n)
        if char.lower() in vowels:
            vowels_and_indices.append((index, char))

    # index from l -r and vowels from r - l
    right = -1
    s = list(s)  # O(n)
    for index, char in vowels_and_indices:  # O(v)
        s[index] = vowels_and_indices[right][1]
        right -= 1
    return "".join(s)  # O(n)
    # O(3n + v) time complexity
    # O(2n + v + 5) space complexity


def test_hello():
    assert reverseVowels("hello") == "holle"


def test_leetcode():
    assert reverseVowels("leetcode") == "leotcede"


def test_empty():
    assert reverseVowels(" ") == " "


def test_odd_vowels():
    assert reverseVowels("lebail") == "libael"


def test_no_vowels():
    assert reverseVowels("dftpqr") == "dftpqr"


def test_caps():
    assert reverseVowels("STOnger") == "STengOr"
