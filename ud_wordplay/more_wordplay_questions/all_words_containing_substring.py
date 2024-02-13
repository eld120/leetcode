'''
Write a function that takes a string substring as an argument and returns an array of all of the words that contain that substring (the substring can appear anywhere in the word).
'''
from typing import List


def find_substrings(substring:str, file_path:str) -> List[str]:
    with open(file_path, 'r') as file:
        words_containing_substrings = []
        for line in file:
            word = line.rstrip('\n')
            if substring in word:
                words_containing_substrings.append(word)
    print(words_containing_substrings)


if __name__ == '__main__':
    find_substrings('PY', '../sowpods.txt' )