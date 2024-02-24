def strStr(haystack: str, needle: str) -> int:
    """
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

    Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

    Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
    """
    if needle in haystack:
        counter = 0
        while counter < len(haystack):
            if needle == haystack[counter : len(needle) + counter]:
                return counter
            counter += 1
    return -1


def test_one():
    assert strStr("sadbutsad", "sad") == 0


def test_two():
    assert strStr("leetcode", "leeto") == -1


def test_three():
    assert strStr("hello", "ll") == 2
