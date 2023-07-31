import pytest
import string


# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


test_one = "Let's take LeetCode contest"
test_two = "God Ding"


def test_reverseWords(string: str) -> str:
    str_list = string.split(" ")
    str_list = (tuple(s) for s in str_list)
    answer = ""
    for index, l in enumerate(str_list):
        for inner in reversed(l):
            answer = answer + inner
        if index >= 0 and index < len(string):
            answer = answer + " "

    print(tuple(answer[:-1]))


if __name__ == "__main__":
    test_reverseWords(test_one)
