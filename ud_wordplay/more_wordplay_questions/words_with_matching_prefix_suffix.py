'''
Write a function that takes a string prefix as the first argument, a string suffix as the second argument, and an integer length as the third argument. It should return an array of all of the words that start with that prefix, end with that suffix, and are that length.
'''
from typing import List

def find_prefix_suffix_length(prefix: str, suffix: str, word_length: int) -> List[str]:
    with open('../sowpods.txt', 'r') as file:
        prefix_suffix_matches = []

        for line in file:
            word = line.rstrip('\n')
            prefix_length = len(prefix)
            suffix_length = len(suffix)
            if len(word) == word_length and prefix == word[:prefix_length] and suffix == word[-1 * suffix_length:]:
                prefix_suffix_matches.append(word)

    print(prefix_suffix_matches)
    return prefix_suffix_matches



# tests/use cases
def test_one():
    assert 'PYTHON' in find_prefix_suffix_length('PY', 'ON', 6)

def test_two():
    assert ['ALUMINUM'] == find_prefix_suffix_length('ALU', 'UM', 8)