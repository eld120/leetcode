from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

    """
    index = 1
    working_prefix = [""]
    if len(strs) == 1:
        return strs[0]
    while index <= len(strs[0]):
        prefix_in_all_strings = True
        prefix = strs[0][:index]
        try:
            for string in strs:
                if prefix != string[:index]:
                    prefix_in_all_strings = False

            if prefix_in_all_strings:
                working_prefix[0] = prefix
            index += 1
        except IndexError:
            return working_prefix[0]
    return working_prefix[0]


def test_one():
    assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_two():
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_three():
    assert longestCommonPrefix([""]) == ""


def test_four():
    assert longestCommonPrefix(["a"]) == "a"


def test_five():
    assert longestCommonPrefix(["flower", "flower", "flower", "flower"]) == "flower"
