'''
Write a function that takes a string phrase and returns a dictionary containing counts of how many times every character appears in phrase.
'''
from typing import Dict 
from collections import Counter

def how_many_char_in_phrase(phrase: str)-> Dict[str, int]:
    return Counter(phrase)



def test_one():
    assert how_many_char_in_phrase('seyamack') == {'s': 1, 'e': 1, 'y':1, 'a':2, 'm':1, 'c':1, 'k':1}

def test_two():
    assert how_many_char_in_phrase('aardvark') == {'a':3, 'r':2, 'd':1, 'v':1, 'k':1}