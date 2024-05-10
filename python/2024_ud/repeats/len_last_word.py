"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
"""
import string


def length_last_thing(s: str) -> int:
    counter = 0
    chars = set(string.ascii_letters)
    for char in reversed(s):
        if char in chars:
            counter += 1
        elif char == " " and counter == 0:
            continue
        else:
            break
    return counter


def test_one():
    assert length_last_thing("Hello World") == 5


def test_two():
    assert length_last_thing(" fly me to the moon ") == 4
