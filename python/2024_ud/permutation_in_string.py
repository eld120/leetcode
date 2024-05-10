from collections import Counter


def check_for_permutations(s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.
    """

    for index, char in enumerate(s2):
        if char == s1[0]:
            if (
                index >= len(s1) - 1
                and s2[index - len(s1) + 1 : index + 1] == s1[::-1]
                or s2[index : index + len(s1)] == s1
            ):
                return True
    return False


def count_chars(s1, s2):
    counter = Counter()
    reference = Counter(s1)
    win_len = 0
    for index, char in enumerate(s2):
        # breakpoint()
        if win_len < len(s1):
            counter[char] += 1
            win_len += 1
        else:
            counter[s2[index - win_len]] -= 1
            counter[char] += 1

        if reference == counter:
            return True
    return False


def test_one():
    assert count_chars("ab", "eidbaooo") == True


def test_77():
    assert count_chars("ab", "ab") == True


def test_80():
    assert count_chars("abc", "bbbca") == True
