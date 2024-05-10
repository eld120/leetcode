from collections import Counter


def min_substring(s: str, t: str) -> str:
    """
    Input: s = "AOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

    Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 10^5
    s and t consist of uppercase and lowercase English letters.

    """
    # start with window as len(s), vars: left, right, current_window, smallest_window

    # Counter, iterate through sting s, left pointer = index, right pointer = index - smallest_window,

    # move right pointer until we have t within the window, then move left pointer to find smallest substring
    if t == s:
        return t

    def target_has_all_values(s_dict, t_dict) -> bool:
        for key in t_dict.keys():
            if t_dict[key] > s_dict[key]:
                return False
        return True

    smallest_window = len(s) + 1
    window = ""
    target_count = Counter(t)
    count = Counter()
    left = 0
    right = 0
    flag = True
    while left < len(s):
        if flag and right < len(s):
            count[s[right]] += 1
            flag = False
            # recalculating/counting keys of both dicts at every iteration is slowing this down
        if target_has_all_values(count, target_count):
            if right - left + 1 < smallest_window:
                smallest_window = right - left + 1
                window = s[left : right + 1]
            count[s[left]] -= 1
            left += 1
            flag = False
        elif right <= len(s) - 1:
            right += 1
            flag = True
        else:
            break

    return window


def test_s_smaller_than_t():
    assert min_substring("a", "aa") == ""


def test_example_one():
    assert min_substring("ADOBECODEBANC", "ABC") == "BANC"


def test_single_char():
    assert min_substring("a", "a") == "a"


def test_answer_at_beginning():
    assert min_substring("ADOBECODEBANC", "ADB") == "ADOB"


# test_answer_at_beginning()


def test_207():
    assert min_substring("cabwefgewcwaefgcf", "cae") == "cwae"


def test_255():
    assert min_substring("abc", "ac") == "abc"
