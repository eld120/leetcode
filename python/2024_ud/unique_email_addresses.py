from typing import List
import re


def num_unique_email(emails: List[str]) -> int:
    """
    Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
    Constraints:

    1 <= emails.length <= 100
    1 <= emails[i].length <= 100
    emails[i] consist of lowercase English letters, '+', '.' and '@'.
    Each emails[i] contains exactly one '@' character.
    All local and domain names are non-empty.
    Local names do not start with a '+' character.
    Domain names end with the ".com" suffix.
    """
    # ans_list = []

    # for email in emails:

    #     found = re.match(r"^.+", email)

    pass


def emails_no_regex(emails: List[int]) -> int:
    counter = set()
    for email in emails:
        ignore_flag = False
        at_flag = False
        temp = []
        for char in email:
            if not at_flag and char == "+":
                ignore_flag = True
            elif char == "@":
                ignore_flag = False
                at_flag = True
            elif not ignore_flag and not at_flag and char == ".":
                continue

            if ignore_flag:
                continue
            else:
                temp.append(char)
        counter.add("".join(temp))

    return len(counter)  # , counter


def test_one():
    assert emails_no_regex(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3


def test_two():
    assert (
        emails_no_regex(
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ]
        )
        == 2
    )
