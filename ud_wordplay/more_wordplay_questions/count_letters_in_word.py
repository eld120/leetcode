'''
Write a function that takes a string word as the first argument, a string letter as the second argument, and returns a count of how many times letter occurs in word.
'''
import pytest


def find_occurances_within_word(word: str, letter: str) -> int:
    counter = 0
    if len(letter) > 1:
        raise TypeError(f'letter: {letter} - must be a single character')
    for char in word:
        if char == letter:
            counter += 1

    return counter



def test_one():
    assert find_occurances_within_word('seyamack', 'a') == 2

def test_two():
    with pytest.raises(TypeError) as exception:
        find_occurances_within_word('seyamack', 'ma')
    assert exception.type == TypeError
    assert 'must be a single character' in str(exception.value)

